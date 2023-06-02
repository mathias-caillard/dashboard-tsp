import dash
from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from src import config
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import numpy as np

from src.data.data import dict_titres
from src.functions.fonction_figure import fig_hist_total, fig_hist_trim_baton, fig_hist_trim_courbe, fig_hist_radar, couleurs_annees



annees = config.liste_annee_maj
trimestre = config.trimestre
couleurs_trimestres = config.couleurs_trimestres
couleurs_annees = px.colors.qualitative.Plotly
dept_maj = ["ARTEMIS", "CITI", "EPH", "INF", "RS2M", "RST"]
dept_min = ["artemis", "citi", "eph", "inf", "rs2m", "rst"]


#Catégories du menu déroulant
categories_historique = [
    # Ecole
    {"label": "Ecole - DF-01: Nombre d\'UP - Total annuel", "value": "df1_tot_ecole"},
    {"label": "DF-02: Nombre d\'étudiants FISE - Total annuel", "value": "df2_tot"},
    {"label": "DF-03: Nombre d\'étudiants FIPA - Total annuel", "value": "df3_tot"},
    {"label": "DF-04: Nombre d\'étudiants DNM - Total annuel", "value": "df4_tot"},
    {"label": "DF-05: Nombre d\'étudiants FTLV - Total annuel", "value": "df5_tot"},
    {"label": "DF-06: Nombre total d\'étudiants - Total annuel", "value": "df6_tot"},

    {"label": "Ecole - DRFD-01: Nombre d\'UP - Total annuel", "value": "drfd1_tot_ecole"},
    {"label": "Ecole - DRFD-02: Nombre d\'UP - Total annuel", "value": "drfd2_tot_ecole"},

    {"label": "Ecole - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_ecole"},
    {"label": "Ecole - DIRE-01: Suivi des contrats de recherche - Comparaison entre années", "value": "dire1_cou_ecole"},
    {"label": "Ecole - DIRE-01: Suivi des contrats de recherche - Total annuel", "value": "dire1_tot_ecole"},
    {"label": "Ecole - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_ecole"},
    {"label": "Ecole - DIRE-02: Brevets et logiciels déposés - Comparaison entre années", "value": "dire2_cou_ecole"},
    {"label": "Ecole - DIRE-02: Brevets et logiciels déposés - Total annuel", "value": "dire2_tot_ecole"},
    {"label": "Ecole - DIRE-03: Contribution au financement de l\'école - Graphique en bâton", "value": "dire3_bat_ecole"},
    {"label": "Ecole - DIRE-03: Contribution au financement de l\'école - Comparaison entre années", "value": "dire3_cou_ecole"},
    {"label": "Ecole - DIRE-03: Contribution au financement de l\'école - Total annuel", "value": "dire3_tot_ecole"},

    {"label": "Ecole - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_ecole"},
    {"label": "Ecole - DAF-01: Dépenses de vacataires - Comparaison entre années", "value": "dafe1_cou_ecole"},
    {"label": "Ecole - DAF-01: Dépenses de vacataires - Total annuel", "value": "daf1_tot_ecole"},
    {"label": "Ecole - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_ecole"},
    {"label": "Ecole - DAF-02: Ressources propres - Comparaison entre années", "value": "daf2_cou_ecole"},
    {"label": "Ecole - DAF-02: Ressources propres - Total annuel", "value": "daf2_tot_ecole"},
    {"label": "Ecole - DAF-03: Ressources d\'état - Graphique en bâton", "value": "daf3_bat_ecole"},
    {"label": "Ecole - DAF-03: Ressources d\'état - Comparaison entre années", "value": "daf3_cou_ecole"},
    {"label": "Ecole - DAF-03: Ressources d\'état - Total annuel", "value": "daf3_tot_ecole"},
    {"label": "Ecole - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_ecole"},
    {"label": "Ecole - DAF-04: Total des dépenses hors permanents et vacataires - Comparaison entre années", "value": "dafe4_cou_ecole"},
    {"label": "Ecole - DAF-04: Total des dépenses hors permanents et vacataires - Total annuel", "value": "daf4_tot_ecole"},
    {"label": "Ecole - DAF-05: Dotation de l\'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_ecole"},
    {"label": "Ecole - DAF-05: Dotation de l\'institut hors permanents et vacataires - Comparaison entre années", "value": "daf5_cou_ecole"},
    {"label": "Ecole - DAF-05: Dotation de l\'institut hors permanents et vacataires - Total annuel", "value": "daf5_tot_ecole"},
    {"label": "Ecole - DAF-06: Chiffre d\'affaire annuel de la recherche - Total annuel", "value": "daf6_tot_ecole"},




    {"label": "DRI-01: Nombre d\'étudiants de TSP partant en stage à l\'étranger - Total annuel", "value": "dri1_tot"},
    {"label": "DRI-02: Nombre d\'étudiants de TSP partant à l\'étranger (académique) - Total annuel", "value": "dri2_tot"},
    {"label": "DRI-03: Nombre d\'étudiants étrangers en échange (stock) - Total annuel", "value": "dri3_tot"},
    {"label": "DRI-04: Nombre  d\'étudiants étrangers, au total, administrativement gérés par TSP – dont DNM comptabilisable par la DF - Total annuel", "value": "dri4_tot"},
    {"label": "DRI-05: Nombre d\'étudiants TSP en double diplôme (entrants et sortants) - Total annuel", "value": "dri5_tot"},
    {"label": "DRI-06: Nombre d\'étudiants étrangers – détail par formation - Total annuel", "value": "dri6_tot"},

    {"label": "Ecole - Graphique radar - Comparaison entre années", "value": "radar_ecole"},


    # ARTEMIS

    # CITI

    # EPH

    # INF

    # RS2M

    # RST


    # Autres

]




