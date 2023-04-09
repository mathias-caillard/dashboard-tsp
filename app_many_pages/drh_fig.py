
import pandas as pd
import plotly.graph_objects as go
from app_many_pages import config


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


def fig_drh_1():
    # Créer une figure avec des sous-figures pour chaque bâton
    fig = go.Figure()

    # Ajouter chaque bâton à la figure
    for col_name in df.columns[débutColonneData: FinColonneData + 1]:
        fig.add_trace(go.Bar(x=[col_name], y=[df[col_name].iloc[1]], name=col_name))

    #Ajout d'un titre
    fig.update_layout(title = "Les ressources humaines à Télécom Sudparis", xaxis_title='Départements', yaxis_title = y_axis[1])

    return fig

def fig_drh_2():
    #Graphique en camenbert
    values = df.iloc[1][débutColonneData: FinColonneData + 1]

    fig2 = go.Figure(data=[go.Pie(labels=x_axis, values=values)])

    # Personnaliser l'apparence du graphique
    fig2.update_layout(title='Répartition des permanents')

    return fig2