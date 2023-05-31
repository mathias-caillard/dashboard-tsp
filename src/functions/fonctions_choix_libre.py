from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from src.functions.fonction_figure import *
from src.fig.df_fig import *
from src.fig.dire_fig import *
from src.fig.daf_fig import *
from src.fig.drfd_fig import *
from src.fig.drh_fig import *
from src.fig.dri_fig import *
from src.fig.departement_fig import *
from src.fig.artemis_fig import *
from src.fig.citi_fig import *
from src.fig.eph_fig import *
from src.fig.inf_fig import *
from src.fig.rs2m_fig import *
from src.fig.rst_fig import *

couleurs = colors_dept
couleurs_all = colors_all


categories_libre = [
    # Fusion avec "categories" de "Choix libre"
    # DF
    {"label": "DF-01: Nombre d\'UP - Total annuel", "value": "df1_tot"},
    {"label": "DF-01: Nombre d\'UP - Graphique en camembert", "value": "df1_cam"},
    {"label": "DF-02: Nombre d\'étudiants FISE", "value": "df2_bat"},
    {"label": "DF-03: Nombre d\'étudiants FIPA", "value": "df3_bat"},
    {"label": "DF-04: Nombre d\'étudiants DNM", "value": "df4_bat"},
    {"label": "DF-05: Nombre d\'étudiants FTLV", "value": "df5_bat"},
    {"label": "DF-06: Nombre total d\'étudiants", "value": "df6_bat"},

    #DRFD
    {"label": "DRFD-01: Publications sur Scopus - Total annuel", "value": "drfd1_tot"},
    {"label": "DRFD-01: Publications sur Scopus - Graphique en camembert", "value": "drfd1_cam"},
    {"label": "DRFD-02: Nombre de doctorants - Total annuel", "value": "drfd2_tot"},
    {"label": "DRFD-02: Nombre de doctorants - Graphique en camembert", "value": "drfd2_cam"},
    {"label": "DRFD-03: H-index médian - Total annuel", "value": "drfd3_tot"},

    #DIRE
    {"label": "DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat"},
    {"label": "DIRE-01: Suivi des contrats de recherche - Comparaison entre départements", "value": "dire1_cou"},
    {"label": "DIRE-01: Suivi des contrats de recherche - Total annuel", "value": "dire1_tot"},
    {"label": "DIRE-01: Suivi des contrats de recherche - Graphique en camembert", "value": "dire1_cam"},
    {"label": "DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat"},
    {"label": "DIRE-02: Brevets et logiciels déposés - Comparaison entre départements", "value": "dire2_cou"},
    {"label": "DIRE-02: Brevets et logiciels déposés - Total annuel", "value": "dire2_tot"},
    {"label": "DIRE-02: Brevets et logiciels déposés - Graphique en camembert", "value": "dire2_cam"},
    {"label": "DIRE-03: Contribution au financement de l\'école - Graphique en bâton", "value": "dire3_bat"},
    {"label": "DIRE-03: Contribution au financement de l\'école - Comparaison entre départements", "value": "dire3_cou"},
    {"label": "DIRE-03: Contribution au financement de l\'école - Total annuel", "value": "dire3_tot"},
    {"label": "DIRE-03: Contribution au financement de l\'école - Graphique en camembert", "value": "dire3_cam"},

    #DAF
    {"label": "DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat"},
    {"label": "DAF-01: Dépenses de vacataires - Comparaison entre départements", "value": "daf1_cou"},
    {"label": "DAF-01: Dépenses de vacataires - Total annuel", "value": "daf1_tot"},
    {"label": "DAF-01: Dépenses de vacataires - Graphique en camembert", "value": "daf1_cam"},
    {"label": "DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat"},
    {"label": "DAF-02: Ressources propres - Comparaison entre départements", "value": "daf2_cou"},
    {"label": "DAF-02: Ressources propres - Total annuel", "value": "daf2_tot"},
    {"label": "DAF-02: Ressources propres - Graphique en camembert", "value": "daf2_cam"},
    {"label": "DAF-03: Ressources d\'état - Graphique en bâton", "value": "daf3_bat"},
    {"label": "DAF-03: Ressources d\'état - Comparaison entre départements", "value": "daf3_cou"},
    {"label": "DAF-03: Ressources d\'état - Total annuel", "value": "daf3_tot"},
    {"label": "DAF-03: Ressources d\'état - Graphique en camembert", "value": "daf3_cam"},
    {"label": "DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat"},
    {"label": "DAF-04: Total des dépenses hors permanents et vacataires - Comparaison entre départements", "value": "daf4_cou"},
    {"label": "DAF-04: Total des dépenses hors permanents et vacataires - Total annuel", "value": "daf4_tot"},
    {"label": "DAF-04: Total des dépenses hors permanents et vacataires - Graphique en camembert", "value": "daf4_cam"},
    {"label": "DAF-05: Dotation de l\'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat"},
    {"label": "DAF-05: Dotation de l\'institut hors permanents et vacataires - Comparaison entre départements", "value": "daf5_cou"},
    {"label": "DAF-05: Dotation de l\'institut hors permanents et vacataires - Total annuel", "value": "daf5_tot"},
    {"label": "DAF-06: Chiffre d\'affaire annuel de la recherche - Graphique en bâton", "value": "daf6_bat"},
    {"label": "DAF-06: Chiffre d\'affaire annuel de la recherche - Graphique en camembert", "value": "daf6_cam"},

    #DRH
    {"label": "DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot"},
    {"label": "DRH-01: Nombre de permanents en ETPT - Graphique en camembert", "value": "drh1_cam"},
    {"label": "DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot"},
    {"label": "DRH-02: Nombre de non-permanents hors recherche en ETPT - Graphique en camembert", "value": "drh2_cam"},
    {"label": "DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat"},
    {"label": "DRH-03: Nombre de non-permanents recherche en ETPT - Comparaison entre départements", "value": "drh3_cou"},
    {"label": "DRH-03: Nombre de non-permanents recherche en ETPT - Total annuel", "value": "drh3_tot"},
    {"label": "DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en camembert", "value": "drh3_cam"},
    {"label": "DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot"},
    {"label": "DRH-04: Nombre de post-docs - Graphique en camembert", "value": "drh4_cam"},
    {"label": "DRH-05: Nombre d\'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot"},
    {"label": "DRH-05: Nombre d\'ETP permanent ayant une nationalité étrangère - Graphique en camembert", "value": "drh5_cam"},
    {"label": "DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot"},
    {"label": "DRH-06: Nombre de nationalités étrangères différentes - Graphique en camembert", "value": "drh6_cam"},




    #DRI

    #ARTEMIS

    #CITI

    #EPH

    #INF

    #RS2M

    #RST

    #Autres

]


