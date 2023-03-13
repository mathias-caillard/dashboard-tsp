import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config

dash.register_page(
    __name__,
    title = "DIRE",
    name = "DIRE",
    order=4
                   )

#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)

#Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 3    #Nombre de lignes de données
sheetName = '2023-DIRE-Tri'   #Nom de la feuille
débutColonneData = 4    #Première colonne de données
FinColonneData = 33  #Dernière colonne de données
df = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

#Récupération des titres des colonnes
x_axis = df.columns.tolist()



#définition de l'axe des ordnnées
y_axis = []
for indicateur in df.Indicateur :
    y_axis.append(indicateur)

premiereColonneAnnuelle = 8
indice_annuelle = []
for i in range(6):
    j_annuel = 5*i + premiereColonneAnnuelle
    indice_annuelle.append((j_annuel))



labels = []
valeur_annuelle1, valeur_annuelle3 =  [], []

for j in indice_annuelle:
    labels.append(x_axis[j])
    valeur_annuelle1.append(df.iloc[0,j])
    valeur_annuelle3.append((df.iloc[2,j]))

fig1 = go.Figure(data=[go.Pie(labels=labels, values=valeur_annuelle1)])

# Personnaliser l'apparence du graphique
fig1.update_layout(title='Suivi des contrats de recherche')

fig3 = go.Figure(data=[go.Pie(labels=labels, values=valeur_annuelle3)])

# Personnaliser l'apparence du graphique
fig3.update_layout(title='Contribution au financement de l\'école')


layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DIRE'),

    dcc.Graph(
        id='example-graph1',
        figure=fig1,
    ),

    dcc.Graph(
        id='example-graph3',
        figure=fig3,
    )

])