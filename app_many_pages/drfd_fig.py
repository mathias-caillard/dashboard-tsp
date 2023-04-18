from app_many_pages import config, effectifs
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random

#Import des couleurs
couleurs = config.colors_dept

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
        fig.add_trace(go.Bar(x=[col_name  + " (" + taille + ")"], y=[df[col_name].iloc[0]], name=col_name,
                             marker=dict(color = [couleurs[i]])))  #effectif du département entre parenthèse
        i+=1

    #Ajout d'un titre
    fig.update_layout(title = "Chiffres sur la recherche à Télécom Sudparis", xaxis_title='Départements', yaxis_title = y_axis[0])

    return fig


def fig_drfd_2() : 

    # Créer une figure avec des sous-figures pour chaque bâton
    fig2 = go.Figure()

    # Ajouter chaque bâton à la figure
    i=0
    for col_name in df.columns[débutColonneData: FinColonneData + 1]:
        taille = str(int(effectif[i]))
        fig2.add_trace(go.Bar(x=[col_name  + " (" + taille + ")"], y=[df[col_name].iloc[1]], name=col_name,
                              marker=dict(color = [couleurs[i]])))    #effectif du département entre parenthèse
        i+=1

    #Ajout d'un titre
    fig2.update_layout(title = "Nombre de doctorants à Télécom SudParis", xaxis_title='Départements', yaxis_title = y_axis[1])

    return fig2


def fig_drfd_3():
    #Figure pour l'évolution sur l'ecole
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=titre_années, y=donnees_ecole))


    #Ajout d'un titre
    fig3.update_layout(title = "Evolution des publications dans le temps" ,xaxis_title='Années', yaxis_title = y_axis[0])

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
    fig4.update_layout(title = "Evolution du nombre de doctorants dans le temps", xaxis_title='Années', yaxis_title = y_axis[1])

    return fig4