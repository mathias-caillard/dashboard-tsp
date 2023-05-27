from config import *
import openpyxl
from src.functions.fonction_data import add_to_dict

data_df=[]
labels_df={}
titre_df = {}
for nom_fichier in liste_fichier:
    data_df_annee = {}
    chemin_fichier = generate_path(nom_fichier)
    fichier_excel = openpyxl.load_workbook(chemin_fichier)
    feuilles = fichier_excel.sheetnames
    for sheet in feuilles:
        if "DF" in sheet:
            if "Tri" in sheet:
                ligneDesTitres = 0  # Numérotation comme dans les liste, matrices...
                nombreLignesData = 5  # Nombre de lignes de données
                debutColonneData = 4
                finColonneData = 7
                df = pd.read_excel(chemin_fichier,sheet_name = sheet, header = ligneDesTitres, nrows = nombreLignesData)
                add_to_dict(df, debutColonneData, finColonneData, nombreLignesData, data_df_annee, titre_df, labels_df)
            else:   #"Annuel" in sheet
                ligneDesTitres = 0  # Numérotation comme dans les liste, matrices...
                nombreLignesData = 1  # Nombre de lignes de données
                debutColonneData = 4
                finColonneData = 10
                df = pd.read_excel(chemin_fichier, sheet_name=sheet, header=ligneDesTitres, nrows=nombreLignesData)
                add_to_dict(df, debutColonneData, finColonneData, nombreLignesData, data_df_annee, titre_df, labels_df)

    data_df.append(data_df_annee)

