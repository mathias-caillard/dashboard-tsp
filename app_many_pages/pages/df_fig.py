
from app_many_pages import config
import pandas as pd
import plotly.express as px


def fig_nb_etudiants() : 
    #Chemin du fichier excel défini dans config.py
    excel_path = config.excel_path

    #afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
    pd.set_option('display.max_columns', None)

    #Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
    ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
    nombreLignesData = 4    #Nombre de lignes de données
    sheetName = '2023-DF-Tri'   #Nom de la feuille
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
    fig.update_layout(title = "Nombre d'étudiants à Télécom Sudparis")

    return fig
