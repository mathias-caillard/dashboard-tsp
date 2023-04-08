import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config

dash.register_page(
    __name__,
    title = "DRH",
    name = "DRH",
    order=6
                   )


#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)

#Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 6    #Nombre de lignes de données
sheetName = '2023-DRH-Annuel'   #Nom de la feuille
débutColonneData = 5    #Première colonne de données
FinColonneData = 15  #Dernière colonne de données
df = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

#définition de l'axe des abscisses
x_axis = df.columns.tolist()[débutColonneData: FinColonneData + 1]



#définition de l'axe des ordnnées
y_axis = []
for indicateur in df.Indicateur :
    y_axis.append(indicateur)



# Créer une figure avec des sous-figures pour chaque bâton
fig = go.Figure()

# Ajouter chaque bâton à la figure
for col_name in df.columns[débutColonneData: FinColonneData + 1]:
    fig.add_trace(go.Bar(x=[col_name], y=[df[col_name].iloc[1]], name=col_name))

#Ajout d'un titre
fig.update_layout(title = "Les ressources humaines à Télécom Sudparis", xaxis_title='Départements', yaxis_title = y_axis[1])


#Graphique en camenbert
values = df.iloc[1][débutColonneData: FinColonneData + 1]

fig2 = go.Figure(data=[go.Pie(labels=x_axis, values=values)])

# Personnaliser l'apparence du graphique
fig2.update_layout(title='Répartition des permanents')

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la Direction des ressources humaines'),

    dcc.Graph(
        id='example-graph',
        figure=fig,
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph2',
        figure=fig2,
        config = {'displaylogo': False}
    )

])