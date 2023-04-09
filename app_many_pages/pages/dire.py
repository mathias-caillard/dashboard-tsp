import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as subplt
from app_many_pages import config
import dash_bootstrap_components as dbc

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


#Regroupement des titres et valeurs voulues pour tracer les figures
labels_annuel, labels_trim = [], []
valeur_annuelle1, valeur_annuelle3 =  [], []
valeur_trim1 = []

for j in indice_annuelle:
    labels_annuel.append(x_axis[j])
    valeur_annuelle1.append(df.iloc[0,j])
    valeur_annuelle3.append((df.iloc[2,j]))
    valeur_trim_j, label_trim_j =[], []
    for i in range(4):
        label_trim_j.append(x_axis[j+i-4])
        valeur_trim_j.append(df.iloc[0,j+i-4])
    valeur_trim1.append(valeur_trim_j)
    labels_trim.append(label_trim_j)



#Création d'une figure avec 6 sous-figure pour y placer des histogrammes
fig1 = subplt.make_subplots(rows=1, cols=6, shared_yaxes=True, horizontal_spacing=0.05)

#Ajout des histogrammes dans chacune des sous-figures
for i in range(6):
    labels_i = labels_trim[i]
    valeur_i = valeur_trim1[i]
    fig1.add_trace(go.Bar(x=labels_i, y=valeur_i, name=labels_i[0][:-3]), row=1, col=i+1)

# Personnaliser l'apparence du graphique
fig1.update_layout(title='Suivi des contrats de recherche')



#Création d'une figure avec 6 sous-figure pour y placer des histogrammes
fig2 = subplt.make_subplots(rows=1, cols=4, shared_yaxes=True, horizontal_spacing=0.05)

#Ajout des histogrammes dans chacune des sous-figures
for i in range(4):
    labels_i = []
    valeur_i = []
    for j in range(6):
        labels_i.append(labels_trim[j][i])
        valeur_i.append((valeur_trim1[j][i]))
    labels_i.append( "ECOLE T" + str(i+1))
    valeur_i.append(sum(valeur_i))
    fig2.add_trace(go.Bar(x=labels_i, y=valeur_i, name= "Trimestre " + str(i+1)), row=1, col=i+1)

# Personnaliser l'apparence du graphique
fig2.update_layout(title='Suivi des contrats de recherche, vision trimestrielle')


fig3 = go.Figure(data=[go.Pie(labels=labels_annuel, values=valeur_annuelle3)])

# Personnaliser l'apparence du graphique
fig3.update_layout(title='Contribution au financement de l\'école')


layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DIRE'),

    dcc.Graph(
        id='example-graph1',
        figure=fig1,
        config = {'displaylogo': False}
        ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='example-graph2',
        figure=fig2,
        config = {'displaylogo': False}
        ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph3',
        figure=fig3,
        config = {'displaylogo': False}
    ),

])