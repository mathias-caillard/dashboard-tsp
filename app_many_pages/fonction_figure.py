import pandas as pd
import math
import plotly.graph_objects as go
from app_many_pages.config import *

couleurs = colors_dept

def fig_annuelle_baton(donnees, xlabel, year, titre_graphe, titre_y, titre_x, couleurs):
    fig = go.Figure()
    for i in range(len(donnees)):
        fig.add_trace(go.Bar(x=[xlabel[i]], y=[donnees[i]],
                             name=xlabel[i],
                             marker=dict(color=[couleurs[i]])))
    # Ajout d'un titre
    fig.update_layout(title=titre_graphe + " en " + str(year),
                      xaxis_title= titre_x,
                      yaxis_title= titre_y)
    return fig

def fig_trim_baton(donnees, xlabel, year, titre_graphe, titre_y, titre_x, couleurs):
    Y = []
    for i in range(len(donnees)):
        Y.append(
            go.Bar(
                x=xlabel[i],
                y=donnees[i],
                name=xlabel[i][0].split(" ")[0],
                width=0.8,
                marker=dict(color=couleurs[i])
            )
        )

    fig = go.Figure(data=Y)
    fig.update_layout(title=titre_graphe + " en " + str(year),
                      xaxis_title=titre_x,
                      yaxis_title=titre_y)
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