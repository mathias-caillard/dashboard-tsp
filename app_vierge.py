# coding: utf-8
#Import des bibliothèques
import dash
from dash import html, dcc
import os
import pandas as pd
import plotly.express as px
from fonctions import *


#Initialisation de l'application
app = dash.Dash(__name__)

#Chemin absolu du répertoire de travail
root_directory = os.path.abspath(os.path.dirname(__file__))

#Chemin relatif de l'image graphe_tennis_séparés.png
image_path = os.path.join(root_directory, 'assets\\graphe_tennis_séparés.png')

#Chemin relatif des fichiers excels
excel_path = os.path.join(root_directory, 'assets\\Saisie-2023-INDICATEUR-DE-SUIVI-Ti.xlsx')

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)


#bar graph test
df = pd.DataFrame({
    "Année": ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"],
    "Nb de nationalités étrangères différentes": [34, 39, 41, 40, 42, 43, 45, 43, 45,51]
})
fig = px.bar(df, x="Année", y="Nb de nationalités étrangères différentes", color = "Nb de nationalités étrangères différentes")

#pie chart test
df2 = pd.DataFrame({
    'type de promo' : ['FISE', 'FIPA', 'DNM', 'FTLV'],
    'nombre' : [355, 452, 34, 78]
})
fig2 = px.pie(df2, values='nombre', names='type de promo')


#test récupération données depuis fichier Excel
df3 = pd.read_excel(excel_path,sheet_name = '2023-DF-Tri')

#test figure type trimestriel



df4 = dfGenIndTri(ligneDesTitres=0, nombreLignesData = 4, sheetName = '2023-DF-Tri', débutColonneTrimestre = 4, excelPath = excel_path)

 #définition de l'axe des ordnnées
y_axis = []
for indicateur in df4.Indicateur :
    y_axis.append(indicateur)

#création de la figure
fig4 = px.bar(df4, x = "trimestre", y = y_axis)


#Définition du layout
app.layout = html.Div([

    #Titre
    html.H1('Bonjour, voici mon application web vierge en Dash sur Python !'),

    #Images
    html.H2('Affichage d\'une image à partir d\'un site web'),
    html.Img(src = 'https://mobilitydb.com/images/plotly.png'), #affichage d'une image sur une site web
    html.H2('Affichage d\'une image locale'),
    html.Img(src = app.get_asset_url('graphe_tennis.png')),  #affichage d'une image locale

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

     dcc.Graph(
        id='example-graph2',
        figure=fig2
    ),

    dcc.Graph(
        id='example-graph4',
        figure=fig4
    ),

])



#Démarrage de l'application
if __name__ == '__main__':
    #Activation du debuggage (permet le hot-reloading)
    app.run_server(debug=True)


