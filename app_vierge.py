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

#Chemin relatif des fichiers excels
excel_path = os.path.join(root_directory, 'assets\\Saisie-2023-INDICATEUR-DE-SUIVI-Ti.xlsx')

excel_path2 = os.path.join(root_directory, 'assets\\Saisie-2023-INDICATEUR-DE-SUIVI-Ti_remplie.xlsx')

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)



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

df3 = pd.read_excel(excel_path,sheet_name = '2023-Ti-DF')
#print(df3)


#Pour construire le plot de df4, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres = 2
nombreLignesData = 4
sheetName = '2023-Ti-DF'
débutColonneTrimestre = 4
df4 = pd.read_excel(excel_path2,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)



#ajouter d'une colonne artificielle "trimestre" dans le dataframe facilitant la création du graphe associé
valeurNouvelleColonne = []
for i in range(débutColonneTrimestre,débutColonneTrimestre + 4) :
    valeurNouvelleColonne.append(df4.columns[i])
df4["trimestre"] = valeurNouvelleColonne



#ajout de nouvelles colonnes dans le dataframe pour chaque type d'étudiant.
ligne = 0
for indicateur in df4.Indicateur :
    valeurPourIndicateur = []
    for i in range(0, nombreLignesData) :
        valeurPourIndicateur.append(df4.iloc[ligne][df4["trimestre"]][i])
    df4[indicateur] = valeurPourIndicateur
    ligne += 1



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

    dcc.Graph(
        id='example-graph4',
        figure=fig4
    ),

])


#2ème layout
app.layout

#Démarrage de l'application
if __name__ == '__main__':
    #Activation du debuggage (permet le hot-reloading)
    app.run_server(debug=True)
    