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


valeur_drh_rst=valeur_tri[5]
valeur_dire1_rst = valeur_trim1[5]
valeur_dire3_rst = valeur_trim3[5]



list_fig_rst=[]
for i in range(4):
    fig_rst = go.Figure()
    fig_rst.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][5]))

    fig_rst.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_rst.append(fig_rst)

def fig_rst_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_rst, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à RST', yaxis_title=y_axis_tri[0])

    return fig

def fig_rst_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_rst, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à RST', yaxis_title=y_axis_dire[0])

    return fig

def fig_rst_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_rst, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à RST', yaxis_title=y_axis_dire[2])

    return fig

def fig_rst_4():
    fig = list_fig_rst[0]
    fig.update_layout(title='Les dépenses de vacataires à RST')
    return fig

def fig_rst_5():
    fig = list_fig_rst[1]
    fig.update_layout(title='Les ressources propres à RST')
    return fig

def fig_rst_6():
    fig = list_fig_rst[2]
    fig.update_layout(title='Les ressources d\'état à RST')
    return fig
def fig_rst_7():
    fig = list_fig_rst[3]
    fig.update_layout(title='Le total des dépenses à RST')
    return fig


sheetName = data.sheet_names[6]
list_line = data.liste_lignes
titre = data.extract_titre(list_line)
annees = data.annees
data_old = data.extract_data_numerous(sheetName, list_line)

list_old_fig_rst=[]
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
    list_old_fig_rst.append(fig_baton)

    fig = go.Figure()
    for i in range(len(annees)):
        fig.add_trace(go.Scatter(x=trimestre, y=data_old[k][i], name="Année " + str(annees[i])))
    list_old_fig_rst.append(fig)


def fig_old_df_rst_1():
    fig = list_old_fig_rst[0]

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à RST de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig

def fig_old_df_rst_2():
    fig = list_old_fig_rst[1]
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à RST de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    return fig

def fig_old_daf_rst_1():

    fig = list_old_fig_rst[2]

    # Ajout d'un titre
    fig.update_layout(title="Dépenses de vacataires à RST de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig

def fig_old_daf_rst_2():
    fig = list_old_fig_rst[3]
    fig.update_layout(title="Dépenses de vacataires à RST de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    return fig

def fig_old_daf_rst_3():
    fig = list_old_fig_rst[4]

    # Ajout d'un titre
    fig.update_layout(title="Ressources propres totales à RST de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    # barmode="group")

    return fig

def fig_old_daf_rst_4():
    fig = list_old_fig_rst[5]

    fig.update_layout(title="Ressources propres totales à RST de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    return fig

def fig_old_daf_rst_5():
    fig = list_old_fig_rst[6]

    # Ajout d'un titre
    fig.update_layout(title="Total des dépenses hors permanents et vacataires à RST de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    # barmode="group")

    return fig

def fig_old_daf_rst_6():
    fig = list_old_fig_rst[7]

    fig.update_layout(title="Total des dépenses hors permanents et vacataires à RST de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    return fig


def fig_old_dire_rst_1():
    fig = list_old_fig_rst[8]

    # Ajout d'un titre
    fig.update_layout(title="CA sur contrats de recherche à RST de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_rst_2():
    fig = list_old_fig_rst[9]
    fig.update_layout(title="CA sur contrats de recherche à RST de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_rst_3():
    fig = list_old_fig_rst[10]

    # Ajout d'un titre
    fig.update_layout(title="Brevets et logiciels déposés à RST de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    # barmode="group")

    return fig

def fig_old_dire_rst_4():
    fig = list_old_fig_rst[11]

    fig.update_layout(title="Brevets et logiciels déposés à RST de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    return fig

def fig_old_dire_rst_5():
    fig = list_old_fig_rst[12]

    # Ajout d'un titre
    fig.update_layout(title="Contribution au financement de l\'école à RST de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    # barmode="group")

    return fig

def fig_old_dire_rst_6():
    fig = list_old_fig_rst[13]

    fig.update_layout(title="Contribution au financement de l\'école à RST de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    return fig

def fig_old_drfd_rst_1():
    fig = list_old_fig_rst[14]

    # Ajout d'un titre
    fig.update_layout(title="Total des publications à RST de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[7])

    return fig

def fig_old_drfd_rst_2():
    fig = list_old_fig_rst[15]

    fig.update_layout(title="Total des publications à RST de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[7])
    return fig

def fig_old_drfd_rst_3():
    fig = list_old_fig_rst[16]

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants à RST de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    # barmode="group")

    return fig

def fig_old_drfd_rst_4():
    fig = list_old_fig_rst[17]

    fig.update_layout(title="Nombre de doctorants à RST de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    return fig

def fig_old_drh_rst_1():
    fig = list_old_fig_rst[18]

    # Ajout d'un titre
    fig.update_layout(title="Permanents en ETPT à RST de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[9])

    return fig

def fig_old_drh_rst_2():
    fig = list_old_fig_rst[19]

    fig.update_layout(title="Permanents en ETPT à RST de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[9])
    return fig

def fig_old_drh_rst_3():
    fig = list_old_fig_rst[20]

    # Ajout d'un titre
    fig.update_layout(title="Non-permanents en ETPT à RST de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig

def fig_old_drh_rst_4():
    fig = list_old_fig_rst[21]

    fig.update_layout(title="Non-permanents en ETPT à RST de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig
