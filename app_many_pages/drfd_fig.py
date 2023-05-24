from app_many_pages import config, effectifs
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random
import data
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import numpy as np
from app_many_pages.data import data_moy
from config import *
import openpyxl

#Import des couleurs
couleurs = config.colors_dept
couleurs_trimestres=config.couleurs_trimestres

#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)




#Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 3    #Nombre de lignes de données
sheetName = '2023-DRFD-Annuel'   #Nom de la feuille
débutColonneData = 4    #Première colonne de données
FinColonneData = 10  #Dernière colonne de données
df = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)





'''
#ajouter d'une colonne artificielle "trimestre" dans le dataframe facilitant la création du graphe associé
valeurNouvelleColonne = []
for i in range(débutColonneData, FinColonneData) :
    valeurNouvelleColonne.append(df.columns[i])
df["Départements"] = valeurNouvelleColonne


#ajout de nouvelles colonnes dans le dataframe pour chaque type d'étudiant.
ligne = 0
for indicateur in df.Indicateur :
    valeurPourIndicateur = []
    for i in range(0, nombreLignesData) :
        valeurPourIndicateur.append(df.iloc[ligne][df["Départements"]][i])
    df[indicateur] = valeurPourIndicateur
    ligne += 1
'''

effectif = effectifs.effectif
print(effectif)

#Extraction des données
data_drfd_2023 = []
for i in range(2):
    data_indic = []
    for j in range(débutColonneData, FinColonneData + 1):
        data_indic.append(df.iloc[i, j]/effectif[j - débutColonneData])
    data_drfd_2023.append(data_indic)





#définition de l'axe des abscisses
x_axis = df.columns.tolist()[débutColonneData: FinColonneData + 1]

#définition de l'axe des ordnnées
y_axis = []
for indicateur in df.Indicateur :
    y_axis.append(indicateur)


#Création des valeurs simulées
titre_années = []
donnees_ecole = [df.iloc[0][FinColonneData]]
for i in range(2023,2027):
    titre_années.append(str(i))
for i in range(2024,2027):
    donnees_ecole.append(donnees_ecole[0] + random.randint(-40, 40))
    


def fig_drfd_1() : 
    # Créer une figure avec des sous-figures pour chaque bâton
    fig = go.Figure()

    # Ajouter chaque bâton à la figure
    i=0
    for col_name in df.columns[débutColonneData: FinColonneData + 1]:
        taille = str(int(effectif[i]))
        fig.add_trace(go.Bar(x=[col_name  + " (" + taille + ")"], y=[df[col_name].iloc[0]/effectif[i]], name=col_name,
                             marker=dict(color = [couleurs[i]])))  #effectif du département entre parenthèse
        i+=1

    #Ajout d'un titre
    fig.update_layout(title = "Chiffres sur la recherche à Télécom Sudparis, pondérés par les effectifs", xaxis_title='Départements', yaxis_title = y_axis[0])

    return fig


def fig_drfd_2() : 

    # Créer une figure avec des sous-figures pour chaque bâton
    fig2 = go.Figure()

    # Ajouter chaque bâton à la figure
    i=0
    for col_name in df.columns[débutColonneData: FinColonneData + 1]:
        taille = str(int(effectif[i]))
        fig2.add_trace(go.Bar(x=[col_name  + " (" + taille + ")"], y=[df[col_name].iloc[1]/effectif[i]], name=col_name,
                              marker=dict(color = [couleurs[i]])))    #effectif du département entre parenthèse
        i+=1

    #Ajout d'un titre
    fig2.update_layout(title = "Nombre de doctorants à Télécom SudParis, pondéré par les effectifs", xaxis_title='Départements', yaxis_title = y_axis[1])

    return fig2


def fig_drfd_3():
    #Figure pour l'évolution sur l'ecole
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=titre_années, y=donnees_ecole))


    #Ajout d'un titre
    fig3.update_layout(title = "Evolution des publications par année" ,xaxis_title='Années', yaxis_title = y_axis[0])

    return fig3



def fig_drfd_4() : 
    #Figure pour l'évolution sur l'ecole
    fig4 = go.Figure()

    #Création des valeurs simulées
    donnees_ecole = [df.iloc[1][FinColonneData]]

    for i in range(2024,2027):
        donnees_ecole.append(donnees_ecole[0] + random.randint(-20, 20))
    fig4.add_trace(go.Scatter(x=titre_années, y=donnees_ecole))


    #Ajout d'un titre
    fig4.update_layout(title = "Evolution du nombre de doctorants par année", xaxis_title='Années', yaxis_title = y_axis[1])

    return fig4




sheetName = data.sheet_names[6]
lines = data.drfd_ligne
titre = data.extract_titre(data.drfd_ligne)
annees = data.annees
data_old_1 = data.extract_data(sheetName, lines[0])
data_old_2 = data.extract_data(sheetName, lines[1])
data_old = [data_old_1 , data_old_2]

trimestre = ['T1', 'T2', 'T3', 'T4']


def fig_old_drfd_1():
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee) + ' - ' + trimestre[j] for j in range(4)],
                y=data_old_1[i],
                name=str(annee),
                width=0.8,

            )
        )

    fig = go.Figure(data=donnee)

    # Ajout d'un titre
    fig.update_layout(title="Total des publications de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    return fig

def fig_old_drfd_1_tri():
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee) + ' - ' + trimestre[j] for j in range(4)],
                y=data_old_1[i],
                name=str(annee),
                width=0.8,
                marker=dict(color=couleurs_trimestres),
            )
        )

    fig = go.Figure(data=donnee)

    # Ajout d'un titre
    fig.update_layout(title="Total des publications de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    return fig

def fig_old_drfd_1_tot():
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee)],
                y=[sum(data_old_1[i])],
                name=str(annee),
            )
        )

    fig = go.Figure(data=donnee)

    # Ajout d'un titre
    fig.update_layout(title="Total des publications de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    # barmode="group")

    return fig

def fig_old_drfd_2():
    fig = go.Figure()
    for i in range(len(annees)):

        fig.add_trace(go.Scatter(x=trimestre, y=data_old_1[i], name="Année " + str(annees[i])))

    fig.update_layout(title="Total des publications de 2015 à 2019, comparaison annuelle par trimestre",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    return fig

def fig_old_drfd_3():
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee) + ' - ' + trimestre[j] for j in range(4)],
                y=data_old_2[i],
                name=str(annee),
                width=0.8,

            )
        )

    fig = go.Figure(data=donnee)

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants de 2015 à 2019, vision annuelle",
                      xaxis_title="Années",
                      yaxis_title=titre[1])

    return fig


def fig_old_drfd_3_tri():
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee) + ' - ' + trimestre[j] for j in range(4)],
                y=data_old_2[i],
                name=str(annee),
                width=0.8,
                marker=dict(color=couleurs_trimestres),

            )
        )

    fig = go.Figure(data=donnee)

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[1])

    return fig

def fig_old_drfd_3_tot():
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee)],
                y=[sum(data_old_2[i])],
                name=str(annee),
            )
        )

    fig = go.Figure(data=donnee)

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig


def fig_old_drfd_4():
    fig = go.Figure()

    # encoder les trimestre : passer d'un String à une valeur int
    label_encoder = LabelEncoder()
    trimestre_encoded = label_encoder.fit_transform([i + 1 for i, _ in enumerate(trimestre)])


    for i in range(len(annees)):

        fig.add_trace(go.Scatter(x=trimestre_encoded, y=data_old_2[i], name="Année " + str(annees[i])))

    # Générer les données moyennes
    y = data_moy(data_old_1)

    # Courbe pour fitter les points
    degree = 3 
    model = LinearRegression()
    model.fit(np.vander(trimestre_encoded, degree + 1), y)

    # Generation des valeurs préditent
    x_pred = np.arange(min(trimestre_encoded), max(trimestre_encoded), 0.1) 
    y_pred = model.predict(np.vander(x_pred, degree + 1))  

    # Ajouter la régression polynomiale
    fig.add_trace(go.Scatter(x=x_pred, y=y_pred, name="Régression", line=dict(dash='dash', color='black'), marker=dict(size=10), visible='legendonly'))



    fig.update_layout(title="Nombre de doctorants de " + str(config.liste_annee[-1]) + " à " + str(config.liste_annee[0]) + ", comparaison annuelle par trimestre",
                      xaxis_title="Années",
                      yaxis_title=titre[1],
                    xaxis = dict(
                    tickvals=[0, 1, 2, 3],
                    ticktext=['T1', 'T2', 'T3', 'T4'])
        )
    return fig