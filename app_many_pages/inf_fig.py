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


valeur_drh_inf=valeur_tri[3]
valeur_dire1_inf = valeur_trim1[3]
valeur_dire3_inf = valeur_trim3[3]



list_fig_inf=[]
for i in range(4):
    fig_inf = go.Figure()
    fig_inf.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][3]))

    fig_inf.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_inf.append(fig_inf)

def fig_inf_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_inf, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à INF', yaxis_title=y_axis_tri[0])

    return fig

def fig_inf_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_inf, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à INF', yaxis_title=y_axis_dire[0])

    return fig

def fig_inf_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_inf, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à INF', yaxis_title=y_axis_dire[2])

    return fig

def fig_inf_4():
    fig = list_fig_inf[0]
    fig.update_layout(title='Les dépenses de vacataires à INF')
    return fig

def fig_inf_5():
    fig = list_fig_inf[1]
    fig.update_layout(title='Les ressources propres à INF')
    return fig

def fig_inf_6():
    fig = list_fig_inf[2]
    fig.update_layout(title='Les ressources d\'état à INF')
    return fig

def fig_inf_7():
    fig = list_fig_inf[3]
    fig.update_layout(title='Le total des dépenses à INF')
    return fig

sheetName = data.sheet_names[4]
list_line = data.liste_lignes
titre = data.extract_titre(list_line)
annees = data.annees
data_old = data.extract_data_numerous(sheetName, list_line)

list_old_fig_inf=[]
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
    list_old_fig_inf.append(fig_baton)

    fig = go.Figure()
    for i in range(len(annees)):
        fig.add_trace(go.Scatter(x=trimestre, y=data_old[k][i], name="Année " + str(annees[i])))
    list_old_fig_inf.append(fig)


def fig_old_df_inf_1():
    fig = list_old_fig_inf[0]

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à INF de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig

def fig_old_df_inf_2():
    fig = list_old_fig_inf[1]
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à INF de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    return fig

