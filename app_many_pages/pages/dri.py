import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd



dash.register_page(
    __name__,
    title = "DRI",
    name = "DRI",
    order=7
                   )

#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)

#Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 4    #Nombre de lignes de données
sheetName = '2023-DRI-Tri'   #Nom de la feuille
débutColonneTrimestre = 4
df = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)



#ajouter d'une colonne artificielle "trimestre" dans le dataframe facilitant la création du graphe associé
valeurNouvelleColonne = []
for i in range(débutColonneTrimestre,débutColonneTrimestre + 4) :
    valeurNouvelleColonne.append(df.columns[i])
df["trimestre"] = valeurNouvelleColonne


#ajout de nouvelles colonnes dans le dataframe pour chaque type d'étudiant.
ligne = 0
for indicateur in df.Indicateur :
    valeurPourIndicateur = []
    for i in range(0, nombreLignesData) :
        valeurPourIndicateur.append(df.iloc[ligne][df["trimestre"]][i])
    df[indicateur] = valeurPourIndicateur
    ligne += 1

#définition de l'axe des ordnnées
y_axis = []
for indicateur in df.Indicateur :
    y_axis.append(indicateur)



#création de la figure
fig = px.bar(df, x = "trimestre", y = y_axis)

#Ajout d'un titre
fig.update_layout(title = "Chiffres sur l'international à Télécom Sudparis")


#Evolution temporelle avec des valeurs simulées
labels, valeur = [], []
for i in range(débutColonneTrimestre,débutColonneTrimestre + 4):
    labels.append(df.columns[i])
    valeur.append((df.iloc[2,i]))

#Ajout de valeur simulées
for j in range(5, 17):
    labels.append("ECOLE T" + str(j))
    valeur.append(valeur[i%4] + rd.randint(-5, 5))

fig2  = go.Figure(data=[go.Bar(x=labels, y=valeur)])

#Ajout d'un titre
fig2.update_layout(title = "Evolution dans le temps du nombre d'étudiants étrangers à Télécom Sudparis")


layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la Direction des relations internationales'),

    dcc.Graph(
        id='example-graph',
        figure=fig,
        config = {'displaylogo': False}
    ),
    dcc.Graph(
        id='example-graph',
        figure=fig2,
        config = {'displaylogo': False}
    ),

    html.Div(children='''
        
    '''),

])