
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src import config
import random as rd
from config import *
import openpyxl
from src.fonction_data import add_to_dict


#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)


data_dri=[]
labels_dri={}
titre_dri = {}
for nom_fichier in liste_fichier:
    data_dri_annee = {}
    chemin_fichier = generate_path(nom_fichier)
    fichier_excel = openpyxl.load_workbook(chemin_fichier)
    feuilles = fichier_excel.sheetnames
    for sheet in feuilles:
        if "DRI" in sheet:
            if "Tri" in sheet:
                ligneDesTitres = 0  # Numérotation comme dans les liste, matrices...
                nombreLignesData = 5  # Nombre de lignes de données
                debutColonneData = 4
                finColonneData = 7
                df = pd.read_excel(chemin_fichier,sheet_name = sheet, header = ligneDesTitres, nrows = nombreLignesData)
                add_to_dict(df, debutColonneData, finColonneData, nombreLignesData, data_dri_annee, titre_dri, labels_dri)

            else:   #"Annuel" in sheet
                ligneDesTitres = 0  # Numérotation comme dans les liste, matrices...
                nombreLignesData = 1  # Nombre de lignes de données
                debutColonneData = 4
                finColonneData = 4
                df = pd.read_excel(chemin_fichier, sheet_name=sheet, header=ligneDesTitres, nrows=nombreLignesData)
                add_to_dict(df, debutColonneData, finColonneData, nombreLignesData, data_dri_annee, titre_dri, labels_dri)

    data_dri.append(data_dri_annee)

"""
for data_ in data_dri:
    print(data_)

for cle, valeur in titre_dri.items():
    print(cle, valeur)

for cle, valeur in labels_dri.items():
    print(cle, valeur)

"""



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
couleurs_trimestres=config.couleurs_trimestres

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

data_dri_2023 = valeur

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
    fig3.update_layout(title="Effectifs sur l'international à Télécom Sudparis")
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

    #fig2  = go.Figure(data=[go.Bar(x=labels2, y=valeur2)])
    fig2 = px.bar(x=labels2, y=valeur2, color=valeur2)

    #Ajout d'un titre
    fig2.update_layout(title = "Evolution temporelle du nombre d'étudiants étrangers à Télécom Sudparis")
    return fig2


def fig_dri_4():
    fig4 = go.Figure()
    for i in range(4):
        valeur2_i=valeur2[4*i: 4*(i+1)]
        fig4.add_trace(go.Scatter(x=labels, y=valeur2_i, name= "Année 202" + str(3+i)))

    fig4.update_layout(title="Evolution temporelle du nombre d'étudiants étrangers à Télécom Sudparis, comparaison annuelle par trimestre")
    return fig4