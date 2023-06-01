import pandas as pd
import math
from sklearn.preprocessing import LabelEncoder
import plotly.graph_objects as go
from src.config import *
from src.data.data import data_complete, data_complete_pondere, data_radar, label_radar, new_titre_y, new_labels, dict_titres
import plotly.colors as colors

couleurs = colors_dept
couleurs_all = colors_all

def adapt_title(title):
    if len(title) > 68:
        i = 68
        while i > 0 and title[i] != " ":
            i -= 1
        if i > 0:
            title = title[:i] + "<br>" + adapt_title(title[i + 1:])
    return title

def adapt_title_y(title_y):
    if len(title_y) > 48:
        i = 48
        while i > 0 and title_y[i] != " ":
            i -= 1
        if i > 0:
            title_y = title_y[:i] + "<br>" + adapt_title_y(title_y[i + 1:])
    return title_y



######################################################################################################################
#FONCTIONS POUR GENERER UNE FIGURE D4UN INDICATEUR SUR UNE SEULE ANNEE


#Indicateur annuel ou trimestriel (avec des départements)
def fig_annuelle_baton(code_indic, year, titre_x, couleurs):
    longueur = len(data_complete_pondere[year - liste_annee_maj[0]][code_indic])
    # Indicateur annuel (premier élément est un chiffre et nom une liste de 4 chiffres)
    if not isinstance(data_complete_pondere[year - liste_annee_maj[0]][code_indic][0], list):
        donnees = data_complete_pondere[year - liste_annee_maj[0]][code_indic]
        xlabel = new_labels[code_indic]
    #Indicateur trimestriel (comparasion entre départements)
    else:
        donnees = [sum(data_complete_pondere[year - liste_annee_maj[0]][code_indic][i]) for i in range(longueur)]
        xlabel = [new_labels[code_indic][i][0].split(" ")[0] for i in range(longueur)]
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
    title = adapt_title(titre_graphe + " en " + str(year) + ", total annuel")
    fig.update_layout(title=title,
                      xaxis_title= titre_x,
                      yaxis_title= adapt_title_y(titre_y))
    

    fig.update_traces(hovertemplate="<br>".join([
        "nombre arrondi : <b>%{y:.2f}</b>"
    ]),
    )

    return fig

#Uniquement pour les indicateurs ou il y a comparaison entre départements
def fig_camembert(code_indic, year, couleurs):
    longueur = len(data_complete_pondere[year - liste_annee_maj[0]][code_indic])
    # Indicateur annuel (premier élément est un chiffre et nom une liste de 4 chiffres)
    if not isinstance(data_complete_pondere[year - liste_annee_maj[0]][code_indic][0], list):
        # Total présent dans les données
        if "Ecole" or "ECOLE" in new_labels[code_indic][-1]:
            donnees = data_complete_pondere[year - liste_annee_maj[0]][code_indic][:-1]
            xlabel = new_labels[code_indic][:-1]
        else:
            donnees = data_complete_pondere[year - liste_annee_maj[0]][code_indic]
            xlabel = new_labels[code_indic]
    #Indicateur trimestriel
    else:
        #Total présent dans les données
        if "Ecole" or "ECOLE" in new_labels[code_indic][-1][0]:
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
    title = adapt_title(titre_graphe + " en " + str(year) + ", graphique en camembert")
    fig.update_layout(title=title)

    fig.update_traces(hovertemplate="<br>".join([
        "%{label}",
        "<b>%{percent:.0%}</b>",
        "nombre arrondi : %{value:.2f}"
    ]),
    name = ""
    )


    return fig

