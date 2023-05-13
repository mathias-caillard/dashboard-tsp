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


valeur_drh_eph=valeur_tri[2]
valeur_dire1_eph = valeur_trim1[2]
valeur_dire3_eph = valeur_trim3[2]



list_fig_eph=[]
for i in range(4):
    fig_eph = go.Figure()
    fig_eph.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][2]))

    fig_eph.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_eph.append(fig_eph)

def fig_eph_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_eph, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à EPH', yaxis_title=y_axis_tri[0])

    return fig

def fig_eph_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_eph, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à EPH', yaxis_title=y_axis_dire[0])

    return fig

def fig_eph_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_eph, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à EPH', yaxis_title=y_axis_dire[2])

    return fig

def fig_eph_4():
    fig = list_fig_eph[0]
    fig.update_layout(title='Les dépenses de vacataires à EPH')
    return fig

def fig_eph_5():
    fig = list_fig_eph[1]
    fig.update_layout(title='Les ressources propres à EPH')
    return fig

def fig_eph_6():
    fig = list_fig_eph[2]
    fig.update_layout(title='Les ressources d\'état à EPH')
    return fig

def fig_eph_7():
    fig = list_fig_eph[3]
    fig.update_layout(title='Le total des dépenses à EPH')
    return fig

sheetName = data.sheet_names[3]
list_line = data.liste_lignes
titre = data.extract_titre(list_line)
annees = data.annees
data_old = data.extract_data_numerous(sheetName, list_line)

list_old_fig_eph=[]
for k in range(len(list_line)):
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee) + ' - ' + trimestre[j] for j in range(4)],
                y=data_old[k][i],
                name=str(annee),
                width=0.8,

            )
        )
    fig_baton = go.Figure(data=donnee)
    list_old_fig_eph.append(fig_baton)

    fig = go.Figure()
    for i in range(len(annees)):
        fig.add_trace(go.Scatter(x=trimestre, y=data_old[k][i], name="Année " + str(annees[i])))
    list_old_fig_eph.append(fig)


def fig_old_df_eph_1():
    fig = list_old_fig_eph[0]

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à EPH de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig

def fig_old_df_eph_2():
    fig = list_old_fig_eph[1]
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à EPH de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    return fig

def fig_old_daf_eph_1():

    fig = list_old_fig_eph[2]

    # Ajout d'un titre
    fig.update_layout(title="Dépenses de vacataires à EPH de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig

def fig_old_daf_eph_2():
    fig = list_old_fig_eph[3]
    fig.update_layout(title="Dépenses de vacataires à EPH de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    return fig

def fig_old_daf_eph_3():
    fig = list_old_fig_eph[4]

    # Ajout d'un titre
    fig.update_layout(title="Ressources propres totales à EPH de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    # barmode="group")

    return fig

def fig_old_daf_eph_4():
    fig = list_old_fig_eph[5]

    fig.update_layout(title="Ressources propres totales à EPH de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    return fig

def fig_old_daf_eph_5():
    fig = list_old_fig_eph[6]

    # Ajout d'un titre
    fig.update_layout(title="Total des dépenses hors permanents et vacataires à EPH de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    # barmode="group")

    return fig

def fig_old_daf_eph_6():
    fig = list_old_fig_eph[7]

    fig.update_layout(title="Total des dépenses hors permanents et vacataires à EPH de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    return fig


def fig_old_dire_eph_1():
    fig = list_old_fig_eph[8]

    # Ajout d'un titre
    fig.update_layout(title="CA sur contrats de recherche à EPH de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_eph_2():
    fig = list_old_fig_eph[9]
    fig.update_layout(title="CA sur contrats de recherche à EPH de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_eph_3():
    fig = list_old_fig_eph[10]

    # Ajout d'un titre
    fig.update_layout(title="Brevets et logiciels déposés à EPH de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    # barmode="group")

    return fig

def fig_old_dire_eph_4():
    fig = list_old_fig_eph[11]

    fig.update_layout(title="Brevets et logiciels déposés à EPH de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    return fig

def fig_old_dire_eph_5():
    fig = list_old_fig_eph[12]

    # Ajout d'un titre
    fig.update_layout(title="Contribution au financement de l\'école à EPH de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    # barmode="group")

    return fig

def fig_old_dire_eph_6():
    fig = list_old_fig_eph[13]

    fig.update_layout(title="Contribution au financement de l\'école à EPH de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    return fig

def fig_old_drfd_eph_1():
    fig = list_old_fig_eph[14]

    # Ajout d'un titre
    fig.update_layout(title="Total des publications à EPH de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[7])

    return fig

def fig_old_drfd_eph_2():
    fig = list_old_fig_eph[15]

    fig.update_layout(title="Total des publications à EPH de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[7])
    return fig

def fig_old_drfd_eph_3():
    fig = list_old_fig_eph[16]

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants à EPH de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    # barmode="group")

    return fig

def fig_old_drfd_eph_4():
    fig = list_old_fig_eph[17]

    fig.update_layout(title="Nombre de doctorants à EPH de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    return fig

def fig_old_drh_eph_1():
    fig = list_old_fig_eph[18]

    # Ajout d'un titre
    fig.update_layout(title="Permanents en ETPT à EPH de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[9])

    return fig

def fig_old_drh_eph_2():
    fig = list_old_fig_eph[19]

    fig.update_layout(title="Permanents en ETPT à EPH de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[9])
    return fig

def fig_old_drh_eph_3():
    fig = list_old_fig_eph[20]

    # Ajout d'un titre
    fig.update_layout(title="Non-permanents en ETPT à EPH de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig

def fig_old_drh_eph_4():
    fig = list_old_fig_eph[21]

    fig.update_layout(title="Non-permanents en ETPT à EPH de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig
