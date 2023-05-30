from src.config import *
import openpyxl
from src.functions.fonction_data import add_to_dict


data_dire=[]
labels_dire={}
titre_dire = {}
for nom_fichier in liste_fichier:
    data_dire_annee = {}
    chemin_fichier = generate_path(nom_fichier)
    fichier_excel = openpyxl.load_workbook(chemin_fichier)
    feuilles = fichier_excel.sheetnames
    for sheet in feuilles:
        if "DIRE" in sheet:
            ligneDesTitres = 0  # Numérotation comme dans les liste, matrices...
            nombreLignesData = 3  # Nombre de lignes de données
            debutColonneData = 4
            finColonneData = 33
            df = pd.read_excel(chemin_fichier,sheet_name = sheet, header = ligneDesTitres, nrows = nombreLignesData)
            add_to_dict(df, debutColonneData, finColonneData, nombreLignesData, data_dire_annee, titre_dire, labels_dire)
    data_dire.append(data_dire_annee)