#Indicateur trimestriel
def fig_trim_baton(code_indic, year, titre_x, couleurs):
    longueur = len(data_complete_pondere[year - liste_annee_maj[0]][code_indic])
    if "DRI" in code_indic and year<2023 :
        donnees = data_complete_pondere[year - liste_annee_maj[0]][code_indic]
        xlabel = [["ECOLE"]]
        titre_x = ""

    elif longueur != 4:
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
            marker = dict(color = donnees[i],colorscale=[[0, colors.sequential.Tealgrn[0]], [1, colors.sequential.Tealgrn[-1]]])
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
    title = adapt_title(titre_graphe + " en " + str(year) + ", graphique en bâton")
    fig.update_layout(title=title,
                      xaxis_title=titre_x,
                      yaxis_title=adapt_title_y(titre_y))
    

    fig.update_traces(hovertemplate="<br>".join([
        "%{label}",
        "%{x}",
        "</b>%{y}</b>"
    ]),
    name = ""
    )
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
        fig.add_trace(go.Scatter(x=trimestre, y=donnees[i], name= xlabel[i][0].split(" ")[0], line=marker)),
    title = adapt_title(titre_graphe + " en " + str(year) + ", comparaison entre départements")
    fig.update_layout(title=title,
                      xaxis_title="Trimestres",
                      yaxis_title=adapt_title_y(titre_y),
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


#Indicateur trimestriel pour un département (indice 0 correspond à ARTEMIS, 1 à CITI,..., 6 à Ecole
def fig_dept_trim_baton(code_indic, year, indice_dept):
    xlabel = new_labels[code_indic][indice_dept]
    donnees = data_complete[year - liste_annee_maj[0]][code_indic][indice_dept]
    titre_graphe = dict_titres[code_indic]
    titre_y = new_titre_y[code_indic]
    name_dept = xlabel[0].split(" ")[0]
    marker = dict(color = donnees,colorscale=[[0, colors.sequential.Tealgrn[0]], [1, colors.sequential.Tealgrn[-1]]])
    Y = go.Bar(
                x=xlabel,
                y=donnees,
                name=name_dept,
                width=0.8,
                marker=marker
            )
    fig = go.Figure(data=Y)
    #Département
    if indice_dept<=5:
        title = titre_graphe + " à " + name_dept + " en " + str(year)
    #Ecole
    else:
        title = titre_graphe + " en " + str(year)
    title = adapt_title(title + ", graphique en bâton")
    fig.update_layout(title=title,
                      xaxis_title="Temps",
                      yaxis_title=adapt_title_y(titre_y),
                      )
    
    fig.update_traces(hovertemplate="<br>".join([
        "%{x}",
        "%{y}"
    ]))

    return fig




#Graphe radar avec un seul profil (pas de superposition)
def fig_radar(year, indic_dept):
    donnees = data_radar[year - liste_annee_maj[0]][indic_dept]
    name_dept = departements[indic_dept]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=donnees,
        theta=label_radar,
        fill='toself',
        name=name_dept + " " + str(year),
        line_color = couleurs[indic_dept]
    ))
    if indic_dept != 6:
        title = adapt_title("Graphique radar du département " + name_dept + " en " + str(year))
    else:
        title = adapt_title("Graphique radar de Télécom SudParis en " + str(year))
    fig.update_layout(
        title=title,
        polar=dict(radialaxis=dict(visible=True, range=[0, max(donnees)])),
        plot_bgcolor='red'
    )

    fig.update_traces(hovertemplate="<br>".join([
        "%{theta}",
        "valeur arrondie : <b>%{r:.2f}</b>"
        
    ]))
    
    return fig

def fig_radar_all_dept(year):
    fig = go.Figure()
    list_max = []
    for i in range(7):
        donnees = data_radar[year - liste_annee_maj[0]][i]
        list_max.append(max(donnees))
        name_dept = departements[i]
        fig.add_trace(go.Scatterpolar(
            r=donnees,
            theta=label_radar,
            fill='toself',
            name=name_dept + " " + str(year),
            line_color=couleurs[i]
        ))
    title = "Graphe radar des départements en " + str(year)
    fig.update_layout(
        title=adapt_title(title),
        polar=dict(radialaxis=dict(visible=True, range=[0, max(list_max)])),
        plot_bgcolor='red'
    )

    
    fig.update_traces(hovertemplate="<br>".join([
        "%{theta}",
        "valeur arrondie : <b>%{r:.2f}</b>"
    ]))

    return fig

######################################################################################################################

######################################################################################################################
#FONCTIONS POUR GENERER UNE FIGURE D4UN INDICATEUR SUR UNE PLUSIEURES ANNEES


def fig_baton_total(donnees, year, titre_graphe, titre_y):
    fig = go.Figure()
    for i in range(len(donnees)):
        fig.add_trace(go.Bar(x=[departements[i]], y=[donnees[i]],
                             name=departements[i],
                             marker=dict(color=[couleurs[i]])))
    # Ajout d'un titre
    title = adapt_title(titre_graphe + " en " + str(year) + ", pondéré par les effectifs")
    fig.update_layout(title=title,
                      xaxis_title='Départements',
                      yaxis_title=adapt_title_y(titre_y))
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