def generate_graphs_libre(selected_annee, value, baseline_graph):


    # Liste des graphiques disponibles

    graphs_libre = {

        # DF
        "df1_tot": fig_annuelle_baton("DF-01", selected_annee, "Départements", couleurs),
        "df1_cam": fig_camembert("DF-01", selected_annee, couleurs),
        "df2_bat": fig_trim_baton("DF-02", selected_annee, "Temps", None),
        "df3_bat": fig_trim_baton("DF-03", selected_annee, "Temps", None),
        "df4_bat": fig_trim_baton("DF-04", selected_annee, "Temps", None),
        "df5_bat": fig_trim_baton("DF-05", selected_annee, "Temps", None),
        "df6_bat": fig_trim_baton("DF-06", selected_annee, "Temps", None),

        # DRFD
        "drfd1_tot": fig_annuelle_baton("DRFD-01", selected_annee, "Départements", couleurs),
        "drfd1_cam": fig_camembert("DRFD-01", selected_annee, couleurs),
        "drfd2_tot": fig_annuelle_baton("DRFD-02", selected_annee, "Départements", couleurs),
        "drfd2_cam": fig_camembert("DRFD-02", selected_annee, couleurs),
        "drfd3_tot": fig_annuelle_baton("DRFD-03", selected_annee, "Départements", couleurs),

        # DIRE
        "dire1_bat": fig_trim_baton("DIRE-01", selected_annee, "Départements", couleurs),
        "dire1_cou": fig_trim_courbe("DIRE-01", selected_annee, couleurs),
        "dire1_tot": fig_annuelle_baton("DIRE-01", selected_annee, "Départements", couleurs),
        "dire1_cam": fig_camembert("DIRE-01", selected_annee, couleurs),
        "dire2_bat": fig_trim_baton("DIRE-02", selected_annee, "Départements", couleurs),
        "dire2_cou": fig_trim_courbe("DIRE-02", selected_annee, couleurs),
        "dire2_tot": fig_annuelle_baton("DIRE-02", selected_annee, "Départements", couleurs),
        "dire2_cam": fig_camembert("DIRE-02", selected_annee, couleurs),
        "dire3_bat": fig_trim_baton("DIRE-03", selected_annee, "Départements", couleurs),
        "dire3_cou": fig_trim_courbe("DIRE-03", selected_annee, couleurs),
        "dire3_tot": fig_annuelle_baton("DIRE-03", selected_annee, "Départements", couleurs),
        "dire3_cam": fig_camembert("DIRE-03", selected_annee, couleurs),

        # DAF
        "daf1_bat": fig_trim_baton("DAF-01", selected_annee, "Départements", couleurs),
        "daf1_cou": fig_trim_courbe("DAF-01", selected_annee, couleurs),
        "daf1_tot": fig_annuelle_baton("DAF-01", selected_annee, "Départements", couleurs),
        "daf1_cam": fig_camembert("DAF-01", selected_annee, couleurs),
        "daf2_bat": fig_trim_baton("DAF-02", selected_annee, "Départements", couleurs),
        "daf2_cou": fig_trim_courbe("DAF-02", selected_annee, couleurs),
        "daf2_tot": fig_annuelle_baton("DAF-02", selected_annee, "Départements", couleurs),
        "daf2_cam": fig_camembert("DAF-02", selected_annee, couleurs),
        "daf3_bat": fig_trim_baton("DAF-03", selected_annee, "Départements", couleurs),
        "daf3_cou": fig_trim_courbe("DAF-03", selected_annee, couleurs),
        "daf3_tot": fig_annuelle_baton("DAF-03", selected_annee, "Départements", couleurs),
        "daf3_cam": fig_camembert("DAF-03", selected_annee, couleurs),
        "daf4_bat": fig_trim_baton("DAF-04", selected_annee, "Départements", couleurs),
        "daf4_cou": fig_trim_courbe("DAF-04", selected_annee, couleurs),
        "daf4_tot": fig_annuelle_baton("DAF-04", selected_annee, "Départements", couleurs),
        "daf4_cam": fig_camembert("DAF-04", selected_annee, couleurs),
        "daf5_bat": fig_trim_baton("DAF-05", selected_annee, "Départements", couleurs),
        "daf5_cou": fig_trim_courbe("DAF-05", selected_annee, couleurs),
        "daf5_tot": fig_annuelle_baton("DAF-05", selected_annee, "Départements", couleurs),
        "daf6_bat": fig_annuelle_baton("DAF-06", selected_annee, "Départements", couleurs),
        "daf6_cam": fig_camembert("DAF-06", selected_annee, couleurs),

        # DRH
        "drh1_tot": fig_annuelle_baton("DRH-01", selected_annee, "Services/Départements", couleurs_all),
        "drh1_cam": fig_camembert("DRH-01", selected_annee, couleurs_all),
        "drh2_tot": fig_annuelle_baton("DRH-02", selected_annee, "Services/Départements", couleurs_all),
        "drh2_cam": fig_camembert("DRH-02", selected_annee, couleurs_all),
        "drh3_bat": fig_trim_baton("DRH-03", selected_annee, "Départements", couleurs),
        "drh3_cou": fig_trim_courbe("DRH-03", selected_annee, couleurs),
        "drh3_tot": fig_annuelle_baton("DRH-03", selected_annee, "Départements", couleurs),
        "drh3_cam": fig_camembert("DRH-03", selected_annee, couleurs),
        "drh4_tot": fig_annuelle_baton("DRH-04", selected_annee, "Services/Départements", couleurs_all),
        "drh4_cam": fig_camembert("DRH-04", selected_annee, couleurs_all),
        "drh5_tot": fig_annuelle_baton("DRH-05", selected_annee, "Services/Départements", couleurs_all),
        "drh5_cam": fig_camembert("DRH-05", selected_annee, couleurs_all),
        "drh6_tot": fig_annuelle_baton("DRH-06", selected_annee, "Services/Départements", couleurs_all),
        "drh6_cam": fig_camembert("DRH-06", selected_annee, couleurs_all),

        # DRI

        # ARTEMIS

        # CITI

        # EPH

        # INF

        # RS2M

        # RST

        # Autres


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
                    figure=graphs_libre[val],
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

    return new_graph_output, {'display': 'none'}