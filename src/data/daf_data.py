from config import generate_path, liste_fichier
import openpyxl
import pandas as pd
from functions.fonction_data import add_to_dict


data_daf=[]
labels_daf={}
titre_daf = {}
for nom_fichier in liste_fichier:
    data_daf_annee = {}
    chemin_fichier = generate_path(nom_fichier)
    fichier_excel = openpyxl.load_workbook(chemin_fichier)
    feuilles = fichier_excel.sheetnames
    for sheet in feuilles:
        if "DAF" in sheet:
            if "Tri" in sheet:
                ligneDesTitres = 0  # Numerotation comme dans les liste, matrices...
                nombreLignesData = 5  # Nombre de lignes de donnees
                debutColonneData = 4
                finColonneData = 33
                df = pd.read_excel(chemin_fichier,sheet_name = sheet, header = ligneDesTitres, nrows = nombreLignesData)
                add_to_dict(df, debutColonneData, finColonneData, nombreLignesData, data_daf_annee, titre_daf, labels_daf)

            else:   #"Annuel" in sheet
                ligneDesTitres = 0  # Numerotation comme dans les liste, matrices...
                nombreLignesData = 1  # Nombre de lignes de donnees
                debutColonneData = 4
                finColonneData = 9
                df = pd.read_excel(chemin_fichier, sheet_name=sheet, header=ligneDesTitres, nrows=nombreLignesData)
                add_to_dict(df, debutColonneData, finColonneData, nombreLignesData, data_daf_annee, titre_daf, labels_daf)

    data_daf.append(data_daf_annee)

