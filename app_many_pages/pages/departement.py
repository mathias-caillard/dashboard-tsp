import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config

dash.register_page(
    __name__,
    title = "Départements",
    name = "Départements",
    order=8
                   )

#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)

ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 3    #Nombre de lignes de données
sheetName = '2023-DRFD-Annuel'   #Nom de la feuille
débutColonneData = 4
finColonneData = 9
df = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)


labels = df.columns.tolist()[débutColonneData: finColonneData + 1]      #Nom des départements
indic = []      #Nom des indicateurs
tab_valeur=[]
for i in range(2):
    indic.append(df.Indicateur[i])
    valeur = []
    for j in range(débutColonneData, finColonneData + 1):
        valeur.append(df.iloc[i, j])
    tab_valeur.append((valeur))


ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 1    #Nombre de lignes de données
sheetName = '2023-DF-Annuel'   #Nom de la feuille
df2 = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

valeur2 = []
for j in range(débutColonneData, finColonneData + 1):
    valeur2.append(df2.iloc[0, j])
tab_valeur.append(valeur2)


ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 1    #Nombre de lignes de données
sheetName = '2023-DAF-Annuel'   #Nom de la feuille
df3 = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

valeur3 = []
for j in range(débutColonneData, finColonneData + 1):
    valeur3.append(df3.iloc[0, j])
tab_valeur.append(valeur3)


ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 1    #Nombre de lignes de données
sheetName = '2023-DRH-Tri'   #Nom de la feuille
df4 = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

valeur4 = []
finColonneData = 24
for i in range(débutColonneData, finColonneData + 1, 4):
    liste = []
    for j in range(4):
        liste.append(df4.iloc[0, i+j])
    valeur4.append(sum(liste))

tab_valeur.append(valeur4)


layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant les départements de Télécom SudParis'),



    html.Div(children='''

    '''),

])