import pandas as pd
import math
import plotly.graph_objects as go
from app_many_pages.config import *
from app_many_pages.data import data_complete, new_titre_y, new_labels, dict_titres

couleurs = colors_dept


def fig_annuelle_baton(code_indic, year, titre_x, couleurs):
    donnees = data_complete[year - liste_annee_maj[0]][code_indic]
    xlabel = new_labels[code_indic]
    titre_graphe = dict_titres[code_indic]
    titre_y = new_titre_y[code_indic]

    fig = go.Figure()
    for i in range(len(donnees)):
        fig.add_trace(go.Bar(x=[xlabel[i]], y=[donnees[i]],
                             name=xlabel[i].split(" ")[0],
                             marker=dict(color=[couleurs[i]])))
    # Ajout d'un titre
    fig.update_layout(title=titre_graphe + " en " + str(year),
                      xaxis_title= titre_x,
                      yaxis_title= titre_y)
    return fig

def fig_trim_baton(code_indic, year, titre_x, couleurs):
    donnees = data_complete[year - liste_annee_maj[0]][code_indic]
    xlabel = new_labels[code_indic]
    titre_graphe = dict_titres[code_indic]
    titre_y = new_titre_y[code_indic]
    Y = []
    for i in range(len(donnees)):
        if couleurs is not None:
            marker = dict(color=couleurs[i])
        else:
            marker = None
        Y.append(
            go.Bar(
                x=xlabel[i],
                y=donnees[i],
                name=xlabel[i][0].split(" ")[0],
                width=0.8,
                marker=marker
            )
        )

    fig = go.Figure(data=Y)
    fig.update_layout(title=titre_graphe + " en " + str(year),
                      xaxis_title=titre_x,
                      yaxis_title=titre_y)
    return fig

def fig_trim_courbe(code_indic, year, couleurs):
    donnees = data_complete[year - liste_annee_maj[0]][code_indic]
    xlabel = trimestre
    titre_graphe = dict_titres[code_indic]
    titre_y = new_titre_y[code_indic]
    fig = go.Figure()
    for i in range(len(years)):
        if couleurs is not None:
            marker = dict(color=couleurs[i])
        else:
            marker = None
        fig.add_trace(go.Scatter(x=trimestre_encoded, y=donnees[i], name="Année " + str(years[i]),
                                 line=dict(color=couleurs_années[i])))

    fig.update_layout(title=titre_graphe + " de " + str(years[0]) + " à " + str(
        years[-1]) + ",<br>comparaison annuelle par trimestre",
                      xaxis_title="Trimestres",
                      yaxis_title=titre_y,
                      xaxis=dict(
                          tickvals=[0, 1, 2, 3],
                          ticktext=['T1', 'T2', 'T3', 'T4']
                      ),
                      hovermode="x"
                      )

    return fig

def fig_baton_total(donnees, year, titre_graphe, titre_y):
    fig = go.Figure()
    for i in range(len(donnees)):
        fig.add_trace(go.Bar(x=[departements[i]], y=[donnees[i]],
                             name=departements[i],
                             marker=dict(color=[couleurs[i]])))
    # Ajout d'un titre
    fig.update_layout(title=titre_graphe + " en " + str(year) + ", pondéré par les effectifs",
                      xaxis_title='Départements',
                      yaxis_title=titre_y)
    return fig


#Même couleur pour un département
def fig_baton_trimestre(donnees, year, titre_graphe, titre_y):
    Y = []
    for i in range(len(donnees)):
        Y.append(
            go.Bar(
                x=[departements[i] + " - " + tri for tri in trimestre],
                y=donnees[i],
                name=departements[i],
                width=0.8,
                marker=dict(color=couleurs[i])
            )
        )

    fig = go.Figure(data=Y)
    fig.update_layout(title=titre_graphe + " en " + str(year) + ", pondéré par les effectifs",
                      xaxis_title='Départements',
                      yaxis_title=titre_y)
    return fig

#Même couleur pour un trimestre (même données que fig_baton_trimestre
def fig_baton_departement(donnees, year, titre_graphe, titre_y):
    Y = []
    for i in range(len(donnees)):
        Y.append(
            go.Bar(
                x=[departements[i] + " - " + tri for tri in trimestre],
                y=donnees[i],
                name=departements[i],
                marker=dict(color=couleurs),
                width=0.8,
            )
        )
    fig = go.Figure(data=Y)
    # Ajout d'un titre
    fig.update_layout(title=titre_graphe + " en " + str(year) + ", pondéré par les effectifs",
                      xaxis_title="Temps",
                      yaxis_title=titre_y)
    return fig