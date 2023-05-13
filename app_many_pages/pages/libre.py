#fichier pour indicateurs avec sélection libre selon les departements.

import dash
from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from app_many_pages.df_fig import *
from app_many_pages.dire_fig import *
from app_many_pages.daf_fig import *
from app_many_pages.drfd_fig import *
from app_many_pages.drh_fig import *
from app_many_pages.dri_fig import *
from app_many_pages.departement_fig import *
from app_many_pages.artemis_fig import *
from app_many_pages.citi_fig import *
from app_many_pages.eph_fig import *
from app_many_pages.inf_fig import *
from app_many_pages.rs2m_fig import *
from app_many_pages.rst_fig import *







categories = [
    # DF
    {"label": "DF - Nombre d\'étudiants", "value": "df_1"},
    {"label": "DF - Nombre d\'UP", "value": "df_2"},
    {"label": "DF - Total des indicateurs en heures équivalentes de 2015 à 2019 - Graphe bâton", "value": "df_old_1"},
    {"label": "DF - Total des indicateurs en heures équivalentes de 2015 à 2019", "value": "df_old_2"},


    # DRFD
    {"label": "DRFD - Publications", "value": "drfd_1"},
    {"label": "DRFD - Nombre de doctorants", "value": "drfd_2"},
    {"label": "DRFD - Evolutions des publications", "value": "drfd_3"},
    {"label": "DRFD - Evolution du nombre de doctorants", "value": "drfd_4"},
    {"label": "DRFD - Publications de 2015 à 2019 - Graphe bâton", "value": "drfd_old_1"},
    {"label": "DRFD - Publications de 2015 à 2019", "value": "drfd_old_2"},
    {"label": "DRFD - Nombre de doctorants de 2015 à 2019 - Graphe bâton", "value": "drfd_old_3"},
    {"label": "DRFD - Nombre de doctorants de 2015 à 2019", "value": "drfd_old_4"},

    # DIRE
    {"label": "DIRE - Suivi des contrats de recherches", "value": "dire_1"},
    {"label": "DIRE - Suivi des contrats de recherches, vision trimestrielle", "value": "dire_2"},
    {"label": "DIRE - Suivi des contrats de recherches, total école", "value": "dire_3"},
    {"label": "DIRE - Contribution au financement de l'école, graphe camembert", "value": "dire_4"},
    {"label": "DIRE - CA des contrats de recherches de 2015 à 2019 - Graphe bâton", "value": "dire_old_1"},
    {"label": "DIRE - CA des contrats de recherches de 2015 à 2019", "value": "dire_old_2"},
    {"label": "DIRE - Brevets et logiciels déposés de 2015 à 2019 - Graphe bâton", "value": "dire_old_3"},
    {"label": "DIRE - Brevets et logiciels déposés de 2015 à 2019", "value": "dire_old_4"},
    {"label": "DIRE - Contribution au financement de l\'école de 2015 à 2019 - Graphe bâton", "value": "dire_old_5"},
    {"label": "DIRE - Contribution au financement de l\'école de 2015 à 2019", "value": "dire_old_6"},

    # DAF
    {"label": "DAF - Chiffre d\'affaire de la recherche", "value": "daf_1"},
    {"label": "DAF - Dépenses de vacataires", "value": "diaf_2"},
    {"label": "DAF - Dépenses de vacataires, vision trimestrielle", "value": "daf_3"},
    {"label": "DAF - Ressource propres", "value": "daf_4"},
    {"label": "DAF - Ressource propres, vision trimestrielle", "value": "daf_5"},
    {"label": "DAF - Ressource d\'état", "value": "daf_6"},
    {"label": "DAF - Ressource d\'état, vision trimestrielle", "value": "daf_7"},
    {"label": "DAF - Total des dépenses", "value": "daf_8"},
    {"label": "DAF - Total des dépenses, vision trimestrielle", "value": "daf_9"},
    {"label": "DAF - Dépenses de vacataires de 2015 à 2019 - Graphe bâton", "value": "daf_old_1"},
    {"label": "DAF - Dépenses de vacataires de 2015 à 2019", "value": "daf_old_2"},
    {"label": "DAF - Ressources propres totales de 2015 à 2019 - Graphe bâton", "value": "daf_old_3"},
    {"label": "DAF - Ressources propres totales de 2015 à 2019", "value": "daf_old_4"},
    {"label": "DAF - Dépenses hors permanents et vacataires de 2015 à 2019 - Graphe bâton", "value": "daf_old_5"},
    {"label": "DAF - Dépenses hors permanents et vacataires de 2015 à 2019", "value": "daf_old_6"},

    # DRH
    {"label": "DRH - Nombre de permanents", "value": "drh_1"},
    {"label": "DRH - Répartition des permanents, vision trimestrielle", "value": "drh_2"},
    {"label": "DRH - Nombre de non-permanents", "value": "drh_3"},
    {"label": "DRH - Evolution du nombre de non-permanents", "value": "drh_4"},
    {"label": "DRH - Permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "drh_old_1"},
    {"label": "DRH - Permanents en ETPT de 2015 à 2019", "value": "drh_old_2"},
    {"label": "DRH - Non-permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "drh_old_3"},
    {"label": "DRH - Non-permanents en ETPT de 2015 à 2019", "value": "drh_old_4"},

    # DRI
    {"label": "DRI - Chiffres sur l'international", "value": "dri_2"},
    {"label": "DRI - Evolution du nombre d\'étudiants étrangers, bâtons", "value": "dri_3"},
    {"label": "DRI - Evolution du nombre d\'étudiants étrangers, courbe", "value": "dri_4"},

    #ARTEMIS
    {"label": "ARTEMIS - Graphe radar année 2023", "value": "dept_2"},
    {"label": "ARTEMIS - Graphe radar année 2023-2024", "value": "dept_1"},
    {"label": "ARTEMIS - Ressources humaines", "value": "artemis_1"},
    {"label": "ARTEMIS - Contrats de recherche", "value": "artemis_2"},
    {"label": "ARTEMIS - Contribution au financement de l\'école", "value": "artemis_3"},
    {"label": "ARTEMIS - Dépense de vacataires", "value": "artemis_4"},
    {"label": "ARTEMIS - Ressources propres", "value": "artemis_5"},
    {"label": "ARTEMIS - Ressources d\'états", "value": "artemis_6"},
    {"label": "ARTEMIS - Total des dépenses", "value": "artemis_7"},
    {"label": "ARTEMIS - Total des indicateurs en heures équivalentes de 2015 à 2019 - Graphe bâton", "value": "artemis_old_df_1"},
    {"label": "ARTEMIS - Total des indicateurs en heures équivalentes de 2015 à 2019", "value": "artemis_old_df_2"},
    {"label": "ARTEMIS - Publications de 2015 à 2019 - Graphe bâton", "value": "artemis_old_drfd_1"},
    {"label": "ARTEMIS - Publications de 2015 à 2019", "value": "artemis_old_drfd_2"},
    {"label": "ARTEMIS - Nombre de doctorants de 2015 à 2019 - Graphe bâton", "value": "artemis_old_drfd_3"},
    {"label": "ARTEMIS - Nombre de doctorants de 2015 à 2019", "value": "artemis_old_drfd_4"},
    {"label": "ARTEMIS - CA des contrats de recherches de 2015 à 2019 - Graphe bâton", "value": "artemis_old_dire_1"},
    {"label": "ARTEMIS - CA des contrats de recherches de 2015 à 2019", "value": "artemis_old_dire_2"},
    {"label": "ARTEMIS - Brevets et logiciels déposés de 2015 à 2019 - Graphe bâton", "value": "artemis_old_dire_3"},
    {"label": "ARTEMIS - Brevets et logiciels déposés de 2015 à 2019", "value": "artemis_old_dire_4"},
    {"label": "ARTEMIS - Contribution au financement de l\'école de 2015 à 2019 - Graphe bâton", "value": "artemis_old_dire_5"},
    {"label": "ARTEMIS - Contribution au financement de l\'école de 2015 à 2019", "value": "artemis_old_dire_6"},
    {"label": "ARTEMIS - Dépenses de vacataires de 2015 à 2019 - Graphe bâton", "value": "artemis_old_daf_1"},
    {"label": "ARTEMIS - Dépenses de vacataires de 2015 à 2019", "value": "artemis_old_daf_2"},
    {"label": "ARTEMIS - Ressources propres totales de 2015 à 2019 - Graphe bâton", "value": "artemis_old_daf_3"},
    {"label": "ARTEMIS - Ressources propres totales de 2015 à 2019", "value": "artemis_old_daf_4"},
    {"label": "ARTEMIS - Dépenses hors permanents et vacataires de 2015 à 2019 - Graphe bâton", "value": "artemis_old_daf_5"},
    {"label": "ARTEMIS - Dépenses hors permanents et vacataires de 2015 à 2019", "value": "artemis_old_daf_6"},
    {"label": "ARTEMIS - Permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "artemis_old_drh_1"},
    {"label": "ARTEMIS - Permanents en ETPT de 2015 à 2019", "value": "artemis_old_drh_2"},
    {"label": "ARTEMIS - Non-permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "artemis_old_drh_3"},
    {"label": "ARTEMIS - Non-permanents en ETPT de 2015 à 2019", "value": "artemis_old_drh_4"},


    #CITI
    {"label": "CITI - Graphe radar année 2023", "value": "dept_3"},
    {"label": "CITI - Ressources humaines", "value": "citi_1"},
    {"label": "CITI - Contrats de recherche", "value": "citi_2"},
    {"label": "CITI - Contribution au financement de l\'école", "value": "citi_3"},
    {"label": "CITI - Dépense de vacataires", "value": "citi_4"},
    {"label": "CITI - Ressources propres", "value": "citi_5"},
    {"label": "CITI - Ressources d\'états", "value": "citi_6"},
    {"label": "CITI - Total des dépenses", "value": "citi_7"},
    {"label": "CITI - Total des indicateurs en heures équivalentes de 2015 à 2019 - Graphe bâton", "value": "citi_old_df_1"},
    {"label": "CITI - Total des indicateurs en heures équivalentes de 2015 à 2019", "value": "citi_old_df_2"},
    {"label": "CITI - Publications de 2015 à 2019 - Graphe bâton", "value": "citi_old_drfd_1"},
    {"label": "CITI - Publications de 2015 à 2019", "value": "citi_old_drfd_2"},
    {"label": "CITI - Nombre de doctorants de 2015 à 2019 - Graphe bâton", "value": "citi_old_drfd_3"},
    {"label": "CITI - Nombre de doctorants de 2015 à 2019", "value": "citi_old_drfd_4"},
    {"label": "CITI - CA des contrats de recherches de 2015 à 2019 - Graphe bâton", "value": "citi_old_dire_1"},
    {"label": "CITI - CA des contrats de recherches de 2015 à 2019", "value": "citi_old_dire_2"},
    {"label": "CITI - Brevets et logiciels déposés de 2015 à 2019 - Graphe bâton", "value": "citi_old_dire_3"},
    {"label": "CITI - Brevets et logiciels déposés de 2015 à 2019", "value": "citi_old_dire_4"},
    {"label": "CITI - Contribution au financement de l\'école de 2015 à 2019 - Graphe bâton", "value": "citi_old_dire_5"},
    {"label": "CITI - Contribution au financement de l\'école de 2015 à 2019", "value": "citi_old_dire_6"},
    {"label": "CITI - Dépenses de vacataires de 2015 à 2019 - Graphe bâton", "value": "citi_old_daf_1"},
    {"label": "CITI - Dépenses de vacataires de 2015 à 2019", "value": "citi_old_daf_2"},
    {"label": "CITI - Ressources propres totales de 2015 à 2019 - Graphe bâton", "value": "citi_old_daf_3"},
    {"label": "CITI - Ressources propres totales de 2015 à 2019", "value": "citi_old_daf_4"},
    {"label": "CITI - Dépenses hors permanents et vacataires de 2015 à 2019 - Graphe bâton", "value": "citi_old_daf_5"},
    {"label": "CITI - Dépenses hors permanents et vacataires de 2015 à 2019", "value": "citi_old_daf_6"},
    {"label": "CITI - Permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "citi_old_drh_1"},
    {"label": "CITI - Permanents en ETPT de 2015 à 2019", "value": "citi_old_drh_2"},
    {"label": "CITI - Non-permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "citi_old_drh_3"},
    {"label": "CITI - Non-permanents en ETPT de 2015 à 2019", "value": "citi_old_drh_4"},


    #EPH
    {"label": "EPH - Graphe radar année 2023", "value": "dept_4"},
    {"label": "EPH - Ressources humaines", "value": "eph_1"},
    {"label": "EPH - Contrats de recherche", "value": "eph_2"},
    {"label": "EPH - Contribution au financement de l\'école", "value": "eph_3"},
    {"label": "EPH - Dépense de vacataires", "value": "eph_4"},
    {"label": "EPH - Ressources propres", "value": "eph_5"},
    {"label": "EPH - Ressources d\'états", "value": "eph_6"},
    {"label": "EPH - Total des dépenses", "value": "eph_7"},
    {"label": "EPH - Total des indicateurs en heures équivalentes de 2015 à 2019 - Graphe bâton", "value": "eph_old_df_1"},
    {"label": "EPH - Total des indicateurs en heures équivalentes de 2015 à 2019", "value": "eph_old_df_2"},
    {"label": "EPH - Publications de 2015 à 2019 - Graphe bâton", "value": "eph_old_drfd_1"},
    {"label": "EPH - Publications de 2015 à 2019", "value": "eph_old_drfd_2"},
    {"label": "EPH - Nombre de doctorants de 2015 à 2019 - Graphe bâton", "value": "eph_old_drfd_3"},
    {"label": "EPH - Nombre de doctorants de 2015 à 2019", "value": "eph_old_drfd_4"},
    {"label": "EPH - CA des contrats de recherches de 2015 à 2019 - Graphe bâton", "value": "eph_old_dire_1"},
    {"label": "EPH - CA des contrats de recherches de 2015 à 2019", "value": "eph_old_dire_2"},
    {"label": "EPH - Brevets et logiciels déposés de 2015 à 2019 - Graphe bâton", "value": "eph_old_dire_3"},
    {"label": "EPH - Brevets et logiciels déposés de 2015 à 2019", "value": "eph_old_dire_4"},
    {"label": "EPH - Contribution au financement de l\'école de 2015 à 2019 - Graphe bâton", "value": "eph_old_dire_5"},
    {"label": "EPH - Contribution au financement de l\'école de 2015 à 2019", "value": "eph_old_dire_6"},
    {"label": "EPH - Dépenses de vacataires de 2015 à 2019 - Graphe bâton", "value": "eph_old_daf_1"},
    {"label": "EPH - Dépenses de vacataires de 2015 à 2019", "value": "eph_old_daf_2"},
    {"label": "EPH - Ressources propres totales de 2015 à 2019 - Graphe bâton", "value": "eph_old_daf_3"},
    {"label": "EPH - Ressources propres totales de 2015 à 2019", "value": "eph_old_daf_4"},
    {"label": "EPH - Dépenses hors permanents et vacataires de 2015 à 2019 - Graphe bâton", "value": "eph_old_daf_5"},
    {"label": "EPH - Dépenses hors permanents et vacataires de 2015 à 2019", "value": "eph_old_daf_6"},
    {"label": "EPH - Permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "eph_old_drh_1"},
    {"label": "EPH - Permanents en ETPT de 2015 à 2019", "value": "eph_old_drh_2"},
    {"label": "EPH - Non-permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "eph_old_drh_3"},
    {"label": "EPH - Non-permanents en ETPT de 2015 à 2019", "value": "eph_old_drh_4"},


    #INF
    {"label": "INF - Graphe radar année 2023", "value": "dept_5"},
    {"label": "INF - Ressources humaines", "value": "inf_1"},
    {"label": "INF - Contrats de recherche", "value": "inf_2"},
    {"label": "INF - Contribution au financement de l\'école", "value": "inf_3"},
    {"label": "INF - Dépense de vacataires", "value": "inf_4"},
    {"label": "INF - Ressources propres", "value": "inf_5"},
    {"label": "INF - Ressources d\'états", "value": "inf_6"},
    {"label": "INF - Total des dépenses", "value": "inf_7"},
    {"label": "INF - Total des indicateurs en heures équivalentes de 2015 à 2019 - Graphe bâton", "value": "inf_old_df_1"},
    {"label": "INF - Total des indicateurs en heures équivalentes de 2015 à 2019", "value": "inf_old_df_2"},
    {"label": "INF - Publications de 2015 à 2019 - Graphe bâton", "value": "inf_old_drfd_1"},
    {"label": "INF - Publications de 2015 à 2019", "value": "inf_old_drfd_2"},
    {"label": "INF - Nombre de doctorants de 2015 à 2019 - Graphe bâton", "value": "inf_old_drfd_3"},
    {"label": "INF - Nombre de doctorants de 2015 à 2019", "value": "inf_old_drfd_4"},
    {"label": "INF - CA des contrats de recherches de 2015 à 2019 - Graphe bâton", "value": "inf_old_dire_1"},
    {"label": "INF - CA des contrats de recherches de 2015 à 2019", "value": "inf_old_dire_2"},
    {"label": "INF - Brevets et logiciels déposés de 2015 à 2019 - Graphe bâton", "value": "inf_old_dire_3"},
    {"label": "INF - Brevets et logiciels déposés de 2015 à 2019", "value": "inf_old_dire_4"},
    {"label": "INF - Contribution au financement de l\'école de 2015 à 2019 - Graphe bâton", "value": "inf_old_dire_5"},
    {"label": "INF - Contribution au financement de l\'école de 2015 à 2019", "value": "inf_old_dire_6"},
    {"label": "INF - Dépenses de vacataires de 2015 à 2019 - Graphe bâton", "value": "inf_old_daf_1"},
    {"label": "INF - Dépenses de vacataires de 2015 à 2019", "value": "inf_old_daf_2"},
    {"label": "INF - Ressources propres totales de 2015 à 2019 - Graphe bâton", "value": "inf_old_daf_3"},
    {"label": "INF - Ressources propres totales de 2015 à 2019", "value": "inf_old_daf_4"},
    {"label": "INF - Dépenses hors permanents et vacataires de 2015 à 2019 - Graphe bâton", "value": "inf_old_daf_5"},
    {"label": "INF - Dépenses hors permanents et vacataires de 2015 à 2019", "value": "inf_old_daf_6"},
    {"label": "INF - Permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "inf_old_drh_1"},
    {"label": "INF - Permanents en ETPT de 2015 à 2019", "value": "inf_old_drh_2"},
    {"label": "INF - Non-permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "inf_old_drh_3"},
    {"label": "INF - Non-permanents en ETPT de 2015 à 2019", "value": "inf_old_drh_4"},


    #RS2M
    {"label": "RS2M - Graphe radar année 2023", "value": "dept_6"},
    {"label": "RS2M - Ressources humaines", "value": "rs2m_1"},
    {"label": "RS2M - Contrats de recherche", "value": "rs2m_2"},
    {"label": "RS2M - Contribution au financement de l\'école", "value": "rs2m_3"},
    {"label": "RS2M - Dépense de vacataires", "value": "rs2m_4"},
    {"label": "RS2M - Ressources propres", "value": "rs2m_5"},
    {"label": "RS2M - Ressources d\'états", "value": "rs2m_6"},
    {"label": "RS2M - Total des dépenses", "value": "rs2m_7"},
    {"label": "RS2M - Total des indicateurs en heures équivalentes de 2015 à 2019 - Graphe bâton", "value": "rs2m_old_df_1"},
    {"label": "RS2M - Total des indicateurs en heures équivalentes de 2015 à 2019", "value": "rs2m_old_df_2"},
    {"label": "RS2M - Publications de 2015 à 2019 - Graphe bâton", "value": "rs2m_old_drfd_1"},
    {"label": "RS2M - Publications de 2015 à 2019", "value": "rs2m_old_drfd_2"},
    {"label": "RS2M - Nombre de doctorants de 2015 à 2019 - Graphe bâton", "value": "rs2m_old_drfd_3"},
    {"label": "RS2M - Nombre de doctorants de 2015 à 2019", "value": "rs2m_old_drfd_4"},
    {"label": "RS2M - CA des contrats de recherches de 2015 à 2019 - Graphe bâton", "value": "rs2m_old_dire_1"},
    {"label": "RS2M - CA des contrats de recherches de 2015 à 2019", "value": "rs2m_old_dire_2"},
    {"label": "RS2M - Brevets et logiciels déposés de 2015 à 2019 - Graphe bâton", "value": "rs2m_old_dire_3"},
    {"label": "RS2M - Brevets et logiciels déposés de 2015 à 2019", "value": "rs2m_old_dire_4"},
    {"label": "RS2M - Contribution au financement de l\'école de 2015 à 2019 - Graphe bâton", "value": "rs2m_old_dire_5"},
    {"label": "RS2M - Contribution au financement de l\'école de 2015 à 2019", "value": "rs2m_old_dire_6"},
    {"label": "RS2M - Dépenses de vacataires de 2015 à 2019 - Graphe bâton", "value": "rs2m_old_daf_1"},
    {"label": "RS2M - Dépenses de vacataires de 2015 à 2019", "value": "rs2m_old_daf_2"},
    {"label": "RS2M - Ressources propres totales de 2015 à 2019 - Graphe bâton", "value": "rs2m_old_daf_3"},
    {"label": "RS2M - Ressources propres totales de 2015 à 2019", "value": "rs2m_old_daf_4"},
    {"label": "RS2M - Dépenses hors permanents et vacataires de 2015 à 2019 - Graphe bâton", "value": "rs2m_old_daf_5"},
    {"label": "RS2M - Dépenses hors permanents et vacataires de 2015 à 2019", "value": "rs2m_old_daf_6"},
    {"label": "RS2M - Permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "rs2m_old_drh_1"},
    {"label": "RS2M - Permanents en ETPT de 2015 à 2019", "value": "rs2m_old_drh_2"},
    {"label": "RS2M - Non-permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "rs2m_old_drh_3"},
    {"label": "RS2M - Non-permanents en ETPT de 2015 à 2019", "value": "rs2m_old_drh_4"},




    #RST
    {"label": "RST - Graphe radar année 2023", "value": "dept_7"},
    {"label": "RST - Ressources humaines", "value": "rst_1"},
    {"label": "RST - Contrats de recherche", "value": "rst_2"},
    {"label": "RST - Contribution au financement de l\'école", "value": "rst_3"},
    {"label": "RST - Dépense de vacataires", "value": "rst_4"},
    {"label": "RST - Ressources propres", "value": "rst_5"},
    {"label": "RST - Ressources d\'états", "value": "rst_6"},
    {"label": "RST - Total des dépenses", "value": "rst_7"},
    {"label": "RST - Total des indicateurs en heures équivalentes de 2015 à 2019 - Graphe bâton", "value": "rst_old_df_1"},
    {"label": "RST - Total des indicateurs en heures équivalentes de 2015 à 2019", "value": "rst_old_df_2"},
    {"label": "RST - Publications de 2015 à 2019 - Graphe bâton", "value": "rst_old_drfd_1"},
    {"label": "RST - Publications de 2015 à 2019", "value": "rst_old_drfd_2"},
    {"label": "RST - Nombre de doctorants de 2015 à 2019 - Graphe bâton", "value": "rst_old_drfd_3"},
    {"label": "RST - Nombre de doctorants de 2015 à 2019", "value": "rst_old_drfd_4"},
    {"label": "RST - CA des contrats de recherches de 2015 à 2019 - Graphe bâton", "value": "rst_old_dire_1"},
    {"label": "RST - CA des contrats de recherches de 2015 à 2019", "value": "rst_old_dire_2"},
    {"label": "RST - Brevets et logiciels déposés de 2015 à 2019 - Graphe bâton", "value": "rst_old_dire_3"},
    {"label": "RST - Brevets et logiciels déposés de 2015 à 2019", "value": "rst_old_dire_4"},
    {"label": "RST - Contribution au financement de l\'école de 2015 à 2019 - Graphe bâton", "value": "rst_old_dire_5"},
    {"label": "RST - Contribution au financement de l\'école de 2015 à 2019", "value": "rst_old_dire_6"},
    {"label": "RST - Dépenses de vacataires de 2015 à 2019 - Graphe bâton", "value": "rst_old_daf_1"},
    {"label": "RST - Dépenses de vacataires de 2015 à 2019", "value": "rst_old_daf_2"},
    {"label": "RST - Ressources propres totales de 2015 à 2019 - Graphe bâton", "value": "rst_old_daf_3"},
    {"label": "RST - Ressources propres totales de 2015 à 2019", "value": "rst_old_daf_4"},
    {"label": "RST - Dépenses hors permanents et vacataires de 2015 à 2019 - Graphe bâton", "value": "rst_old_daf_5"},
    {"label": "RST - Dépenses hors permanents et vacataires de 2015 à 2019", "value": "rst_old_daf_6"},
    {"label": "RST - Permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "rst_old_drh_1"},
    {"label": "RST - Permanents en ETPT de 2015 à 2019", "value": "rst_old_drh_2"},
    {"label": "RST - Non-permanents en ETPT de 2015 à 2019 - Graphe bâton", "value": "rst_old_drh_3"},
    {"label": "RST - Non-permanents en ETPT de 2015 à 2019", "value": "rst_old_drh_4"},


    {"label": "Graphes radar des départements", "value": "dept_8"},

    ]








dash.register_page(
    __name__,
    title = "Choix libre",
    name = "Choix libre",
    order=9,
    active= False

)

layout = dbc.Container(children=[
    html.H1(children='Dans cette page, vous pouvez afficher les graphes de votre choix'),

    html.H2(children='Sélections des graphes à afficher'),

    #joue le rôle de variable globale 
    dcc.Store(id='old-value', data=[]),

    dcc.Dropdown(
        options=categories,
        id="checklist-input",
        multi=True,

    ),

    # Boucle pour générer les graphiques

        dbc.Container(id="graph-container",
            children=[],
            fluid = True),


],


fluid = True)




@callback(
    Output("old-value", "data"),
    [Input("checklist-input", "value")],
    [State("old-value", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return value


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories):
    cat_id = cat["value"]

    @callback(
        Output(f"collapse{i + 1}", "is_open"),
        [Input("checklist-input", "value")],
        [State(f"collapse{i + 1}", "is_open"), State("old-value", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        if (cat_id in value and cat_id in data) or (cat_id not in value and cat_id not in data):
            return is_open
        return not is_open
        



# Définissez le callback pour générer les graphiques par département
@callback(
    Output("graph-container", "children"),
    [Input("checklist-input", "value")]
)

def generate_graphs(value):
    # Liste des graphiques disponibles
    graphs = {
        #DF
        "df_1": fig_df_1(),
        "df_2": fig_df_2_update(get_df_DF_annuel()),
        "df_old_1": fig_old_df_1(),
        "df_old_2": fig_old_df_2(),

        #DRFD
        "drfd_1": fig_drfd_1(),
        "drfd_2": fig_drfd_2(),
        "drfd_3": fig_drfd_3(),
        "drfd_4": fig_drfd_4(),
        "drfd_old_1": fig_old_drfd_1(),
        "drfd_old_2": fig_old_drfd_2(),
        "drfd_old_3": fig_old_drfd_3(),
        "drfd_old_4": fig_old_drfd_4(),



        #DIRE
        "dire_1": fig_dire_1(),
        "dire_2": fig_dire_2(),
        "dire_3": fig_dire_3(),
        "dire_4": fig_dire_4(),
        "dire_old_1": fig_old_dire_1(),
        "dire_old_2": fig_old_dire_2(),
        "dire_old_3": fig_old_dire_3(),
        "dire_old_4": fig_old_dire_4(),
        "dire_old_5": fig_old_dire_5(),
        "dire_old_6": fig_old_dire_6(),

        #DAF
        "daf_1": fig_daf_1(),
        "daf_2": fig_daf_2(),
        "daf_3": fig_daf_3(),
        "daf_4": fig_daf_4(),
        "daf_5": fig_daf_5(),
        "daf_6": fig_daf_6(),
        "daf_7": fig_daf_7(),
        "daf_8": fig_daf_8(),
        "daf_9": fig_daf_9(),
        "daf_old_1": fig_old_daf_1(),
        "daf_old_2": fig_old_daf_2(),
        "daf_old_3": fig_old_daf_3(),
        "daf_old_4": fig_old_daf_4(),
        "daf_old_5": fig_old_daf_5(),
        "daf_old_6": fig_old_daf_6(),


        #DRH
        "drh_1": fig_drh_1(),
        "drh_2": fig_drh_2(),
        "drh_3": fig_drh_3(),
        "drh_4": fig_drh_4(),
        "drh_old_1": fig_old_drh_1(),
        "drh_old_2": fig_old_drh_2(),
        "drh_old_3": fig_old_drh_3(),
        "drh_old_4": fig_old_drh_4(),

        #DRI
        "dri_2": fig_dri_2(),
        "dri_3": fig_dri_3(),
        "dri_4": fig_dri_4(),

        #ARTEMIS
        "dept_2": fig_dept_2(),
        "dept_1": fig_dept_1(),
        "artemis_1": fig_artemis_1(),
        "artemis_2": fig_artemis_2(),
        "artemis_3": fig_artemis_3(),
        "artemis_4": fig_artemis_4(),
        "artemis_5": fig_artemis_5(),
        "artemis_6": fig_artemis_6(),
        "artemis_7": fig_artemis_7(),
        "artemis_old_df_1": fig_old_df_artemis_1(),
        "artemis_old_df_2": fig_old_df_artemis_2(),
        "artemis_old_drfd_1": fig_old_drfd_artemis_1(),
        "artemis_old_drfd_2": fig_old_drfd_artemis_2(),
        "artemis_old_drfd_3": fig_old_drfd_artemis_3(),
        "artemis_old_drfd_4": fig_old_drfd_artemis_4(),
        "artemis_old_dire_1": fig_old_dire_artemis_1(),
        "artemis_old_dire_2": fig_old_dire_artemis_2(),
        "artemis_old_dire_3": fig_old_dire_artemis_3(),
        "artemis_old_dire_4": fig_old_dire_artemis_4(),
        "artemis_old_dire_5": fig_old_dire_artemis_5(),
        "artemis_old_dire_6": fig_old_dire_artemis_6(),
        "artemis_old_daf_1": fig_old_daf_artemis_1(),
        "artemis_old_daf_2": fig_old_daf_artemis_2(),
        "artemis_old_daf_3": fig_old_daf_artemis_3(),
        "artemis_old_daf_4": fig_old_daf_artemis_4(),
        "artemis_old_daf_5": fig_old_daf_artemis_5(),
        "artemis_old_daf_6": fig_old_daf_artemis_6(),
        "artemis_old_drh_1": fig_old_drh_artemis_1(),
        "artemis_old_drh_2": fig_old_drh_artemis_2(),
        "artemis_old_drh_3": fig_old_drh_artemis_3(),
        "artemis_old_drh_4": fig_old_drh_artemis_4(),



        #CITI
        "dept_3": fig_dept_3(),
        "citi_1": fig_citi_1(),
        "citi_2": fig_citi_2(),
        "citi_3": fig_citi_3(),
        "citi_4": fig_citi_4(),
        "citi_5": fig_citi_5(),
        "citi_6": fig_citi_6(),
        "citi_7": fig_citi_7(),
        "citi_old_df_1": fig_old_df_citi_1(),
        "citi_old_df_2": fig_old_df_citi_2(),
        "citi_old_drfd_1": fig_old_drfd_citi_1(),
        "citi_old_drfd_2": fig_old_drfd_citi_2(),
        "citi_old_drfd_3": fig_old_drfd_citi_3(),
        "citi_old_drfd_4": fig_old_drfd_citi_4(),
        "citi_old_dire_1": fig_old_dire_citi_1(),
        "citi_old_dire_2": fig_old_dire_citi_2(),
        "citi_old_dire_3": fig_old_dire_citi_3(),
        "citi_old_dire_4": fig_old_dire_citi_4(),
        "citi_old_dire_5": fig_old_dire_citi_5(),
        "citi_old_dire_6": fig_old_dire_citi_6(),
        "citi_old_daf_1": fig_old_daf_citi_1(),
        "citi_old_daf_2": fig_old_daf_citi_2(),
        "citi_old_daf_3": fig_old_daf_citi_3(),
        "citi_old_daf_4": fig_old_daf_citi_4(),
        "citi_old_daf_5": fig_old_daf_citi_5(),
        "citi_old_daf_6": fig_old_daf_citi_6(),
        "citi_old_drh_1": fig_old_drh_citi_1(),
        "citi_old_drh_2": fig_old_drh_citi_2(),
        "citi_old_drh_3": fig_old_drh_citi_3(),
        "citi_old_drh_4": fig_old_drh_citi_4(),

        #EPH
        "dept_4": fig_dept_4(),
        "eph_1": fig_eph_1(),
        "eph_2": fig_eph_2(),
        "eph_3": fig_eph_3(),
        "eph_4": fig_eph_4(),
        "eph_5": fig_eph_5(),
        "eph_6": fig_eph_6(),
        "eph_7": fig_eph_7(),
        "eph_old_df_1": fig_old_df_eph_1(),
        "eph_old_df_2": fig_old_df_eph_2(),
        "eph_old_drfd_1": fig_old_drfd_eph_1(),
        "eph_old_drfd_2": fig_old_drfd_eph_2(),
        "eph_old_drfd_3": fig_old_drfd_eph_3(),
        "eph_old_drfd_4": fig_old_drfd_eph_4(),
        "eph_old_dire_1": fig_old_dire_eph_1(),
        "eph_old_dire_2": fig_old_dire_eph_2(),
        "eph_old_dire_3": fig_old_dire_eph_3(),
        "eph_old_dire_4": fig_old_dire_eph_4(),
        "eph_old_dire_5": fig_old_dire_eph_5(),
        "eph_old_dire_6": fig_old_dire_eph_6(),
        "eph_old_daf_1": fig_old_daf_eph_1(),
        "eph_old_daf_2": fig_old_daf_eph_2(),
        "eph_old_daf_3": fig_old_daf_eph_3(),
        "eph_old_daf_4": fig_old_daf_eph_4(),
        "eph_old_daf_5": fig_old_daf_eph_5(),
        "eph_old_daf_6": fig_old_daf_eph_6(),
        "eph_old_drh_1": fig_old_drh_eph_1(),
        "eph_old_drh_2": fig_old_drh_eph_2(),
        "eph_old_drh_3": fig_old_drh_eph_3(),
        "eph_old_drh_4": fig_old_drh_eph_4(),

        #INF
        "dept_5": fig_dept_5(),
        "inf_1": fig_inf_1(),
        "inf_2": fig_inf_2(),
        "inf_3": fig_inf_3(),
        "inf_4": fig_inf_4(),
        "inf_5": fig_inf_5(),
        "inf_6": fig_inf_6(),
        "inf_7": fig_inf_7(),
        "inf_old_df_1": fig_old_df_inf_1(),
        "inf_old_df_2": fig_old_df_inf_2(),
        "inf_old_drfd_1": fig_old_drfd_inf_1(),
        "inf_old_drfd_2": fig_old_drfd_inf_2(),
        "inf_old_drfd_3": fig_old_drfd_inf_3(),
        "inf_old_drfd_4": fig_old_drfd_inf_4(),
        "inf_old_dire_1": fig_old_dire_inf_1(),
        "inf_old_dire_2": fig_old_dire_inf_2(),
        "inf_old_dire_3": fig_old_dire_inf_3(),
        "inf_old_dire_4": fig_old_dire_inf_4(),
        "inf_old_dire_5": fig_old_dire_inf_5(),
        "inf_old_dire_6": fig_old_dire_inf_6(),
        "inf_old_daf_1": fig_old_daf_inf_1(),
        "inf_old_daf_2": fig_old_daf_inf_2(),
        "inf_old_daf_3": fig_old_daf_inf_3(),
        "inf_old_daf_4": fig_old_daf_inf_4(),
        "inf_old_daf_5": fig_old_daf_inf_5(),
        "inf_old_daf_6": fig_old_daf_inf_6(),
        "inf_old_drh_1": fig_old_drh_inf_1(),
        "inf_old_drh_2": fig_old_drh_inf_2(),
        "inf_old_drh_3": fig_old_drh_inf_3(),
        "inf_old_drh_4": fig_old_drh_inf_4(),

        #RS2M
        "dept_6": fig_dept_6(),
        "rs2m_1": fig_rs2m_1(),
        "rs2m_2": fig_rs2m_2(),
        "rs2m_3": fig_rs2m_3(),
        "rs2m_4": fig_rs2m_4(),
        "rs2m_5": fig_rs2m_5(),
        "rs2m_6": fig_rs2m_6(),
        "rs2m_7": fig_rs2m_7(),
        "rs2m_old_df_1": fig_old_df_rs2m_1(),
        "rs2m_old_df_2": fig_old_df_rs2m_2(),
        "rs2m_old_drfd_1": fig_old_drfd_rs2m_1(),
        "rs2m_old_drfd_2": fig_old_drfd_rs2m_2(),
        "rs2m_old_drfd_3": fig_old_drfd_rs2m_3(),
        "rs2m_old_drfd_4": fig_old_drfd_rs2m_4(),
        "rs2m_old_dire_1": fig_old_dire_rs2m_1(),
        "rs2m_old_dire_2": fig_old_dire_rs2m_2(),
        "rs2m_old_dire_3": fig_old_dire_rs2m_3(),
        "rs2m_old_dire_4": fig_old_dire_rs2m_4(),
        "rs2m_old_dire_5": fig_old_dire_rs2m_5(),
        "rs2m_old_dire_6": fig_old_dire_rs2m_6(),
        "rs2m_old_daf_1": fig_old_daf_rs2m_1(),
        "rs2m_old_daf_2": fig_old_daf_rs2m_2(),
        "rs2m_old_daf_3": fig_old_daf_rs2m_3(),
        "rs2m_old_daf_4": fig_old_daf_rs2m_4(),
        "rs2m_old_daf_5": fig_old_daf_rs2m_5(),
        "rs2m_old_daf_6": fig_old_daf_rs2m_6(),
        "rs2m_old_drh_1": fig_old_drh_rs2m_1(),
        "rs2m_old_drh_2": fig_old_drh_rs2m_2(),
        "rs2m_old_drh_3": fig_old_drh_rs2m_3(),
        "rs2m_old_drh_4": fig_old_drh_rs2m_4(),

        #RST
        "dept_7": fig_dept_7(),
        "rst_1": fig_rst_1(),
        "rst_2": fig_rst_2(),
        "rst_3": fig_rst_3(),
        "rst_4": fig_rst_4(),
        "rst_5": fig_rst_5(),
        "rst_6": fig_rst_6(),
        "rst_7": fig_rst_7(),
        "rst_old_df_1": fig_old_df_rst_1(),
        "rst_old_df_2": fig_old_df_rst_2(),
        "rst_old_drfd_1": fig_old_drfd_rst_1(),
        "rst_old_drfd_2": fig_old_drfd_rst_2(),
        "rst_old_drfd_3": fig_old_drfd_rst_3(),
        "rst_old_drfd_4": fig_old_drfd_rst_4(),
        "rst_old_dire_1": fig_old_dire_rst_1(),
        "rst_old_dire_2": fig_old_dire_rst_2(),
        "rst_old_dire_3": fig_old_dire_rst_3(),
        "rst_old_dire_4": fig_old_dire_rst_4(),
        "rst_old_dire_5": fig_old_dire_rst_5(),
        "rst_old_dire_6": fig_old_dire_rst_6(),
        "rst_old_daf_1": fig_old_daf_rst_1(),
        "rst_old_daf_2": fig_old_daf_rst_2(),
        "rst_old_daf_3": fig_old_daf_rst_3(),
        "rst_old_daf_4": fig_old_daf_rst_4(),
        "rst_old_daf_5": fig_old_daf_rst_5(),
        "rst_old_daf_6": fig_old_daf_rst_6(),
        "rst_old_drh_1": fig_old_drh_rst_1(),
        "rst_old_drh_2": fig_old_drh_rst_2(),
        "rst_old_drh_3": fig_old_drh_rst_3(),
        "rst_old_drh_4": fig_old_drh_rst_4(),

        "dept_8": fig_dept_8(),
    }
    if value is None:
        value = []
    # Création de la liste des IDs de collapse ouverts
    open_collapse_ids = ["collapse{}".format(val) for val in value]

    # Génération des graphiques et des collapses
    graph_output = []
    for val in value:

        graph_output.append(
            dbc.Collapse(
                dcc.Graph(
                    figure=graphs[val],
                    config={'displaylogo': False}
                ),
                id="collapse{}".format(val),
                is_open=("collapse{}".format(val) in open_collapse_ids),


            )
        )

    new_graph_output = []

    i = 0
    while 2*i < len(graph_output) : 
        if (2*i + 1 < len(graph_output)) :

            graph1 = graph_output[2*i]
            graph2 = graph_output[2*i+1]
            
            new_graph_output.append(
                dbc.Row(children = [
                    dbc.Col(graph1, width = 6),
                    dbc.Col(graph2, width = 6)
                ])
            )
            new_graph_output.append(html.Hr(style={'borderTop': '2px solid #000000'}))  # Ligne horizontale pour mieux séparer les graphes)
        
        else : 
            graph = graph_output[2*i]
            new_graph_output.append(
                dbc.Row(children = [
                    dbc.Col(graph)
                ])
            )
            new_graph_output.append(html.Hr(style={'borderTop': '2px solid #000000'}))  # Ligne horizontale pour mieux séparer les graphes)
        i += 1


    return new_graph_output


"""
    #ARTEMIS
    dbc.Collapse(
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    figure=fig_dept_1(),
                    config={'displaylogo': False}
                ),
                width="auto"
            ),
            dbc.Col(
                dcc.Graph(
                    figure=fig_dept_2(),
                    config={'displaylogo': False}
                ),
                width="auto"
            ),

        ]),

        id="collapse1",
        is_open=False,
    ),

    #CITI
    dbc.Collapse(

                dcc.Graph(
                    figure=fig_dept_3(),
                    config={'displaylogo': False}
                ),

        id="collapse2",
        is_open=False,
    ),

    dbc.Collapse(

                dcc.Graph(
                    figure=fig_dept_4(),
                    config={'displaylogo': False}
                ),

        id="collapse3",
        is_open=False,
    ),

    dbc.Collapse(

                dcc.Graph(
                    figure=fig_dept_5(),
                    config={'displaylogo': False}
                ),

        id="collapse4",
        is_open=False,
    ),

    dbc.Collapse(
                dcc.Graph(
                    figure=fig_dept_6(),
                    config={'displaylogo': False}
                ),

        id="collapse5",
        is_open=False,
    ),
    dbc.Collapse(

                dcc.Graph(
                    figure=fig_dept_7(),
                    config={'displaylogo': False}
                ),

        id="collapse6",
        is_open=False,
    ),

"""



"""

#ARTEMIS
@callback(
    Output("collapse1", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse1", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_1(value, is_open, data):
    if (1 in value and 1 in data) or (1 not in value and 1 not in data) : 
        return is_open
    return not is_open

#CITI
@callback(
    Output("collapse2", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse2", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_2(value, is_open, data):
    if (2 in value and 2 in data) or (2 not in value and 2 not in data) : 
        return is_open
    return not is_open

#EPH
@callback(
    Output("collapse3", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse3", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_3(value, is_open, data):
    if (3 in value and 3 in data) or (3 not in value and 3 not in data) : 
        return is_open
    return not is_open

#INF
@callback(
    Output("collapse4", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse4", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_4(value, is_open, data):
    if (4 in value and 4 in data) or (4 not in value and 4 not in data) : 
        return is_open
    return not is_open

#RS2M
@callback(
    Output("collapse5", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse5", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_5(value, is_open, data):
    if (5 in value and 5 in data) or (5 not in value and 5 not in data) : 
        return is_open
    return not is_open

#RST
@callback(
    Output("collapse6", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse6", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_6(value, is_open, data):
    if (6 in value and 6 in data) or (6 not in value and 6 not in data) : 
        return is_open
    return not is_open

"""

