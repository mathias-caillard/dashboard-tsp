
import pandas as pd
import plotly.graph_objects as go
from app_many_pages import config

#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)

#Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 1    #Nombre de lignes de données
sheetName = '2023-DAF-Annuel'   #Nom de la feuille
débutColonneData = 4    #Première colonne de données
FinColonneData = 9  #Dernière colonne de données
df = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

'''
#ajouter d'une colonne artificielle "trimestre" dans le dataframe facilitant la création du graphe associé
valeurNouvelleColonne = []
for i in range(débutColonneData, FinColonneData ) :
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
'''



#définition de l'axe des abscisses
x_axis = df.columns.tolist()[débutColonneData: FinColonneData + 1]



#définition de l'axe des ordnnées
y_axis = []
for indicateur in df.Indicateur :
    y_axis.append(indicateur)


def fig_daf_1():
    # Créer une figure avec des sous-figures pour chaque bâton
    fig = go.Figure()

    # Ajouter chaque bâton à la figure
    for col_name in df.columns[débutColonneData: FinColonneData + 1]:
        fig.add_trace(go.Bar(x=[col_name], y=[df[col_name].iloc[0]], name=col_name))

    #Calcul de la moyenne
    mean_value = df.mean(axis=1, numeric_only=True).iloc[0]

    # Ajouter la ligne moyenne à la figure
    fig.add_trace(go.Scatter(x=df.columns[débutColonneData: FinColonneData + 1], y=[mean_value] * (FinColonneData + 1 - débutColonneData), mode='lines', name='Moyenne'))

    #Ajout d'un titre
    fig.update_layout(title = "Chiffre d\'affaire de la recherche à Télécom Sudparis", xaxis_title='Départements', yaxis_title = y_axis[0])

    return fig
