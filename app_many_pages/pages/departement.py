import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import random as rd
import plotly.graph_objects as go
import plotly.subplots as subplt
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
tab_valeur=[]   #Tableau des données

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

indic.append(df2.Indicateur[0] + "(en centaine)")
valeur2 = []
for j in range(débutColonneData, finColonneData + 1):
    valeur2.append(df2.iloc[0, j]/100)
tab_valeur.append(valeur2)


ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 1    #Nombre de lignes de données
sheetName = '2023-DAF-Annuel'   #Nom de la feuille
df3 = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

indic.append("CA Recherche annuel (en centaine de millier €)")
valeur3 = []
for j in range(débutColonneData, finColonneData + 1):
    valeur3.append(df3.iloc[0, j]/100000)
tab_valeur.append(valeur3)


ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 1    #Nombre de lignes de données
sheetName = '2023-DRH-Tri'   #Nom de la feuille
df4 = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

indic.append(df4.Indicateur[0])
valeur4 = []
finColonneData = 24
for i in range(débutColonneData, finColonneData + 1, 4):
    liste = []
    for j in range(4):
        liste.append(df4.iloc[0, i+j])
    valeur4.append(sum(liste))
tab_valeur.append(valeur4)

#Réorganisation des données (transposition)
data = []
nb_indicateur = len (tab_valeur)        #5 indicateurs
for i in range (len(tab_valeur[0])):
    data_i = []
    for j in range(nb_indicateur):
        data_i.append((tab_valeur[j][i]))
    data.append(data_i)

#Simulation pour une autre année
data_sim_0 = [x + rd.randint(-5, 10) for x in data[0]]


#Pondération des données par la taille du département
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 2    #Nombre de lignes de données
sheetName = '2023-DRH-Annuel'   #Nom de la feuille
df5 = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

#Récupération des effectifs des départements
effectif = []
for i in range(10,16):
    effectif.append(df5.iloc[1,i])

#Création des données pondérées
data_ponderees = []
for i in range(len(data)):
    data_ponderees_i = []
    for j in range(len(data[i])):
        data_ponderees_i.append((data[i][j] / effectif[i]))
    data_ponderees.append(data_ponderees_i)




#Création des figures

#Superposition de 2 graphes radar
fig = go.Figure()
fig.add_trace(go.Scatterpolar(r = data[0],theta = indic,fill = 'toself',name = labels[0] + " 2023",))
fig.add_trace(go.Scatterpolar(r=data_sim_0, theta=indic, fill='toself', name=labels[0] + " 2024"))
fig.update_layout(
    title = "Graphe radar du département " + labels[0] + " pondéré par les effectifs (2023 et 2024)",
    polar=dict(radialaxis=dict(range=[0, 65]))
)

#Affichage de plusieurs graphe radar

list_fig = []
for i in range(len(labels)):
    fig2 = go.Figure()
    fig2.add_trace(go.Scatterpolar(
        r = data[i],
        theta=indic,
        fill='toself',
        name = labels[i] + " 2023"
    ))
    fig2.update_layout(
        title="Graphe radar du département " + labels[i] + " pondéré par les effectifs",
        polar=dict(radialaxis=dict(range=[0, 65]))
    )
    list_fig.append(fig2)

fig3 = go.Figure()
for i in range(len(data_ponderees)):
    fig3.add_trace(go.Scatterpolar(r = data_ponderees[i],theta = indic,fill = 'toself',name = labels[i] + " 2023",))

fig3.update_layout(
    title="Graphes radar des département pondérés par leurs effectifs",
    polar=dict(radialaxis=dict(dtick = 1.0))
)




layout = html.Div(
    style={},
    children=[
    html.H1(children='Bienvenue sur la page concernant les départements de Télécom SudParis'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    dcc.Graph(
        id='example-graph2',
        figure=list_fig[0]
    ),
    dcc.Graph(
        id='example-graph3',
        figure=list_fig[1]
    ),
    dcc.Graph(
        id='example-graph4',
        figure=list_fig[2]
    ),
    dcc.Graph(
        id='example-graph5',
        figure=list_fig[3]
    ),
    dcc.Graph(
        id='example-graph6',
        figure=list_fig[4]
    ),
    dcc.Graph(
        id='example-graph7',
        figure=list_fig[5]
    ),
    dcc.Graph(
        id='example-graph8',
        figure=fig3
    ),


    html.Div(children='''

    '''),

])