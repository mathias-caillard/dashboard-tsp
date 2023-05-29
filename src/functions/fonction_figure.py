import pandas as pd
import math
from sklearn.preprocessing import LabelEncoder
import plotly.graph_objects as go
from src.config import *
from src.data.data import data_complete_pondere, new_titre_y, new_labels, dict_titres

couleurs = colors_dept

#Indicateur annuel ou trimestriel avec uniquement 4 trimestre (pas de départements)
def fig_annuelle_baton(code_indic, year, titre_x, couleurs):
    donnees = data_complete_pondere[year - liste_annee_maj[0]][code_indic]
    xlabel = new_labels[code_indic]
    titre_graphe = dict_titres[code_indic]
    titre_y = new_titre_y[code_indic]
    fig = go.Figure()
    #print(code_indic, donnees)
    for i in range(len(donnees)):
        if couleurs is not None:
            marker = dict(color=couleurs[i])
        else:
            marker = dict(color="blue")
        fig.add_trace(go.Bar(x=[xlabel[i]], y=[donnees[i]],
                             name=xlabel[i].split(" ")[0],
                             marker=marker))
    # Ajout d'un titre
    fig.update_layout(title=titre_graphe + " en " + str(year),
                      xaxis_title= titre_x,
                      yaxis_title= titre_y)
    return fig

#Uniquement pour les indicateurs ou il y a comparaison entre départements
def fig_camembert(code_indic, year, couleurs):
    longueur = len(data_complete_pondere[year - liste_annee_maj[0]][code_indic])
    # Indicateur annuel (premier élément est un chiffre et nom une liste de 4 chiffres)
    if not isinstance(data_complete_pondere[year - liste_annee_maj[0]][code_indic][0], list):
        # Total présent dans les données
        if "Ecole" in new_labels[code_indic][-1]:
            donnees = data_complete_pondere[year - liste_annee_maj[0]][code_indic][:-1]
            xlabel = new_labels[code_indic][:-1]
        else:
            donnees = data_complete_pondere[year - liste_annee_maj[0]][code_indic]
            xlabel = new_labels[code_indic]
    #Indicateur trimestriel
    else:
        #Total présent dans les données
        if "Ecole" in new_labels[code_indic][-1][0]:
            donnees = [sum(data_complete_pondere[year - liste_annee_maj[0]][code_indic][i]) for i in range(longueur - 1)]
            xlabel = [new_labels[code_indic][i][0].split(" ")[0] for i in range(longueur-1)]
        else:
            donnees = [sum(data_complete_pondere[year - liste_annee_maj[0]][code_indic][i]) for i in range(longueur)]
            xlabel = [new_labels[code_indic][i][0].split(" ")[0] for i in range(longueur)]
    titre_graphe = dict_titres[code_indic]
    # Création du camembert
    fig = go.Figure(data=[go.Pie(labels=xlabel, values=donnees, marker_colors=couleurs)])
    # Personnalisation du camembert
    fig.update_traces(hoverinfo="label+percent+value", textinfo="label+percent")
    # Ajout d'un titre
    fig.update_layout(title=titre_graphe + " en " + str(year))
    return fig

#Indicateur trimestriel
def fig_trim_baton(code_indic, year, titre_x, couleurs):
    longueur = len(data_complete_pondere[year - liste_annee_maj[0]][code_indic])
    if longueur != 4:
        donnees = data_complete_pondere[year - liste_annee_maj[0]][code_indic]
        xlabel = new_labels[code_indic]
    else:
        donnees = [[data_complete_pondere[year - liste_annee_maj[0]][code_indic][i] for i in range(longueur)]]
        xlabel = [[new_labels[code_indic][i] for i in range(longueur)]]


    titre_graphe = dict_titres[code_indic]
    titre_y = new_titre_y[code_indic]
    Y = []
    for i in range(len(donnees)):
        if couleurs is not None:
            marker = dict(color=couleurs[i])
        else:
            marker = dict(color="blue")
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
    donnees = data_complete_pondere[year - liste_annee_maj[0]][code_indic]
    xlabel = new_labels[code_indic]
    titre_graphe = dict_titres[code_indic]
    titre_y = new_titre_y[code_indic]
    # encoder les trimestre : passer d'un String à une valeur int
    label_encoder = LabelEncoder()
    trimestre_encoded = label_encoder.fit_transform([i + 1 for i, _ in enumerate(trimestre)])
    fig = go.Figure()
    for i in range(len(donnees)):
        if couleurs is not None:
            marker = dict(color=couleurs[i])
        else:
            marker = dict(color="blue")
        fig.add_trace(go.Scatter(x=trimestre_encoded, y=donnees[i], name= xlabel[i][0].split(" ")[0], line=marker)),

    fig.update_layout(title=titre_graphe + " en " + str(year) + ",<br>comparaison annuelle par trimestre",
                      xaxis_title="Trimestres",
                      yaxis_title=titre_y,
                      xaxis=dict(
                          tickvals=[0, 1, 2, 3],
                          ticktext=['T1', 'T2', 'T3', 'T4']
                      ),
                      hovermode="x"
                      )
    fig.update_traces(hovertemplate="<br>".join([
        " Trimestre : %{x}",
        "Total : <b>%{y:.0f}</b>",
    ]))
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