def generate_graphs_historique(selected_years, value, baseline_graph):

    # Liste des graphiques disponibles
    graphs = {
        # Ecole
        "df1_tot_ecole": fig_hist_total("DF-01", selected_years, 6),
        "df2_tot": fig_hist_total("DF-02", selected_years, 0),
        "df3_tot": fig_hist_total("DF-03", selected_years, 0),
        "df4_tot": fig_hist_total("DF-04", selected_years, 0),
        "df5_tot": fig_hist_total("DF-05", selected_years, 0),
        "df6_tot": fig_hist_total("DF-06", selected_years, 0),

        "drfd1_tot_ecole": fig_hist_total("DRFD-01", selected_years, 6),
        "drfd2_tot_ecole": fig_hist_total("DRFD-02", selected_years, 6),

        "dire1_bat_ecole": fig_hist_trim_baton("DIRE-01", selected_years, 6),
        "dire1_cou_ecole": fig_hist_trim_courbe("DIRE-01", selected_years, 6),
        "dire1_tot_ecole": fig_hist_total("DIRE-01", selected_years, 6),
        "dire2_bat_ecole": fig_hist_trim_baton("DIRE-02", selected_years, 6),
        "dire2_cou_ecole": fig_hist_trim_courbe("DIRE-02", selected_years, 6),
        "dire2_tot_ecole": fig_hist_total("DIRE-02", selected_years, 6),
        "dire3_bat_ecole": fig_hist_trim_baton("DIRE-03", selected_years, 6),
        "dire3_cou_ecole": fig_hist_trim_courbe("DIRE-03", selected_years, 6),
        "dire3_tot_ecole": fig_hist_total("DIRE-03", selected_years, 6),

        "daf1_bat_ecole": fig_hist_trim_baton("DAF-01", selected_years, 6),
        "daf1_cou_ecole": fig_hist_trim_courbe("DAF-01", selected_years, 6),
        "daf1_tot_ecole": fig_hist_total("DAF-01", selected_years, 6),
        "daf2_bat_ecole": fig_hist_trim_baton("DAF-02", selected_years, 6),
        "daf2_cou_ecole": fig_hist_trim_courbe("DAF-02", selected_years, 6),
        "daf2_tot_ecole": fig_hist_total("DAF-02", selected_years, 6),
        "daf3_bat_ecole": fig_hist_trim_baton("DAF-03", selected_years, 6),
        "daf3_cou_ecole": fig_hist_trim_courbe("DAF-03", selected_years, 6),
        "daf3_tot_ecole": fig_hist_total("DAF-03", selected_years, 6),
        "daf4_bat_ecole": fig_hist_trim_baton("DAF-04", selected_years, 6),
        "daf4_cou_ecole": fig_hist_trim_courbe("DAF-04", selected_years, 6),
        "daf4_tot_ecole": fig_hist_total("DAF-04", selected_years, 6),
        "daf5_bat_ecole": fig_hist_trim_baton("DAF-05", selected_years, 6),
        "daf5_cou_ecole": fig_hist_trim_courbe("DAF-05", selected_years, 6),
        "daf5_tot_ecole": fig_hist_total("DAF-05", selected_years, 6),
        "daf6_tot_ecole": fig_hist_total("DAF-06", selected_years, 6),

        "dri1_tot": fig_hist_total("DRI-01", selected_years, 0),
        "dri2_tot": fig_hist_total("DRI-02", selected_years, 0),
        "dri3_tot": fig_hist_total("DRI-03", selected_years, 0),
        "dri4_tot": fig_hist_total("DRI-04", selected_years, 0),
        "dri5_tot": fig_hist_total("DRI-05", selected_years, 0),
        "dri6_tot": fig_hist_total("DRI-06", selected_years, 0),

        "radar_ecole": fig_hist_radar(selected_years, 6),


        #ARTEMIS

        #CITI

        #EPH

        #INF

        #RS2M

        #RST



        #Autres

        }

    if value is None:
        value = []
    # Création de la liste des IDs de collapse ouverts
    open_collapse_ids = ["collapse-df{}".format(val) for val in value]

    # Génération des graphiques et des collapses
    graph_output = baseline_graph
    for val in value:
        graph_output.append(
            dbc.Collapse(
                dcc.Graph(
                    figure=graphs[val],
                    config={'displaylogo': False}
                ),
                id="collapse-df{}".format(val),
                is_open=("collapse-df{}".format(val) in open_collapse_ids),

            )
        )

    new_graph_output = []

    i = 0
    while 2 * i < len(graph_output):
        if (2 * i + 1 < len(graph_output)):

            graph1 = graph_output[2 * i]
            graph2 = graph_output[2 * i + 1]

            new_graph_output.append(
                dbc.Row(children=[
                    dbc.Col(graph1, width=6),
                    dbc.Col(graph2, width=6)
                ])
            )
            new_graph_output.append(
                html.Hr(style={'borderTop': '2px solid #000000'}))  # Ligne horizontale pour mieux séparer les graphes)

        else:
            graph = graph_output[2 * i]
            new_graph_output.append(
                dbc.Row(children=[
                    dbc.Col(graph)
                ])
            )
            new_graph_output.append(
                html.Hr(style={'borderTop': '2px solid #000000'}))  # Ligne horizontale pour mieux séparer les graphes)
        i += 1

    return new_graph_output, {'display' : 'none'}



def update_old_value_(value, old_value):
    return value


def toggle_collapse_(value, is_open, data, cat_id):
    if (cat_id in value and cat_id in data) or (cat_id not in value and cat_id not in data):
        return is_open
    return not is_open

