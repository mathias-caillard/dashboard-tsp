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


valeur_drh_rs2m=valeur_tri[4]
valeur_dire1_rs2m = valeur_trim1[4]
valeur_dire3_rs2m = valeur_trim3[4]



list_fig_rs2m=[]
for i in range(4):
    fig_rs2m = go.Figure()
    fig_rs2m.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][4]))

    fig_rs2m.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_rs2m.append(fig_rs2m)

def fig_rs2m_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_rs2m, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à RS2M', yaxis_title=y_axis_tri[0])

    return fig

def fig_rs2m_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_rs2m, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à RS2M', yaxis_title=y_axis_dire[0])

    return fig

def fig_rs2m_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_rs2m, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à RS2M', yaxis_title=y_axis_dire[2])

    return fig

def fig_rs2m_4():
    fig = list_fig_rs2m[0]
    fig.update_layout(title='Les dépenses de vacataires à RS2M')
    return fig

def fig_rs2m_5():
    fig = list_fig_rs2m[1]
    fig.update_layout(title='Les ressources propres à RS2M')
    return fig

def fig_rs2m_6():
    fig = list_fig_rs2m[2]
    fig.update_layout(title='Les ressources d\'état à RS2M')
    return fig

def fig_rs2m_7():
    fig = list_fig_rs2m[3]
    fig.update_layout(title='Le total des dépenses à RS2M')
    return fig


sheetName = data.sheet_names[5]
list_line = data.liste_lignes
titre = data.extract_titre(list_line)
annees = data.annees
data_old = data.extract_data_numerous(sheetName, list_line)

list_old_fig_rs2m=[]
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
    list_old_fig_rs2m.append(fig_baton)

    fig = go.Figure()
    for i in range(len(annees)):
        fig.add_trace(go.Scatter(x=trimestre, y=data_old[k][i], name="Année " + str(annees[i])))
    list_old_fig_rs2m.append(fig)


def fig_old_df_rs2m_1():
    fig = list_old_fig_rs2m[0]

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à RS2M de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig

def fig_old_df_rs2m_2():
    fig = list_old_fig_rs2m[1]
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à RS2M de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    return fig

def fig_old_daf_rs2m_1():

    fig = list_old_fig_rs2m[2]

    # Ajout d'un titre
    fig.update_layout(title="Dépenses de vacataires à RS2M de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig

def fig_old_daf_rs2m_2():
    fig = list_old_fig_rs2m[3]
    fig.update_layout(title="Dépenses de vacataires à RS2M de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    return fig

def fig_old_daf_rs2m_3():
    fig = list_old_fig_rs2m[4]

    # Ajout d'un titre
    fig.update_layout(title="Ressources propres totales à RS2M de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    # barmode="group")

    return fig

def fig_old_daf_rs2m_4():
    fig = list_old_fig_rs2m[5]

    fig.update_layout(title="Ressources propres totales à RS2M de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    return fig

def fig_old_daf_rs2m_5():
    fig = list_old_fig_rs2m[6]

    # Ajout d'un titre
    fig.update_layout(title="Total des dépenses hors permanents et vacataires à RS2M de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    # barmode="group")

    return fig

def fig_old_daf_rs2m_6():
    fig = list_old_fig_rs2m[7]

    fig.update_layout(title="Total des dépenses hors permanents et vacataires à RS2M de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    return fig


def fig_old_dire_rs2m_1():
    fig = list_old_fig_rs2m[8]

    # Ajout d'un titre
    fig.update_layout(title="CA sur contrats de recherche à RS2M de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_rs2m_2():
    fig = list_old_fig_rs2m[9]
    fig.update_layout(title="CA sur contrats de recherche à RS2M de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_rs2m_3():
    fig = list_old_fig_rs2m[10]

    # Ajout d'un titre
    fig.update_layout(title="Brevets et logiciels déposés à RS2M de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    # barmode="group")

    return fig

def fig_old_dire_rs2m_4():
    fig = list_old_fig_rs2m[11]

    fig.update_layout(title="Brevets et logiciels déposés à RS2M de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    return fig

def fig_old_dire_rs2m_5():
    fig = list_old_fig_rs2m[12]

    # Ajout d'un titre
    fig.update_layout(title="Contribution au financement de l\'école à RS2M de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    # barmode="group")

    return fig

def fig_old_dire_rs2m_6():
    fig = list_old_fig_rs2m[13]

    fig.update_layout(title="Contribution au financement de l\'école à RS2M de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    return fig

def fig_old_drfd_rs2m_1():
    fig = list_old_fig_rs2m[14]

    # Ajout d'un titre
    fig.update_layout(title="Total des publications à RS2M de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[7])

    return fig

def fig_old_drfd_rs2m_2():
    fig = list_old_fig_rs2m[15]

    fig.update_layout(title="Total des publications à RS2M de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[7])
    return fig

def fig_old_drfd_rs2m_3():
    fig = list_old_fig_rs2m[16]

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants à RS2M de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    # barmode="group")

    return fig

def fig_old_drfd_rs2m_4():
    fig = list_old_fig_rs2m[17]

    fig.update_layout(title="Nombre de doctorants à RS2M de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    return fig

def fig_old_drh_rs2m_1():
    fig = list_old_fig_rs2m[18]

    # Ajout d'un titre
    fig.update_layout(title="Permanents en ETPT à RS2M de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[9])

    return fig

def fig_old_drh_rs2m_2():
    fig = list_old_fig_rs2m[19]

    fig.update_layout(title="Permanents en ETPT à RS2M de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[9])
    return fig

def fig_old_drh_rs2m_3():
    fig = list_old_fig_rs2m[20]

    # Ajout d'un titre
    fig.update_layout(title="Non-permanents en ETPT à RS2M de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig

def fig_old_drh_rs2m_4():
    fig = list_old_fig_rs2m[21]

    fig.update_layout(title="Non-permanents en ETPT à RS2M de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig
