#Import des biblioth�ques
import dash
from dash import html
import os

#Initialisation de l'application
app = dash.Dash(__name__)

#Chemin absolu du r�pertoire de travail
root_directory = os.path.abspath(os.path.dirname(__file__))

#Chemin relatif de l'image
image_path = os.path.join(root_directory, 'Images\graphe_tennis.png')
print(image_path)

#D�finition du layout
app.layout = html.Div([
    #Titre
    html.H1('Bonjour, voici mon application web vierge en Dash sur Python !'),

    #Images
    #html.Img(src = 'https://rapids.ai/assets/images/Plotly_Dash_logo.png'), (fonctionne avec une source de type lien web)
    html.Img(src = image_path) #ne fonctionne pas


])


#D�marrage de l'application
if __name__ == '__main__':
    #Activation du d�buggage
    app.run_server(debug=True)