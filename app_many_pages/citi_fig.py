import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd
import data
from drh_fig import trimestre, valeur_tri,y_axis_tri
from dire_fig import valeur_trim1, valeur_trim3, y_axis as y_axis_dire
from daf_fig import valeur_tri as valeur_daf, y_axis_tri as y_axis_daf

valeur_drh_citi=valeur_tri[1]
valeur_dire1_citi = valeur_trim1[1]
valeur_dire3_citi = valeur_trim3[1]



list_fig_citi=[]
for i in range(4):
    fig_citi = go.Figure()
    fig_citi.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][1]))

    fig_citi.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_citi.append(fig_citi)

def fig_citi_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_citi, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à CITI', yaxis_title=y_axis_tri[0])

    return fig

def fig_citi_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_citi, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à CITI', yaxis_title=y_axis_dire[0])

    return fig

def fig_citi_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_citi, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à CITI', yaxis_title=y_axis_dire[2])

    return fig

def fig_citi_4():
    fig = list_fig_citi[0]
    fig.update_layout(title='Les dépenses de vacataires à CITI')
    return fig

def fig_citi_5():
    fig = list_fig_citi[1]
    fig.update_layout(title='Les ressources propres à CITI')
    return fig
def fig_citi_6():
    fig = list_fig_citi[2]
    fig.update_layout(title='Les ressources d\'état à CITI')
    return fig
def fig_citi_7():
    fig = list_fig_citi[3]
    fig.update_layout(title='Le total des dépenses à CITI')
    return fig


sheetName = data.sheet_names[2]
list_line = data.liste_lignes
titre = data.extract_titre(list_line)
annees = data.annees
data_old = data.extract_data_numerous(sheetName, list_line)

list_old_fig_citi=[]
for k in range(len(list_line)):
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee) + ' - ' + trimestre[j] for j in range(4)],
                y=data_old[k][i],
                name=str(annee),
                width=0.8,
                marker=dict(color="blue")
            )
        )
    fig_baton = go.Figure(data=donnee)
    list_old_fig_citi.append(fig_baton)

    fig = go.Figure()
    for i in range(len(annees)):
        fig.add_trace(go.Scatter(x=trimestre, y=data_old[k][i], name="Année " + str(annees[i])))
    list_old_fig_citi.append(fig)


def fig_old_df_citi_1():
    fig = list_old_fig_citi[0]

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à CITI de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig

def fig_old_df_citi_2():
    fig = list_old_fig_citi[1]
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à CITI de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    return fig

def fig_old_daf_citi_1():

    fig = list_old_fig_citi[2]

    # Ajout d'un titre
    fig.update_layout(title="Dépenses de vacataires à CITI de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig

def fig_old_daf_citi_2():
    fig = list_old_fig_citi[3]
    fig.update_layout(title="Dépenses de vacataires à CITI de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    return fig

def fig_old_daf_citi_3():
    fig = list_old_fig_citi[4]

    # Ajout d'un titre
    fig.update_layout(title="Ressources propres totales à CITI de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    # barmode="group")

    return fig

def fig_old_daf_citi_4():
    fig = list_old_fig_citi[5]

    fig.update_layout(title="Ressources propres totales à CITI de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    return fig

def fig_old_daf_citi_5():
    fig = list_old_fig_citi[6]

    # Ajout d'un titre
    fig.update_layout(title="Total des dépenses hors permanents et vacataires à CITI de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    # barmode="group")

    return fig

def fig_old_daf_citi_6():
    fig = list_old_fig_citi[7]

    fig.update_layout(title="Total des dépenses hors permanents et vacataires à CITI de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    return fig


def fig_old_dire_citi_1():
    fig = list_old_fig_citi[8]

    # Ajout d'un titre
    fig.update_layout(title="CA sur contrats de recherche à CITI de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_citi_2():
    fig = list_old_fig_citi[9]
    fig.update_layout(title="CA sur contrats de recherche à CITI de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_citi_3():
    fig = list_old_fig_citi[10]

    # Ajout d'un titre
    fig.update_layout(title="Brevets et logiciels déposés à CITI de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    # barmode="group")

    return fig

def fig_old_dire_citi_4():
    fig = list_old_fig_citi[11]

    fig.update_layout(title="Brevets et logiciels déposés à CITI de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    return fig

def fig_old_dire_citi_5():
    fig = list_old_fig_citi[12]

    # Ajout d'un titre
    fig.update_layout(title="Contribution au financement de l\'école à CITI de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    # barmode="group")

    return fig

def fig_old_dire_citi_6():
    fig = list_old_fig_citi[13]

    fig.update_layout(title="Contribution au financement de l\'école à CITI de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    return fig

def fig_old_drfd_citi_1():
    fig = list_old_fig_citi[14]

    # Ajout d'un titre
    fig.update_layout(title="Total des publications à CITI de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[7])

    return fig

def fig_old_drfd_citi_2():
    fig = list_old_fig_citi[15]

    fig.update_layout(title="Total des publications à CITI de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[7])
    return fig

def fig_old_drfd_citi_3():
    fig = list_old_fig_citi[16]

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants à CITI de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    # barmode="group")

    return fig

def fig_old_drfd_citi_4():
    fig = list_old_fig_citi[17]

    fig.update_layout(title="Nombre de doctorants à CITI de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    return fig

def fig_old_drh_citi_1():
    fig = list_old_fig_citi[18]

    # Ajout d'un titre
    fig.update_layout(title="Permanents en ETPT à CITI de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[9])

    return fig

def fig_old_drh_citi_2():
    fig = list_old_fig_citi[19]

    fig.update_layout(title="Permanents en ETPT à CITI de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[9])
    return fig

def fig_old_drh_citi_3():
    fig = list_old_fig_citi[20]

    # Ajout d'un titre
    fig.update_layout(title="Non-permanents en ETPT à CITI de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig

def fig_old_drh_citi_4():
    fig = list_old_fig_citi[21]

    fig.update_layout(title="Non-permanents en ETPT à CITI de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig
