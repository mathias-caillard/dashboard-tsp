
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
    fig.add_trace(go.Bar(x=['ECOLE'], y=[sum([(df.iloc[1,j]) for j in range(débutColonneData, FinColonneData+1)])], name='ECOLE'))

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


# Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres2 = 0  # Numérotation comme dans les liste, matrices...
nombreLignesData2 = 1  # Nombre de lignes de données
sheetName2 = '2023-DRH-Tri'  # Nom de la feuille
débutColonneData2 = 4  # Première colonne de données
FinColonneData2 = 31  # Dernière colonne de données
df2 = pd.read_excel(excel_path, sheet_name=sheetName2, header=ligneDesTitres2, nrows=nombreLignesData2)

# définition de l'axe des abscisses
x_axis_tri = df.columns.tolist()[débutColonneData2: FinColonneData2 + 1]

departement = ['ARTEMIS', 'CITI', 'EPH', 'INF', 'RS2M', 'RST', 'ECOLE']
trimestre = ['Trimestre 1', 'Trimestre 2', 'Trimestre 3', 'Trimestre 4']

valeur_tri = []
for i in range(7):
    valeur_tri_i = []
    for j in range(4):
        valeur_tri_i.append(df2.iloc[0, débutColonneData2 + 4 * i + j])
    valeur_tri.append(valeur_tri_i)

# définition de l'axe des ordnnées
y_axis_tri = []
for indicateur in df2.Indicateur:
    y_axis_tri.append(indicateur)
def fig_drh_3():

    fig3 = go.Figure()

    for i in range(7):
        fig3.add_trace(go.Bar(x=trimestre, y=valeur_tri[i], name= departement[i]))

    fig3.update_layout(title='Nombre de non-permanents en ETPT', xaxis_title='Trimestre', yaxis_title = y_axis_tri[0])

    return fig3

def fig_drh_4():
    fig = go.Figure()
    for i in range(7):
        fig.add_trace(go.Scatter(x=trimestre, y=valeur_tri[i], name=departement[i]))

    fig.update_layout(title='Evolution temporelle du nombre de non-permanents en ETPT', yaxis_title=y_axis_tri[0])
    return fig