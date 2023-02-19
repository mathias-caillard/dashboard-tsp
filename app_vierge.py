# coding: utf-8
#Import des bibliothèques
import dash
from dash import html
import os

#Initialisation de l'application
app = dash.Dash(__name__)

#Chemin absolu du répertoire de travail
root_directory = os.path.abspath(os.path.dirname(__file__))

#Chemin relatif de l'image
#image_path = os.path.join(root_directory, 'Images\\graphe_tennis.png')

#Définition du layout
app.layout = html.Div([

    #Titre
    html.H1('Bonjour, voici mon application web vierge en Dash sur Python !'),

    #Images
    html.Img(src = 'https://rapids.ai/assets/images/Plotly_Dash_logo.png'), #affichage d'une image sur une site web
    html.Img(src = app.get_asset_url('graphe_tennis.png'))  #affichage d'une image locale


])


#Démarrage de l'application
if __name__ == '__main__':
    #Activation du debuggage
    app.run_server(debug=True)