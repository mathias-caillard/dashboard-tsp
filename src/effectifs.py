
import pandas as pd
from src import config


#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)

#Récupération des effectifs
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 2    #Nombre de lignes de données
sheetName = '2023-DRH-Annuel'   #Nom de la feuille
df5 = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

#Récupération des effectifs des departements
effectif = []
for i in range(10,16):
    effectif.append(df5.iloc[0,i])

effectif.append(sum(effectif))