def fig_old_daf_inf_1():

    fig = list_old_fig_inf[2]

    # Ajout d'un titre
    fig.update_layout(title="Dépenses de vacataires à INF de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig

def fig_old_daf_inf_2():
    fig = list_old_fig_inf[3]
    fig.update_layout(title="Dépenses de vacataires à INF de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    return fig

def fig_old_daf_inf_3():
    fig = list_old_fig_inf[4]

    # Ajout d'un titre
    fig.update_layout(title="Ressources propres totales à INF de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    # barmode="group")

    return fig

def fig_old_daf_inf_4():
    fig = list_old_fig_inf[5]

    fig.update_layout(title="Ressources propres totales à INF de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    return fig

def fig_old_daf_inf_5():
    fig = list_old_fig_inf[6]

    # Ajout d'un titre
    fig.update_layout(title="Total des dépenses hors permanents et vacataires à INF de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    # barmode="group")

    return fig

def fig_old_daf_inf_6():
    fig = list_old_fig_inf[7]

    fig.update_layout(title="Total des dépenses hors permanents et vacataires à INF de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    return fig


def fig_old_dire_inf_1():
    fig = list_old_fig_inf[8]

    # Ajout d'un titre
    fig.update_layout(title="CA sur contrats de recherche à INF de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_inf_2():
    fig = list_old_fig_inf[9]
    fig.update_layout(title="CA sur contrats de recherche à INF de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_inf_3():
    fig = list_old_fig_inf[10]

    # Ajout d'un titre
    fig.update_layout(title="Brevets et logiciels déposés à INF de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    # barmode="group")

    return fig

def fig_old_dire_inf_4():
    fig = list_old_fig_inf[11]

    fig.update_layout(title="Brevets et logiciels déposés à INF de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    return fig

def fig_old_dire_inf_5():
    fig = list_old_fig_inf[12]

    # Ajout d'un titre
    fig.update_layout(title="Contribution au financement de l\'école à INF de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    # barmode="group")

    return fig

def fig_old_dire_inf_6():
    fig = list_old_fig_inf[13]

    fig.update_layout(title="Contribution au financement de l\'école à INF de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    return fig

def fig_old_drfd_inf_1():
    fig = list_old_fig_inf[14]

    # Ajout d'un titre
    fig.update_layout(title="Total des publications à INF de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[7])

    return fig

def fig_old_drfd_inf_2():
    fig = list_old_fig_inf[15]

    fig.update_layout(title="Total des publications à INF de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[7])
    return fig

def fig_old_drfd_inf_3():
    fig = list_old_fig_inf[16]

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants à INF de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    # barmode="group")

    return fig

def fig_old_drfd_inf_4():
    fig = list_old_fig_inf[17]

    fig.update_layout(title="Nombre de doctorants à INF de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    return fig

def fig_old_drh_inf_1():
    fig = list_old_fig_inf[18]

    # Ajout d'un titre
    fig.update_layout(title="Permanents en ETPT à INF de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[9])

    return fig

def fig_old_drh_inf_2():
    fig = list_old_fig_inf[19]

    fig.update_layout(title="Permanents en ETPT à INF de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[9])
    return fig

def fig_old_drh_inf_3():
    fig = list_old_fig_inf[20]

    # Ajout d'un titre
    fig.update_layout(title="Non-permanents en ETPT à INF de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig

def fig_old_drh_inf_4():
    fig = list_old_fig_inf[21]

    fig.update_layout(title="Non-permanents en ETPT à INF de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig


list_old_fig_tot_inf=[]
for k in range(len(list_line)):
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee)],
                y=[sum(data_old[k][i])],
                name=str(annee),
            )
        )
    fig_tot = go.Figure(data=donnee)
    list_old_fig_tot_inf.append(fig_tot)

def fig_old_df_tot_inf_1():
    fig = list_old_fig_tot_inf[0]

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à INF de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig


def fig_old_daf_tot_inf_1():

    fig = list_old_fig_tot_inf[1]

    # Ajout d'un titre
    fig.update_layout(title="Dépenses de vacataires à INF de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig



def fig_old_daf_tot_inf_3():
    fig = list_old_fig_tot_inf[2]

    # Ajout d'un titre
    fig.update_layout(title="Ressources propres totales à INF de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    # barmode="group")

    return fig


def fig_old_daf_tot_inf_5():
    fig = list_old_fig_tot_inf[3]

    # Ajout d'un titre
    fig.update_layout(title="Total des dépenses hors permanents et vacataires à INF de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    # barmode="group")

    return fig


def fig_old_dire_tot_inf_1():
    fig = list_old_fig_tot_inf[4]

    # Ajout d'un titre
    fig.update_layout(title="CA sur contrats de recherche à INF de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig


def fig_old_dire_tot_inf_3():
    fig = list_old_fig_tot_inf[5]

    # Ajout d'un titre
    fig.update_layout(title="Brevets et logiciels déposés à INF de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    # barmode="group")

    return fig

def fig_old_dire_tot_inf_5():
    fig = list_old_fig_tot_inf[6]

    # Ajout d'un titre
    fig.update_layout(title="Contribution au financement de l\'école à INF de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    # barmode="group")

    return fig


def fig_old_drfd_tot_inf_1():
    fig = list_old_fig_tot_inf[7]

    # Ajout d'un titre
    fig.update_layout(title="Total des publications à INF de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[7])

    return fig

def fig_old_drfd_tot_inf_3():
    fig = list_old_fig_tot_inf[8]

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants à INF de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    # barmode="group")

    return fig

def fig_old_drh_tot_inf_1():
    fig = list_old_fig_tot_inf[9]

    # Ajout d'un titre
    fig.update_layout(title="Permanents en ETPT à INF de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[9])

    return fig

def fig_old_drh_tot_inf_3():
    fig = list_old_fig_tot_inf[10]

    # Ajout d'un titre
    fig.update_layout(title="Non-permanents en ETPT à INF de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig