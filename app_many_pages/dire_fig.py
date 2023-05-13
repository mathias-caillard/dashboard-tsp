from app_many_pages import config
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as subplt
import data

#Import des couleurs
couleurs = config.colors_dept

#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)

#Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 3    #Nombre de lignes de données
sheetName = '2023-DIRE-Tri'   #Nom de la feuille
débutColonneData = 4    #Première colonne de données
FinColonneData = 33  #Dernière colonne de données
df = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

#Récupération des titres des colonnes
x_axis = df.columns.tolist()



#définition de l'axe des ordnnées
y_axis = []
for indicateur in df.Indicateur :
    y_axis.append(indicateur)

premiereColonneAnnuelle = 8
indice_annuelle = []
for i in range(6):
    j_annuel = 5*i + premiereColonneAnnuelle
    indice_annuelle.append((j_annuel))


#Regroupement des titres et valeurs voulues pour tracer les figures
labels_annuel, labels_trim = [], []
valeur_annuelle1, valeur_annuelle3 =  [], []
valeur_trim1, valeur_trim3 = [], []

for j in indice_annuelle:
    labels_annuel.append(x_axis[j])
    valeur_annuelle1.append(df.iloc[0,j])
    valeur_annuelle3.append((df.iloc[2,j]))
    valeur_trim1_j, valeur_trim3_j, label_trim_j =[], [], []
    for i in range(4):
        label_trim_j.append(x_axis[j+i-4])
        valeur_trim1_j.append(df.iloc[0,j+i-4])
        valeur_trim3_j.append(df.iloc[2, j + i - 4])
    valeur_trim1.append(valeur_trim1_j)
    valeur_trim3.append(valeur_trim3_j)
    labels_trim.append(label_trim_j)


departement = ['ARTEMIS', 'CITI', 'EPH', 'INF', 'RS2M', 'RST']
trimestre = ['Trimestre 1', 'Trimestre 2', 'Trimestre 3', 'Trimestre 4']

def fig_dire_1() : 
    #Création d'une figure avec 6 sous-figure pour y placer des histogrammes
    fig1 = subplt.make_subplots(rows=1, cols=6, shared_yaxes=True, horizontal_spacing=0.05)

    #Ajout des histogrammes dans chacune des sous-figures
    for i in range(6):
        labels_i = labels_trim[i]
        valeur_i = valeur_trim1[i]
        fig1.add_trace(go.Bar(x=labels_i, y=valeur_i, name=labels_i[0][:-3],
                              marker=dict(color = 4*[couleurs[i]])), row=1, col=i+1)

    # Personnaliser l'apparence du graphique
    fig1.update_layout(title='Suivi des contrats de recherche')

    return fig1



def fig_dire_2():

    #Création d'une figure avec 4 sous-figure pour y placer des histogrammes
    #fig2 = subplt.make_subplots(rows=1, cols=4, shared_yaxes=True, horizontal_spacing=0.05)
    fig2 = go.Figure()
    #Ajout des histogrammes dans chacune des sous-figures

    for i in range(4):
        labels_i = []
        valeur_i = []
        for j in range(6):
            labels_i.append(labels_trim[j][i])
            valeur_i.append((valeur_trim1[j][i]))

    for i in range(6):
        fig2.add_trace(go.Bar(x=trimestre, y=valeur_trim1[i], name= departement[i],
                              marker=dict(color = couleurs[i])))

    # Personnaliser l'apparence du graphique
    fig2.update_layout(title='Suivi des contrats de recherche, vision trimestrielle')

    return fig2

def fig_dire_3():
    fig3 = go.Figure()
    labels = []
    valeur= []
    for i in range(4):
        labels_i = []
        valeur_i = []
        for j in range(6):
            labels_i.append(labels_trim[j][i])
            valeur_i.append((valeur_trim1[j][i]))
        labels.append( "ECOLE T" + str(i+1))
        valeur.append(sum(valeur_i))
    fig3.add_trace(go.Scatter(x=labels, y=valeur))

    # Personnaliser l'apparence du graphique
    fig3.update_layout(title='Suivi des contrats de recherche, total école')
    return fig3



def fig_dire_4():
    fig4 = go.Figure(data=[go.Pie(labels=labels_annuel, values=valeur_annuelle3,
                                  marker_colors=couleurs)],)


    # Personnaliser l'apparence du graphique
    fig4.update_layout(title='Contribution au financement de l\'école')
    return fig4



sheetName = data.sheet_names[0]
lines = data.dire_ligne
titre = data.extract_titre(data.dire_ligne)
annees = data.annees
data_old_1 = data.extract_data(sheetName, lines[0])
data_old_2 = data.extract_data(sheetName, lines[1])
data_old_3 = data.extract_data(sheetName, lines[2])


def fig_old_dire_1():
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
    fig.update_layout(title="CA sur contrats de recherche de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    # barmode="group")

    return fig

def fig_old_dire_2():
    fig = go.Figure()
    for i in range(len(annees)):

        fig.add_trace(go.Scatter(x=trimestre, y=data_old_1[i], name="Année " + str(annees[i])))

    fig.update_layout(title="CA sur contrats de recherche de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    return fig

def fig_old_dire_3():
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
    fig.update_layout(title="Brevets et logiciels déposés de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig

def fig_old_dire_4():
    fig = go.Figure()
    for i in range(len(annees)):

        fig.add_trace(go.Scatter(x=trimestre, y=data_old_2[i], name="Année " + str(annees[i])))

    fig.update_layout(title="Brevets et logiciels déposés de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    return fig

def fig_old_dire_5():
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee) + ' - ' + trimestre[j] for j in range(4)],
                y=data_old_3[i],
                name=str(annee),
                width=0.8,

            )
        )

    fig = go.Figure(data=donnee)

    # Ajout d'un titre
    fig.update_layout(title="Contribution au financement de l\'école de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    # barmode="group")

    return fig

def fig_old_dire_6():
    fig = go.Figure()
    for i in range(len(annees)):

        fig.add_trace(go.Scatter(x=trimestre, y=data_old_3[i], name="Année " + str(annees[i])))

    fig.update_layout(title="Contribution au financement de l\'école de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    return fig