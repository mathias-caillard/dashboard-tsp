from   config import generate_path, liste_fichier
import openpyxl
import pandas as pd
from   functions.fonction_data import add_to_dict

data_drh=[]
labels_drh={}
titre_drh = {}
for nom_fichier in liste_fichier:
    data_drh_annee = {}
    chemin_fichier = generate_path(nom_fichier)
    fichier_excel = openpyxl.load_workbook(chemin_fichier)
    feuilles = fichier_excel.sheetnames
    for sheet in feuilles:
        if "DRH" in sheet:
            if "Tri" in sheet:
                ligneDesTitres = 0  # Numérotation comme dans les liste, matrices...
                nombreLignesData = 1  # Nombre de lignes de données
                debutColonneData = 4
                finColonneData = 31
                df = pd.read_excel(chemin_fichier,sheet_name = sheet, header = ligneDesTitres, nrows = nombreLignesData)
                add_to_dict(df, debutColonneData, finColonneData, nombreLignesData, data_drh_annee, titre_drh, labels_drh)

            else:   #"Annuel" in sheet
                ligneDesTitres = 0  # Numérotation comme dans les liste, matrices...
                nombreLignesData = 5  # Nombre de lignes de données
                debutColonneData = 4
                finColonneData = 15
                df = pd.read_excel(chemin_fichier, sheet_name=sheet, header=ligneDesTitres, nrows=nombreLignesData)
                add_to_dict(df, debutColonneData, finColonneData, nombreLignesData, data_drh_annee, titre_drh, labels_drh)

    data_drh.append(data_drh_annee)



