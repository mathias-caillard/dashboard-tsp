
import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as subplt
from app_many_pages import config
from app_many_pages import effectifs

effectif = effectifs.effectif

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
    i=0
    for col_name in df.columns[débutColonneData: FinColonneData + 1]:
        fig.add_trace(go.Bar(x=[col_name], y=[df[col_name].iloc[0]], name=col_name + " (" + str(int(effectif[i])) + ")"))
        i+=1

    #Calcul de la moyenne
    mean_value = df.mean(axis=1, numeric_only=True).iloc[0]

    # Ajouter la ligne moyenne à la figure
    fig.add_trace(go.Scatter(x=df.columns[débutColonneData: FinColonneData + 1], y=[mean_value] * (FinColonneData + 1 - débutColonneData), mode='lines', name='Moyenne'))

    #Ajout d'un titre
    fig.update_layout(title = "Chiffre d\'affaire de la recherche à Télécom Sudparis", xaxis_title='Départements', yaxis_title = y_axis[0])

    return fig


#Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 4    #Nombre de lignes de données
sheetName = '2023-DAF-Tri'   #Nom de la feuille
débutColonneData = 4    #Première colonne de données
FinColonneData = 33  #Dernière colonne de données
df2 = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

#définition de l'axe des abscisses
x_axis_tri = df2.columns.tolist()[débutColonneData: FinColonneData + 1]

y_axis_tri = []
for indicateur in df2.Indicateur :
    y_axis_tri.append(indicateur)


#Récupération des données
labels_tri=[]
labels_annuel=[]
valeur_tri = []
valeur_annuel = []
for i in range(4):
    valeur_annuel_indic=[]
    valeur_tri_indic=[]

    for j in range(6):
        valeur_j_tri=[]
        valeur_j_annuel=[]
        for k in range(4):
            valeur_j_tri.append(df2.iloc[i, débutColonneData + 5*j +k])
        valeur_tri_indic.append((valeur_j_tri))
        valeur_j_annuel.append(df2.iloc[i, débutColonneData + 5*j + 4])
        labels_annuel.append(x_axis_tri[5*j + 4])
    valeur_tri.append(valeur_tri_indic)


for j in range(6):
    labels_j=[]
    for k in range(4):
        labels_j.append(x_axis_tri[5*j + k])
    labels_tri.append(labels_j)


#Transposition des données
valeur_tri_dep=[]
for i in range(4):
    valeur_dep=[]
    for j in range(4):
        valeur_dep_j=[]
        for k in range(6):
            valeur_dep_j.append(valeur_tri[i][k][j])
        valeur_dep.append(valeur_dep_j)
    valeur_tri_dep.append(valeur_dep)

labels_tri_dep=[]
for j in range(4):
    labels_dep_j = []
    for k in range(6):
        labels_dep_j.append(labels_tri[k][j])
    labels_tri_dep.append(labels_dep_j)


def fig_daf_2():
    # Création d'une figure avec 6 sous-figure pour y placer des histogrammes
    fig2 = subplt.make_subplots(rows=1, cols=6, shared_yaxes=True, horizontal_spacing=0.05)

    # Ajout des histogrammes dans chacune des sous-figures
    for i in range(6):
        labels_i = labels_tri[i]
        valeur_i = valeur_tri[0][i]
        fig2.add_trace(go.Bar(x=labels_i, y=valeur_i, name=labels_annuel[i].replace('Année', '') + " (" + str(int(effectif[i])) + ")"), row=1, col=i + 1)

    # Personnaliser l'apparence du graphique
    fig2.update_layout(title='Dépenses de vacataires', yaxis_title = y_axis_tri[0])

    return fig2

def fig_daf_3():
    # Création d'une figure avec 6 sous-figure pour y placer des histogrammes
    fig3 = subplt.make_subplots(rows=1, cols=4, shared_yaxes=True, horizontal_spacing=0.05)

    # Ajout des histogrammes dans chacune des sous-figures
    for i in range(4):
        labels_i = labels_tri_dep[i]
        valeur_i = valeur_tri_dep[0][i]
        fig3.add_trace(go.Bar(x=labels_i, y=valeur_i, name="Trimestre " + str(i+1)), row=1, col=i + 1)

    # Personnaliser l'apparence du graphique
    fig3.update_layout(title='Dépenses de vacataires, vision trimestrielle', yaxis_title=y_axis_tri[0])

    return fig3

