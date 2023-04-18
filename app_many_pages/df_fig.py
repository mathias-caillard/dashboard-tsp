
from app_many_pages import config
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import effectifs

#Import des couleurs
couleurs = config.colors_dept

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

effectif = effectifs.effectif

def fig_df_1() :


    #création de la figure
    fig = px.bar(df, x = "trimestre", y = y_axis)

    #Ajout d'un titre
    fig.update_layout(title = "Nombre d'étudiants à Télécom Sudparis")

    return fig


#Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 1    #Nombre de lignes de données
sheetName = '2023-DF-Annuel'   #Nom de la feuille
débutColonneData = 4
finColonneData = 10
df2 = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

#définition de l'axe des abscisses
x_axis_annuel = df2.columns.tolist()[débutColonneData: finColonneData + 1]

#définition de l'axe des ordnnées
y_axis_annuel = []
for indicateur in df2.Indicateur :
    y_axis_annuel.append(indicateur)

valeur_annuel = []
for i in range(débutColonneData, finColonneData):
    valeur_annuel.append(df2.iloc[0, i])
def fig_df_2():
    fig = go.Figure()

    # Ajouter chaque bâton à la figure
    i = 0
    for col_name in df2.columns[débutColonneData: finColonneData + 1]:
        taille = str(int(effectif[i]))
        fig.add_trace(go.Bar(x=[col_name + " (" + taille + ")"], y=[df2[col_name].iloc[0]],
                             name=col_name, marker=dict(color = [couleurs[i]])))  # effectif du département entre parenthèse
        i += 1

    # Ajout d'un titre
    fig.update_layout(title="Nombre d\'UP produites par Télécom SudParis", xaxis_title='Départements',
                      yaxis_title=y_axis_annuel[0])

    return fig

