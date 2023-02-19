# coding: utf-8
#Import des bibliothèques
import dash
from dash import html, dcc
import os
import pandas as pd
import plotly.express as px


#Initialisation de l'application
app = dash.Dash(__name__)

#Chemin absolu du répertoire de travail
root_directory = os.path.abspath(os.path.dirname(__file__))

#Chemin relatif de l'image graphe_tennis_séparés.png
image_path = os.path.join(root_directory, 'assets\\graphe_tennis_séparés.png')


df = pd.DataFrame({
    "Année": ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"],
    "Nb de nationalités étrangères différentes": [34, 39, 41, 40, 42, 43, 45, 43, 45,51]
})

fig = px.bar(df, x="Année", y="Nb de nationalités étrangères différentes", color = "Nb de nationalités étrangères différentes")

df2 = pd.DataFrame({
    'type de promo' : ['FISE', 'FIPA', 'DNM', 'FTLV'],
    'nombre' : [355, 452, 34, 78]
})

fig2 = px.pie(df2, values='nombre', names='type de promo')

#Définition du layout
app.layout = html.Div([

    #Titre
    html.H1('Bonjour, voici mon application web vierge en Dash sur Python !'),

    #Images
    html.H2('Affichage d\'une image à partir d\'un site web'),
    html.Img(src = 'https://rapids.ai/assets/images/Plotly_Dash_logo.png'), #affichage d'une image sur une site web
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




    


])


#Démarrage de l'application
if __name__ == '__main__':
    #Activation du debuggage (permet le hot-reloading)
    app.run_server(debug=True)