import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src import config
import random as rd
import data
from fig.drh_fig import trimestre, valeur_tri,y_axis_tri
from fig.dire_fig import valeur_trim1, valeur_trim3, y_axis as y_axis_dire
from fig.daf_fig import valeur_tri as valeur_daf, y_axis_tri as y_axis_daf


couleurs_trimestres=config.couleurs_trimestres

valeur_drh_artemis=valeur_tri[0]
valeur_dire1_artemis = valeur_trim1[0]
valeur_dire3_artemis = valeur_trim3[0]



list_fig_artemis=[]
for i in range(4):
    fig_artemis = go.Figure()
    fig_artemis.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][0]))

    fig_artemis.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_artemis.append(fig_artemis)

def fig_artemis_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_artemis, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à ARTEMIS', yaxis_title=y_axis_tri[0])

    return fig

def fig_artemis_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_artemis, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à ARTEMIS', yaxis_title=y_axis_dire[0])

    return fig

def fig_artemis_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_artemis, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à ARTEMIS', yaxis_title=y_axis_dire[2])

    return fig

def fig_artemis_4():
    fig = list_fig_artemis[0]
    fig.update_layout(title='Les dépenses de vacataires à ARTEMIS')
    return fig

def fig_artemis_5():
    fig = list_fig_artemis[1]
    fig.update_layout(title='Les ressources propres à ARTEMIS')
    return fig

def fig_artemis_6():
    fig = list_fig_artemis[2]
    fig.update_layout(title='Les ressources d\'état à ARTEMIS')
    return fig
def fig_artemis_7():
    fig = list_fig_artemis[3]
    fig.update_layout(title='Le total des dépenses à ARTEMIS')
    return fig

sheetName = data.data.sheet_names[1]
list_line = data.data.liste_lignes
titre = data.data.extract_titre(list_line)
annees = data.data.annees
data_old = data.data.extract_data_numerous(sheetName, list_line)

list_old_fig_artemis=[]
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
    list_old_fig_artemis.append(fig_baton)

    fig = go.Figure()
    for i in range(len(annees)):
        fig.add_trace(go.Scatter(x=trimestre, y=data_old[k][i], name="Année " + str(annees[i])))
    list_old_fig_artemis.append(fig)







def fig_old_df_artemis_1():
    fig = list_old_fig_artemis[0]

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à ARTEMIS de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig

def fig_old_df_artemis_2():
    fig = list_old_fig_artemis[1]
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à ARTEMIS de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[0])
    return fig

def fig_old_daf_artemis_1():

    fig = list_old_fig_artemis[2]

    # Ajout d'un titre
    fig.update_layout(title="Dépenses de vacataires à ARTEMIS de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig

def fig_old_daf_artemis_2():
    fig = list_old_fig_artemis[3]
    fig.update_layout(title="Dépenses de vacataires à ARTEMIS de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    return fig

def fig_old_daf_artemis_3():
    fig = list_old_fig_artemis[4]

    # Ajout d'un titre
    fig.update_layout(title="Ressources propres totales à ARTEMIS de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    # barmode="group")

    return fig

def fig_old_daf_artemis_4():
    fig = list_old_fig_artemis[5]

    fig.update_layout(title="Ressources propres totales à ARTEMIS de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    return fig

def fig_old_daf_artemis_5():
    fig = list_old_fig_artemis[6]

    # Ajout d'un titre
    fig.update_layout(title="Total des dépenses hors permanents et vacataires à ARTEMIS de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    # barmode="group")

    return fig

def fig_old_daf_artemis_6():
    fig = list_old_fig_artemis[7]

    fig.update_layout(title="Total des dépenses hors permanents et vacataires à ARTEMIS de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    return fig


def fig_old_dire_artemis_1():
    fig = list_old_fig_artemis[8]

    # Ajout d'un titre
    fig.update_layout(title="CA sur contrats de recherche à ARTEMIS de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_artemis_2():
    fig = list_old_fig_artemis[9]
    fig.update_layout(title="CA sur contrats de recherche à ARTEMIS de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig

def fig_old_dire_artemis_3():
    fig = list_old_fig_artemis[10]

    # Ajout d'un titre
    fig.update_layout(title="Brevets et logiciels déposés à ARTEMIS de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    # barmode="group")

    return fig

def fig_old_dire_artemis_4():
    fig = list_old_fig_artemis[11]

    fig.update_layout(title="Brevets et logiciels déposés à ARTEMIS de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    return fig

def fig_old_dire_artemis_5():
    fig = list_old_fig_artemis[12]

    # Ajout d'un titre
    fig.update_layout(title="Contribution au financement de l\'école à ARTEMIS de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    # barmode="group")

    return fig

def fig_old_dire_artemis_6():
    fig = list_old_fig_artemis[13]

    fig.update_layout(title="Contribution au financement de l\'école à ARTEMIS de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    return fig

def fig_old_drfd_artemis_1():
    fig = list_old_fig_artemis[14]

    # Ajout d'un titre
    fig.update_layout(title="Total des publications à ARTEMIS de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[7])

    return fig

def fig_old_drfd_artemis_2():
    fig = list_old_fig_artemis[15]

    fig.update_layout(title="Total des publications à ARTEMIS de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[7])
    return fig

def fig_old_drfd_artemis_3():
    fig = list_old_fig_artemis[16]

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants à ARTEMIS de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    # barmode="group")

    return fig

def fig_old_drfd_artemis_4():
    fig = list_old_fig_artemis[17]

    fig.update_layout(title="Nombre de doctorants à ARTEMIS de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    return fig

def fig_old_drh_artemis_1():
    fig = list_old_fig_artemis[18]

    # Ajout d'un titre
    fig.update_layout(title="Permanents en ETPT à ARTEMIS de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[9])

    return fig

def fig_old_drh_artemis_2():
    fig = list_old_fig_artemis[19]

    fig.update_layout(title="Permanents en ETPT à ARTEMIS de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[9])
    return fig

def fig_old_drh_artemis_3():
    fig = list_old_fig_artemis[20]

    # Ajout d'un titre
    fig.update_layout(title="Non-permanents en ETPT à ARTEMIS de 2015 à 2019, graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig

def fig_old_drh_artemis_4():
    fig = list_old_fig_artemis[21]

    fig.update_layout(title="Non-permanents en ETPT à ARTEMIS de 2015 à 2019",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig

#Figure avec total annuel

list_old_fig_tot_artemis=[]
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
    list_old_fig_tot_artemis.append(fig_tot)

def fig_old_df_tot_artemis_1():
    fig = list_old_fig_tot_artemis[0]

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à ARTEMIS de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig


def fig_old_daf_tot_artemis_1():

    fig = list_old_fig_tot_artemis[1]

    # Ajout d'un titre
    fig.update_layout(title="Dépenses de vacataires à ARTEMIS de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig



def fig_old_daf_tot_artemis_3():
    fig = list_old_fig_tot_artemis[2]

    # Ajout d'un titre
    fig.update_layout(title="Ressources propres totales à ARTEMIS de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    # barmode="group")

    return fig


def fig_old_daf_tot_artemis_5():
    fig = list_old_fig_tot_artemis[3]

    # Ajout d'un titre
    fig.update_layout(title="Total des dépenses hors permanents et vacataires à ARTEMIS de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    # barmode="group")

    return fig


def fig_old_dire_tot_artemis_1():
    fig = list_old_fig_tot_artemis[4]

    # Ajout d'un titre
    fig.update_layout(title="CA sur contrats de recherche à ARTEMIS de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig


def fig_old_dire_tot_artemis_3():
    fig = list_old_fig_tot_artemis[5]

    # Ajout d'un titre
    fig.update_layout(title="Brevets et logiciels déposés à ARTEMIS de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    # barmode="group")

    return fig

def fig_old_dire_tot_artemis_5():
    fig = list_old_fig_tot_artemis[6]

    # Ajout d'un titre
    fig.update_layout(title="Contribution au financement de l\'école à ARTEMIS de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    # barmode="group")

    return fig


def fig_old_drfd_tot_artemis_1():
    fig = list_old_fig_tot_artemis[7]

    # Ajout d'un titre
    fig.update_layout(title="Total des publications à ARTEMIS de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[7])

    return fig

def fig_old_drfd_tot_artemis_3():
    fig = list_old_fig_tot_artemis[8]

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants à ARTEMIS de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    # barmode="group")

    return fig

def fig_old_drh_tot_artemis_1():
    fig = list_old_fig_tot_artemis[9]

    # Ajout d'un titre
    fig.update_layout(title="Permanents en ETPT à ARTEMIS de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[9])

    return fig

def fig_old_drh_tot_artemis_3():
    fig = list_old_fig_tot_artemis[10]

    # Ajout d'un titre
    fig.update_layout(title="Non-permanents en ETPT à ARTEMIS de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig


#Figure trimestrielle:

list_old_fig_tri_artemis=[]
for k in range(len(list_line)):
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee) + ' - ' + trimestre[j] for j in range(4)],
                y=data_old[k][i],
                marker=dict(color=couleurs_trimestres),
                name=str(annee),
            )
        )
    fig_tri = go.Figure(data=donnee)
    list_old_fig_tri_artemis.append(fig_tri)

def fig_old_df_artemis_1_tri():
    fig = list_old_fig_tri_artemis[0]

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes à ARTEMIS de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig


def fig_old_daf_artemis_1_tri():

    fig = list_old_fig_tri_artemis[1]

    # Ajout d'un titre
    fig.update_layout(title="Dépenses de vacataires à ARTEMIS de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[1])
    # barmode="group")

    return fig



def fig_old_daf_artemis_3_tri():
    fig = list_old_fig_tri_artemis[2]

    # Ajout d'un titre
    fig.update_layout(title="Ressources propres totales à ARTEMIS de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[2])
    # barmode="group")

    return fig


def fig_old_daf_artemis_5_tri():
    fig = list_old_fig_tri_artemis[3]

    # Ajout d'un titre
    fig.update_layout(title="Total des dépenses hors permanents et vacataires à ARTEMIS de 2015 à 2019,vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[3])
    # barmode="group")

    return fig


def fig_old_dire_artemis_1_tri():
    fig = list_old_fig_tri_artemis[4]

    # Ajout d'un titre
    fig.update_layout(title="CA sur contrats de recherche à ARTEMIS de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[4])
    return fig


def fig_old_dire_artemis_3_tri():
    fig = list_old_fig_tri_artemis[5]

    # Ajout d'un titre
    fig.update_layout(title="Brevets et logiciels déposés à ARTEMIS de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[5])
    # barmode="group")

    return fig

def fig_old_dire_artemis_5_tri():
    fig = list_old_fig_tri_artemis[6]

    # Ajout d'un titre
    fig.update_layout(title="Contribution au financement de l\'école à ARTEMIS de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[6])
    # barmode="group")

    return fig


def fig_old_drfd_artemis_1_tri():
    fig = list_old_fig_tri_artemis[7]

    # Ajout d'un titre
    fig.update_layout(title="Total des publications à ARTEMIS de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[7])

    return fig

def fig_old_drfd_artemis_3_tri():
    fig = list_old_fig_tri_artemis[8]

    # Ajout d'un titre
    fig.update_layout(title="Nombre de doctorants à ARTEMIS de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[8])
    # barmode="group")

    return fig

def fig_old_drh_artemis_1_tri():
    fig = list_old_fig_tri_artemis[9]

    # Ajout d'un titre
    fig.update_layout(title="Permanents en ETPT à ARTEMIS de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[9])

    return fig

def fig_old_drh_artemis_3_tri():
    fig = list_old_fig_tri_artemis[10]

    # Ajout d'un titre
    fig.update_layout(title="Non-permanents en ETPT à ARTEMIS de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[10])
    return fig

