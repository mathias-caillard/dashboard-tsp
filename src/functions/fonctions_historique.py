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

    {"label": "Ecole - DRFD-01: Publications sur Scopus - Total annuel", "value": "drfd1_tot_ecole"},
    {"label": "Ecole - DRFD-02: Nombre de doctorants - Total annuel", "value": "drfd2_tot_ecole"},
    {"label": "Ecole - DRFD-03: H-index médian - Total annuel", "value": "drfd3_tot_ecole"},

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
    {"label": "Ecole - DAF-01: Dépenses de vacataires - Comparaison entre années", "value": "daf1_cou_ecole"},
    {"label": "Ecole - DAF-01: Dépenses de vacataires - Total annuel", "value": "daf1_tot_ecole"},
    {"label": "Ecole - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_ecole"},
    {"label": "Ecole - DAF-02: Ressources propres - Comparaison entre années", "value": "daf2_cou_ecole"},
    {"label": "Ecole - DAF-02: Ressources propres - Total annuel", "value": "daf2_tot_ecole"},
    {"label": "Ecole - DAF-03: Ressources d\'état - Graphique en bâton", "value": "daf3_bat_ecole"},
    {"label": "Ecole - DAF-03: Ressources d\'état - Comparaison entre années", "value": "daf3_cou_ecole"},
    {"label": "Ecole - DAF-03: Ressources d\'état - Total annuel", "value": "daf3_tot_ecole"},
    {"label": "Ecole - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_ecole"},
    {"label": "Ecole - DAF-04: Total des dépenses hors permanents et vacataires - Comparaison entre années", "value": "daf4_cou_ecole"},
    {"label": "Ecole - DAF-04: Total des dépenses hors permanents et vacataires - Total annuel", "value": "daf4_tot_ecole"},
    {"label": "Ecole - DAF-05: Dotation de l\'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_ecole"},
    {"label": "Ecole - DAF-05: Dotation de l\'institut hors permanents et vacataires - Comparaison entre années", "value": "daf5_cou_ecole"},
    {"label": "Ecole - DAF-05: Dotation de l\'institut hors permanents et vacataires - Total annuel", "value": "daf5_tot_ecole"},
    {"label": "Ecole - DAF-06: Chiffre d\'affaire annuel de la recherche - Total annuel", "value": "daf6_tot_ecole"},


    {"label": "Ecole - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_ecole"},
    {"label": "Ecole - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_ecole"},
    {"label": "Ecole - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_ecole"},
    {"label": "Ecole - DRH-03: Nombre de non-permanents recherche en ETPT - Comparaison entre années", "value": "drh3_cou_ecole"},
    {"label": "Ecole - DRH-03: Nombre de non-permanents recherche en ETPT - Total annuel", "value": "drh3_tot_ecole"},
    {"label": "Ecole - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_ecole"},
    {"label": "Ecole - DRH-05: Nombre d\'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_ecole"},
    {"label": "Ecole - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_ecole"},

    {"label": "DRI-01: Nombre d\'étudiants de TSP partant en stage à l\'étranger - Total annuel", "value": "dri1_tot"},
    {"label": "DRI-02: Nombre d\'étudiants de TSP partant à l\'étranger (académique) - Total annuel", "value": "dri2_tot"},
    {"label": "DRI-03: Nombre d\'étudiants étrangers en échange (stock) - Total annuel", "value": "dri3_tot"},
    {"label": "DRI-04: Nombre  d\'étudiants étrangers, au total, administrativement gérés par TSP – dont DNM comptabilisable par la DF - Total annuel", "value": "dri4_tot"},
    {"label": "DRI-05: Nombre d\'étudiants TSP en double diplôme (entrants et sortants) - Total annuel", "value": "dri5_tot"},
    {"label": "DRI-06: Nombre d\'étudiants étrangers – détail par formation - Total annuel", "value": "dri6_tot"},

    {"label": "Ecole - Graphique radar - Comparaison entre années", "value": "radar_ecole"},


    # ARTEMIS
    {"label": "ARTEMIS - DF-01: Nombre d\'UP - Total annuel", "value": "df1_tot_artemis"},

    {"label": "ARTEMIS - DRFD-01: Publications sur Scopus - Total annuel", "value": "drfd1_tot_artemis"},
    {"label": "ARTEMIS - DRFD-02: Nombre de doctorants - Total annuel", "value": "drfd2_tot_artemis"},
    {"label": "ARTEMIS - DRFD-03: H-index médian - Total annuel", "value": "drfd3_tot_artemis"},

    {"label": "ARTEMIS - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_artemis"},
    {"label": "ARTEMIS - DIRE-01: Suivi des contrats de recherche - Comparaison entre années", "value": "dire1_cou_artemis"},
    {"label": "ARTEMIS - DIRE-01: Suivi des contrats de recherche - Total annuel", "value": "dire1_tot_artemis"},
    {"label": "ARTEMIS - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_artemis"},
    {"label": "ARTEMIS - DIRE-02: Brevets et logiciels déposés - Comparaison entre années", "value": "dire2_cou_artemis"},
    {"label": "ARTEMIS - DIRE-02: Brevets et logiciels déposés - Total annuel", "value": "dire2_tot_artemis"},
    {"label": "ARTEMIS - DIRE-03: Contribution au financement de l'école - Graphique en bâton", "value": "dire3_bat_artemis"},
    {"label": "ARTEMIS - DIRE-03: Contribution au financement de l'école - Comparaison entre années", "value": "dire3_cou_artemis"},
    {"label": "ARTEMIS - DIRE-03: Contribution au financement de l'école - Total annuel", "value": "dire3_tot_artemis"},

    {"label": "ARTEMIS - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_artemis"},
    {"label": "ARTEMIS - DAF-01: Dépenses de vacataires - Comparaison entre années", "value": "daf1_cou_artemis"},
    {"label": "ARTEMIS - DAF-01: Dépenses de vacataires - Total annuel", "value": "daf1_tot_artemis"},
    {"label": "ARTEMIS - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_artemis"},
    {"label": "ARTEMIS - DAF-02: Ressources propres - Comparaison entre années", "value": "daf2_cou_artemis"},
    {"label": "ARTEMIS - DAF-02: Ressources propres - Total annuel", "value": "daf2_tot_artemis"},
    {"label": "ARTEMIS - DAF-03: Ressources d'état - Graphique en bâton", "value": "daf3_bat_artemis"},
    {"label": "ARTEMIS - DAF-03: Ressources d'état - Comparaison entre années", "value": "daf3_cou_artemis"},
    {"label": "ARTEMIS - DAF-03: Ressources d'état - Total annuel", "value": "daf3_tot_artemis"},
    {"label": "ARTEMIS - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_artemis"},
    {"label": "ARTEMIS - DAF-04: Total des dépenses hors permanents et vacataires - Comparaison entre années", "value": "daf4_cou_artemis"},
    {"label": "ARTEMIS - DAF-04: Total des dépenses hors permanents et vacataires - Total annuel", "value": "daf4_tot_artemis"},
    {"label": "ARTEMIS - DAF-05: Dotation de l'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_artemis"},
    {"label": "ARTEMIS - DAF-05: Dotation de l'institut hors permanents et vacataires - Comparaison entre années", "value": "daf5_cou_artemis"},
    {"label": "ARTEMIS - DAF-05: Dotation de l'institut hors permanents et vacataires - Total annuel", "value": "daf5_tot_artemis"},
    {"label": "ARTEMIS - DAF-06: Chiffre d'affaire annuel de la recherche - Total annuel", "value": "daf6_tot_artemis"},


    {"label": "ARTEMIS - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_artemis"},
    {"label": "ARTEMIS - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_artemis"},
    {"label": "ARTEMIS - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_artemis"},
    {"label": "ARTEMIS - DRH-03: Nombre de non-permanents recherche en ETPT - Comparaison entre années", "value": "drh3_cou_artemis"},
    {"label": "ARTEMIS - DRH-03: Nombre de non-permanents recherche en ETPT - Total annuel", "value": "drh3_tot_artemis"},
    {"label": "ARTEMIS - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_artemis"},
    {"label": "ARTEMIS - DRH-05: Nombre d'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_artemis"},
    {"label": "ARTEMIS - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_artemis"},

    {"label": "ARTEMIS - Graphique radar - Comparaison entre années", "value": "radar_artemis"},

    # CITI
    {"label": "CITI - DF-01: Nombre d\'UP - Total annuel", "value": "df1_tot_citi"},

    {"label": "CITI - DRFD-01: Publications sur Scopus - Total annuel", "value": "drfd1_tot_citi"},
    {"label": "CITI - DRFD-02: Nombre de doctorants - Total annuel", "value": "drfd2_tot_citi"},
    {"label": "CITI - DRFD-03: H-index médian - Total annuel", "value": "drfd3_tot_citi"},

    {"label": "CITI - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_citi"},
    {"label": "CITI - DIRE-01: Suivi des contrats de recherche - Comparaison entre années", "value": "dire1_cou_citi"},
    {"label": "CITI - DIRE-01: Suivi des contrats de recherche - Total annuel", "value": "dire1_tot_citi"},
    {"label": "CITI - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_citi"},
    {"label": "CITI - DIRE-02: Brevets et logiciels déposés - Comparaison entre années", "value": "dire2_cou_citi"},
    {"label": "CITI - DIRE-02: Brevets et logiciels déposés - Total annuel", "value": "dire2_tot_citi"},
    {"label": "CITI - DIRE-03: Contribution au financement de l'école - Graphique en bâton", "value": "dire3_bat_citi"},
    {"label": "CITI - DIRE-03: Contribution au financement de l'école - Comparaison entre années", "value": "dire3_cou_citi"},
    {"label": "CITI - DIRE-03: Contribution au financement de l'école - Total annuel", "value": "dire3_tot_citi"},

    {"label": "CITI - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_citi"},
    {"label": "CITI - DAF-01: Dépenses de vacataires - Comparaison entre années", "value": "daf1_cou_citi"},
    {"label": "CITI - DAF-01: Dépenses de vacataires - Total annuel", "value": "daf1_tot_citi"},
    {"label": "CITI - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_citi"},
    {"label": "CITI - DAF-02: Ressources propres - Comparaison entre années", "value": "daf2_cou_citi"},
    {"label": "CITI - DAF-02: Ressources propres - Total annuel", "value": "daf2_tot_citi"},
    {"label": "CITI - DAF-03: Ressources d'état - Graphique en bâton", "value": "daf3_bat_citi"},
    {"label": "CITI - DAF-03: Ressources d'état - Comparaison entre années", "value": "daf3_cou_citi"},
    {"label": "CITI - DAF-03: Ressources d'état - Total annuel", "value": "daf3_tot_citi"},
    {"label": "CITI - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_citi"},
    {"label": "CITI - DAF-04: Total des dépenses hors permanents et vacataires - Comparaison entre années", "value": "daf4_cou_citi"},
    {"label": "CITI - DAF-04: Total des dépenses hors permanents et vacataires - Total annuel", "value": "daf4_tot_citi"},
    {"label": "CITI - DAF-05: Dotation de l'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_citi"},
    {"label": "CITI - DAF-05: Dotation de l'institut hors permanents et vacataires - Comparaison entre années", "value": "daf5_cou_citi"},
    {"label": "CITI - DAF-05: Dotation de l'institut hors permanents et vacataires - Total annuel", "value": "daf5_tot_citi"},
    {"label": "CITI - DAF-06: Chiffre d'affaire annuel de la recherche - Total annuel", "value": "daf6_tot_citi"},

    {"label": "CITI - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_citi"},
    {"label": "CITI - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_citi"},
    {"label": "CITI - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_citi"},
    {"label": "CITI - DRH-03: Nombre de non-permanents recherche en ETPT - Comparaison entre années", "value": "drh3_cou_citi"},
    {"label": "CITI - DRH-03: Nombre de non-permanents recherche en ETPT - Total annuel", "value": "drh3_tot_citi"},
    {"label": "CITI - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_citi"},
    {"label": "CITI - DRH-05: Nombre d'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_citi"},
    {"label": "CITI - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_citi"},

    {"label": "CITI - Graphique radar - Comparaison entre années", "value": "radar_citi"},

    # EPH
    {"label": "EPH - DF-01: Nombre d\'UP - Total annuel", "value": "df1_tot_eph"},

    {"label": "EPH - DRFD-01: Publications sur Scopus - Total annuel", "value": "drfd1_tot_eph"},
    {"label": "EPH - DRFD-02: Nombre de doctorants - Total annuel", "value": "drfd2_tot_eph"},
    {"label": "EPH - DRFD-03: H-index médian - Total annuel", "value": "drfd3_tot_eph"},

    {"label": "EPH - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_eph"},
    {"label": "EPH - DIRE-01: Suivi des contrats de recherche - Comparaison entre années", "value": "dire1_cou_eph"},
    {"label": "EPH - DIRE-01: Suivi des contrats de recherche - Total annuel", "value": "dire1_tot_eph"},
    {"label": "EPH - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_eph"},
    {"label": "EPH - DIRE-02: Brevets et logiciels déposés - Comparaison entre années", "value": "dire2_cou_eph"},
    {"label": "EPH - DIRE-02: Brevets et logiciels déposés - Total annuel", "value": "dire2_tot_eph"},
    {"label": "EPH - DIRE-03: Contribution au financement de l'école - Graphique en bâton", "value": "dire3_bat_eph"},
    {"label": "EPH - DIRE-03: Contribution au financement de l'école - Comparaison entre années", "value": "dire3_cou_eph"},
    {"label": "EPH - DIRE-03: Contribution au financement de l'école - Total annuel", "value": "dire3_tot_eph"},

    {"label": "EPH - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_eph"},
    {"label": "EPH - DAF-01: Dépenses de vacataires - Comparaison entre années", "value": "daf1_cou_eph"},
    {"label": "EPH - DAF-01: Dépenses de vacataires - Total annuel", "value": "daf1_tot_eph"},
    {"label": "EPH - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_eph"},
    {"label": "EPH - DAF-02: Ressources propres - Comparaison entre années", "value": "daf2_cou_eph"},
    {"label": "EPH - DAF-02: Ressources propres - Total annuel", "value": "daf2_tot_eph"},
    {"label": "EPH - DAF-03: Ressources d'état - Graphique en bâton", "value": "daf3_bat_eph"},
    {"label": "EPH - DAF-03: Ressources d'état - Comparaison entre années", "value": "daf3_cou_eph"},
    {"label": "EPH - DAF-03: Ressources d'état - Total annuel", "value": "daf3_tot_eph"},
    {"label": "EPH - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_eph"},
    {"label": "EPH - DAF-04: Total des dépenses hors permanents et vacataires - Comparaison entre années", "value": "daf4_cou_eph"},
    {"label": "EPH - DAF-04: Total des dépenses hors permanents et vacataires - Total annuel", "value": "daf4_tot_eph"},
    {"label": "EPH - DAF-05: Dotation de l'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_eph"},
    {"label": "EPH - DAF-05: Dotation de l'institut hors permanents et vacataires - Comparaison entre années", "value": "daf5_cou_eph"},
    {"label": "EPH - DAF-05: Dotation de l'institut hors permanents et vacataires - Total annuel", "value": "daf5_tot_eph"},
    {"label": "EPH - DAF-06: Chiffre d'affaire annuel de la recherche - Total annuel", "value": "daf6_tot_eph"},

    {"label": "EPH - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_eph"},
    {"label": "EPH - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_eph"},
    {"label": "EPH - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_eph"},
    {"label": "EPH - DRH-03: Nombre de non-permanents recherche en ETPT - Comparaison entre années", "value": "drh3_cou_eph"},
    {"label": "EPH - DRH-03: Nombre de non-permanents recherche en ETPT - Total annuel", "value": "drh3_tot_eph"},
    {"label": "EPH - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_eph"},
    {"label": "EPH - DRH-05: Nombre d'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_eph"},
    {"label": "EPH - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_eph"},

    {"label": "EPH - Graphique radar - Comparaison entre années", "value": "radar_eph"},


    # INF
    {"label": "INF - DF-01: Nombre d\'UP - Total annuel", "value": "df1_tot_inf"},

    {"label": "INF - DRFD-01: Publications sur Scopus - Total annuel", "value": "drfd1_tot_inf"},
    {"label": "INF - DRFD-02: Nombre de doctorants - Total annuel", "value": "drfd2_tot_inf"},
    {"label": "INF - DRFD-03: H-index médian - Total annuel", "value": "drfd3_tot_inf"},

    {"label": "INF - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_inf"},
    {"label": "INF - DIRE-01: Suivi des contrats de recherche - Comparaison entre années", "value": "dire1_cou_inf"},
    {"label": "INF - DIRE-01: Suivi des contrats de recherche - Total annuel", "value": "dire1_tot_inf"},
    {"label": "INF - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_inf"},
    {"label": "INF - DIRE-02: Brevets et logiciels déposés - Comparaison entre années", "value": "dire2_cou_inf"},
    {"label": "INF - DIRE-02: Brevets et logiciels déposés - Total annuel", "value": "dire2_tot_inf"},
    {"label": "INF - DIRE-03: Contribution au financement de l'école - Graphique en bâton", "value": "dire3_bat_inf"},
    {"label": "INF - DIRE-03: Contribution au financement de l'école - Comparaison entre années", "value": "dire3_cou_inf"},
    {"label": "INF - DIRE-03: Contribution au financement de l'école - Total annuel", "value": "dire3_tot_inf"},

    {"label": "INF - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_inf"},
    {"label": "INF - DAF-01: Dépenses de vacataires - Comparaison entre années", "value": "daf1_cou_inf"},
    {"label": "INF - DAF-01: Dépenses de vacataires - Total annuel", "value": "daf1_tot_inf"},
    {"label": "INF - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_inf"},
    {"label": "INF - DAF-02: Ressources propres - Comparaison entre années", "value": "daf2_cou_inf"},
    {"label": "INF - DAF-02: Ressources propres - Total annuel", "value": "daf2_tot_inf"},
    {"label": "INF - DAF-03: Ressources d'état - Graphique en bâton", "value": "daf3_bat_inf"},
    {"label": "INF - DAF-03: Ressources d'état - Comparaison entre années", "value": "daf3_cou_inf"},
    {"label": "INF - DAF-03: Ressources d'état - Total annuel", "value": "daf3_tot_inf"},
    {"label": "INF - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_inf"},
    {"label": "INF - DAF-04: Total des dépenses hors permanents et vacataires - Comparaison entre années", "value": "daf4_cou_inf"},
    {"label": "INF - DAF-04: Total des dépenses hors permanents et vacataires - Total annuel", "value": "daf4_tot_inf"},
    {"label": "INF - DAF-05: Dotation de l'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_inf"},
    {"label": "INF - DAF-05: Dotation de l'institut hors permanents et vacataires - Comparaison entre années", "value": "daf5_cou_inf"},
    {"label": "INF - DAF-05: Dotation de l'institut hors permanents et vacataires - Total annuel", "value": "daf5_tot_inf"},
    {"label": "INF - DAF-06: Chiffre d'affaire annuel de la recherche - Total annuel", "value": "daf6_tot_inf"},

    {"label": "INF - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_inf"},
    {"label": "INF - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_inf"},
    {"label": "INF - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_inf"},
    {"label": "INF - DRH-03: Nombre de non-permanents recherche en ETPT - Comparaison entre années", "value": "drh3_cou_inf"},
    {"label": "INF - DRH-03: Nombre de non-permanents recherche en ETPT - Total annuel", "value": "drh3_tot_inf"},
    {"label": "INF - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_inf"},
    {"label": "INF - DRH-05: Nombre d'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_inf"},
    {"label": "INF - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_inf"},

    {"label": "INF - Graphique radar - Comparaison entre années", "value": "radar_inf"},


    # RS2M
    {"label": "RS2M - DF-01: Nombre d\'UP - Total annuel", "value": "df1_tot_rs2m"},

    {"label": "RS2M - DRFD-01: Publications sur Scopus - Total annuel", "value": "drfd1_tot_rs2m"},
    {"label": "RS2M - DRFD-02: Nombre de doctorants - Total annuel", "value": "drfd2_tot_rs2m"},
    {"label": "RS2M - DRFD-03: H-index médian - Total annuel", "value": "drfd3_tot_rs2m"},

    {"label": "RS2M - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_rs2m"},
    {"label": "RS2M - DIRE-01: Suivi des contrats de recherche - Comparaison entre années", "value": "dire1_cou_rs2m"},
    {"label": "RS2M - DIRE-01: Suivi des contrats de recherche - Total annuel", "value": "dire1_tot_rs2m"},
    {"label": "RS2M - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_rs2m"},
    {"label": "RS2M - DIRE-02: Brevets et logiciels déposés - Comparaison entre années", "value": "dire2_cou_rs2m"},
    {"label": "RS2M - DIRE-02: Brevets et logiciels déposés - Total annuel", "value": "dire2_tot_rs2m"},
    {"label": "RS2M - DIRE-03: Contribution au financement de l'école - Graphique en bâton", "value": "dire3_bat_rs2m"},
    {"label": "RS2M - DIRE-03: Contribution au financement de l'école - Comparaison entre années", "value": "dire3_cou_rs2m"},
    {"label": "RS2M - DIRE-03: Contribution au financement de l'école - Total annuel", "value": "dire3_tot_rs2m"},

    {"label": "RS2M - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_rs2m"},
    {"label": "RS2M - DAF-01: Dépenses de vacataires - Comparaison entre années", "value": "daf1_cou_rs2m"},
    {"label": "RS2M - DAF-01: Dépenses de vacataires - Total annuel", "value": "daf1_tot_rs2m"},
    {"label": "RS2M - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_rs2m"},
    {"label": "RS2M - DAF-02: Ressources propres - Comparaison entre années", "value": "daf2_cou_rs2m"},
    {"label": "RS2M - DAF-02: Ressources propres - Total annuel", "value": "daf2_tot_rs2m"},
    {"label": "RS2M - DAF-03: Ressources d'état - Graphique en bâton", "value": "daf3_bat_rs2m"},
    {"label": "RS2M - DAF-03: Ressources d'état - Comparaison entre années", "value": "daf3_cou_rs2m"},
    {"label": "RS2M - DAF-03: Ressources d'état - Total annuel", "value": "daf3_tot_rs2m"},
    {"label": "RS2M - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_rs2m"},
    {"label": "RS2M - DAF-04: Total des dépenses hors permanents et vacataires - Comparaison entre années", "value": "daf4_cou_rs2m"},
    {"label": "RS2M - DAF-04: Total des dépenses hors permanents et vacataires - Total annuel", "value": "daf4_tot_rs2m"},
    {"label": "RS2M - DAF-05: Dotation de l'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_rs2m"},
    {"label": "RS2M - DAF-05: Dotation de l'institut hors permanents et vacataires - Comparaison entre années", "value": "daf5_cou_rs2m"},
    {"label": "RS2M - DAF-05: Dotation de l'institut hors permanents et vacataires - Total annuel", "value": "daf5_tot_rs2m"},
    {"label": "RS2M - DAF-06: Chiffre d'affaire annuel de la recherche - Total annuel", "value": "daf6_tot_rs2m"},

    {"label": "RS2M - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_rs2m"},
    {"label": "RS2M - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_rs2m"},
    {"label": "RS2M - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_rs2m"},
    {"label": "RS2M - DRH-03: Nombre de non-permanents recherche en ETPT - Comparaison entre années", "value": "drh3_cou_rs2m"},
    {"label": "RS2M - DRH-03: Nombre de non-permanents recherche en ETPT - Total annuel", "value": "drh3_tot_rs2m"},
    {"label": "RS2M - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_rs2m"},
    {"label": "RS2M - DRH-05: Nombre d'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_rs2m"},
    {"label": "RS2M - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_rs2m"},

    {"label": "RS2M - Graphique radar - Comparaison entre années", "value": "radar_rs2m"},


    # RST
    {"label": "RST - DF-01: Nombre d\'UP - Total annuel", "value": "df1_tot_rst"},

    {"label": "RST - DRFD-01: Publications sur Scopus - Total annuel", "value": "drfd1_tot_rst"},
    {"label": "RST - DRFD-02: Nombre de doctorants - Total annuel", "value": "drfd2_tot_rst"},
    {"label": "RST - DRFD-03: H-index médian - Total annuel", "value": "drfd3_tot_rst"},

    {"label": "RST - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_rst"},
    {"label": "RST - DIRE-01: Suivi des contrats de recherche - Comparaison entre années", "value": "dire1_cou_rst"},
    {"label": "RST - DIRE-01: Suivi des contrats de recherche - Total annuel", "value": "dire1_tot_rst"},
    {"label": "RST - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_rst"},
    {"label": "RST - DIRE-02: Brevets et logiciels déposés - Comparaison entre années", "value": "dire2_cou_rst"},
    {"label": "RST - DIRE-02: Brevets et logiciels déposés - Total annuel", "value": "dire2_tot_rst"},
    {"label": "RST - DIRE-03: Contribution au financement de l'école - Graphique en bâton", "value": "dire3_bat_rst"},
    {"label": "RST - DIRE-03: Contribution au financement de l'école - Comparaison entre années", "value": "dire3_cou_rst"},
    {"label": "RST - DIRE-03: Contribution au financement de l'école - Total annuel", "value": "dire3_tot_rst"},

    {"label": "RST - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_rst"},
    {"label": "RST - DAF-01: Dépenses de vacataires - Comparaison entre années", "value": "daf1_cou_rst"},
    {"label": "RST - DAF-01: Dépenses de vacataires - Total annuel", "value": "daf1_tot_rst"},
    {"label": "RST - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_rst"},
    {"label": "RST - DAF-02: Ressources propres - Comparaison entre années", "value": "daf2_cou_rst"},
    {"label": "RST - DAF-02: Ressources propres - Total annuel", "value": "daf2_tot_rst"},
    {"label": "RST - DAF-03: Ressources d'état - Graphique en bâton", "value": "daf3_bat_rst"},
    {"label": "RST - DAF-03: Ressources d'état - Comparaison entre années", "value": "daf3_cou_rst"},
    {"label": "RST - DAF-03: Ressources d'état - Total annuel", "value": "daf3_tot_rst"},
    {"label": "RST - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_rst"},
    {"label": "RST - DAF-04: Total des dépenses hors permanents et vacataires - Comparaison entre années", "value": "daf4_cou_rst"},
    {"label": "RST - DAF-04: Total des dépenses hors permanents et vacataires - Total annuel", "value": "daf4_tot_rst"},
    {"label": "RST - DAF-05: Dotation de l'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_rst"},
    {"label": "RST - DAF-05: Dotation de l'institut hors permanents et vacataires - Comparaison entre années", "value": "daf5_cou_rst"},
    {"label": "RST - DAF-05: Dotation de l'institut hors permanents et vacataires - Total annuel", "value": "daf5_tot_rst"},
    {"label": "RST - DAF-06: Chiffre d'affaire annuel de la recherche - Total annuel", "value": "daf6_tot_rst"},


    {"label": "RST - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_rst"},
    {"label": "RST - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_rst"},
    {"label": "RST - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_rst"},
    {"label": "RST - DRH-03: Nombre de non-permanents recherche en ETPT - Comparaison entre années", "value": "drh3_cou_rst"},
    {"label": "RST - DRH-03: Nombre de non-permanents recherche en ETPT - Total annuel", "value": "drh3_tot_rst"},
    {"label": "RST - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_rst"},
    {"label": "RST - DRH-05: Nombre d'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_rst"},
    {"label": "RST - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_rst"},

    {"label": "RST - Graphique radar - Comparaison entre années", "value": "radar_rst"},


    # Autres
    #DF
    {"label": "DF - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_df"},
    {"label": "DF - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_df"},
    {"label": "DF - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_df"},
    {"label": "DF - DRH-05: Nombre d'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_df"},
    {"label": "DF - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_df"},

    #DRFD
    {"label": "DRFD - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_drfd"},
    {"label": "DRFD - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_drfd"},
    {"label": "DRFD - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_drfd"},
    {"label": "DRFD - DRH-05: Nombre d'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_drfd"},
    {"label": "DRFD - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_drfd"},

    #DIRE
    {"label": "DIRE - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_dire"},
    {"label": "DIRE - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_dire"},
    {"label": "DIRE - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_dire"},
    {"label": "DIRE - DRH-05: Nombre d'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_dire"},
    {"label": "DIRE - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_dire"},

    #DRI
    {"label": "DRI - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_dri"},
    {"label": "DRI - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_dri"},
    {"label": "DRI - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_dri"},
    {"label": "DRI - DRH-05: Nombre d'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_dri"},
    {"label": "DRI - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_dri"},

    #DCOM
    {"label": "DCOM - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot_dcom"},
    {"label": "DCOM - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot_dcom"},
    {"label": "DCOM - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot_dcom"},
    {"label": "DCOM - DRH-05: Nombre d'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot_dcom"},
    {"label": "DCOM - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot_dcom"},

]




def generate_graphs_historique(selected_years, value, baseline_graph):

    # Liste des graphiques disponibles
    graphs = {}

    #Ecole
    if "df1_tot_ecole" in value:
        graphs["df1_tot_ecole"] = fig_hist_total("DF-01", selected_years, 6)
    if "df2_tot" in value:
        graphs["df2_tot"] = fig_hist_total("DF-02", selected_years, 6)
    if "df3_tot" in value:
        graphs["df3_tot"] = fig_hist_total("DF-03", selected_years, 6)
    if "df4_tot" in value:
        graphs["df4_tot"] = fig_hist_total("DF-04", selected_years, 6)
    if "df5_tot" in value:
        graphs["df5_tot"] = fig_hist_total("DF-05", selected_years, 6)
    if "df6_tot" in value:
        graphs["df6_tot"] = fig_hist_total("DF-06", selected_years, 6)

    if "drfd1_tot_ecole" in value:
        graphs["drfd1_tot_ecole"] = fig_hist_total("DRFD-01", selected_years, 6)
    if "drfd2_tot_ecole" in value:
        graphs["drfd2_tot_ecole"] = fig_hist_total("DRFD-02", selected_years, 6)
    if "drfd3_tot_ecole" in value:
        graphs["drfd3_tot_ecole"] = fig_hist_total("DRFD-03", selected_years, 6)

    if "dire1_bat_ecole" in value:
        graphs["dire1_bat_ecole"] = fig_hist_trim_baton("DIRE-01", selected_years, 6)
    if "dire1_cou_ecole" in value:
        graphs["dire1_cou_ecole"] = fig_hist_trim_courbe("DIRE-01", selected_years, 6)
    if "dire1_tot_ecole" in value:
        graphs["dire1_tot_ecole"] = fig_hist_total("DIRE-01", selected_years, 6)
    if "dire2_bat_ecole" in value:
        graphs["dire2_bat_ecole"] = fig_hist_trim_baton("DIRE-02", selected_years, 6)
    if "dire2_cou_ecole" in value:
        graphs["dire2_cou_ecole"] = fig_hist_trim_courbe("DIRE-02", selected_years, 6)
    if "dire2_tot_ecole" in value:
        graphs["dire2_tot_ecole"] = fig_hist_total("DIRE-02", selected_years, 6)
    if "dire3_bat_ecole" in value:
        graphs["dire3_bat_ecole"] = fig_hist_trim_baton("DIRE-03", selected_years, 6)
    if "dire3_cou_ecole" in value:
        graphs["dire3_cou_ecole"] = fig_hist_trim_courbe("DIRE-03", selected_years, 6)
    if "dire3_tot_ecole" in value:
        graphs["dire3_tot_ecole"] = fig_hist_total("DIRE-03", selected_years, 6)

    if "daf1_bat_ecole" in value:
        graphs["daf1_bat_ecole"] = fig_hist_trim_baton("DAF-01", selected_years, 6)
    if "daf1_cou_ecole" in value:
        graphs["daf1_cou_ecole"] = fig_hist_trim_courbe("DAF-01", selected_years, 6)
    if "daf1_tot_ecole" in value:
        graphs["daf1_tot_ecole"] = fig_hist_total("DAF-01", selected_years, 6)
    if "daf2_bat_ecole" in value:
        graphs["daf2_bat_ecole"] = fig_hist_trim_baton("DAF-02", selected_years, 6)
    if "daf2_cou_ecole" in value:
        graphs["daf2_cou_ecole"] = fig_hist_trim_courbe("DAF-02", selected_years, 6)
    if "daf2_tot_ecole" in value:
        graphs["daf2_tot_ecole"] = fig_hist_total("DAF-02", selected_years, 6)
    if "daf3_bat_ecole" in value:
        graphs["daf3_bat_ecole"] = fig_hist_trim_baton("DAF-03", selected_years, 6)
    if "daf3_cou_ecole" in value:
        graphs["daf3_cou_ecole"] = fig_hist_trim_courbe("DAF-03", selected_years, 6)
    if "daf3_tot_ecole" in value:
        graphs["daf3_tot_ecole"] = fig_hist_total("DAF-03", selected_years, 6)
    if "daf4_bat_ecole" in value:
        graphs["daf4_bat_ecole"] = fig_hist_trim_baton("DAF-04", selected_years, 6)
    if "daf4_cou_ecole" in value:
        graphs["daf4_cou_ecole"] = fig_hist_trim_courbe("DAF-04", selected_years, 6)
    if "daf4_tot_ecole" in value:
        graphs["daf4_tot_ecole"] = fig_hist_total("DAF-04", selected_years, 6)
    if "daf5_bat_ecole" in value:
        graphs["daf5_bat_ecole"] = fig_hist_trim_baton("DAF-05", selected_years, 6)
    if "daf5_cou_ecole" in value:
        graphs["daf5_cou_ecole"] = fig_hist_trim_courbe("DAF-05", selected_years, 6)
    if "daf5_tot_ecole" in value:
        graphs["daf5_tot_ecole"] = fig_hist_total("DAF-05", selected_years, 6)
    if "daf6_tot_ecole" in value:
        graphs["daf6_tot_ecole"] = fig_hist_total("DAF-06", selected_years, 6)

    if "drh1_tot_ecole" in value:
        graphs["drh1_tot_ecole"] = fig_hist_total("DRH-01", selected_years, 11)
    if "drh2_tot_ecole" in value:
        graphs["drh2_tot_ecole"] = fig_hist_total("DRH-02", selected_years, 11)
    if "drh3_bat_ecole" in value:
        graphs["drh3_bat_ecole"] = fig_hist_trim_baton("DRH-03", selected_years, 6)
    if "drh3_cou_ecole" in value:
        graphs["drh3_cou_ecole"] = fig_hist_trim_courbe("DRH-03", selected_years, 6)
    if "drh3_tot_ecole" in value:
        graphs["drh3_tot_ecole"] = fig_hist_total("DRH-03", selected_years, 6)
    if "drh4_tot_ecole" in value:
        graphs["drh4_tot_ecole"] = fig_hist_total("DRH-04", selected_years, 11)
    if "drh5_tot_ecole" in value:
        graphs["drh5_tot_ecole"] = fig_hist_total("DRH-05", selected_years, 11)
    if "drh6_tot_ecole" in value:
        graphs["drh6_tot_ecole"] = fig_hist_total("DRH-06", selected_years, 11)

    if "dri1_tot" in value:
        graphs["dri1_tot"] = fig_hist_total("DRI-01", selected_years, 0)
    if "dri2_tot" in value:
        graphs["dri2_tot"] = fig_hist_total("DRI-02", selected_years, 0)
    if "dri3_tot" in value:
        graphs["dri3_tot"] = fig_hist_total("DRI-03", selected_years, 0)
    if "dri4_tot" in value:
        graphs["dri4_tot"] = fig_hist_total("DRI-04", selected_years, 0)
    if "dri5_tot" in value:
        graphs["dri5_tot"] = fig_hist_total("DRI-05", selected_years, 0)
    if "dri6_tot" in value:
        graphs["dri6_tot"] = fig_hist_total("DRI-06", selected_years, 0)

    if "radar_ecole" in value:
        graphs["radar_ecole"] = fig_hist_radar(selected_years, 6)

    #ARTEMIS
    if "df1_tot_artemis" in value:
        graphs["df1_tot_artemis"] = fig_hist_total("DF-01", selected_years, 0)
    if "drfd1_tot_artemis" in value:
        graphs["drfd1_tot_artemis"] = fig_hist_total("DRFD-01", selected_years, 0)
    if "drfd2_tot_artemis" in value:
        graphs["drfd2_tot_artemis"] = fig_hist_total("DRFD-02", selected_years, 0)
    if "drfd3_tot_artemis" in value:
        graphs["drfd3_tot_artemis"] = fig_hist_total("DRFD-03", selected_years, 0)

    if "dire1_bat_artemis" in value:
        graphs["dire1_bat_artemis"] = fig_hist_trim_baton("DIRE-01", selected_years, 0)
    if "dire1_cou_artemis" in value:
        graphs["dire1_cou_artemis"] = fig_hist_trim_courbe("DIRE-01", selected_years, 0)
    if "dire1_tot_artemis" in value:
        graphs["dire1_tot_artemis"] = fig_hist_total("DIRE-01", selected_years, 0)
    if "dire2_bat_artemis" in value:
        graphs["dire2_bat_artemis"] = fig_hist_trim_baton("DIRE-02", selected_years, 0)
    if "dire2_cou_artemis" in value:
        graphs["dire2_cou_artemis"] = fig_hist_trim_courbe("DIRE-02", selected_years, 0)
    if "dire2_tot_artemis" in value:
        graphs["dire2_tot_artemis"] = fig_hist_total("DIRE-02", selected_years, 0)
    if "dire3_bat_artemis" in value:
        graphs["dire3_bat_artemis"] = fig_hist_trim_baton("DIRE-03", selected_years, 0)
    if "dire3_cou_artemis" in value:
        graphs["dire3_cou_artemis"] = fig_hist_trim_courbe("DIRE-03", selected_years, 0)
    if "dire3_tot_artemis" in value:
        graphs["dire3_tot_artemis"] = fig_hist_total("DIRE-03", selected_years, 0)

    if "daf1_bat_artemis" in value:
        graphs["daf1_bat_artemis"] = fig_hist_trim_baton("DAF-01", selected_years, 0)
    if "daf1_cou_artemis" in value:
        graphs["daf1_cou_artemis"] = fig_hist_trim_courbe("DAF-01", selected_years, 0)
    if "daf1_tot_artemis" in value:
        graphs["daf1_tot_artemis"] = fig_hist_total("DAF-01", selected_years, 0)
    if "daf2_bat_artemis" in value:
        graphs["daf2_bat_artemis"] = fig_hist_trim_baton("DAF-02", selected_years, 0)
    if "daf2_cou_artemis" in value:
        graphs["daf2_cou_artemis"] = fig_hist_trim_courbe("DAF-02", selected_years, 0)
    if "daf2_tot_artemis" in value:
        graphs["daf2_tot_artemis"] = fig_hist_total("DAF-02", selected_years, 0)
    if "daf3_bat_artemis" in value:
        graphs["daf3_bat_artemis"] = fig_hist_trim_baton("DAF-03", selected_years, 0)
    if "daf3_cou_artemis" in value:
        graphs["daf3_cou_artemis"] = fig_hist_trim_courbe("DAF-03", selected_years, 0)
    if "daf3_tot_artemis" in value:
        graphs["daf3_tot_artemis"] = fig_hist_total("DAF-03", selected_years, 0)
    if "daf4_bat_artemis" in value:
        graphs["daf4_bat_artemis"] = fig_hist_trim_baton("DAF-04", selected_years, 0)
    if "daf4_cou_artemis" in value:
        graphs["daf4_cou_artemis"] = fig_hist_trim_courbe("DAF-04", selected_years, 0)
    if "daf4_tot_artemis" in value:
        graphs["daf4_tot_artemis"] = fig_hist_total("DAF-04", selected_years, 0)
    if "daf5_bat_artemis" in value:
        graphs["daf5_bat_artemis"] = fig_hist_trim_baton("DAF-05", selected_years, 0)
    if "daf5_cou_artemis" in value:
        graphs["daf5_cou_artemis"] = fig_hist_trim_courbe("DAF-05", selected_years, 0)
    if "daf5_tot_artemis" in value:
        graphs["daf5_tot_artemis"] = fig_hist_total("DAF-05", selected_years, 0)
    if "daf6_tot_artemis" in value:
        graphs["daf6_tot_artemis"] = fig_hist_total("DAF-06", selected_years, 0)

    if "drh1_tot_artemis" in value:
        graphs["drh1_tot_artemis"] = fig_hist_total("DRH-01", selected_years, 5)
    if "drh2_tot_artemis" in value:
        graphs["drh2_tot_artemis"] = fig_hist_total("DRH-02", selected_years, 5)
    if "drh3_bat_artemis" in value:
        graphs["drh3_bat_artemis"] = fig_hist_trim_baton("DRH-03", selected_years, 0)
    if "drh3_cou_artemis" in value:
        graphs["drh3_cou_artemis"] = fig_hist_trim_courbe("DRH-03", selected_years, 0)
    if "drh3_tot_artemis" in value:
        graphs["drh3_tot_artemis"] = fig_hist_total("DRH-03", selected_years, 0)
    if "drh4_tot_artemis" in value:
        graphs["drh4_tot_artemis"] = fig_hist_total("DRH-04", selected_years, 5)
    if "drh5_tot_artemis" in value:
        graphs["drh5_tot_artemis"] = fig_hist_total("DRH-05", selected_years, 5)
    if "drh6_tot_artemis" in value:
        graphs["drh6_tot_artemis"] = fig_hist_total("DRH-06", selected_years, 5)

    if "radar_artemis" in value:
        graphs["radar_artemis"] = fig_hist_radar(selected_years, 0)

    #CITI
    if "df1_tot_citi" in value:
        graphs["df1_tot_citi"] = fig_hist_total("DF-01", selected_years, 1)
    if "drfd1_tot_citi" in value:
        graphs["drfd1_tot_citi"] = fig_hist_total("DRFD-01", selected_years, 1)
    if "drfd2_tot_citi" in value:
        graphs["drfd2_tot_citi"] = fig_hist_total("DRFD-02", selected_years, 1)
    if "drfd3_tot_citi" in value:
        graphs["drfd3_tot_citi"] = fig_hist_total("DRFD-03", selected_years, 1)

    if "dire1_bat_citi" in value:
        graphs["dire1_bat_citi"] = fig_hist_trim_baton("DIRE-01", selected_years, 1)
    if "dire1_cou_citi" in value:
        graphs["dire1_cou_citi"] = fig_hist_trim_courbe("DIRE-01", selected_years, 1)
    if "dire1_tot_citi" in value:
        graphs["dire1_tot_citi"] = fig_hist_total("DIRE-01", selected_years, 1)
    if "dire2_bat_citi" in value:
        graphs["dire2_bat_citi"] = fig_hist_trim_baton("DIRE-02", selected_years, 1)
    if "dire2_cou_citi" in value:
        graphs["dire2_cou_citi"] = fig_hist_trim_courbe("DIRE-02", selected_years, 1)
    if "dire2_tot_citi" in value:
        graphs["dire2_tot_citi"] = fig_hist_total("DIRE-02", selected_years, 1)
    if "dire3_bat_citi" in value:
        graphs["dire3_bat_citi"] = fig_hist_trim_baton("DIRE-03", selected_years, 1)
    if "dire3_cou_citi" in value:
        graphs["dire3_cou_citi"] = fig_hist_trim_courbe("DIRE-03", selected_years, 1)
    if "dire3_tot_citi" in value:
        graphs["dire3_tot_citi"] = fig_hist_total("DIRE-03", selected_years, 1)

    if "daf1_bat_citi" in value:
        graphs["daf1_bat_citi"] = fig_hist_trim_baton("DAF-01", selected_years, 1)
    if "daf1_cou_citi" in value:
        graphs["daf1_cou_citi"] = fig_hist_trim_courbe("DAF-01", selected_years, 1)
    if "daf1_tot_citi" in value:
        graphs["daf1_tot_citi"] = fig_hist_total("DAF-01", selected_years, 1)
    if "daf2_bat_citi" in value:
        graphs["daf2_bat_citi"] = fig_hist_trim_baton("DAF-02", selected_years, 1)
    if "daf2_cou_citi" in value:
        graphs["daf2_cou_citi"] = fig_hist_trim_courbe("DAF-02", selected_years, 1)
    if "daf2_tot_citi" in value:
        graphs["daf2_tot_citi"] = fig_hist_total("DAF-02", selected_years, 1)
    if "daf3_bat_citi" in value:
        graphs["daf3_bat_citi"] = fig_hist_trim_baton("DAF-03", selected_years, 1)
    if "daf3_cou_citi" in value:
        graphs["daf3_cou_citi"] = fig_hist_trim_courbe("DAF-03", selected_years, 1)
    if "daf3_tot_citi" in value:
        graphs["daf3_tot_citi"] = fig_hist_total("DAF-03", selected_years, 1)
    if "daf4_bat_citi" in value:
        graphs["daf4_bat_citi"] = fig_hist_trim_baton("DAF-04", selected_years, 1)
    if "daf4_cou_citi" in value:
        graphs["daf4_cou_citi"] = fig_hist_trim_courbe("DAF-04", selected_years, 1)
    if "daf4_tot_citi" in value:
        graphs["daf4_tot_citi"] = fig_hist_total("DAF-04", selected_years, 1)
    if "daf5_bat_citi" in value:
        graphs["daf5_bat_citi"] = fig_hist_trim_baton("DAF-05", selected_years, 1)
    if "daf5_cou_citi" in value:
        graphs["daf5_cou_citi"] = fig_hist_trim_courbe("DAF-05", selected_years, 1)
    if "daf5_tot_citi" in value:
        graphs["daf5_tot_citi"] = fig_hist_total("DAF-05", selected_years, 1)
    if "daf6_tot_citi" in value:
        graphs["daf6_tot_citi"] = fig_hist_total("DAF-06", selected_years, 1)

    if "drh1_tot_citi" in value:
        graphs["drh1_tot_citi"] = fig_hist_total("DRH-01", selected_years, 6)
    if "drh2_tot_citi" in value:
        graphs["drh2_tot_citi"] = fig_hist_total("DRH-02", selected_years, 6)
    if "drh3_bat_citi" in value:
        graphs["drh3_bat_citi"] = fig_hist_trim_baton("DRH-03", selected_years, 1)
    if "drh3_cou_citi" in value:
        graphs["drh3_cou_citi"] = fig_hist_trim_courbe("DRH-03", selected_years, 1)
    if "drh3_tot_citi" in value:
        graphs["drh3_tot_citi"] = fig_hist_total("DRH-03", selected_years, 1)
    if "drh4_tot_citi" in value:
        graphs["drh4_tot_citi"] = fig_hist_total("DRH-04", selected_years, 6)
    if "drh5_tot_citi" in value:
        graphs["drh5_tot_citi"] = fig_hist_total("DRH-05", selected_years, 6)
    if "drh6_tot_citi" in value:
        graphs["drh6_tot_citi"] = fig_hist_total("DRH-06", selected_years, 6)

    if "radar_citi" in value:
        graphs["radar_citi"] = fig_hist_radar(selected_years, 1)

    #EPH
    if "df1_tot_eph" in value:
        graphs["df1_tot_eph"] = fig_hist_total("DF-01", selected_years, 2)
    if "drfd1_tot_eph" in value:
        graphs["drfd1_tot_eph"] = fig_hist_total("DRFD-01", selected_years, 2)
    if "drfd2_tot_eph" in value:
        graphs["drfd2_tot_eph"] = fig_hist_total("DRFD-02", selected_years, 2)
    if "drfd3_tot_eph" in value:
        graphs["drfd3_tot_eph"] = fig_hist_total("DRFD-03", selected_years, 2)

    if "dire1_bat_eph" in value:
        graphs["dire1_bat_eph"] = fig_hist_trim_baton("DIRE-01", selected_years, 2)
    if "dire1_cou_eph" in value:
        graphs["dire1_cou_eph"] = fig_hist_trim_courbe("DIRE-01", selected_years, 2)
    if "dire1_tot_eph" in value:
        graphs["dire1_tot_eph"] = fig_hist_total("DIRE-01", selected_years, 2)
    if "dire2_bat_eph" in value:
        graphs["dire2_bat_eph"] = fig_hist_trim_baton("DIRE-02", selected_years, 2)
    if "dire2_cou_eph" in value:
        graphs["dire2_cou_eph"] = fig_hist_trim_courbe("DIRE-02", selected_years, 2)
    if "dire2_tot_eph" in value:
        graphs["dire2_tot_eph"] = fig_hist_total("DIRE-02", selected_years, 2)
    if "dire3_bat_eph" in value:
        graphs["dire3_bat_eph"] = fig_hist_trim_baton("DIRE-03", selected_years, 2)
    if "dire3_cou_eph" in value:
        graphs["dire3_cou_eph"] = fig_hist_trim_courbe("DIRE-03", selected_years, 2)
    if "dire3_tot_eph" in value:
        graphs["dire3_tot_eph"] = fig_hist_total("DIRE-03", selected_years, 2)

    if "daf1_bat_eph" in value:
        graphs["daf1_bat_eph"] = fig_hist_trim_baton("DAF-01", selected_years, 2)
    if "daf1_cou_eph" in value:
        graphs["daf1_cou_eph"] = fig_hist_trim_courbe("DAF-01", selected_years, 2)
    if "daf1_tot_eph" in value:
        graphs["daf1_tot_eph"] = fig_hist_total("DAF-01", selected_years, 2)
    if "daf2_bat_eph" in value:
        graphs["daf2_bat_eph"] = fig_hist_trim_baton("DAF-02", selected_years, 2)
    if "daf2_cou_eph" in value:
        graphs["daf2_cou_eph"] = fig_hist_trim_courbe("DAF-02", selected_years, 2)
    if "daf2_tot_eph" in value:
        graphs["daf2_tot_eph"] = fig_hist_total("DAF-02", selected_years, 2)
    if "daf3_bat_eph" in value:
        graphs["daf3_bat_eph"] = fig_hist_trim_baton("DAF-03", selected_years, 2)
    if "daf3_cou_eph" in value:
        graphs["daf3_cou_eph"] = fig_hist_trim_courbe("DAF-03", selected_years, 2)
    if "daf3_tot_eph" in value:
        graphs["daf3_tot_eph"] = fig_hist_total("DAF-03", selected_years, 2)
    if "daf4_bat_eph" in value:
        graphs["daf4_bat_eph"] = fig_hist_trim_baton("DAF-04", selected_years, 2)
    if "daf4_cou_eph" in value:
        graphs["daf4_cou_eph"] = fig_hist_trim_courbe("DAF-04", selected_years, 2)
    if "daf4_tot_eph" in value:
        graphs["daf4_tot_eph"] = fig_hist_total("DAF-04", selected_years, 2)
    if "daf5_bat_eph" in value:
        graphs["daf5_bat_eph"] = fig_hist_trim_baton("DAF-05", selected_years, 2)
    if "daf5_cou_eph" in value:
        graphs["daf5_cou_eph"] = fig_hist_trim_courbe("DAF-05", selected_years, 2)
    if "daf5_tot_eph" in value:
        graphs["daf5_tot_eph"] = fig_hist_total("DAF-05", selected_years, 2)
    if "daf6_tot_eph" in value:
        graphs["daf6_tot_eph"] = fig_hist_total("DAF-06", selected_years, 2)

    if "drh1_tot_eph" in value:
        graphs["drh1_tot_eph"] = fig_hist_total("DRH-01", selected_years, 7)
    if "drh2_tot_eph" in value:
        graphs["drh2_tot_eph"] = fig_hist_total("DRH-02", selected_years, 7)
    if "drh3_bat_eph" in value:
        graphs["drh3_bat_eph"] = fig_hist_trim_baton("DRH-03", selected_years, 2)
    if "drh3_cou_eph" in value:
        graphs["drh3_cou_eph"] = fig_hist_trim_courbe("DRH-03", selected_years, 2)
    if "drh3_tot_eph" in value:
        graphs["drh3_tot_eph"] = fig_hist_total("DRH-03", selected_years, 2)
    if "drh4_tot_eph" in value:
        graphs["drh4_tot_eph"] = fig_hist_total("DRH-04", selected_years, 7)
    if "drh5_tot_eph" in value:
        graphs["drh5_tot_eph"] = fig_hist_total("DRH-05", selected_years, 7)
    if "drh6_tot_eph" in value:
        graphs["drh6_tot_eph"] = fig_hist_total("DRH-06", selected_years, 7)

    if "radar_eph" in value:
        graphs["radar_eph"] = fig_hist_radar(selected_years, 2)

    #INF
    if "df1_tot_inf" in value:
        graphs["df1_tot_inf"] = fig_hist_total("DF-01", selected_years, 3)
    if "drfd1_tot_inf" in value:
        graphs["drfd1_tot_inf"] = fig_hist_total("DRFD-01", selected_years, 3)
    if "drfd2_tot_inf" in value:
        graphs["drfd2_tot_inf"] = fig_hist_total("DRFD-02", selected_years, 3)
    if "drfd3_tot_inf" in value:
        graphs["drfd3_tot_inf"] = fig_hist_total("DRFD-03", selected_years, 3)

    if "dire1_bat_inf" in value:
        graphs["dire1_bat_inf"] = fig_hist_trim_baton("DIRE-01", selected_years, 3)
    if "dire1_cou_inf" in value:
        graphs["dire1_cou_inf"] = fig_hist_trim_courbe("DIRE-01", selected_years, 3)
    if "dire1_tot_inf" in value:
        graphs["dire1_tot_inf"] = fig_hist_total("DIRE-01", selected_years, 3)
    if "dire2_bat_inf" in value:
        graphs["dire2_bat_inf"] = fig_hist_trim_baton("DIRE-02", selected_years, 3)
    if "dire2_cou_inf" in value:
        graphs["dire2_cou_inf"] = fig_hist_trim_courbe("DIRE-02", selected_years, 3)
    if "dire2_tot_inf" in value:
        graphs["dire2_tot_inf"] = fig_hist_total("DIRE-02", selected_years, 3)
    if "dire3_bat_inf" in value:
        graphs["dire3_bat_inf"] = fig_hist_trim_baton("DIRE-03", selected_years, 3)
    if "dire3_cou_inf" in value:
        graphs["dire3_cou_inf"] = fig_hist_trim_courbe("DIRE-03", selected_years, 3)
    if "dire3_tot_inf" in value:
        graphs["dire3_tot_inf"] = fig_hist_total("DIRE-03", selected_years, 3)

    if "daf1_bat_inf" in value:
        graphs["daf1_bat_inf"] = fig_hist_trim_baton("DAF-01", selected_years, 3)
    if "daf1_cou_inf" in value:
        graphs["daf1_cou_inf"] = fig_hist_trim_courbe("DAF-01", selected_years, 3)
    if "daf1_tot_inf" in value:
        graphs["daf1_tot_inf"] = fig_hist_total("DAF-01", selected_years, 3)
    if "daf2_bat_inf" in value:
        graphs["daf2_bat_inf"] = fig_hist_trim_baton("DAF-02", selected_years, 3)
    if "daf2_cou_inf" in value:
        graphs["daf2_cou_inf"] = fig_hist_trim_courbe("DAF-02", selected_years, 3)
    if "daf2_tot_inf" in value:
        graphs["daf2_tot_inf"] = fig_hist_total("DAF-02", selected_years, 3)
    if "daf3_bat_inf" in value:
        graphs["daf3_bat_inf"] = fig_hist_trim_baton("DAF-03", selected_years, 3)
    if "daf3_cou_inf" in value:
        graphs["daf3_cou_inf"] = fig_hist_trim_courbe("DAF-03", selected_years, 3)
    if "daf3_tot_inf" in value:
        graphs["daf3_tot_inf"] = fig_hist_total("DAF-03", selected_years, 3)
    if "daf4_bat_inf" in value:
        graphs["daf4_bat_inf"] = fig_hist_trim_baton("DAF-04", selected_years, 3)
    if "daf4_cou_inf" in value:
        graphs["daf4_cou_inf"] = fig_hist_trim_courbe("DAF-04", selected_years, 3)
    if "daf4_tot_inf" in value:
        graphs["daf4_tot_inf"] = fig_hist_total("DAF-04", selected_years, 3)
    if "daf5_bat_inf" in value:
        graphs["daf5_bat_inf"] = fig_hist_trim_baton("DAF-05", selected_years, 3)
    if "daf5_cou_inf" in value:
        graphs["daf5_cou_inf"] = fig_hist_trim_courbe("DAF-05", selected_years, 3)
    if "daf5_tot_inf" in value:
        graphs["daf5_tot_inf"] = fig_hist_total("DAF-05", selected_years, 3)
    if "daf6_tot_inf" in value:
        graphs["daf6_tot_inf"] = fig_hist_total("DAF-06", selected_years, 3)

    if "drh1_tot_inf" in value:
        graphs["drh1_tot_inf"] = fig_hist_total("DRH-01", selected_years, 8)
    if "drh2_tot_inf" in value:
        graphs["drh2_tot_inf"] = fig_hist_total("DRH-02", selected_years, 8)
    if "drh3_bat_inf" in value:
        graphs["drh3_bat_inf"] = fig_hist_trim_baton("DRH-03", selected_years, 3)
    if "drh3_cou_inf" in value:
        graphs["drh3_cou_inf"] = fig_hist_trim_courbe("DRH-03", selected_years, 3)
    if "drh3_tot_inf" in value:
        graphs["drh3_tot_inf"] = fig_hist_total("DRH-03", selected_years, 3)
    if "drh4_tot_inf" in value:
        graphs["drh4_tot_inf"] = fig_hist_total("DRH-04", selected_years, 8)
    if "drh5_tot_inf" in value:
        graphs["drh5_tot_inf"] = fig_hist_total("DRH-05", selected_years, 8)
    if "drh6_tot_inf" in value:
        graphs["drh6_tot_inf"] = fig_hist_total("DRH-06", selected_years, 8)

    if "radar_inf" in value:
        graphs["radar_inf"] = fig_hist_radar(selected_years, 3)

    #RS2M
    if "df1_tot_rs2m" in value:
        graphs["df1_tot_rs2m"] = fig_hist_total("DF-01", selected_years, 4)
    if "drfd1_tot_rs2m" in value:
        graphs["drfd1_tot_rs2m"] = fig_hist_total("DRFD-01", selected_years, 4)
    if "drfd2_tot_rs2m" in value:
        graphs["drfd2_tot_rs2m"] = fig_hist_total("DRFD-02", selected_years, 4)
    if "drfd3_tot_rs2m" in value:
        graphs["drfd3_tot_rs2m"] = fig_hist_total("DRFD-03", selected_years, 4)

    if "dire1_bat_rs2m" in value:
        graphs["dire1_bat_rs2m"] = fig_hist_trim_baton("DIRE-01", selected_years, 4)
    if "dire1_cou_rs2m" in value:
        graphs["dire1_cou_rs2m"] = fig_hist_trim_courbe("DIRE-01", selected_years, 4)
    if "dire1_tot_rs2m" in value:
        graphs["dire1_tot_rs2m"] = fig_hist_total("DIRE-01", selected_years, 4)
    if "dire2_bat_rs2m" in value:
        graphs["dire2_bat_rs2m"] = fig_hist_trim_baton("DIRE-02", selected_years, 4)
    if "dire2_cou_rs2m" in value:
        graphs["dire2_cou_rs2m"] = fig_hist_trim_courbe("DIRE-02", selected_years, 4)
    if "dire2_tot_rs2m" in value:
        graphs["dire2_tot_rs2m"] = fig_hist_total("DIRE-02", selected_years, 4)
    if "dire3_bat_rs2m" in value:
        graphs["dire3_bat_rs2m"] = fig_hist_trim_baton("DIRE-03", selected_years, 4)
    if "dire3_cou_rs2m" in value:
        graphs["dire3_cou_rs2m"] = fig_hist_trim_courbe("DIRE-03", selected_years, 4)
    if "dire3_tot_rs2m" in value:
        graphs["dire3_tot_rs2m"] = fig_hist_total("DIRE-03", selected_years, 4)

    if "daf1_bat_rs2m" in value:
        graphs["daf1_bat_rs2m"] = fig_hist_trim_baton("DAF-01", selected_years, 4)
    if "daf1_cou_rs2m" in value:
        graphs["daf1_cou_rs2m"] = fig_hist_trim_courbe("DAF-01", selected_years, 4)
    if "daf1_tot_rs2m" in value:
        graphs["daf1_tot_rs2m"] = fig_hist_total("DAF-01", selected_years, 4)
    if "daf2_bat_rs2m" in value:
        graphs["daf2_bat_rs2m"] = fig_hist_trim_baton("DAF-02", selected_years, 4)
    if "daf2_cou_rs2m" in value:
        graphs["daf2_cou_rs2m"] = fig_hist_trim_courbe("DAF-02", selected_years, 4)
    if "daf2_tot_rs2m" in value:
        graphs["daf2_tot_rs2m"] = fig_hist_total("DAF-02", selected_years, 4)
    if "daf3_bat_rs2m" in value:
        graphs["daf3_bat_rs2m"] = fig_hist_trim_baton("DAF-03", selected_years, 4)
    if "daf3_cou_rs2m" in value:
        graphs["daf3_cou_rs2m"] = fig_hist_trim_courbe("DAF-03", selected_years, 4)
    if "daf3_tot_rs2m" in value:
        graphs["daf3_tot_rs2m"] = fig_hist_total("DAF-03", selected_years, 4)
    if "daf4_bat_rs2m" in value:
        graphs["daf4_bat_rs2m"] = fig_hist_trim_baton("DAF-04", selected_years, 4)
    if "daf4_cou_rs2m" in value:
        graphs["daf4_cou_rs2m"] = fig_hist_trim_courbe("DAF-04", selected_years, 4)
    if "daf4_tot_rs2m" in value:
        graphs["daf4_tot_rs2m"] = fig_hist_total("DAF-04", selected_years, 4)
    if "daf5_bat_rs2m" in value:
        graphs["daf5_bat_rs2m"] = fig_hist_trim_baton("DAF-05", selected_years, 4)
    if "daf5_cou_rs2m" in value:
        graphs["daf5_cou_rs2m"] = fig_hist_trim_courbe("DAF-05", selected_years, 4)
    if "daf5_tot_rs2m" in value:
        graphs["daf5_tot_rs2m"] = fig_hist_total("DAF-05", selected_years, 4)
    if "daf6_tot_rs2m" in value:
        graphs["daf6_tot_rs2m"] = fig_hist_total("DAF-06", selected_years, 4)

    if "drh1_tot_rs2m" in value:
        graphs["drh1_tot_rs2m"] = fig_hist_total("DRH-01", selected_years, 9)
    if "drh2_tot_rs2m" in value:
        graphs["drh2_tot_rs2m"] = fig_hist_total("DRH-02", selected_years, 9)
    if "drh3_bat_rs2m" in value:
        graphs["drh3_bat_rs2m"] = fig_hist_trim_baton("DRH-03", selected_years, 4)
    if "drh3_cou_rs2m" in value:
        graphs["drh3_cou_rs2m"] = fig_hist_trim_courbe("DRH-03", selected_years, 4)
    if "drh3_tot_rs2m" in value:
        graphs["drh3_tot_rs2m"] = fig_hist_total("DRH-03", selected_years, 4)
    if "drh4_tot_rs2m" in value:
        graphs["drh4_tot_rs2m"] = fig_hist_total("DRH-04", selected_years, 9)
    if "drh5_tot_rs2m" in value:
        graphs["drh5_tot_rs2m"] = fig_hist_total("DRH-05", selected_years, 9)
    if "drh6_tot_rs2m" in value:
        graphs["drh6_tot_rs2m"] = fig_hist_total("DRH-06", selected_years, 9)

    if "radar_rs2m" in value:
        graphs["radar_rs2m"] = fig_hist_radar(selected_years, 4)

    #RST
    if "df1_tot_rst" in value:
        graphs["df1_tot_rst"] = fig_hist_total("DF-01", selected_years, 5)
    if "drfd1_tot_rst" in value:
        graphs["drfd1_tot_rst"] = fig_hist_total("DRFD-01", selected_years, 5)
    if "drfd2_tot_rst" in value:
        graphs["drfd2_tot_rst"] = fig_hist_total("DRFD-02", selected_years, 5)
    if "drfd3_tot_rst" in value:
        graphs["drfd3_tot_rst"] = fig_hist_total("DRFD-03", selected_years, 5)
    if "dire1_bat_rst" in value:
        graphs["dire1_bat_rst"] = fig_hist_trim_baton("DIRE-01", selected_years, 5)
    if "dire1_cou_rst" in value:
        graphs["dire1_cou_rst"] = fig_hist_trim_courbe("DIRE-01", selected_years, 5)
    if "dire1_tot_rst" in value:
        graphs["dire1_tot_rst"] = fig_hist_total("DIRE-01", selected_years, 5)
    if "dire2_bat_rst" in value:
        graphs["dire2_bat_rst"] = fig_hist_trim_baton("DIRE-02", selected_years, 5)
    if "dire2_cou_rst" in value:
        graphs["dire2_cou_rst"] = fig_hist_trim_courbe("DIRE-02", selected_years, 5)
    if "dire2_tot_rst" in value:
        graphs["dire2_tot_rst"] = fig_hist_total("DIRE-02", selected_years, 5)
    if "dire3_bat_rst" in value:
        graphs["dire3_bat_rst"] = fig_hist_trim_baton("DIRE-03", selected_years, 5)
    if "dire3_cou_rst" in value:
        graphs["dire3_cou_rst"] = fig_hist_trim_courbe("DIRE-03", selected_years, 5)
    if "dire3_tot_rst" in value:
        graphs["dire3_tot_rst"] = fig_hist_total("DIRE-03", selected_years, 5)
    if "daf1_bat_rst" in value:
        graphs["daf1_bat_rst"] = fig_hist_trim_baton("DAF-01", selected_years, 5)
    if "daf1_cou_rst" in value:
        graphs["daf1_cou_rst"] = fig_hist_trim_courbe("DAF-01", selected_years, 5)
    if "daf1_tot_rst" in value:
        graphs["daf1_tot_rst"] = fig_hist_total("DAF-01", selected_years, 5)
    if "daf2_bat_rst" in value:
        graphs["daf2_bat_rst"] = fig_hist_trim_baton("DAF-02", selected_years, 5)
    if "daf2_cou_rst" in value:
        graphs["daf2_cou_rst"] = fig_hist_trim_courbe("DAF-02", selected_years, 5)
    if "daf2_tot_rst" in value:
        graphs["daf2_tot_rst"] = fig_hist_total("DAF-02", selected_years, 5)
    if "daf3_bat_rst" in value:
        graphs["daf3_bat_rst"] = fig_hist_trim_baton("DAF-03", selected_years, 5)
    if "daf3_cou_rst" in value:
        graphs["daf3_cou_rst"] = fig_hist_trim_courbe("DAF-03", selected_years, 5)
    if "daf3_tot_rst" in value:
        graphs["daf3_tot_rst"] = fig_hist_total("DAF-03", selected_years, 5)
    if "daf4_bat_rst" in value:
        graphs["daf4_bat_rst"] = fig_hist_trim_baton("DAF-04", selected_years, 5)
    if "daf4_cou_rst" in value:
        graphs["daf4_cou_rst"] = fig_hist_trim_courbe("DAF-04", selected_years, 5)
    if "daf4_tot_rst" in value:
        graphs["daf4_tot_rst"] = fig_hist_total("DAF-04", selected_years, 5)
    if "daf5_bat_rst" in value:
        graphs["daf5_bat_rst"] = fig_hist_trim_baton("DAF-05", selected_years, 5)
    if "daf5_cou_rst" in value:
        graphs["daf5_cou_rst"] = fig_hist_trim_courbe("DAF-05", selected_years, 5)
    if "daf5_tot_rst" in value:
        graphs["daf5_tot_rst"] = fig_hist_total("DAF-05", selected_years, 5)
    if "daf6_tot_rst" in value:
        graphs["daf6_tot_rst"] = fig_hist_total("DAF-06", selected_years, 5)
    if "drh1_tot_rst" in value:
        graphs["drh1_tot_rst"] = fig_hist_total("DRH-01", selected_years, 10)
    if "drh2_tot_rst" in value:
        graphs["drh2_tot_rst"] = fig_hist_total("DRH-02", selected_years, 10)
    if "drh3_bat_rst" in value:
        graphs["drh3_bat_rst"] = fig_hist_trim_baton("DRH-03", selected_years, 5)
    if "drh3_cou_rst" in value:
        graphs["drh3_cou_rst"] = fig_hist_trim_courbe("DRH-03", selected_years, 5)
    if "drh3_tot_rst" in value:
        graphs["drh3_tot_rst"] = fig_hist_total("DRH-03", selected_years, 5)
    if "drh4_tot_rst" in value:
        graphs["drh4_tot_rst"] = fig_hist_total("DRH-04", selected_years, 10)
    if "drh5_tot_rst" in value:
        graphs["drh5_tot_rst"] = fig_hist_total("DRH-05", selected_years, 10)
    if "drh6_tot_rst" in value:
        graphs["drh6_tot_rst"] = fig_hist_total("DRH-06", selected_years, 10)
    if "radar_rst" in value:
        graphs["radar_rst"] = fig_hist_radar(selected_years, 5)

    #Autres
    #DF
    if "drh1_tot_df" in value:
        graphs["drh1_tot_df"] = fig_hist_total("DRH-01", selected_years, 0)
    if "drh2_tot_df" in value:
        graphs["drh2_tot_df"] = fig_hist_total("DRH-02", selected_years, 0)
    if "drh4_tot_df" in value:
        graphs["drh4_tot_df"] = fig_hist_total("DRH-04", selected_years, 0)
    if "drh5_tot_df" in value:
        graphs["drh5_tot_df"] = fig_hist_total("DRH-05", selected_years, 0)
    if "drh6_tot_df" in value:
        graphs["drh6_tot_df"] = fig_hist_total("DRH-06", selected_years, 0)
    #DRFD
    if "drh1_tot_drfd" in value:
        graphs["drh1_tot_drfd"] = fig_hist_total("DRH-01", selected_years, 1)
    if "drh2_tot_drfd" in value:
        graphs["drh2_tot_drfd"] = fig_hist_total("DRH-02", selected_years, 1)
    if "drh4_tot_drfd" in value:
        graphs["drh4_tot_drfd"] = fig_hist_total("DRH-04", selected_years, 1)
    if "drh5_tot_drfd" in value:
        graphs["drh5_tot_drfd"] = fig_hist_total("DRH-05", selected_years, 1)
    if "drh6_tot_drfd" in value:
        graphs["drh6_tot_drfd"] = fig_hist_total("DRH-06", selected_years, 1)
    #DIRE
    if "drh1_tot_dire" in value:
        graphs["drh1_tot_dire"] = fig_hist_total("DRH-01", selected_years, 2)
    if "drh2_tot_dire" in value:
        graphs["drh2_tot_dire"] = fig_hist_total("DRH-02", selected_years, 2)
    if "drh4_tot_dire" in value:
        graphs["drh4_tot_dire"] = fig_hist_total("DRH-04", selected_years, 2)
    if "drh5_tot_dire" in value:
        graphs["drh5_tot_dire"] = fig_hist_total("DRH-05", selected_years, 2)
    if "drh6_tot_dire" in value:
        graphs["drh6_tot_dire"] = fig_hist_total("DRH-06", selected_years, 2)
    #DRI
    if "drh1_tot_dri" in value:
        graphs["drh1_tot_dri"] = fig_hist_total("DRH-01", selected_years, 3)
    if "drh2_tot_dri" in value:
        graphs["drh2_tot_dri"] = fig_hist_total("DRH-02", selected_years, 3)
    if "drh4_tot_dri" in value:
        graphs["drh4_tot_dri"] = fig_hist_total("DRH-04", selected_years, 3)
    if "drh5_tot_dri" in value:
        graphs["drh5_tot_dri"] = fig_hist_total("DRH-05", selected_years, 3)
    if "drh6_tot_dri" in value:
        graphs["drh6_tot_dri"] = fig_hist_total("DRH-06", selected_years, 3)
    #DCOM
    if "drh1_tot_dcom" in value:
        graphs["drh1_tot_dcom"] = fig_hist_total("DRH-01", selected_years, 4)
    if "drh2_tot_dcom" in value:
        graphs["drh2_tot_dcom"] = fig_hist_total("DRH-02", selected_years, 4)
    if "drh4_tot_dcom" in value:
        graphs["drh4_tot_dcom"] = fig_hist_total("DRH-04", selected_years, 4)
    if "drh5_tot_dcom" in value:
        graphs["drh5_tot_dcom"] = fig_hist_total("DRH-05", selected_years, 4)
    if "drh6_tot_dcom" in value:
        graphs["drh6_tot_dcom"] = fig_hist_total("DRH-06", selected_years, 4)



    if value is None:
        value = []
    # Création de la liste des IDs de collapse ouverts
    open_collapse_ids = ["collapse-df{}".format(val) for val in value]

    """
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
    """
    # Filtrer les graphiques sélectionnés
    selected_graphs = [graph_id for graph_id in value]

    # Générer uniquement les graphiques sélectionnés
    graph_output = [dcc.Graph(figure=graphs[graph_id], config={'displaylogo': False}) for graph_id in selected_graphs]


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

