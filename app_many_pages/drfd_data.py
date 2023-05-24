from config import *
import openpyxl
from app_many_pages.fonction_data import add_to_dict


data_drfd=[]
labels_drfd={}
titre_drfd = {}
for nom_fichier in liste_fichier:
    data_drfd_annee = {}
    chemin_fichier = generate_path(nom_fichier)
    fichier_excel = openpyxl.load_workbook(chemin_fichier)
    feuilles = fichier_excel.sheetnames
    for sheet in feuilles:
        if "DRFD" in sheet:
            ligneDesTitres = 0  # Numérotation comme dans les liste, matrices...
            nombreLignesData = 3  # Nombre de lignes de données
            debutColonneData = 4
            finColonneData = 10
            df = pd.read_excel(chemin_fichier,sheet_name = sheet, header = ligneDesTitres, nrows = nombreLignesData)
            add_to_dict(df, debutColonneData, finColonneData, nombreLignesData, data_drfd_annee, titre_drfd, labels_drfd)
    data_drfd.append(data_drfd_annee)



