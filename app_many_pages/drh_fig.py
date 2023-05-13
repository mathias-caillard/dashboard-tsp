
import pandas as pd
import plotly.graph_objects as go
from app_many_pages import config
import data


#Import des couleurs
couleurs_dept = config.colors_dept
couleurs = config.colors_dir[0:5]
couleurs += couleurs_dept

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
    i=0
    for col_name in df.columns[débutColonneData: FinColonneData + 1]:
        fig.add_trace(go.Bar(x=[col_name], y=[df[col_name].iloc[1]], name=col_name
                             ,marker=dict(color = [couleurs[i]])))
        i+=1
    fig.add_trace(go.Bar(x=['ECOLE'], y=[sum([(df.iloc[1,j]) for j in range(débutColonneData, FinColonneData+1)])],
                         name='ECOLE', marker=dict(color = [couleurs[i]])))

    #Ajout d'un titre
    fig.update_layout(title = "Les ressources humaines à Télécom Sudparis", xaxis_title='Départements', yaxis_title = y_axis[1])

    return fig

def fig_drh_2():
    #Graphique en camenbert
    values = df.iloc[1][débutColonneData: FinColonneData + 1]

    fig2 = go.Figure(data=[go.Pie(labels=x_axis, values=values
                                  , marker_colors=couleurs)])

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
x_axis_tri = df2.columns.tolist()[débutColonneData2: FinColonneData2 + 1]

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
        fig3.add_trace(go.Bar(x=trimestre, y=valeur_tri[i], name= departement[i]
                              , marker=dict(color = 4*[couleurs_dept[i]])))

    fig3.update_layout(title='Nombre de non-permanents en ETPT', xaxis_title='Trimestre', yaxis_title = y_axis_tri[0])

    return fig3

def fig_drh_4():
    fig = go.Figure()
    for i in range(7):
        fig.add_trace(go.Scatter(x=trimestre, y=valeur_tri[i], name=departement[i]
                                 , marker=dict(color = 4*[couleurs_dept[i]])
                                 , line=dict(color = couleurs_dept[i])))

    fig.update_layout(title='Evolution temporelle du nombre de non-permanents en ETPT', yaxis_title=y_axis_tri[0])
    return fig


sheetName = data.sheet_names[0]
lines = data.drh_ligne
titre = data.extract_titre(data.drh_ligne)
annees = data.annees
data_old_1 = data.extract_data(sheetName, lines[0])
data_old_2 = data.extract_data(sheetName, lines[1])

trimestre = ['T1', 'T2', 'T3', 'T4']


def fig_old_drh_1():
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
    fig.update_layout(title="Permanents en ETPT de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    # barmode="group")

    return fig

def fig_old_drh_2():
    fig = go.Figure()
    for i in range(len(annees)):

        fig.add_trace(go.Scatter(x=trimestre, y=data_old_1[i], name="Année " + str(annees[i])))

    fig.update_layout(title="Permanents en ETPT de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    return fig

def fig_old_drh_3():
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
    fig.update_layout(title="Non-permanents en ETPT de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig

def fig_old_drh_4():
    fig = go.Figure()
    for i in range(len(annees)):

        fig.add_trace(go.Scatter(x=trimestre, y=data_old_2[i], name="Année " + str(annees[i])))

    fig.update_layout(title="Non-permanents en ETPT de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    return fig