"""  graphs = {
        # Ecole
        "df1_tot_ecole": fig_hist_total("DF-01", selected_years, 6),
        "df2_tot": fig_hist_total("DF-02", selected_years, 0),
        "df3_tot": fig_hist_total("DF-03", selected_years, 0),
        "df4_tot": fig_hist_total("DF-04", selected_years, 0),
        "df5_tot": fig_hist_total("DF-05", selected_years, 0),
        "df6_tot": fig_hist_total("DF-06", selected_years, 0),

        "drfd1_tot_ecole": fig_hist_total("DRFD-01", selected_years, 6),
        "drfd2_tot_ecole": fig_hist_total("DRFD-02", selected_years, 6),
        "drfd3_tot_ecole": fig_hist_total("DRFD-03", selected_years, 6),

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

        "drh1_tot_ecole": fig_hist_total("DRH-01", selected_years, 11),
        "drh2_tot_ecole": fig_hist_total("DRH-02", selected_years, 11),
        "drh3_bat_ecole": fig_hist_trim_baton("DRH-03", selected_years, 6),
        "drh3_cou_ecole": fig_hist_trim_courbe("DRH-03", selected_years, 6),
        "drh3_tot_ecole": fig_hist_total("DRH-03", selected_years, 6),
        "drh4_tot_ecole": fig_hist_total("DRH-04", selected_years, 11),
        "drh5_tot_ecole": fig_hist_total("DRH-05", selected_years, 11),
        "drh6_tot_ecole": fig_hist_total("DRH-06", selected_years, 11),

        "dri1_tot": fig_hist_total("DRI-01", selected_years, 0),
        "dri2_tot": fig_hist_total("DRI-02", selected_years, 0),
        "dri3_tot": fig_hist_total("DRI-03", selected_years, 0),
        "dri4_tot": fig_hist_total("DRI-04", selected_years, 0),
        "dri5_tot": fig_hist_total("DRI-05", selected_years, 0),
        "dri6_tot": fig_hist_total("DRI-06", selected_years, 0),

        "radar_ecole": fig_hist_radar(selected_years, 6),


        #ARTEMIS
        "df1_tot_artemis": fig_hist_total("DF-01", selected_years, 0),

        "drfd1_tot_artemis": fig_hist_total("DRFD-01", selected_years, 0),
        "drfd2_tot_artemis": fig_hist_total("DRFD-02", selected_years, 0),
        "drfd3_tot_artemis": fig_hist_total("DRFD-03", selected_years, 0),

        "dire1_bat_artemis": fig_hist_trim_baton("DIRE-01", selected_years, 0),
        "dire1_cou_artemis": fig_hist_trim_courbe("DIRE-01", selected_years, 0),
        "dire1_tot_artemis": fig_hist_total("DIRE-01", selected_years, 0),
        "dire2_bat_artemis": fig_hist_trim_baton("DIRE-02", selected_years, 0),
        "dire2_cou_artemis": fig_hist_trim_courbe("DIRE-02", selected_years, 0),
        "dire2_tot_artemis": fig_hist_total("DIRE-02", selected_years, 0),
        "dire3_bat_artemis": fig_hist_trim_baton("DIRE-03", selected_years, 0),
        "dire3_cou_artemis": fig_hist_trim_courbe("DIRE-03", selected_years, 0),
        "dire3_tot_artemis": fig_hist_total("DIRE-03", selected_years, 0),

        "daf1_bat_artemis": fig_hist_trim_baton("DAF-01", selected_years, 0),
        "daf1_cou_artemis": fig_hist_trim_courbe("DAF-01", selected_years, 0),
        "daf1_tot_artemis": fig_hist_total("DAF-01", selected_years, 0),
        "daf2_bat_artemis": fig_hist_trim_baton("DAF-02", selected_years, 0),
        "daf2_cou_artemis": fig_hist_trim_courbe("DAF-02", selected_years, 0),
        "daf2_tot_artemis": fig_hist_total("DAF-02", selected_years, 0),
        "daf3_bat_artemis": fig_hist_trim_baton("DAF-03", selected_years, 0),
        "daf3_cou_artemis": fig_hist_trim_courbe("DAF-03", selected_years, 0),
        "daf3_tot_artemis": fig_hist_total("DAF-03", selected_years, 0),
        "daf4_bat_artemis": fig_hist_trim_baton("DAF-04", selected_years, 0),
        "daf4_cou_artemis": fig_hist_trim_courbe("DAF-04", selected_years, 0),
        "daf4_tot_artemis": fig_hist_total("DAF-04", selected_years, 0),
        "daf5_bat_artemis": fig_hist_trim_baton("DAF-05", selected_years, 0),
        "daf5_cou_artemis": fig_hist_trim_courbe("DAF-05", selected_years, 0),
        "daf5_tot_artemis": fig_hist_total("DAF-05", selected_years, 0),
        "daf6_tot_artemis": fig_hist_total("DAF-06", selected_years, 0),

        "drh1_tot_artemis": fig_hist_total("DRH-01", selected_years, 5),
        "drh2_tot_artemis": fig_hist_total("DRH-02", selected_years, 5),
        "drh3_bat_artemis": fig_hist_trim_baton("DRH-03", selected_years, 0),
        "drh3_cou_artemis": fig_hist_trim_courbe("DRH-03", selected_years, 0),
        "drh3_tot_artemis": fig_hist_total("DRH-03", selected_years, 0),
        "drh4_tot_artemis": fig_hist_total("DRH-04", selected_years, 5),
        "drh5_tot_artemis": fig_hist_total("DRH-05", selected_years, 5),
        "drh6_tot_artemis": fig_hist_total("DRH-06", selected_years, 5),

        "radar_artemis": fig_hist_radar(selected_years, 0),

        #CITI
        "df1_tot_citi": fig_hist_total("DF-01", selected_years, 1),
        "drfd1_tot_citi": fig_hist_total("DRFD-01", selected_years, 1),
        "drfd2_tot_citi": fig_hist_total("DRFD-02", selected_years, 1),
        "drfd3_tot_citi": fig_hist_total("DRFD-03", selected_years, 1),
        "dire1_bat_citi": fig_hist_trim_baton("DIRE-01", selected_years, 1),
        "dire1_cou_citi": fig_hist_trim_courbe("DIRE-01", selected_years, 1),
        "dire1_tot_citi": fig_hist_total("DIRE-01", selected_years, 1),
        "dire2_bat_citi": fig_hist_trim_baton("DIRE-02", selected_years, 1),
        "dire2_cou_citi": fig_hist_trim_courbe("DIRE-02", selected_years, 1),
        "dire2_tot_citi": fig_hist_total("DIRE-02", selected_years, 1),
        "dire3_bat_citi": fig_hist_trim_baton("DIRE-03", selected_years, 1),
        "dire3_cou_citi": fig_hist_trim_courbe("DIRE-03", selected_years, 1),
        "dire3_tot_citi": fig_hist_total("DIRE-03", selected_years, 1),
        "daf1_bat_citi": fig_hist_trim_baton("DAF-01", selected_years, 1),
        "daf1_cou_citi": fig_hist_trim_courbe("DAF-01", selected_years, 1),
        "daf1_tot_citi": fig_hist_total("DAF-01", selected_years, 1),
        "daf2_bat_citi": fig_hist_trim_baton("DAF-02", selected_years, 1),
        "daf2_cou_citi": fig_hist_trim_courbe("DAF-02", selected_years, 1),
        "daf2_tot_citi": fig_hist_total("DAF-02", selected_years, 1),
        "daf3_bat_citi": fig_hist_trim_baton("DAF-03", selected_years, 1),
        "daf3_cou_citi": fig_hist_trim_courbe("DAF-03", selected_years, 1),
        "daf3_tot_citi": fig_hist_total("DAF-03", selected_years, 1),
        "daf4_bat_citi": fig_hist_trim_baton("DAF-04", selected_years, 1),
        "daf4_cou_citi": fig_hist_trim_courbe("DAF-04", selected_years, 1),
        "daf4_tot_citi": fig_hist_total("DAF-04", selected_years, 1),
        "daf5_bat_citi": fig_hist_trim_baton("DAF-05", selected_years, 1),
        "daf5_cou_citi": fig_hist_trim_courbe("DAF-05", selected_years, 1),
        "daf5_tot_citi": fig_hist_total("DAF-05", selected_years, 1),
        "daf6_tot_citi": fig_hist_total("DAF-06", selected_years, 1),
        "drh1_tot_citi": fig_hist_total("DRH-01", selected_years, 6),
        "drh2_tot_citi": fig_hist_total("DRH-02", selected_years, 6),
        "drh3_bat_citi": fig_hist_trim_baton("DRH-03", selected_years, 1),
        "drh3_cou_citi": fig_hist_trim_courbe("DRH-03", selected_years, 1),
        "drh3_tot_citi": fig_hist_total("DRH-03", selected_years, 1),
        "drh4_tot_citi": fig_hist_total("DRH-04", selected_years, 6),
        "drh5_tot_citi": fig_hist_total("DRH-05", selected_years, 6),
        "drh6_tot_citi": fig_hist_total("DRH-06", selected_years, 6),
        "radar_citi": fig_hist_radar(selected_years, 1),

        #EPH
        "df1_tot_eph": fig_hist_total("DF-01", selected_years, 2),
        "drfd1_tot_eph": fig_hist_total("DRFD-01", selected_years, 2),
        "drfd2_tot_eph": fig_hist_total("DRFD-02", selected_years, 2),
        "drfd3_tot_eph": fig_hist_total("DRFD-03", selected_years, 2),
        "dire1_bat_eph": fig_hist_trim_baton("DIRE-01", selected_years, 2),
        "dire1_cou_eph": fig_hist_trim_courbe("DIRE-01", selected_years, 2),
        "dire1_tot_eph": fig_hist_total("DIRE-01", selected_years, 2),
        "dire2_bat_eph": fig_hist_trim_baton("DIRE-02", selected_years, 2),
        "dire2_cou_eph": fig_hist_trim_courbe("DIRE-02", selected_years, 2),
        "dire2_tot_eph": fig_hist_total("DIRE-02", selected_years, 2),
        "dire3_bat_eph": fig_hist_trim_baton("DIRE-03", selected_years, 2),
        "dire3_cou_eph": fig_hist_trim_courbe("DIRE-03", selected_years, 2),
        "dire3_tot_eph": fig_hist_total("DIRE-03", selected_years, 2),
        "daf1_bat_eph": fig_hist_trim_baton("DAF-01", selected_years, 2),
        "daf1_cou_eph": fig_hist_trim_courbe("DAF-01", selected_years, 2),
        "daf1_tot_eph": fig_hist_total("DAF-01", selected_years, 2),
        "daf2_bat_eph": fig_hist_trim_baton("DAF-02", selected_years, 2),
        "daf2_cou_eph": fig_hist_trim_courbe("DAF-02", selected_years, 2),
        "daf2_tot_eph": fig_hist_total("DAF-02", selected_years, 2),
        "daf3_bat_eph": fig_hist_trim_baton("DAF-03", selected_years, 2),
        "daf3_cou_eph": fig_hist_trim_courbe("DAF-03", selected_years, 2),
        "daf3_tot_eph": fig_hist_total("DAF-03", selected_years, 2),
        "daf4_bat_eph": fig_hist_trim_baton("DAF-04", selected_years, 2),
        "daf4_cou_eph": fig_hist_trim_courbe("DAF-04", selected_years, 2),
        "daf4_tot_eph": fig_hist_total("DAF-04", selected_years, 2),
        "daf5_bat_eph": fig_hist_trim_baton("DAF-05", selected_years, 2),
        "daf5_cou_eph": fig_hist_trim_courbe("DAF-05", selected_years, 2),
        "daf5_tot_eph": fig_hist_total("DAF-05", selected_years, 2),
        "daf6_tot_eph": fig_hist_total("DAF-06", selected_years, 2),
        "drh1_tot_eph": fig_hist_total("DRH-01", selected_years, 7),
        "drh2_tot_eph": fig_hist_total("DRH-02", selected_years, 7),
        "drh3_bat_eph": fig_hist_trim_baton("DRH-03", selected_years, 2),
        "drh3_cou_eph": fig_hist_trim_courbe("DRH-03", selected_years, 2),
        "drh3_tot_eph": fig_hist_total("DRH-03", selected_years, 2),
        "drh4_tot_eph": fig_hist_total("DRH-04", selected_years, 7),
        "drh5_tot_eph": fig_hist_total("DRH-05", selected_years, 7),
        "drh6_tot_eph": fig_hist_total("DRH-06", selected_years, 7),
        "radar_eph": fig_hist_radar(selected_years, 2),

        #INF
        "df1_tot_inf": fig_hist_total("DF-01", selected_years, 3),
        "drfd1_tot_inf": fig_hist_total("DRFD-01", selected_years, 3),
        "drfd2_tot_inf": fig_hist_total("DRFD-02", selected_years, 3),
        "drfd3_tot_inf": fig_hist_total("DRFD-03", selected_years, 3),
        "dire1_bat_inf": fig_hist_trim_baton("DIRE-01", selected_years, 3),
        "dire1_cou_inf": fig_hist_trim_courbe("DIRE-01", selected_years, 3),
        "dire1_tot_inf": fig_hist_total("DIRE-01", selected_years, 3),
        "dire2_bat_inf": fig_hist_trim_baton("DIRE-02", selected_years, 3),
        "dire2_cou_inf": fig_hist_trim_courbe("DIRE-02", selected_years, 3),
        "dire2_tot_inf": fig_hist_total("DIRE-02", selected_years, 3),
        "dire3_bat_inf": fig_hist_trim_baton("DIRE-03", selected_years, 3),
        "dire3_cou_inf": fig_hist_trim_courbe("DIRE-03", selected_years, 3),
        "dire3_tot_inf": fig_hist_total("DIRE-03", selected_years, 3),
        "daf1_bat_inf": fig_hist_trim_baton("DAF-01", selected_years, 3),
        "daf1_cou_inf": fig_hist_trim_courbe("DAF-01", selected_years, 3),
        "daf1_tot_inf": fig_hist_total("DAF-01", selected_years, 3),
        "daf2_bat_inf": fig_hist_trim_baton("DAF-02", selected_years, 3),
        "daf2_cou_inf": fig_hist_trim_courbe("DAF-02", selected_years, 3),
        "daf2_tot_inf": fig_hist_total("DAF-02", selected_years, 3),
        "daf3_bat_inf": fig_hist_trim_baton("DAF-03", selected_years, 3),
        "daf3_cou_inf": fig_hist_trim_courbe("DAF-03", selected_years, 3),
        "daf3_tot_inf": fig_hist_total("DAF-03", selected_years, 3),
        "daf4_bat_inf": fig_hist_trim_baton("DAF-04", selected_years, 3),
        "daf4_cou_inf": fig_hist_trim_courbe("DAF-04", selected_years, 3),
        "daf4_tot_inf": fig_hist_total("DAF-04", selected_years, 3),
        "daf5_bat_inf": fig_hist_trim_baton("DAF-05", selected_years, 3),
        "daf5_cou_inf": fig_hist_trim_courbe("DAF-05", selected_years, 3),
        "daf5_tot_inf": fig_hist_total("DAF-05", selected_years, 3),
        "daf6_tot_inf": fig_hist_total("DAF-06", selected_years, 3),
        "drh1_tot_inf": fig_hist_total("DRH-01", selected_years, 8),
        "drh2_tot_inf": fig_hist_total("DRH-02", selected_years, 8),
        "drh3_bat_inf": fig_hist_trim_baton("DRH-03", selected_years, 3),
        "drh3_cou_inf": fig_hist_trim_courbe("DRH-03", selected_years, 3),
        "drh3_tot_inf": fig_hist_total("DRH-03", selected_years, 3),
        "drh4_tot_inf": fig_hist_total("DRH-04", selected_years, 8),
        "drh5_tot_inf": fig_hist_total("DRH-05", selected_years, 8),
        "drh6_tot_inf": fig_hist_total("DRH-06", selected_years, 8),
        "radar_inf": fig_hist_radar(selected_years, 3),


        #RS2M
        "df1_tot_rs2m": fig_hist_total("DF-01", selected_years, 4),
        "drfd1_tot_rs2m": fig_hist_total("DRFD-01", selected_years, 4),
        "drfd2_tot_rs2m": fig_hist_total("DRFD-02", selected_years, 4),
        "drfd3_tot_rs2m": fig_hist_total("DRFD-03", selected_years, 4),
        "dire1_bat_rs2m": fig_hist_trim_baton("DIRE-01", selected_years, 4),
        "dire1_cou_rs2m": fig_hist_trim_courbe("DIRE-01", selected_years, 4),
        "dire1_tot_rs2m": fig_hist_total("DIRE-01", selected_years, 4),
        "dire2_bat_rs2m": fig_hist_trim_baton("DIRE-02", selected_years, 4),
        "dire2_cou_rs2m": fig_hist_trim_courbe("DIRE-02", selected_years, 4),
        "dire2_tot_rs2m": fig_hist_total("DIRE-02", selected_years, 4),
        "dire3_bat_rs2m": fig_hist_trim_baton("DIRE-03", selected_years, 4),
        "dire3_cou_rs2m": fig_hist_trim_courbe("DIRE-03", selected_years, 4),
        "dire3_tot_rs2m": fig_hist_total("DIRE-03", selected_years, 4),
        "daf1_bat_rs2m": fig_hist_trim_baton("DAF-01", selected_years, 4),
        "daf1_cou_rs2m": fig_hist_trim_courbe("DAF-01", selected_years, 4),
        "daf1_tot_rs2m": fig_hist_total("DAF-01", selected_years, 4),
        "daf2_bat_rs2m": fig_hist_trim_baton("DAF-02", selected_years, 4),
        "daf2_cou_rs2m": fig_hist_trim_courbe("DAF-02", selected_years, 4),
        "daf2_tot_rs2m": fig_hist_total("DAF-02", selected_years, 4),
        "daf3_bat_rs2m": fig_hist_trim_baton("DAF-03", selected_years, 4),
        "daf3_cou_rs2m": fig_hist_trim_courbe("DAF-03", selected_years, 4),
        "daf3_tot_rs2m": fig_hist_total("DAF-03", selected_years, 4),
        "daf4_bat_rs2m": fig_hist_trim_baton("DAF-04", selected_years, 4),
        "daf4_cou_rs2m": fig_hist_trim_courbe("DAF-04", selected_years, 4),
        "daf4_tot_rs2m": fig_hist_total("DAF-04", selected_years, 4),
        "daf5_bat_rs2m": fig_hist_trim_baton("DAF-05", selected_years, 4),
        "daf5_cou_rs2m": fig_hist_trim_courbe("DAF-05", selected_years, 4),
        "daf5_tot_rs2m": fig_hist_total("DAF-05", selected_years, 4),
        "daf6_tot_rs2m": fig_hist_total("DAF-06", selected_years, 4),
        "drh1_tot_rs2m": fig_hist_total("DRH-01", selected_years, 9),
        "drh2_tot_rs2m": fig_hist_total("DRH-02", selected_years, 9),
        "drh3_bat_rs2m": fig_hist_trim_baton("DRH-03", selected_years, 4),
        "drh3_cou_rs2m": fig_hist_trim_courbe("DRH-03", selected_years, 4),
        "drh3_tot_rs2m": fig_hist_total("DRH-03", selected_years, 4),
        "drh4_tot_rs2m": fig_hist_total("DRH-04", selected_years, 9),
        "drh5_tot_rs2m": fig_hist_total("DRH-05", selected_years, 9),
        "drh6_tot_rs2m": fig_hist_total("DRH-06", selected_years, 9),
        "radar_rs2m": fig_hist_radar(selected_years, 4),

        #RST
        "df1_tot_rst": fig_hist_total("DF-01", selected_years, 5),
        "drfd1_tot_rst": fig_hist_total("DRFD-01", selected_years, 5),
        "drfd2_tot_rst": fig_hist_total("DRFD-02", selected_years, 5),
        "drfd3_tot_rst": fig_hist_total("DRFD-03", selected_years, 5),
        "dire1_bat_rst": fig_hist_trim_baton("DIRE-01", selected_years, 5),
        "dire1_cou_rst": fig_hist_trim_courbe("DIRE-01", selected_years, 5),
        "dire1_tot_rst": fig_hist_total("DIRE-01", selected_years, 5),
        "dire2_bat_rst": fig_hist_trim_baton("DIRE-02", selected_years, 5),
        "dire2_cou_rst": fig_hist_trim_courbe("DIRE-02", selected_years, 5),
        "dire2_tot_rst": fig_hist_total("DIRE-02", selected_years, 5),
        "dire3_bat_rst": fig_hist_trim_baton("DIRE-03", selected_years, 5),
        "dire3_cou_rst": fig_hist_trim_courbe("DIRE-03", selected_years, 5),
        "dire3_tot_rst": fig_hist_total("DIRE-03", selected_years, 5),
        "daf1_bat_rst": fig_hist_trim_baton("DAF-01", selected_years, 5),
        "daf1_cou_rst": fig_hist_trim_courbe("DAF-01", selected_years, 5),
        "daf1_tot_rst": fig_hist_total("DAF-01", selected_years, 5),
        "daf2_bat_rst": fig_hist_trim_baton("DAF-02", selected_years, 5),
        "daf2_cou_rst": fig_hist_trim_courbe("DAF-02", selected_years, 5),
        "daf2_tot_rst": fig_hist_total("DAF-02", selected_years, 5),
        "daf3_bat_rst": fig_hist_trim_baton("DAF-03", selected_years, 5),
        "daf3_cou_rst": fig_hist_trim_courbe("DAF-03", selected_years, 5),
        "daf3_tot_rst": fig_hist_total("DAF-03", selected_years, 5),
        "daf4_bat_rst": fig_hist_trim_baton("DAF-04", selected_years, 5),
        "daf4_cou_rst": fig_hist_trim_courbe("DAF-04", selected_years, 5),
        "daf4_tot_rst": fig_hist_total("DAF-04", selected_years, 5),
        "daf5_bat_rst": fig_hist_trim_baton("DAF-05", selected_years, 5),
        "daf5_cou_rst": fig_hist_trim_courbe("DAF-05", selected_years, 5),
        "daf5_tot_rst": fig_hist_total("DAF-05", selected_years, 5),
        "daf6_tot_rst": fig_hist_total("DAF-06", selected_years, 5),
        "drh1_tot_rst": fig_hist_total("DRH-01", selected_years, 10),
        "drh2_tot_rst": fig_hist_total("DRH-02", selected_years, 10),
        "drh3_bat_rst": fig_hist_trim_baton("DRH-03", selected_years, 5),
        "drh3_cou_rst": fig_hist_trim_courbe("DRH-03", selected_years, 5),
        "drh3_tot_rst": fig_hist_total("DRH-03", selected_years, 5),
        "drh4_tot_rst": fig_hist_total("DRH-04", selected_years, 10),
        "drh5_tot_rst": fig_hist_total("DRH-05", selected_years, 10),
        "drh6_tot_rst": fig_hist_total("DRH-06", selected_years, 10),
        "radar_rst": fig_hist_radar(selected_years, 5),


        #Autres

        #DF
        "drh1_tot_df": fig_hist_total("DRH-01", selected_years, 0),
        "drh2_tot_df": fig_hist_total("DRH-02", selected_years, 0),
        "drh4_tot_df": fig_hist_total("DRH-04", selected_years, 0),
        "drh5_tot_df": fig_hist_total("DRH-05", selected_years, 0),
        "drh6_tot_df": fig_hist_total("DRH-06", selected_years, 0),

        #DRFD
        "drh1_tot_drfd": fig_hist_total("DRH-01", selected_years, 1),
        "drh2_tot_drfd": fig_hist_total("DRH-02", selected_years, 1),
        "drh4_tot_drfd": fig_hist_total("DRH-04", selected_years, 1),
        "drh5_tot_drfd": fig_hist_total("DRH-05", selected_years, 1),
        "drh6_tot_drfd": fig_hist_total("DRH-06", selected_years, 1),

        #DIRE
        "drh1_tot_dire": fig_hist_total("DRH-01", selected_years, 2),
        "drh2_tot_dire": fig_hist_total("DRH-02", selected_years, 2),
        "drh4_tot_dire": fig_hist_total("DRH-04", selected_years, 2),
        "drh5_tot_dire": fig_hist_total("DRH-05", selected_years, 2),
        "drh6_tot_dire": fig_hist_total("DRH-06", selected_years, 2),

        #DRI
        "drh1_tot_dri": fig_hist_total("DRH-01", selected_years, 3),
        "drh2_tot_dri": fig_hist_total("DRH-02", selected_years, 3),
        "drh4_tot_dri": fig_hist_total("DRH-04", selected_years, 3),
        "drh5_tot_dri": fig_hist_total("DRH-05", selected_years, 3),
        "drh6_tot_dri": fig_hist_total("DRH-06", selected_years, 3),

        #DCOM
        "drh1_tot_dcom": fig_hist_total("DRH-01", selected_years, 4),
        "drh2_tot_dcom": fig_hist_total("DRH-02", selected_years, 4),
        "drh4_tot_dcom": fig_hist_total("DRH-04", selected_years, 4),
        "drh5_tot_dcom": fig_hist_total("DRH-05", selected_years, 4),
        "drh6_tot_dcom": fig_hist_total("DRH-06", selected_years, 4),

        }
"""