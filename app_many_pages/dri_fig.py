
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd



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


trimestre = ['Trimestre 1', 'Trimestre 2', 'Trimestre 3', 'Trimestre 4']

df2 = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData + 1)

labels, valeur = [], []
for i in range(débutColonneTrimestre,débutColonneTrimestre + 4):
    labels.append(df2.columns[i])

for i in range(5):
    valeur_i=[]
    for j in range(débutColonneTrimestre,débutColonneTrimestre + 4):
        valeur_i.append((df2.iloc[i,j]))
    valeur.append(valeur_i)

y_axis2 = []
for indicateur in df2.Indicateur :
    y_axis2.append(indicateur)

def fig_dri_1():
    #création de la figure
    fig = px.bar(df, x = "trimestre", y = y_axis)

    #Ajout d'un titre
    fig.update_layout(title = "Chiffres sur l'international à Télécom Sudparis")


    return fig


def fig_dri_3():

    fig3=go.Figure()
    for i in range(5):
        fig3.add_trace(go.Bar(x=labels, y=valeur[i], name=y_axis2[i]))

    # Ajout d'un titre
    fig3.update_layout(title="Chiffres sur l'international à Télécom Sudparis")
    return fig3

valeur2 = valeur[2].copy()
valeur2_sim = []
labels2=[]
# Ajout de valeur simulées
for i in range(2020, 2024):
    for j in range(4):
        labels2.append("Année " + str(i) + " T" + str(j+1))
        if i!=2023:
            valeur2_sim.append(valeur2[j] + rd.randint(-5, 5))
valeur2 = valeur2_sim + valeur2

def fig_dri_2():

    fig2  = go.Figure(data=[go.Bar(x=labels2, y=valeur2)])

    #Ajout d'un titre
    fig2.update_layout(title = "Evolution dans le temps du nombre d'étudiants étrangers à Télécom Sudparis")
    return fig2

def fig_dri_4():
    fig4 = go.Figure()
    for i in range(4):
        valeur2_i=valeur2[4*i: 4*(i+1)]
        fig4.add_trace(go.Scatter(x=labels, y=valeur2_i, name= "Année 202" + str(3+i)))

    fig4.update_layout(title="Evolution dans le temps du nombre d'étudiants étrangers à Télécom Sudparis")
    return fig4