def fig_daf_4():
    # Création d'une figure avec 6 sous-figure pour y placer des histogrammes
    fig = subplt.make_subplots(rows=1, cols=6, shared_yaxes=True, horizontal_spacing=0.05)

    # Ajout des histogrammes dans chacune des sous-figures
    for i in range(6):
        labels_i = labels_tri[i]
        valeur_i = valeur_tri[1][i]
        fig.add_trace(go.Bar(x=labels_i, y=valeur_i,
                              name=labels_annuel[i].replace('Année', '') + " (" + str(int(effectif[i])) + ")"), row=1,
                       col=i + 1)

    # Personnaliser l'apparence du graphique
    fig.update_layout(title='Ressources propres', yaxis_title=y_axis_tri[1])

    return fig

def fig_daf_5():
    # Création d'une figure avec 6 sous-figure pour y placer des histogrammes
    fig = subplt.make_subplots(rows=1, cols=4, shared_yaxes=True, horizontal_spacing=0.05)

    # Ajout des histogrammes dans chacune des sous-figures
    for i in range(4):
        labels_i = labels_tri_dep[i]
        valeur_i = valeur_tri_dep[1][i]
        fig.add_trace(go.Bar(x=labels_i, y=valeur_i, name="Trimestre " + str(i + 1)), row=1, col=i + 1)

    # Personnaliser l'apparence du graphique
    fig.update_layout(title='Ressources propres, vision trimestrielle', yaxis_title=y_axis_tri[1])

    return fig

def fig_daf_6():
    # Création d'une figure avec 6 sous-figure pour y placer des histogrammes
    fig = subplt.make_subplots(rows=1, cols=6, shared_yaxes=True, horizontal_spacing=0.05)

    # Ajout des histogrammes dans chacune des sous-figures
    for i in range(6):
        labels_i = labels_tri[i]
        valeur_i = valeur_tri[2][i]
        fig.add_trace(go.Bar(x=labels_i, y=valeur_i,
                              name=labels_annuel[i].replace('Année', '') + " (" + str(int(effectif[i])) + ")"), row=1,
                       col=i + 1)

    # Personnaliser l'apparence du graphique
    fig.update_layout(title='Ressources d\'état', yaxis_title=y_axis_tri[2])

    return fig

def fig_daf_7():
    # Création d'une figure avec 6 sous-figure pour y placer des histogrammes
    fig = subplt.make_subplots(rows=1, cols=4, shared_yaxes=True, horizontal_spacing=0.05)

    # Ajout des histogrammes dans chacune des sous-figures
    for i in range(4):
        labels_i = labels_tri_dep[i]
        valeur_i = valeur_tri_dep[2][i]
        fig.add_trace(go.Bar(x=labels_i, y=valeur_i, name="Trimestre " + str(i + 1)), row=1, col=i + 1)

    # Personnaliser l'apparence du graphique
    fig.update_layout(title='Ressources d\'état, vision trimestrielle', yaxis_title=y_axis_tri[2])

    return fig


def fig_daf_8():
    # Création d'une figure avec 6 sous-figure pour y placer des histogrammes
    fig = subplt.make_subplots(rows=1, cols=6, shared_yaxes=True, horizontal_spacing=0.05)

    # Ajout des histogrammes dans chacune des sous-figures
    for i in range(6):
        labels_i = labels_tri[i]
        valeur_i = valeur_tri[3][i]
        fig.add_trace(go.Bar(x=labels_i, y=valeur_i,
                              name=labels_annuel[i].replace('Année', '') + " (" + str(int(effectif[i])) + ")"), row=1,
                       col=i + 1)

    # Personnaliser l'apparence du graphique
    fig.update_layout(title='Total des dépenses hors permanents et vacataires', yaxis_title=y_axis_tri[3])

    return fig

def fig_daf_9():
    # Création d'une figure avec 6 sous-figure pour y placer des histogrammes
    fig = subplt.make_subplots(rows=1, cols=4, shared_yaxes=True, horizontal_spacing=0.05)

    # Ajout des histogrammes dans chacune des sous-figures
    for i in range(4):
        labels_i = labels_tri_dep[i]
        valeur_i = valeur_tri_dep[3][i]
        fig.add_trace(go.Bar(x=labels_i, y=valeur_i, name="Trimestre " + str(i + 1)), row=1, col=i + 1)

    # Personnaliser l'apparence du graphique
    fig.update_layout(title='Total des dépenses hors permanents et vacataires, vision trimestrielle', yaxis_title=y_axis_tri[3])

    return fig