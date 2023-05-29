

import dash
from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from src.fig import daf_fig, df_fig, dire_fig, drfd_fig, drh_fig, dri_fig, artemis_fig, citi_fig, eph_fig, inf_fig, rs2m_fig, rst_fig
from src import config

import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import numpy as np
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
from src.data.data import dict_titres
from src.functions.fonction_figure import fig_annuelle_baton, fig_camembert, fig_trim_baton, couleurs



annee = config.liste_annee
trimestre = config.trimestre
couleurs_trimestres = config.couleurs_trimestres
couleurs_années = px.colors.qualitative.Plotly
dept_maj = ["ARTEMIS", "CITI", "EPH", "INF", "RS2M", "RST"]
dept_min = ["artemis", "citi", "eph", "inf", "rs2m", "rst"]

titres_y = data.data.titres_y
titres_graphe = data.data.titres_graphe
effectif_dept = data.data.effectif_dept
label = [[str(year) + " - " + tri for tri in trimestre] for year in annee]


#Récupération des données
data_old_global = df_fig.data_old + daf_fig.data_old + dire_fig.data_old + drfd_fig.data_old + drh_fig.data_old
data_old_artemis = artemis_fig.data_old
data_old_citi = citi_fig.data_old
data_old_eph = eph_fig.data_old
data_old_inf = inf_fig.data_old
data_old_rs2m = rs2m_fig.data_old
data_old_rst = rst_fig.data_old



#Initialisation des paramètres
selected_global = data_old_global
selected_artemis = data_old_artemis
selected_citi = data_old_citi
selected_eph = data_old_eph
selected_inf = data_old_inf
selected_rs2m = data_old_rs2m
selected_rst = data_old_rst

selected_annee = annee
selected_label = label


#Catégories du menu déroulant
categories = [
    # DF
    {"label": "DF - " + titres_graphe[0] + ", colorisé par année", "value": "df_old_1_an"},
    {"label": "DF - " + titres_graphe[0] + ", colorisé par trimestre", "value": "df_old_1_tri"},
    {"label": "DF - " + titres_graphe[0] + ", total annuel", "value": "df_old_1_tot"},
    {"label": "DF - " + titres_graphe[0] + ", comparaison annuelle par trimestre", "value": "df_old_1_comp"},

    #DAF
    {"label": "DAF - " + titres_graphe[1] + ", colorisé par année", "value": "daf_old_1_an"},
    {"label": "DAF - " + titres_graphe[1] + ", colorisé par trimestre", "value": "daf_old_1_tri"},
    {"label": "DAF - " + titres_graphe[1] + ", total annuel", "value": "daf_old_1_tot"},
    {"label": "DAF - " + titres_graphe[1] + ", comparaison annuelle par trimestre", "value": "daf_old_1_comp"},
    {"label": "DAF - " + titres_graphe[2] + ", colorisé par année", "value": "daf_old_2_an"},
    {"label": "DAF - " + titres_graphe[2] + ", colorisé par trimestre", "value": "daf_old_2_tri"},
    {"label": "DAF - " + titres_graphe[2] + ", total annuel", "value": "daf_old_2_tot"},
    {"label": "DAF - " + titres_graphe[2] + ", comparaison annuelle par trimestre", "value": "daf_old_2_comp"},
    {"label": "DAF - " + titres_graphe[3] + ", colorisé par année", "value": "daf_old_3_an"},
    {"label": "DAF - " + titres_graphe[3] + ", colorisé par trimestre", "value": "daf_old_3_tri"},
    {"label": "DAF - " + titres_graphe[3] + ", total annuel", "value": "daf_old_3_tot"},
    {"label": "DAF - " + titres_graphe[3] + ", comparaison annuelle par trimestre", "value": "daf_old_3_comp"},

    #DIRE
    {"label": "DIRE - " + titres_graphe[4] + ", colorisé par année", "value": "dire_old_1_an"},
    {"label": "DIRE - " + titres_graphe[4] + ", colorisé par trimestre", "value": "dire_old_1_tri"},
    {"label": "DIRE - " + titres_graphe[4] + ", total annuel", "value": "dire_old_1_tot"},
    {"label": "DIRE - " + titres_graphe[4] + ", comparaison annuelle par trimestre", "value": "dire_old_1_comp"},
    {"label": "DIRE - " + titres_graphe[5] + ", colorisé par année", "value": "dire_old_2_an"},
    {"label": "DIRE - " + titres_graphe[5] + ", colorisé par trimestre", "value": "dire_old_2_tri"},
    {"label": "DIRE - " + titres_graphe[5] + ", total annuel", "value": "dire_old_2_tot"},
    {"label": "DIRE - " + titres_graphe[5] + ", comparaison annuelle par trimestre", "value": "dire_old_2_comp"},
    {"label": "DIRE - " + titres_graphe[6] + ", colorisé par année", "value": "dire_old_3_an"},
    {"label": "DIRE - " + titres_graphe[6] + ", colorisé par trimestre", "value": "dire_old_3_tri"},
    {"label": "DIRE - " + titres_graphe[6] + ", total annuel", "value": "dire_old_3_tot"},
    {"label": "DIRE - " + titres_graphe[6] + ", comparaison annuelle par trimestre", "value": "dire_old_3_comp"},

    #DRFD
    {"label": "DRFD - " + titres_graphe[7] + ", colorisé par année", "value": "drfd_old_1_an"},
    {"label": "DRFD - " + titres_graphe[7] + ", colorisé par trimestre", "value": "drfd_old_1_tri"},
    {"label": "DRFD - " + titres_graphe[7] + ", total annuel", "value": "drfd_old_1_tot"},
    {"label": "DRFD - " + titres_graphe[7] + ", comparaison annuelle par trimestre", "value": "drfd_old_1_comp"},
    {"label": "DRFD - " + titres_graphe[8] + ", colorisé par année", "value": "drfd_old_2_an"},
    {"label": "DRFD - " + titres_graphe[8] + ", colorisé par trimestre", "value": "drfd_old_2_tri"},
    {"label": "DRFD - " + titres_graphe[8] + ", total annuel", "value": "drfd_old_2_tot"},
    {"label": "DRFD - " + titres_graphe[8] + ", comparaison annuelle par trimestre", "value": "drfd_old_2_comp"},

    #DRH
    {"label": "DRH - " + titres_graphe[9] + ", colorisé par année", "value": "drh_old_1_an"},
    {"label": "DRH - " + titres_graphe[9] + ", colorisé par trimestre", "value": "drh_old_1_tri"},
    {"label": "DRH - " + titres_graphe[9] + ", total annuel", "value": "drh_old_1_tot"},
    {"label": "DRH - " + titres_graphe[9] + ", comparaison annuelle par trimestre", "value": "drh_old_1_comp"},
    {"label": "DRH - " + titres_graphe[10] + ", colorisé par année", "value": "drh_old_2_an"},
    {"label": "DRH - " + titres_graphe[10] + ", colorisé par trimestre", "value": "drh_old_2_tri"},
    {"label": "DRH - " + titres_graphe[10] + ", total annuel", "value": "drh_old_2_tot"},
    {"label": "DRH - " + titres_graphe[10] + ", comparaison annuelle par trimestre", "value": "drh_old_2_comp"},


    #ARTEMIS
    {"label": "ARTEMIS - " + titres_graphe[0] + ", colorisé par année", "value": "artemis_old_0_an"},
    {"label": "ARTEMIS - " + titres_graphe[0] + ", colorisé par trimestre", "value": "artemis_old_0_tri"},
    {"label": "ARTEMIS - " + titres_graphe[0] + ", total annuel", "value": "artemis_old_0_tot"},
    {"label": "ARTEMIS - " + titres_graphe[0] + ", comparaison annuelle par trimestre", "value": "artemis_old_0_comp"},
    {"label": "ARTEMIS - " + titres_graphe[1] + ", colorisé par année", "value": "artemis_old_1_an"},
    {"label": "ARTEMIS - " + titres_graphe[1] + ", colorisé par trimestre", "value": "artemis_old_1_tri"},
    {"label": "ARTEMIS - " + titres_graphe[1] + ", total annuel", "value": "artemis_old_1_tot"},
    {"label": "ARTEMIS - " + titres_graphe[1] + ", comparaison annuelle par trimestre", "value": "artemis_old_1_comp"},
    {"label": "ARTEMIS - " + titres_graphe[2] + ", colorisé par année", "value": "artemis_old_2_an"},
    {"label": "ARTEMIS - " + titres_graphe[2] + ", colorisé par trimestre", "value": "artemis_old_2_tri"},
    {"label": "ARTEMIS - " + titres_graphe[2] + ", total annuel", "value": "artemis_old_2_tot"},
    {"label": "ARTEMIS - " + titres_graphe[2] + ", comparaison annuelle par trimestre", "value": "artemis_old_2_comp"},
    {"label": "ARTEMIS - " + titres_graphe[3] + ", colorisé par année", "value": "artemis_old_3_an"},
    {"label": "ARTEMIS - " + titres_graphe[3] + ", colorisé par trimestre", "value": "artemis_old_3_tri"},
    {"label": "ARTEMIS - " + titres_graphe[3] + ", total annuel", "value": "artemis_old_3_tot"},
    {"label": "ARTEMIS - " + titres_graphe[3] + ", comparaison annuelle par trimestre", "value": "artemis_old_3_comp"},
    {"label": "ARTEMIS - " + titres_graphe[4] + ", colorisé par année", "value": "artemis_old_4_an"},
    {"label": "ARTEMIS - " + titres_graphe[4] + ", colorisé par trimestre", "value": "artemis_old_4_tri"},
    {"label": "ARTEMIS - " + titres_graphe[4] + ", total annuel", "value": "artemis_old_4_tot"},
    {"label": "ARTEMIS - " + titres_graphe[4] + ", comparaison annuelle par trimestre", "value": "artemis_old_4_comp"},
    {"label": "ARTEMIS - " + titres_graphe[5] + ", colorisé par année", "value": "artemis_old_5_an"},
    {"label": "ARTEMIS - " + titres_graphe[5] + ", colorisé par trimestre", "value": "artemis_old_5_tri"},
    {"label": "ARTEMIS - " + titres_graphe[5] + ", total annuel", "value": "artemis_old_5_tot"},
    {"label": "ARTEMIS - " + titres_graphe[5] + ", comparaison annuelle par trimestre", "value": "artemis_old_5_comp"},
    {"label": "ARTEMIS - " + titres_graphe[6] + ", colorisé par année", "value": "artemis_old_6_an"},
    {"label": "ARTEMIS - " + titres_graphe[6] + ", colorisé par trimestre", "value": "artemis_old_6_tri"},
    {"label": "ARTEMIS - " + titres_graphe[6] + ", total annuel", "value": "artemis_old_6_tot"},
    {"label": "ARTEMIS - " + titres_graphe[6] + ", comparaison annuelle par trimestre", "value": "artemis_old_6_comp"},
    {"label": "ARTEMIS - " + titres_graphe[7] + ", colorisé par année", "value": "artemis_old_7_an"},
    {"label": "ARTEMIS - " + titres_graphe[7] + ", colorisé par trimestre", "value": "artemis_old_7_tri"},
    {"label": "ARTEMIS - " + titres_graphe[7] + ", total annuel", "value": "artemis_old_7_tot"},
    {"label": "ARTEMIS - " + titres_graphe[7] + ", comparaison annuelle par trimestre", "value": "artemis_old_7_comp"},
    {"label": "ARTEMIS - " + titres_graphe[8] + ", colorisé par année", "value": "artemis_old_8_an"},
    {"label": "ARTEMIS - " + titres_graphe[8] + ", colorisé par trimestre", "value": "artemis_old_8_tri"},
    {"label": "ARTEMIS - " + titres_graphe[8] + ", total annuel", "value": "artemis_old_8_tot"},
    {"label": "ARTEMIS - " + titres_graphe[8] + ", comparaison annuelle par trimestre", "value": "artemis_old_8_comp"},
    {"label": "ARTEMIS - " + titres_graphe[9] + ", colorisé par année", "value": "artemis_old_9_an"},
    {"label": "ARTEMIS - " + titres_graphe[9] + ", colorisé par trimestre", "value": "artemis_old_9_tri"},
    {"label": "ARTEMIS - " + titres_graphe[9] + ", total annuel", "value": "artemis_old_9_tot"},
    {"label": "ARTEMIS - " + titres_graphe[9] + ", comparaison annuelle par trimestre", "value": "artemis_old_9_comp"},
    {"label": "ARTEMIS - " + titres_graphe[10] + ", colorisé par année", "value": "artemis_old_10_an"},
    {"label": "ARTEMIS - " + titres_graphe[10] + ", colorisé par trimestre", "value": "artemis_old_10_tri"},
    {"label": "ARTEMIS - " + titres_graphe[10] + ", total annuel", "value": "artemis_old_10_tot"},
    {"label": "ARTEMIS - " + titres_graphe[10] + ", comparaison annuelle par trimestre", "value": "artemis_old_10_comp"},

    #CITI
    {"label": "CITI - " + titres_graphe[0] + ", colorisé par année", "value": "citi_old_0_an"},
    {"label": "CITI - " + titres_graphe[0] + ", colorisé par trimestre", "value": "citi_old_0_tri"},
    {"label": "CITI - " + titres_graphe[0] + ", total annuel", "value": "citi_old_0_tot"},
    {"label": "CITI - " + titres_graphe[0] + ", comparaison annuelle par trimestre", "value": "citi_old_0_comp"},
    {"label": "CITI - " + titres_graphe[1] + ", colorisé par année", "value": "citi_old_1_an"},
    {"label": "CITI - " + titres_graphe[1] + ", colorisé par trimestre", "value": "citi_old_1_tri"},
    {"label": "CITI - " + titres_graphe[1] + ", total annuel", "value": "citi_old_1_tot"},
    {"label": "CITI - " + titres_graphe[1] + ", comparaison annuelle par trimestre", "value": "citi_old_1_comp"},
    {"label": "CITI - " + titres_graphe[2] + ", colorisé par année", "value": "citi_old_2_an"},
    {"label": "CITI - " + titres_graphe[2] + ", colorisé par trimestre", "value": "citi_old_2_tri"},
    {"label": "CITI - " + titres_graphe[2] + ", total annuel", "value": "citi_old_2_tot"},
    {"label": "CITI - " + titres_graphe[2] + ", comparaison annuelle par trimestre", "value": "citi_old_2_comp"},
    {"label": "CITI - " + titres_graphe[3] + ", colorisé par année", "value": "citi_old_3_an"},
    {"label": "CITI - " + titres_graphe[3] + ", colorisé par trimestre", "value": "citi_old_3_tri"},
    {"label": "CITI - " + titres_graphe[3] + ", total annuel", "value": "citi_old_3_tot"},
    {"label": "CITI - " + titres_graphe[3] + ", comparaison annuelle par trimestre", "value": "citi_old_3_comp"},
    {"label": "CITI - " + titres_graphe[4] + ", colorisé par année", "value": "citi_old_4_an"},
    {"label": "CITI - " + titres_graphe[4] + ", colorisé par trimestre", "value": "citi_old_4_tri"},
    {"label": "CITI - " + titres_graphe[4] + ", total annuel", "value": "citi_old_4_tot"},
    {"label": "CITI - " + titres_graphe[4] + ", comparaison annuelle par trimestre", "value": "citi_old_4_comp"},
    {"label": "CITI - " + titres_graphe[5] + ", colorisé par année", "value": "citi_old_5_an"},
    {"label": "CITI - " + titres_graphe[5] + ", colorisé par trimestre", "value": "citi_old_5_tri"},
    {"label": "CITI - " + titres_graphe[5] + ", total annuel", "value": "citi_old_5_tot"},
    {"label": "CITI - " + titres_graphe[5] + ", comparaison annuelle par trimestre", "value": "citi_old_5_comp"},
    {"label": "CITI - " + titres_graphe[6] + ", colorisé par année", "value": "citi_old_6_an"},
    {"label": "CITI - " + titres_graphe[6] + ", colorisé par trimestre", "value": "citi_old_6_tri"},
    {"label": "CITI - " + titres_graphe[6] + ", total annuel", "value": "citi_old_6_tot"},
    {"label": "CITI - " + titres_graphe[6] + ", comparaison annuelle par trimestre", "value": "citi_old_6_comp"},
    {"label": "CITI - " + titres_graphe[7] + ", colorisé par année", "value": "citi_old_7_an"},
    {"label": "CITI - " + titres_graphe[7] + ", colorisé par trimestre", "value": "citi_old_7_tri"},
    {"label": "CITI - " + titres_graphe[7] + ", total annuel", "value": "citi_old_7_tot"},
    {"label": "CITI - " + titres_graphe[7] + ", comparaison annuelle par trimestre", "value": "citi_old_7_comp"},
    {"label": "CITI - " + titres_graphe[8] + ", colorisé par année", "value": "citi_old_8_an"},
    {"label": "CITI - " + titres_graphe[8] + ", colorisé par trimestre", "value": "citi_old_8_tri"},
    {"label": "CITI - " + titres_graphe[8] + ", total annuel", "value": "citi_old_8_tot"},
    {"label": "CITI - " + titres_graphe[8] + ", comparaison annuelle par trimestre", "value": "citi_old_8_comp"},
    {"label": "CITI - " + titres_graphe[9] + ", colorisé par année", "value": "citi_old_9_an"},
    {"label": "CITI - " + titres_graphe[9] + ", colorisé par trimestre", "value": "citi_old_9_tri"},
    {"label": "CITI - " + titres_graphe[9] + ", total annuel", "value": "citi_old_9_tot"},
    {"label": "CITI - " + titres_graphe[9] + ", comparaison annuelle par trimestre", "value": "citi_old_9_comp"},
    {"label": "CITI - " + titres_graphe[10] + ", colorisé par année", "value": "citi_old_10_an"},
    {"label": "CITI - " + titres_graphe[10] + ", colorisé par trimestre", "value": "citi_old_10_tri"},
    {"label": "CITI - " + titres_graphe[10] + ", total annuel", "value": "citi_old_10_tot"},
    {"label": "CITI - " + titres_graphe[10] + ", comparaison annuelle par trimestre", "value": "citi_old_10_comp"},

    #EPH
    {"label": "EPH - " + titres_graphe[0] + ", colorisé par année", "value": "eph_old_0_an"},
    {"label": "EPH - " + titres_graphe[0] + ", colorisé par trimestre", "value": "eph_old_0_tri"},
    {"label": "EPH - " + titres_graphe[0] + ", total annuel", "value": "eph_old_0_tot"},
    {"label": "EPH - " + titres_graphe[0] + ", comparaison annuelle par trimestre", "value": "eph_old_0_comp"},
    {"label": "EPH - " + titres_graphe[1] + ", colorisé par année", "value": "eph_old_1_an"},
    {"label": "EPH - " + titres_graphe[1] + ", colorisé par trimestre", "value": "eph_old_1_tri"},
    {"label": "EPH - " + titres_graphe[1] + ", total annuel", "value": "eph_old_1_tot"},
    {"label": "EPH - " + titres_graphe[1] + ", comparaison annuelle par trimestre", "value": "eph_old_1_comp"},
    {"label": "EPH - " + titres_graphe[2] + ", colorisé par année", "value": "eph_old_2_an"},
    {"label": "EPH - " + titres_graphe[2] + ", colorisé par trimestre", "value": "eph_old_2_tri"},
    {"label": "EPH - " + titres_graphe[2] + ", total annuel", "value": "eph_old_2_tot"},
    {"label": "EPH - " + titres_graphe[2] + ", comparaison annuelle par trimestre", "value": "eph_old_2_comp"},
    {"label": "EPH - " + titres_graphe[3] + ", colorisé par année", "value": "eph_old_3_an"},
    {"label": "EPH - " + titres_graphe[3] + ", colorisé par trimestre", "value": "eph_old_3_tri"},
    {"label": "EPH - " + titres_graphe[3] + ", total annuel", "value": "eph_old_3_tot"},
    {"label": "EPH - " + titres_graphe[3] + ", comparaison annuelle par trimestre", "value": "eph_old_3_comp"},
    {"label": "EPH - " + titres_graphe[4] + ", colorisé par année", "value": "eph_old_4_an"},
    {"label": "EPH - " + titres_graphe[4] + ", colorisé par trimestre", "value": "eph_old_4_tri"},
    {"label": "EPH - " + titres_graphe[4] + ", total annuel", "value": "eph_old_4_tot"},
    {"label": "EPH - " + titres_graphe[4] + ", comparaison annuelle par trimestre", "value": "eph_old_4_comp"},
    {"label": "EPH - " + titres_graphe[5] + ", colorisé par année", "value": "eph_old_5_an"},
    {"label": "EPH - " + titres_graphe[5] + ", colorisé par trimestre", "value": "eph_old_5_tri"},
    {"label": "EPH - " + titres_graphe[5] + ", total annuel", "value": "eph_old_5_tot"},
    {"label": "EPH - " + titres_graphe[5] + ", comparaison annuelle par trimestre", "value": "eph_old_5_comp"},
    {"label": "EPH - " + titres_graphe[6] + ", colorisé par année", "value": "eph_old_6_an"},
    {"label": "EPH - " + titres_graphe[6] + ", colorisé par trimestre", "value": "eph_old_6_tri"},
    {"label": "EPH - " + titres_graphe[6] + ", total annuel", "value": "eph_old_6_tot"},
    {"label": "EPH - " + titres_graphe[6] + ", comparaison annuelle par trimestre", "value": "eph_old_6_comp"},
    {"label": "EPH - " + titres_graphe[7] + ", colorisé par année", "value": "eph_old_7_an"},
    {"label": "EPH - " + titres_graphe[7] + ", colorisé par trimestre", "value": "eph_old_7_tri"},
    {"label": "EPH - " + titres_graphe[7] + ", total annuel", "value": "eph_old_7_tot"},
    {"label": "EPH - " + titres_graphe[7] + ", comparaison annuelle par trimestre", "value": "eph_old_7_comp"},
    {"label": "EPH - " + titres_graphe[8] + ", colorisé par année", "value": "eph_old_8_an"},
    {"label": "EPH - " + titres_graphe[8] + ", colorisé par trimestre", "value": "eph_old_8_tri"},
    {"label": "EPH - " + titres_graphe[8] + ", total annuel", "value": "eph_old_8_tot"},
    {"label": "EPH - " + titres_graphe[8] + ", comparaison annuelle par trimestre", "value": "eph_old_8_comp"},
    {"label": "EPH - " + titres_graphe[9] + ", colorisé par année", "value": "eph_old_9_an"},
    {"label": "EPH - " + titres_graphe[9] + ", colorisé par trimestre", "value": "eph_old_9_tri"},
    {"label": "EPH - " + titres_graphe[9] + ", total annuel", "value": "eph_old_9_tot"},
    {"label": "EPH - " + titres_graphe[9] + ", comparaison annuelle par trimestre", "value": "eph_old_9_comp"},
    {"label": "EPH - " + titres_graphe[10] + ", colorisé par année", "value": "eph_old_10_an"},
    {"label": "EPH - " + titres_graphe[10] + ", colorisé par trimestre", "value": "eph_old_10_tri"},
    {"label": "EPH - " + titres_graphe[10] + ", total annuel", "value": "eph_old_10_tot"},
    {"label": "EPH - " + titres_graphe[10] + ", comparaison annuelle par trimestre", "value": "eph_old_10_comp"},

    #INF
    {"label": "INF - " + titres_graphe[0] + ", colorisé par année", "value": "inf_old_0_an"},
    {"label": "INF - " + titres_graphe[0] + ", colorisé par trimestre", "value": "inf_old_0_tri"},
    {"label": "INF - " + titres_graphe[0] + ", total annuel", "value": "inf_old_0_tot"},
    {"label": "INF - " + titres_graphe[0] + ", comparaison annuelle par trimestre", "value": "inf_old_0_comp"},
    {"label": "INF - " + titres_graphe[1] + ", colorisé par année", "value": "inf_old_1_an"},
    {"label": "INF - " + titres_graphe[1] + ", colorisé par trimestre", "value": "inf_old_1_tri"},
    {"label": "INF - " + titres_graphe[1] + ", total annuel", "value": "inf_old_1_tot"},
    {"label": "INF - " + titres_graphe[1] + ", comparaison annuelle par trimestre", "value": "inf_old_1_comp"},
    {"label": "INF - " + titres_graphe[2] + ", colorisé par année", "value": "inf_old_2_an"},
    {"label": "INF - " + titres_graphe[2] + ", colorisé par trimestre", "value": "inf_old_2_tri"},
    {"label": "INF - " + titres_graphe[2] + ", total annuel", "value": "inf_old_2_tot"},
    {"label": "INF - " + titres_graphe[2] + ", comparaison annuelle par trimestre", "value": "inf_old_2_comp"},
    {"label": "INF - " + titres_graphe[3] + ", colorisé par année", "value": "inf_old_3_an"},
    {"label": "INF - " + titres_graphe[3] + ", colorisé par trimestre", "value": "inf_old_3_tri"},
    {"label": "INF - " + titres_graphe[3] + ", total annuel", "value": "inf_old_3_tot"},
    {"label": "INF - " + titres_graphe[3] + ", comparaison annuelle par trimestre", "value": "inf_old_3_comp"},
    {"label": "INF - " + titres_graphe[4] + ", colorisé par année", "value": "inf_old_4_an"},
    {"label": "INF - " + titres_graphe[4] + ", colorisé par trimestre", "value": "inf_old_4_tri"},
    {"label": "INF - " + titres_graphe[4] + ", total annuel", "value": "inf_old_4_tot"},
    {"label": "INF - " + titres_graphe[4] + ", comparaison annuelle par trimestre", "value": "inf_old_4_comp"},
    {"label": "INF - " + titres_graphe[5] + ", colorisé par année", "value": "inf_old_5_an"},
    {"label": "INF - " + titres_graphe[5] + ", colorisé par trimestre", "value": "inf_old_5_tri"},
    {"label": "INF - " + titres_graphe[5] + ", total annuel", "value": "inf_old_5_tot"},
    {"label": "INF - " + titres_graphe[5] + ", comparaison annuelle par trimestre", "value": "inf_old_5_comp"},
    {"label": "INF - " + titres_graphe[6] + ", colorisé par année", "value": "inf_old_6_an"},
    {"label": "INF - " + titres_graphe[6] + ", colorisé par trimestre", "value": "inf_old_6_tri"},
    {"label": "INF - " + titres_graphe[6] + ", total annuel", "value": "inf_old_6_tot"},
    {"label": "INF - " + titres_graphe[6] + ", comparaison annuelle par trimestre", "value": "inf_old_6_comp"},
    {"label": "INF - " + titres_graphe[7] + ", colorisé par année", "value": "inf_old_7_an"},
    {"label": "INF - " + titres_graphe[7] + ", colorisé par trimestre", "value": "inf_old_7_tri"},
    {"label": "INF - " + titres_graphe[7] + ", total annuel", "value": "inf_old_7_tot"},
    {"label": "INF - " + titres_graphe[7] + ", comparaison annuelle par trimestre", "value": "inf_old_7_comp"},
    {"label": "INF - " + titres_graphe[8] + ", colorisé par année", "value": "inf_old_8_an"},
    {"label": "INF - " + titres_graphe[8] + ", colorisé par trimestre", "value": "inf_old_8_tri"},
    {"label": "INF - " + titres_graphe[8] + ", total annuel", "value": "inf_old_8_tot"},
    {"label": "INF - " + titres_graphe[8] + ", comparaison annuelle par trimestre", "value": "inf_old_8_comp"},
    {"label": "INF - " + titres_graphe[9] + ", colorisé par année", "value": "inf_old_9_an"},
    {"label": "INF - " + titres_graphe[9] + ", colorisé par trimestre", "value": "inf_old_9_tri"},
    {"label": "INF - " + titres_graphe[9] + ", total annuel", "value": "inf_old_9_tot"},
    {"label": "INF - " + titres_graphe[9] + ", comparaison annuelle par trimestre", "value": "inf_old_9_comp"},
    {"label": "INF - " + titres_graphe[10] + ", colorisé par année", "value": "inf_old_10_an"},
    {"label": "INF - " + titres_graphe[10] + ", colorisé par trimestre", "value": "inf_old_10_tri"},
    {"label": "INF - " + titres_graphe[10] + ", total annuel", "value": "inf_old_10_tot"},
    {"label": "INF - " + titres_graphe[10] + ", comparaison annuelle par trimestre", "value": "inf_old_10_comp"},

    #RS2M
    {"label": "RS2M - " + titres_graphe[0] + ", colorisé par année", "value": "rs2m_old_0_an"},
    {"label": "RS2M - " + titres_graphe[0] + ", colorisé par trimestre", "value": "rs2m_old_0_tri"},
    {"label": "RS2M - " + titres_graphe[0] + ", total annuel", "value": "rs2m_old_0_tot"},
    {"label": "RS2M - " + titres_graphe[0] + ", comparaison annuelle par trimestre", "value": "rs2m_old_0_comp"},
    {"label": "RS2M - " + titres_graphe[1] + ", colorisé par année", "value": "rs2m_old_1_an"},
    {"label": "RS2M - " + titres_graphe[1] + ", colorisé par trimestre", "value": "rs2m_old_1_tri"},
    {"label": "RS2M - " + titres_graphe[1] + ", total annuel", "value": "rs2m_old_1_tot"},
    {"label": "RS2M - " + titres_graphe[1] + ", comparaison annuelle par trimestre", "value": "rs2m_old_1_comp"},
    {"label": "RS2M - " + titres_graphe[2] + ", colorisé par année", "value": "rs2m_old_2_an"},
    {"label": "RS2M - " + titres_graphe[2] + ", colorisé par trimestre", "value": "rs2m_old_2_tri"},
    {"label": "RS2M - " + titres_graphe[2] + ", total annuel", "value": "rs2m_old_2_tot"},
    {"label": "RS2M - " + titres_graphe[2] + ", comparaison annuelle par trimestre", "value": "rs2m_old_2_comp"},
    {"label": "RS2M - " + titres_graphe[3] + ", colorisé par année", "value": "rs2m_old_3_an"},
    {"label": "RS2M - " + titres_graphe[3] + ", colorisé par trimestre", "value": "rs2m_old_3_tri"},
    {"label": "RS2M - " + titres_graphe[3] + ", total annuel", "value": "rs2m_old_3_tot"},
    {"label": "RS2M - " + titres_graphe[3] + ", comparaison annuelle par trimestre", "value": "rs2m_old_3_comp"},
    {"label": "RS2M - " + titres_graphe[4] + ", colorisé par année", "value": "rs2m_old_4_an"},
    {"label": "RS2M - " + titres_graphe[4] + ", colorisé par trimestre", "value": "rs2m_old_4_tri"},
    {"label": "RS2M - " + titres_graphe[4] + ", total annuel", "value": "rs2m_old_4_tot"},
    {"label": "RS2M - " + titres_graphe[4] + ", comparaison annuelle par trimestre", "value": "rs2m_old_4_comp"},
    {"label": "RS2M - " + titres_graphe[5] + ", colorisé par année", "value": "rs2m_old_5_an"},
    {"label": "RS2M - " + titres_graphe[5] + ", colorisé par trimestre", "value": "rs2m_old_5_tri"},
    {"label": "RS2M - " + titres_graphe[5] + ", total annuel", "value": "rs2m_old_5_tot"},
    {"label": "RS2M - " + titres_graphe[5] + ", comparaison annuelle par trimestre", "value": "rs2m_old_5_comp"},
    {"label": "RS2M - " + titres_graphe[6] + ", colorisé par année", "value": "rs2m_old_6_an"},
    {"label": "RS2M - " + titres_graphe[6] + ", colorisé par trimestre", "value": "rs2m_old_6_tri"},
    {"label": "RS2M - " + titres_graphe[6] + ", total annuel", "value": "rs2m_old_6_tot"},
    {"label": "RS2M - " + titres_graphe[6] + ", comparaison annuelle par trimestre", "value": "rs2m_old_6_comp"},
    {"label": "RS2M - " + titres_graphe[7] + ", colorisé par année", "value": "rs2m_old_7_an"},
    {"label": "RS2M - " + titres_graphe[7] + ", colorisé par trimestre", "value": "rs2m_old_7_tri"},
    {"label": "RS2M - " + titres_graphe[7] + ", total annuel", "value": "rs2m_old_7_tot"},
    {"label": "RS2M - " + titres_graphe[7] + ", comparaison annuelle par trimestre", "value": "rs2m_old_7_comp"},
    {"label": "RS2M - " + titres_graphe[8] + ", colorisé par année", "value": "rs2m_old_8_an"},
    {"label": "RS2M - " + titres_graphe[8] + ", colorisé par trimestre", "value": "rs2m_old_8_tri"},
    {"label": "RS2M - " + titres_graphe[8] + ", total annuel", "value": "rs2m_old_8_tot"},
    {"label": "RS2M - " + titres_graphe[8] + ", comparaison annuelle par trimestre", "value": "rs2m_old_8_comp"},
    {"label": "RS2M - " + titres_graphe[9] + ", colorisé par année", "value": "rs2m_old_9_an"},
    {"label": "RS2M - " + titres_graphe[9] + ", colorisé par trimestre", "value": "rs2m_old_9_tri"},
    {"label": "RS2M - " + titres_graphe[9] + ", total annuel", "value": "rs2m_old_9_tot"},
    {"label": "RS2M - " + titres_graphe[9] + ", comparaison annuelle par trimestre", "value": "rs2m_old_9_comp"},
    {"label": "RS2M - " + titres_graphe[10] + ", colorisé par année", "value": "rs2m_old_10_an"},
    {"label": "RS2M - " + titres_graphe[10] + ", colorisé par trimestre", "value": "rs2m_old_10_tri"},
    {"label": "RS2M - " + titres_graphe[10] + ", total annuel", "value": "rs2m_old_10_tot"},
    {"label": "RS2M - " + titres_graphe[10] + ", comparaison annuelle par trimestre", "value": "rs2m_old_10_comp"},

    #RST
    {"label": "RST - " + titres_graphe[0] + ", colorisé par année", "value": "rst_old_0_an"},
    {"label": "RST - " + titres_graphe[0] + ", colorisé par trimestre", "value": "rst_old_0_tri"},
    {"label": "RST - " + titres_graphe[0] + ", total annuel", "value": "rst_old_0_tot"},
    {"label": "RST - " + titres_graphe[0] + ", comparaison annuelle par trimestre", "value": "rst_old_0_comp"},
    {"label": "RST - " + titres_graphe[1] + ", colorisé par année", "value": "rst_old_1_an"},
    {"label": "RST - " + titres_graphe[1] + ", colorisé par trimestre", "value": "rst_old_1_tri"},
    {"label": "RST - " + titres_graphe[1] + ", total annuel", "value": "rst_old_1_tot"},
    {"label": "RST - " + titres_graphe[1] + ", comparaison annuelle par trimestre", "value": "rst_old_1_comp"},
    {"label": "RST - " + titres_graphe[2] + ", colorisé par année", "value": "rst_old_2_an"},
    {"label": "RST - " + titres_graphe[2] + ", colorisé par trimestre", "value": "rst_old_2_tri"},
    {"label": "RST - " + titres_graphe[2] + ", total annuel", "value": "rst_old_2_tot"},
    {"label": "RST - " + titres_graphe[2] + ", comparaison annuelle par trimestre", "value": "rst_old_2_comp"},
    {"label": "RST - " + titres_graphe[3] + ", colorisé par année", "value": "rst_old_3_an"},
    {"label": "RST - " + titres_graphe[3] + ", colorisé par trimestre", "value": "rst_old_3_tri"},
    {"label": "RST - " + titres_graphe[3] + ", total annuel", "value": "rst_old_3_tot"},
    {"label": "RST - " + titres_graphe[3] + ", comparaison annuelle par trimestre", "value": "rst_old_3_comp"},
    {"label": "RST - " + titres_graphe[4] + ", colorisé par année", "value": "rst_old_4_an"},
    {"label": "RST - " + titres_graphe[4] + ", colorisé par trimestre", "value": "rst_old_4_tri"},
    {"label": "RST - " + titres_graphe[4] + ", total annuel", "value": "rst_old_4_tot"},
    {"label": "RST - " + titres_graphe[4] + ", comparaison annuelle par trimestre", "value": "rst_old_4_comp"},
    {"label": "RST - " + titres_graphe[5] + ", colorisé par année", "value": "rst_old_5_an"},
    {"label": "RST - " + titres_graphe[5] + ", colorisé par trimestre", "value": "rst_old_5_tri"},
    {"label": "RST - " + titres_graphe[5] + ", total annuel", "value": "rst_old_5_tot"},
    {"label": "RST - " + titres_graphe[5] + ", comparaison annuelle par trimestre", "value": "rst_old_5_comp"},
    {"label": "RST - " + titres_graphe[6] + ", colorisé par année", "value": "rst_old_6_an"},
    {"label": "RST - " + titres_graphe[6] + ", colorisé par trimestre", "value": "rst_old_6_tri"},
    {"label": "RST - " + titres_graphe[6] + ", total annuel", "value": "rst_old_6_tot"},
    {"label": "RST - " + titres_graphe[6] + ", comparaison annuelle par trimestre", "value": "rst_old_6_comp"},
    {"label": "RST - " + titres_graphe[7] + ", colorisé par année", "value": "rst_old_7_an"},
    {"label": "RST - " + titres_graphe[7] + ", colorisé par trimestre", "value": "rst_old_7_tri"},
    {"label": "RST - " + titres_graphe[7] + ", total annuel", "value": "rst_old_7_tot"},
    {"label": "RST - " + titres_graphe[7] + ", comparaison annuelle par trimestre", "value": "rst_old_7_comp"},
    {"label": "RST - " + titres_graphe[8] + ", colorisé par année", "value": "rst_old_8_an"},
    {"label": "RST - " + titres_graphe[8] + ", colorisé par trimestre", "value": "rst_old_8_tri"},
    {"label": "RST - " + titres_graphe[8] + ", total annuel", "value": "rst_old_8_tot"},
    {"label": "RST - " + titres_graphe[8] + ", comparaison annuelle par trimestre", "value": "rst_old_8_comp"},
    {"label": "RST - " + titres_graphe[9] + ", colorisé par année", "value": "rst_old_9_an"},
    {"label": "RST - " + titres_graphe[9] + ", colorisé par trimestre", "value": "rst_old_9_tri"},
    {"label": "RST - " + titres_graphe[9] + ", total annuel", "value": "rst_old_9_tot"},
    {"label": "RST - " + titres_graphe[9] + ", comparaison annuelle par trimestre", "value": "rst_old_9_comp"},
    {"label": "RST - " + titres_graphe[10] + ", colorisé par année", "value": "rst_old_10_an"},
    {"label": "RST - " + titres_graphe[10] + ", colorisé par trimestre", "value": "rst_old_10_tri"},
    {"label": "RST - " + titres_graphe[10] + ", total annuel", "value": "rst_old_10_tot"},
    {"label": "RST - " + titres_graphe[10] + ", comparaison annuelle par trimestre", "value": "rst_old_10_comp"},



    #Fusion avec "categories" de "Choix libre"
    # DF
    {"label": "DF - Nombre d\'étudiants", "value": "df_1"},
    {"label": "DF - Nombre d\'UP", "value": "df_2"},

    


    # DRFD
    {"label": "DRFD - Publications", "value": "drfd_1"},
    {"label": "DRFD - Nombre de doctorants", "value": "drfd_2"},
    {"label": "DRFD - Evolutions des publications", "value": "drfd_3"},
    {"label": "DRFD - Evolution du nombre de doctorants", "value": "drfd_4"},

    # DIRE
    {"label": "DIRE - Suivi des contrats de recherches", "value": "dire_1"},
    {"label": "DIRE - Suivi des contrats de recherches, vision trimestrielle", "value": "dire_2"},
    {"label": "DIRE - Suivi des contrats de recherches, total école", "value": "dire_3"},
    {"label": "DIRE - Contribution au financement de l'école, graphe camembert", "value": "dire_4"},


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

    # DRH
    {"label": "DRH - Nombre de permanents", "value": "drh_1"},
    {"label": "DRH - Répartition des permanents, vision trimestrielle", "value": "drh_2"},
    {"label": "DRH - Nombre de non-permanents", "value": "drh_3"},
    {"label": "DRH - Evolution du nombre de non-permanents", "value": "drh_4"},


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

    #CITI
    {"label": "CITI - Graphe radar année 2023", "value": "dept_3"},
    {"label": "CITI - Ressources humaines", "value": "citi_1"},
    {"label": "CITI - Contrats de recherche", "value": "citi_2"},
    {"label": "CITI - Contribution au financement de l\'école", "value": "citi_3"},
    {"label": "CITI - Dépense de vacataires", "value": "citi_4"},
    {"label": "CITI - Ressources propres", "value": "citi_5"},
    {"label": "CITI - Ressources d\'états", "value": "citi_6"},
    {"label": "CITI - Total des dépenses", "value": "citi_7"},



    #EPH
    {"label": "EPH - Graphe radar année 2023", "value": "dept_4"},
    {"label": "EPH - Ressources humaines", "value": "eph_1"},
    {"label": "EPH - Contrats de recherche", "value": "eph_2"},
    {"label": "EPH - Contribution au financement de l\'école", "value": "eph_3"},
    {"label": "EPH - Dépense de vacataires", "value": "eph_4"},
    {"label": "EPH - Ressources propres", "value": "eph_5"},
    {"label": "EPH - Ressources d\'états", "value": "eph_6"},


    #INF
    {"label": "INF - Graphe radar année 2023", "value": "dept_5"},
    {"label": "INF - Ressources humaines", "value": "inf_1"},
    {"label": "INF - Contrats de recherche", "value": "inf_2"},
    {"label": "INF - Contribution au financement de l\'école", "value": "inf_3"},
    {"label": "INF - Dépense de vacataires", "value": "inf_4"},
    {"label": "INF - Ressources propres", "value": "inf_5"},
    {"label": "INF - Ressources d\'états", "value": "inf_6"},
    {"label": "INF - Total des dépenses", "value": "inf_7"},


    #RS2M
    {"label": "RS2M - Graphe radar année 2023", "value": "dept_6"},
    {"label": "RS2M - Ressources humaines", "value": "rs2m_1"},
    {"label": "RS2M - Contrats de recherche", "value": "rs2m_2"},
    {"label": "RS2M - Contribution au financement de l\'école", "value": "rs2m_3"},
    {"label": "RS2M - Dépense de vacataires", "value": "rs2m_4"},
    {"label": "RS2M - Ressources propres", "value": "rs2m_5"},
    {"label": "RS2M - Ressources d\'états", "value": "rs2m_6"},
    {"label": "RS2M - Total des dépenses", "value": "rs2m_7"},





    #RST
    {"label": "RST - Graphe radar année 2023", "value": "dept_7"},
    {"label": "RST - Ressources humaines", "value": "rst_1"},
    {"label": "RST - Contrats de recherche", "value": "rst_2"},
    {"label": "RST - Contribution au financement de l\'école", "value": "rst_3"},
    {"label": "RST - Dépense de vacataires", "value": "rst_4"},
    {"label": "RST - Ressources propres", "value": "rst_5"},
    {"label": "RST - Ressources d\'états", "value": "rst_6"},
    {"label": "RST - Total des dépenses", "value": "rst_7"},

    {"label": "Graphes radar des départements", "value": "dept_8"},

]





def fig_old_annuelle_baton(donnees, years, labels, titre_graphe, titre_y):
    
    Y=[]
    for i, year in enumerate(years):
        Y.append(
            go.Bar(
                x=labels[i],
                y=donnees[i],
                name=str(year),
                width=0.8,
                marker=dict(color=couleurs_années[i])
            )
        )


    fig = go.Figure(data=Y)

    fig.update_traces(hovertemplate="<br>".join([
        "Trimestre : %{x}",
        "Total : <b>%{y:.0f}</b>",
                      ])
                    )

    # Ajout d'un titre
    if years[0] != years[-1] :
        titre_fig = titre_graphe + " de " + str(years[0]) + " à " + str(years[-1]) + ",<br>colorisé par année"
    else : 
        titre_fig = titre_graphe + " en " + str(years[0]) + ",<br>colorisé par année"


    fig.update_layout(title=titre_fig,
                      xaxis_title="Temps",
                      yaxis_title=titre_y)
    return fig

def fig_old_trimestrielle(donnees, years, labels, titre_graphe, titre_y):
    Y = []
    for i, year in enumerate(years):
        Y.append(
            go.Bar(
                x=labels[i],
                y=donnees[i],
                name=str(year),
                marker=dict(color=couleurs_trimestres),
                width=0.8,
            )
        )
    fig = go.Figure(data=Y)

    fig.update_traces(hovertemplate="<br>".join([
        "Trimestre : %{x}",
        "Total : <b>%{y:.0f}</b>",
                      ])
                    )

    # Ajout d'un titre
    if years[0] != years[-1] :
        titre_fig = titre_graphe + " de " + str(years[0]) + " à " + str(years[-1]) + ",<br>colorisé par trimestre"
    else : 
        titre_fig = titre_graphe + " en " + str(years[0]) + ",<br>colorisé par trimestre"

    fig.update_layout(title=titre_fig,
                      xaxis_title="Temps",
                      yaxis_title=titre_y)


    return fig

def fig_old_total(donnees, years, titre_graphe, titre_y):


    x = []
    y = []
    for i, year in enumerate(years):
        x.append(str(year))
        y.append(sum(donnees[i]))
    


    if years[0] != years[-1] :
        titre_fig = titre_graphe + " de " + str(years[0]) + " à " + str(years[-1]) + ",<br>total annuel"
        fig = px.bar(x=x, y=y, color=y, color_continuous_scale="Tealgrn")
        fig.update_traces(hovertemplate="<br>".join([
            "Année : %{x}",
            "Total : <b>%{y:.0f}</b>",
                        ]))
    else : 
        fig = go.Figure(go.Indicator(
        mode = "number",
        value = y[0]))

        
        titre_fig = titre_graphe + " en " + str(years[0]) + ",<br>total annuel"

    # Ajout d'un titre


    fig.update_layout(title=titre_fig,
                      xaxis_title="Années",
                      yaxis_title=titre_y,
                      legend_title = "",
                      hovermode = "y")

    return fig

def fig_old_annuelle_courbe(donnees, years, titre_graphe, titre_y):
    fig = go.Figure()


    # encoder les trimestre : passer d'un String à une valeur int
    label_encoder = LabelEncoder()
    trimestre_encoded = label_encoder.fit_transform([i + 1 for i, _ in enumerate(trimestre)])

    for i in range(len(years)):
        fig.add_trace(go.Scatter(x=trimestre_encoded, y=donnees[i], name="Année " + str(years[i]), line=dict(color=couleurs_années[i])))

 # Générer les données moyennes
    y = data.data.data_moy(donnees)

    # Courbe pour fitter les points
    degree = 3 
    model = LinearRegression()
    model.fit(np.vander(trimestre_encoded, degree + 1), y)

    # Generation des valeurs préditent
    x_pred = np.arange(min(trimestre_encoded), max(trimestre_encoded), 0.1) 
    y_pred = model.predict(np.vander(x_pred, degree + 1))  

    # Ajouter la régression polynomiale
    visible_bool = False
    if years[0] != years[-1] : 
        visible_bool = True
    fig.add_trace(go.Scatter(x=x_pred, y=y_pred, name="Régression", line=dict(dash='dash', color='black'), marker=dict(size=10), visible = visible_bool))

    if years[0] != years[-1] :
        titre_fig = titre_graphe + " de " + str(years[0]) + " à " + str(years[-1]) + ",<br>comparaison annuelle par trimestre"
    else : 
        titre_fig = titre_graphe + " en " + str(years[0]) + ",<br>comparaison annuelle par trimestre"

    fig.update_layout(title=titre_fig,
                      xaxis_title="Trimestres",
                      yaxis_title=titre_y,
                    xaxis = dict(
                    tickvals=[0, 1, 2, 3],
                    ticktext=['T1', 'T2', 'T3', 'T4']
                    ),
                    hovermode = "x"
                    )
    

    fig.update_traces(hovertemplate="<br>".join([
        " Trimestre : %{x}",
        "Total : <b>%{y:.0f}</b>",
                      ])
                    )
    
    return fig




def generate_graphs_(selected_years, value, baseline_graph):
    #update_data([selected_annee[0], selected_annee[-1]])

    if not isinstance(selected_years, list):
        selected_years = [selected_years, selected_years]


    selected_global = [data_old[selected_years[0] - min(annee): selected_years[1] - min(annee) + 1] for data_old in
                       data_old_global]
    selected_artemis = [data_old[selected_years[0] - min(annee): selected_years[1] - min(annee) + 1] for data_old in
                       data_old_artemis]
    selected_citi = [data_old[selected_years[0] - min(annee): selected_years[1] - min(annee) + 1] for data_old in
                       data_old_citi]
    selected_eph = [data_old[selected_years[0] - min(annee): selected_years[1] - min(annee) + 1] for data_old in
                       data_old_eph]
    selected_inf = [data_old[selected_years[0] - min(annee): selected_years[1] - min(annee) + 1] for data_old in
                       data_old_inf]
    selected_rs2m = [data_old[selected_years[0] - min(annee): selected_years[1] - min(annee) + 1] for data_old in
                       data_old_rs2m]
    selected_rst = [data_old[selected_years[0] - min(annee): selected_years[1] - min(annee) + 1] for data_old in
                       data_old_rst]
    selected_annee = [year for year in range(selected_years[0], selected_years[1] + 1)]
    selected_label = label[selected_years[0] - min(annee): selected_years[1] - min(annee) + 1]


    # Liste des graphiques disponibles
    graphs = {
        """
        # DF
        "df_old_1_an": fig_old_annuelle_baton(selected_global[0], selected_annee, selected_label, titres_graphe[0], titres_y[0]),
        "df_old_1_tri": fig_old_trimestrielle(selected_global[0], selected_annee, selected_label, titres_graphe[0], titres_y[0]),
        "df_old_1_tot": fig_old_total(selected_global[0], selected_annee, titres_graphe[0], titres_y[0]),
        "df_old_1_comp": fig_old_annuelle_courbe(selected_global[0], selected_annee, titres_graphe[0], titres_y[0]),
        """
        """
        #DAF
        "daf_old_1_an": fig_old_annuelle_baton(selected_global[1], selected_annee, selected_label, titres_graphe[1],titres_y[1]),
        "daf_old_1_tri": fig_old_trimestrielle(selected_global[1], selected_annee, selected_label, titres_graphe[1],titres_y[1]),
        "daf_old_1_tot": fig_old_total(selected_global[1], selected_annee, titres_graphe[1], titres_y[1]),
        "daf_old_1_comp": fig_old_annuelle_courbe(selected_global[1], selected_annee, titres_graphe[1], titres_y[1]),
        "daf_old_2_an": fig_old_annuelle_baton(selected_global[2], selected_annee, selected_label, titres_graphe[2],titres_y[2]),
        "daf_old_2_tri": fig_old_trimestrielle(selected_global[2], selected_annee, selected_label, titres_graphe[2],titres_y[2]),
        "daf_old_2_tot": fig_old_total(selected_global[2], selected_annee, titres_graphe[2], titres_y[2]),
        "daf_old_2_comp": fig_old_annuelle_courbe(selected_global[2], selected_annee, titres_graphe[2], titres_y[2]),
        "daf_old_3_an": fig_old_annuelle_baton(selected_global[3], selected_annee, selected_label, titres_graphe[3], titres_y[3]),
        "daf_old_3_tri": fig_old_trimestrielle(selected_global[3], selected_annee, selected_label, titres_graphe[3], titres_y[3]),
        "daf_old_3_tot": fig_old_total(selected_global[3], selected_annee, titres_graphe[3], titres_y[3]),
        "daf_old_3_comp": fig_old_annuelle_courbe(selected_global[3], selected_annee, titres_graphe[3], titres_y[3]),
        """
        """
        #DIRE
        "dire_old_1_an": fig_old_annuelle_baton(selected_global[4], selected_annee, selected_label, titres_graphe[4], titres_y[4]),
        "dire_old_1_tri": fig_old_trimestrielle(selected_global[4], selected_annee, selected_label, titres_graphe[4], titres_y[4]),
        "dire_old_1_tot": fig_old_total(selected_global[4], selected_annee, titres_graphe[4], titres_y[4]),
        "dire_old_1_comp": fig_old_annuelle_courbe(selected_global[4], selected_annee, titres_graphe[4], titres_y[4]),
        "dire_old_2_an": fig_old_annuelle_baton(selected_global[5], selected_annee, selected_label, titres_graphe[5], titres_y[5]),
        "dire_old_2_tri": fig_old_trimestrielle(selected_global[5], selected_annee, selected_label, titres_graphe[5], titres_y[5]),
        "dire_old_2_tot": fig_old_total(selected_global[5], selected_annee, titres_graphe[5], titres_y[5]),
        "dire_old_2_comp": fig_old_annuelle_courbe(selected_global[5], selected_annee, titres_graphe[5], titres_y[5]),
        "dire_old_3_an": fig_old_annuelle_baton(selected_global[6], selected_annee, selected_label, titres_graphe[6], titres_y[6]),
        "dire_old_3_tri": fig_old_trimestrielle(selected_global[6], selected_annee, selected_label, titres_graphe[6], titres_y[6]),
        "dire_old_3_tot": fig_old_total(selected_global[6], selected_annee, titres_graphe[6], titres_y[6]),
        "dire_old_3_comp": fig_old_annuelle_courbe(selected_global[6], selected_annee, titres_graphe[6], titres_y[6]),

        #DRFD
        "drfd_old_1_an": fig_old_annuelle_baton(selected_global[7], selected_annee, selected_label, titres_graphe[7], titres_y[7]),
        "drfd_old_1_tri": fig_old_trimestrielle(selected_global[7], selected_annee, selected_label, titres_graphe[7], titres_y[7]),
        "drfd_old_1_tot": fig_old_total(selected_global[7], selected_annee, titres_graphe[7], titres_y[7]),
        "drfd_old_1_comp": fig_old_annuelle_courbe(selected_global[7], selected_annee, titres_graphe[7], titres_y[7]),
        "drfd_old_2_an": fig_old_annuelle_baton(selected_global[8], selected_annee, selected_label, titres_graphe[8], titres_y[8]),
        "drfd_old_2_tri": fig_old_trimestrielle(selected_global[8], selected_annee, selected_label, titres_graphe[8], titres_y[8]),
        "drfd_old_2_tot": fig_old_total(selected_global[8], selected_annee, titres_graphe[8], titres_y[8]),
        "drfd_old_2_comp": fig_old_annuelle_courbe(selected_global[8], selected_annee, titres_graphe[8], titres_y[8]),

        #DRH
        "drh_old_1_an": fig_old_annuelle_baton(selected_global[9], selected_annee, selected_label, titres_graphe[9], titres_y[9]),
        "drh_old_1_tri": fig_old_trimestrielle(selected_global[9], selected_annee, selected_label, titres_graphe[9], titres_y[9]),
        "drh_old_1_tot": fig_old_total(selected_global[9], selected_annee, titres_graphe[9], titres_y[9]),
        "drh_old_1_comp": fig_old_annuelle_courbe(selected_global[9], selected_annee, titres_graphe[9], titres_y[9]),
        "drh_old_2_an": fig_old_annuelle_baton(selected_global[10], selected_annee, selected_label, titres_graphe[10], titres_y[10]),
        "drh_old_2_tri": fig_old_trimestrielle(selected_global[10], selected_annee, selected_label, titres_graphe[10], titres_y[10]),
        "drh_old_2_tot": fig_old_total(selected_global[10], selected_annee, titres_graphe[10], titres_y[10]),
        "drh_old_2_comp": fig_old_annuelle_courbe(selected_global[10], selected_annee, titres_graphe[10], titres_y[10]),

        # ARTEMIS
        "artemis_old_0_an": fig_old_annuelle_baton(selected_artemis[0], selected_annee, selected_label, titres_graphe[0] + " à ARTEMIS ", titres_y[0]),
        "artemis_old_0_tri": fig_old_trimestrielle(selected_artemis[0], selected_annee, selected_label, titres_graphe[0] + " à ARTEMIS ",  titres_y[0]),
        "artemis_old_0_tot": fig_old_total(selected_artemis[0], selected_annee, titres_graphe[0] + " à ARTEMIS ", titres_y[0]),
        "artemis_old_0_comp": fig_old_annuelle_courbe(selected_artemis[0], selected_annee, titres_graphe[0] + " à ARTEMIS ", titres_y[0]),
        "artemis_old_1_an": fig_old_annuelle_baton(selected_artemis[1], selected_annee, selected_label, titres_graphe[1] + " à ARTEMIS ", titres_y[1]),
        "artemis_old_1_tri": fig_old_trimestrielle(selected_artemis[1], selected_annee, selected_label, titres_graphe[1] + " à ARTEMIS ", titres_y[1]),
        "artemis_old_1_tot": fig_old_total(selected_artemis[1], selected_annee, titres_graphe[1] + " à ARTEMIS ", titres_y[1]),
        "artemis_old_1_comp": fig_old_annuelle_courbe(selected_artemis[1], selected_annee, titres_graphe[1] + " à ARTEMIS ", titres_y[1]),
        "artemis_old_2_an": fig_old_annuelle_baton(selected_artemis[2], selected_annee, selected_label, titres_graphe[2] + " à ARTEMIS ", titres_y[2]),
        "artemis_old_2_tri": fig_old_trimestrielle(selected_artemis[2], selected_annee, selected_label, titres_graphe[2] + " à ARTEMIS ", titres_y[2]),
        "artemis_old_2_tot": fig_old_total(selected_artemis[2], selected_annee, titres_graphe[2] + " à ARTEMIS ", titres_y[2]),
        "artemis_old_2_comp": fig_old_annuelle_courbe(selected_artemis[2], selected_annee, titres_graphe[2] + " à ARTEMIS ", titres_y[2]),
        "artemis_old_3_an": fig_old_annuelle_baton(selected_artemis[3], selected_annee, selected_label, titres_graphe[3] + " à ARTEMIS ", titres_y[3]),
        "artemis_old_3_tri": fig_old_trimestrielle(selected_artemis[3], selected_annee, selected_label, titres_graphe[3] + " à ARTEMIS ", titres_y[3]),
        "artemis_old_3_tot": fig_old_total(selected_artemis[3], selected_annee, titres_graphe[3] + " à ARTEMIS ", titres_y[3]),
        "artemis_old_3_comp": fig_old_annuelle_courbe(selected_artemis[3], selected_annee, titres_graphe[3] + " à ARTEMIS ", titres_y[3]),
        "artemis_old_4_an": fig_old_annuelle_baton(selected_artemis[4], selected_annee, selected_label, titres_graphe[4] + " à ARTEMIS ", titres_y[4]),
        "artemis_old_4_tri": fig_old_trimestrielle(selected_artemis[4], selected_annee, selected_label, titres_graphe[4] + " à ARTEMIS ", titres_y[4]),
        "artemis_old_4_tot": fig_old_total(selected_artemis[4], selected_annee, titres_graphe[4] + " à ARTEMIS ", titres_y[4]),
        "artemis_old_4_comp": fig_old_annuelle_courbe(selected_artemis[4], selected_annee, titres_graphe[4] + " à ARTEMIS ", titres_y[4]),
        "artemis_old_5_an": fig_old_annuelle_baton(selected_artemis[5], selected_annee, selected_label, titres_graphe[5] + " à ARTEMIS ", titres_y[5]),
        "artemis_old_5_tri": fig_old_trimestrielle(selected_artemis[5], selected_annee, selected_label, titres_graphe[5] + " à ARTEMIS ", titres_y[5]),
        "artemis_old_5tot": fig_old_total(selected_artemis[5], selected_annee, titres_graphe[5] + " à ARTEMIS ", titres_y[5]),
        "artemis_old_5_comp": fig_old_annuelle_courbe(selected_artemis[5], selected_annee, titres_graphe[5] + " à ARTEMIS ", titres_y[5]),
        "artemis_old_6_an": fig_old_annuelle_baton(selected_artemis[6], selected_annee, selected_label, titres_graphe[6] + " à ARTEMIS ", titres_y[6]),
        "artemis_old_6_tri": fig_old_trimestrielle(selected_artemis[6], selected_annee, selected_label, titres_graphe[6] + " à ARTEMIS ", titres_y[6]),
        "artemis_old_6_tot": fig_old_total(selected_artemis[6], selected_annee, titres_graphe[6] + " à ARTEMIS ", titres_y[6]),
        "artemis_old_6_comp": fig_old_annuelle_courbe(selected_artemis[6], selected_annee, titres_graphe[6] + " à ARTEMIS ", titres_y[6]),
        "artemis_old_7_an": fig_old_annuelle_baton(selected_artemis[7], selected_annee, selected_label, titres_graphe[7] + " à ARTEMIS ", titres_y[7]),
        "artemis_old_7_tri": fig_old_trimestrielle(selected_artemis[7], selected_annee, selected_label, titres_graphe[7] + " à ARTEMIS ", titres_y[7]),
        "artemis_old_7_tot": fig_old_total(selected_artemis[7], selected_annee, titres_graphe[7] + " à ARTEMIS ", titres_y[7]),
        "artemis_old_7_comp": fig_old_annuelle_courbe(selected_artemis[7], selected_annee, titres_graphe[7] + " à ARTEMIS ", titres_y[7]),
        "artemis_old_8_an": fig_old_annuelle_baton(selected_artemis[8], selected_annee, selected_label, titres_graphe[8] + " à ARTEMIS ", titres_y[8]),
        "artemis_old_8_tri": fig_old_trimestrielle(selected_artemis[8], selected_annee, selected_label, titres_graphe[8] + " à ARTEMIS ", titres_y[8]),
        "artemis_old_8_tot": fig_old_total(selected_artemis[8], selected_annee, titres_graphe[8] + " à ARTEMIS ", titres_y[8]),
        "artemis_old_8_comp": fig_old_annuelle_courbe(selected_artemis[8], selected_annee,  titres_graphe[8] + " à ARTEMIS ", titres_y[8]),
        "artemis_old_9_an": fig_old_annuelle_baton(selected_artemis[9], selected_annee, selected_label, titres_graphe[9] + " à ARTEMIS ", titres_y[9]),
        "artemis_old_9_tri": fig_old_trimestrielle(selected_artemis[9], selected_annee, selected_label, titres_graphe[9] + " à ARTEMIS ", titres_y[9]),
        "artemis_old_9_tot": fig_old_total(selected_artemis[9], selected_annee, titres_graphe[9] + " à ARTEMIS ", titres_y[9]),
        "artemis_old_9_comp": fig_old_annuelle_courbe(selected_artemis[9], selected_annee, titres_graphe[9] + " à ARTEMIS ", titres_y[9]),
        "artemis_old_10_an": fig_old_annuelle_baton(selected_artemis[10], selected_annee, selected_label, titres_graphe[10] + " à ARTEMIS ", titres_y[10]),
        "artemis_old_10_tri": fig_old_trimestrielle(selected_artemis[10], selected_annee, selected_label, titres_graphe[10] + " à ARTEMIS ", titres_y[10]),
        "artemis_old_10_tot": fig_old_total(selected_artemis[10], selected_annee, titres_graphe[10] + " à ARTEMIS ", titres_y[10]),
        "artemis_old_10_comp": fig_old_annuelle_courbe(selected_artemis[10], selected_annee, titres_graphe[10] + " à ARTEMIS ", titres_y[10]),

        # CITI
        "citi_old_0_an": fig_old_annuelle_baton(selected_citi[0], selected_annee, selected_label, titres_graphe[0] + " à CITI ", titres_y[0]),
        "citi_old_0_tri": fig_old_trimestrielle(selected_citi[0], selected_annee, selected_label, titres_graphe[0] + " à CITI ", titres_y[0]),
        "citi_old_0_tot": fig_old_total(selected_citi[0], selected_annee, titres_graphe[0] + " à CITI ", titres_y[0]),
        "citi_old_0_comp": fig_old_annuelle_courbe(selected_citi[0], selected_annee, titres_graphe[0] + " à CITI ", titres_y[0]),
        "citi_old_1_an": fig_old_annuelle_baton(selected_citi[1], selected_annee, selected_label, titres_graphe[1] + " à CITI ", titres_y[1]),
        "citi_old_1_tri": fig_old_trimestrielle(selected_citi[1], selected_annee, selected_label, titres_graphe[1] + " à CITI ", titres_y[1]),
        "citi_old_1_tot": fig_old_total(selected_citi[1], selected_annee, titres_graphe[1] + " à CITI ", titres_y[1]),
        "citi_old_1_comp": fig_old_annuelle_courbe(selected_citi[1], selected_annee, titres_graphe[1] + " à CITI ", titres_y[1]),
        "citi_old_2_an": fig_old_annuelle_baton(selected_citi[2], selected_annee, selected_label, titres_graphe[2] + " à CITI ", titres_y[2]),
        "citi_old_2_tri": fig_old_trimestrielle(selected_citi[2], selected_annee, selected_label, titres_graphe[2] + " à CITI ", titres_y[2]),
        "citi_old_2_tot": fig_old_total(selected_citi[2], selected_annee, titres_graphe[2] + " à CITI ", titres_y[2]),
        "citi_old_2_comp": fig_old_annuelle_courbe(selected_citi[2], selected_annee, titres_graphe[2] + " à CITI ", titres_y[2]),
        "citi_old_3_an": fig_old_annuelle_baton(selected_citi[3], selected_annee, selected_label, titres_graphe[3] + " à CITI ", titres_y[3]),
        "citi_old_3_tri": fig_old_trimestrielle(selected_citi[3], selected_annee, selected_label, titres_graphe[3] + " à CITI ", titres_y[3]),
        "citi_old_3_tot": fig_old_total(selected_citi[3], selected_annee, titres_graphe[3] + " à CITI ", titres_y[3]),
        "citi_old_3_comp": fig_old_annuelle_courbe(selected_citi[3], selected_annee, titres_graphe[3] + " à CITI ", titres_y[3]),
        "citi_old_4_an": fig_old_annuelle_baton(selected_citi[4], selected_annee, selected_label, titres_graphe[4] + " à CITI ", titres_y[4]),
        "citi_old_4_tri": fig_old_trimestrielle(selected_citi[4], selected_annee, selected_label, titres_graphe[4] + " à CITI ", titres_y[4]),
        "citi_old_4_tot": fig_old_total(selected_citi[4], selected_annee, titres_graphe[4] + " à CITI ", titres_y[4]),
        "citi_old_4_comp": fig_old_annuelle_courbe(selected_citi[4], selected_annee, titres_graphe[4] + " à CITI ", titres_y[4]),
        "citi_old_5_an": fig_old_annuelle_baton(selected_citi[5], selected_annee, selected_label, titres_graphe[5] + " à CITI ", titres_y[5]),
        "citi_old_5_tri": fig_old_trimestrielle(selected_citi[5], selected_annee, selected_label, titres_graphe[5] + " à CITI ", titres_y[5]),
        "citi_old_5_tot": fig_old_total(selected_citi[5], selected_annee, titres_graphe[5] + " à CITI ", titres_y[5]),
        "citi_old_5_comp": fig_old_annuelle_courbe(selected_citi[5], selected_annee, titres_graphe[5] + " à CITI ", titres_y[5]),
        "citi_old_6_an": fig_old_annuelle_baton(selected_citi[6], selected_annee, selected_label, titres_graphe[6] + " à CITI ", titres_y[6]),
        "citi_old_6_tri": fig_old_trimestrielle(selected_citi[6], selected_annee, selected_label, titres_graphe[6] + " à CITI ", titres_y[6]),
        "citi_old_6_tot": fig_old_total(selected_citi[6], selected_annee, titres_graphe[6] + " à CITI ", titres_y[6]),
        "citi_old_6_comp": fig_old_annuelle_courbe(selected_citi[6], selected_annee, titres_graphe[6] + " à CITI ", titres_y[6]),
        "citi_old_7_an": fig_old_annuelle_baton(selected_citi[7], selected_annee, selected_label, titres_graphe[7] + " à CITI ", titres_y[7]),
        "citi_old_7_tri": fig_old_trimestrielle(selected_citi[7], selected_annee, selected_label, titres_graphe[7] + " à CITI ", titres_y[7]),
        "citi_old_7_tot": fig_old_total(selected_citi[7], selected_annee, titres_graphe[7] + " à CITI ", titres_y[7]),
        "citi_old_7_comp": fig_old_annuelle_courbe(selected_citi[7], selected_annee, titres_graphe[7] + " à CITI ", titres_y[7]),
        "citi_old_8_an": fig_old_annuelle_baton(selected_citi[8], selected_annee, selected_label, titres_graphe[8] + " à CITI ", titres_y[8]),
        "citi_old_8_tri": fig_old_trimestrielle(selected_citi[8], selected_annee, selected_label, titres_graphe[8] + " à CITI ", titres_y[8]),
        "citi_old_8_tot": fig_old_total(selected_citi[8], selected_annee, titres_graphe[8] + " à CITI ", titres_y[8]),
        "citi_old_8_comp": fig_old_annuelle_courbe(selected_citi[8], selected_annee, titres_graphe[8] + " à CITI ", titres_y[8]),
        "citi_old_9_an": fig_old_annuelle_baton(selected_citi[9], selected_annee, selected_label, titres_graphe[9] + " à CITI ", titres_y[9]),
        "citi_old_9_tri": fig_old_trimestrielle(selected_citi[9], selected_annee, selected_label, titres_graphe[9] + " à CITI ", titres_y[9]),
        "citi_old_9_tot": fig_old_total(selected_citi[9], selected_annee, titres_graphe[9] + " à CITI ", titres_y[9]),
        "citi_old_9_comp": fig_old_annuelle_courbe(selected_citi[9], selected_annee, titres_graphe[9] + " à CITI ", titres_y[9]),
        "citi_old_10_an": fig_old_annuelle_baton(selected_citi[10], selected_annee, selected_label, titres_graphe[10] + " à CITI ", titres_y[10]),
        "citi_old_10_tri": fig_old_trimestrielle(selected_citi[10], selected_annee, selected_label, titres_graphe[10] + " à CITI ", titres_y[10]),
        "citi_old_10_tot": fig_old_total(selected_citi[10], selected_annee, titres_graphe[10] + " à CITI ", titres_y[10]),
        "citi_old_10_comp": fig_old_annuelle_courbe(selected_citi[10], selected_annee, titres_graphe[10] + " à CITI ", titres_y[10]),

        # EPH
        "eph_old_0_an": fig_old_annuelle_baton(selected_eph[0], selected_annee, selected_label, titres_graphe[0] + " à EPH ", titres_y[0]),
        "eph_old_0_tri": fig_old_trimestrielle(selected_eph[0], selected_annee, selected_label, titres_graphe[0] + " à EPH ", titres_y[0]),
        "eph_old_0_tot": fig_old_total(selected_eph[0], selected_annee, titres_graphe[0] + " à EPH ", titres_y[0]),
        "eph_old_0_comp": fig_old_annuelle_courbe(selected_eph[0], selected_annee, titres_graphe[0] + " à EPH ", titres_y[0]),
        "eph_old_1_an": fig_old_annuelle_baton(selected_eph[1], selected_annee, selected_label, titres_graphe[1] + " à EPH ", titres_y[1]),
        "eph_old_1_tri": fig_old_trimestrielle(selected_eph[1], selected_annee, selected_label, titres_graphe[1] + " à EPH ", titres_y[1]),
        "eph_old_1_tot": fig_old_total(selected_eph[1], selected_annee, titres_graphe[1] + " à EPH ", titres_y[1]),
        "eph_old_1_comp": fig_old_annuelle_courbe(selected_eph[1], selected_annee, titres_graphe[1] + " à EPH ", titres_y[1]),
        "eph_old_2_an": fig_old_annuelle_baton(selected_eph[2], selected_annee, selected_label, titres_graphe[2] + " à EPH ", titres_y[2]),
        "eph_old_2_tri": fig_old_trimestrielle(selected_eph[2], selected_annee, selected_label, titres_graphe[2] + " à EPH ", titres_y[2]),
        "eph_old_2_tot": fig_old_total(selected_eph[2], selected_annee, titres_graphe[2] + " à EPH ", titres_y[2]),
        "eph_old_2_comp": fig_old_annuelle_courbe(selected_eph[2], selected_annee, titres_graphe[2] + " à EPH ", titres_y[2]),
        "eph_old_3_an": fig_old_annuelle_baton(selected_eph[3], selected_annee, selected_label, titres_graphe[3] + " à EPH ", titres_y[3]),
        "eph_old_3_tri": fig_old_trimestrielle(selected_eph[3], selected_annee, selected_label, titres_graphe[3] + " à EPH ", titres_y[3]),
        "eph_old_3_tot": fig_old_total(selected_eph[3], selected_annee, titres_graphe[3] + " à EPH ", titres_y[3]),
        "eph_old_3_comp": fig_old_annuelle_courbe(selected_eph[3], selected_annee, titres_graphe[3] + " à EPH ", titres_y[3]),
        "eph_old_4_an": fig_old_annuelle_baton(selected_eph[4], selected_annee, selected_label, titres_graphe[4] + " à EPH ", titres_y[4]),
        "eph_old_4_tri": fig_old_trimestrielle(selected_eph[4], selected_annee, selected_label, titres_graphe[4] + " à EPH ", titres_y[4]),
        "eph_old_4_tot": fig_old_total(selected_eph[4], selected_annee, titres_graphe[4] + " à EPH ", titres_y[4]),
        "eph_old_4_comp": fig_old_annuelle_courbe(selected_eph[4], selected_annee, titres_graphe[4] + " à EPH ", titres_y[4]),
        "eph_old_5_an": fig_old_annuelle_baton(selected_eph[5], selected_annee, selected_label, titres_graphe[5] + " à EPH ", titres_y[5]),
        "eph_old_5_tri": fig_old_trimestrielle(selected_eph[5], selected_annee, selected_label, titres_graphe[5] + " à EPH ", titres_y[5]),
        "eph_old_5_tot": fig_old_total(selected_eph[5], selected_annee, titres_graphe[5] + " à EPH ", titres_y[5]),
        "eph_old_5_comp": fig_old_annuelle_courbe(selected_eph[5], selected_annee, titres_graphe[5] + " à EPH ", titres_y[5]),
        "eph_old_6_an": fig_old_annuelle_baton(selected_eph[6], selected_annee, selected_label, titres_graphe[6] + " à EPH ", titres_y[6]),
        "eph_old_6_tri": fig_old_trimestrielle(selected_eph[6], selected_annee, selected_label, titres_graphe[6] + " à EPH ", titres_y[6]),
        "eph_old_6_tot": fig_old_total(selected_eph[6], selected_annee, titres_graphe[6] + " à EPH ", titres_y[6]),
        "eph_old_6_comp": fig_old_annuelle_courbe(selected_eph[6], selected_annee, titres_graphe[6] + " à EPH ", titres_y[6]),
        "eph_old_7_an": fig_old_annuelle_baton(selected_eph[7], selected_annee, selected_label, titres_graphe[7] + " à EPH ", titres_y[7]),
        "eph_old_7_tri": fig_old_trimestrielle(selected_eph[7], selected_annee, selected_label, titres_graphe[7] + " à EPH ", titres_y[7]),
        "eph_old_7_tot": fig_old_total(selected_eph[7], selected_annee, titres_graphe[7] + " à EPH ", titres_y[7]),
        "eph_old_7_comp": fig_old_annuelle_courbe(selected_eph[7], selected_annee, titres_graphe[7] + " à EPH ", titres_y[7]),
        "eph_old_8_an": fig_old_annuelle_baton(selected_eph[8], selected_annee, selected_label, titres_graphe[8] + " à EPH ", titres_y[8]),
        "eph_old_8_tri": fig_old_trimestrielle(selected_eph[8], selected_annee, selected_label, titres_graphe[8] + " à EPH ", titres_y[8]),
        "eph_old_8_tot": fig_old_total(selected_eph[8], selected_annee, titres_graphe[8] + " à EPH ", titres_y[8]),
        "eph_old_8_comp": fig_old_annuelle_courbe(selected_eph[8], selected_annee, titres_graphe[8] + " à EPH ", titres_y[8]),
        "eph_old_9_an": fig_old_annuelle_baton(selected_eph[9], selected_annee, selected_label, titres_graphe[9] + " à EPH ", titres_y[9]),
        "eph_old_9_tri": fig_old_trimestrielle(selected_eph[9], selected_annee, selected_label, titres_graphe[9] + " à EPH ", titres_y[9]),
        "eph_old_9_tot": fig_old_total(selected_eph[9], selected_annee, titres_graphe[9] + " à EPH ", titres_y[9]),
        "eph_old_9_comp": fig_old_annuelle_courbe(selected_eph[9], selected_annee, titres_graphe[9] + " à EPH ", titres_y[9]),
        "eph_old_10_an": fig_old_annuelle_baton(selected_eph[10], selected_annee, selected_label, titres_graphe[10] + " à EPH ", titres_y[10]),
        "eph_old_10_tri": fig_old_trimestrielle(selected_eph[10], selected_annee, selected_label, titres_graphe[10] + " à EPH ", titres_y[10]),
        "eph_old_10_tot": fig_old_total(selected_eph[10], selected_annee, titres_graphe[10] + " à EPH ", titres_y[10]),
        "eph_old_10_comp": fig_old_annuelle_courbe(selected_eph[10], selected_annee, titres_graphe[10] + " à EPH ", titres_y[10]),

        # INF
        "inf_old_0_an": fig_old_annuelle_baton(selected_inf[0], selected_annee, selected_label, titres_graphe[0] + " à INF ", titres_y[0]),
        "inf_old_0_tri": fig_old_trimestrielle(selected_inf[0], selected_annee, selected_label, titres_graphe[0] + " à INF ", titres_y[0]),
        "inf_old_0_tot": fig_old_total(selected_inf[0], selected_annee, titres_graphe[0] + " à INF ", titres_y[0]),
        "inf_old_0_comp": fig_old_annuelle_courbe(selected_inf[0], selected_annee, titres_graphe[0] + " à INF ", titres_y[0]),
        "inf_old_1_an": fig_old_annuelle_baton(selected_inf[1], selected_annee, selected_label, titres_graphe[1] + " à INF ", titres_y[1]),
        "inf_old_1_tri": fig_old_trimestrielle(selected_inf[1], selected_annee, selected_label, titres_graphe[1] + " à INF ", titres_y[1]),
        "inf_old_1_tot": fig_old_total(selected_inf[1], selected_annee, titres_graphe[1] + " à INF ", titres_y[1]),
        "inf_old_1_comp": fig_old_annuelle_courbe(selected_inf[1], selected_annee, titres_graphe[1] + " à INF ", titres_y[1]),
        "inf_old_2_an": fig_old_annuelle_baton(selected_inf[2], selected_annee, selected_label, titres_graphe[2] + " à INF ", titres_y[2]),
        "inf_old_2_tri": fig_old_trimestrielle(selected_inf[2], selected_annee, selected_label, titres_graphe[2] + " à INF ", titres_y[2]),
        "inf_old_2_tot": fig_old_total(selected_inf[2], selected_annee, titres_graphe[2] + " à INF ", titres_y[2]),
        "inf_old_2_comp": fig_old_annuelle_courbe(selected_inf[2], selected_annee, titres_graphe[2] + " à INF ", titres_y[2]),
        "inf_old_3_an": fig_old_annuelle_baton(selected_inf[3], selected_annee, selected_label, titres_graphe[3] + " à INF ", titres_y[3]),
        "inf_old_3_tri": fig_old_trimestrielle(selected_inf[3], selected_annee, selected_label, titres_graphe[3] + " à INF ", titres_y[3]),
        "inf_old_3_tot": fig_old_total(selected_inf[3], selected_annee, titres_graphe[3] + " à INF ", titres_y[3]),
        "inf_old_3_comp": fig_old_annuelle_courbe(selected_inf[3], selected_annee, titres_graphe[3] + " à INF ", titres_y[3]),
        "inf_old_4_an": fig_old_annuelle_baton(selected_inf[4], selected_annee, selected_label, titres_graphe[4] + " à INF ", titres_y[4]),
        "inf_old_4_tri": fig_old_trimestrielle(selected_inf[4], selected_annee, selected_label, titres_graphe[4] + " à INF ", titres_y[4]),
        "inf_old_4_tot": fig_old_total(selected_inf[4], selected_annee, titres_graphe[4] + " à INF ", titres_y[4]),
        "inf_old_4_comp": fig_old_annuelle_courbe(selected_inf[4], selected_annee, titres_graphe[4] + " à INF ", titres_y[4]),
        "inf_old_5_an": fig_old_annuelle_baton(selected_inf[5], selected_annee, selected_label, titres_graphe[5] + " à INF ", titres_y[5]),
        "inf_old_5_tri": fig_old_trimestrielle(selected_inf[5], selected_annee, selected_label, titres_graphe[5] + " à INF ", titres_y[5]),
        "inf_old_5tot": fig_old_total(selected_inf[5], selected_annee, titres_graphe[5] + " à INF ", titres_y[5]),
        "inf_old_5_comp": fig_old_annuelle_courbe(selected_inf[5], selected_annee, titres_graphe[5] + " à INF ", titres_y[5]),
        "inf_old_6_an": fig_old_annuelle_baton(selected_inf[6], selected_annee, selected_label, titres_graphe[6] + " à INF ", titres_y[6]),
        "inf_old_6_tri": fig_old_trimestrielle(selected_inf[6], selected_annee, selected_label, titres_graphe[6] + " à INF ", titres_y[6]),
        "inf_old_6_tot": fig_old_total(selected_inf[6], selected_annee, titres_graphe[6] + " à INF ", titres_y[6]),
        "inf_old_6_comp": fig_old_annuelle_courbe(selected_inf[6], selected_annee, titres_graphe[6] + " à INF ", titres_y[6]),
        "inf_old_7_an": fig_old_annuelle_baton(selected_inf[7], selected_annee, selected_label, titres_graphe[7] + " à INF ", titres_y[7]),
        "inf_old_7_tri": fig_old_trimestrielle(selected_inf[7], selected_annee, selected_label, titres_graphe[7] + " à INF ", titres_y[7]),
        "inf_old_7_tot": fig_old_total(selected_inf[7], selected_annee, titres_graphe[7] + " à INF ", titres_y[7]),
        "inf_old_7_comp": fig_old_annuelle_courbe(selected_inf[7], selected_annee, titres_graphe[7] + " à INF ", titres_y[7]),
        "inf_old_8_an": fig_old_annuelle_baton(selected_inf[8], selected_annee, selected_label, titres_graphe[8] + " à INF ", titres_y[8]),
        "inf_old_8_tri": fig_old_trimestrielle(selected_inf[8], selected_annee, selected_label, titres_graphe[8] + " à INF ", titres_y[8]),
        "inf_old_8_tot": fig_old_total(selected_inf[8], selected_annee, titres_graphe[8] + " à INF ", titres_y[8]),
        "inf_old_8_comp": fig_old_annuelle_courbe(selected_inf[8], selected_annee, titres_graphe[8] + " à INF ", titres_y[8]),
        "inf_old_9_an": fig_old_annuelle_baton(selected_inf[9], selected_annee, selected_label, titres_graphe[9] + " à INF ", titres_y[9]),
        "inf_old_9_tri": fig_old_trimestrielle(selected_inf[9], selected_annee, selected_label, titres_graphe[9] + " à INF ", titres_y[9]),
        "inf_old_9_tot": fig_old_total(selected_inf[9], selected_annee, titres_graphe[9] + " à INF ", titres_y[9]),
        "inf_old_9_comp": fig_old_annuelle_courbe(selected_inf[9], selected_annee, titres_graphe[9] + " à INF ", titres_y[9]),
        "inf_old_10_an": fig_old_annuelle_baton(selected_inf[10], selected_annee, selected_label, titres_graphe[10] + " à INF ", titres_y[10]),
        "inf_old_10_tri": fig_old_trimestrielle(selected_inf[10], selected_annee, selected_label, titres_graphe[10] + " à INF ", titres_y[10]),
        "inf_old_10_tot": fig_old_total(selected_inf[10], selected_annee, titres_graphe[10] + " à INF ", titres_y[10]),
        "inf_old_10_comp": fig_old_annuelle_courbe(selected_inf[10], selected_annee, titres_graphe[10] + " à INF ", titres_y[10]),

        # RS2M
        "rs2m_old_0_an": fig_old_annuelle_baton(selected_rs2m[0], selected_annee, selected_label, titres_graphe[0] + " à RS2M ", titres_y[0]),
        "rs2m_old_0_tri": fig_old_trimestrielle(selected_rs2m[0], selected_annee, selected_label, titres_graphe[0] + " à RS2M ", titres_y[0]),
        "rs2m_old_0_tot": fig_old_total(selected_rs2m[0], selected_annee, titres_graphe[0] + " à RS2M ", titres_y[0]),
        "rs2m_old_0_comp": fig_old_annuelle_courbe(selected_rs2m[0], selected_annee, titres_graphe[0] + " à RS2M ", titres_y[0]),
        "rs2m_old_1_an": fig_old_annuelle_baton(selected_rs2m[1], selected_annee, selected_label, titres_graphe[1] + " à RS2M ", titres_y[1]),
        "rs2m_old_1_tri": fig_old_trimestrielle(selected_rs2m[1], selected_annee, selected_label, titres_graphe[1] + " à RS2M ", titres_y[1]),
        "rs2m_old_1_tot": fig_old_total(selected_rs2m[1], selected_annee, titres_graphe[1] + " à RS2M ", titres_y[1]),
        "rs2m_old_1_comp": fig_old_annuelle_courbe(selected_rs2m[1], selected_annee, titres_graphe[1] + " à RS2M ", titres_y[1]),
        "rs2m_old_2_an": fig_old_annuelle_baton(selected_rs2m[2], selected_annee, selected_label, titres_graphe[2] + " à RS2M ", titres_y[2]),
        "rs2m_old_2_tri": fig_old_trimestrielle(selected_rs2m[2], selected_annee, selected_label, titres_graphe[2] + " à RS2M ", titres_y[2]),
        "rs2m_old_2_tot": fig_old_total(selected_rs2m[2], selected_annee, titres_graphe[2] + " à RS2M ", titres_y[2]),
        "rs2m_old_2_comp": fig_old_annuelle_courbe(selected_rs2m[2], selected_annee, titres_graphe[2] + " à RS2M ", titres_y[2]),
        "rs2m_old_3_an": fig_old_annuelle_baton(selected_rs2m[3], selected_annee, selected_label, titres_graphe[3] + " à RS2M ", titres_y[3]),
        "rs2m_old_3_tri": fig_old_trimestrielle(selected_rs2m[3], selected_annee, selected_label, titres_graphe[3] + " à RS2M ", titres_y[3]),
        "rs2m_old_3_tot": fig_old_total(selected_rs2m[3], selected_annee, titres_graphe[3] + " à RS2M ", titres_y[3]),
        "rs2m_old_3_comp": fig_old_annuelle_courbe(selected_rs2m[3], selected_annee, titres_graphe[3] + " à RS2M ", titres_y[3]),
        "rs2m_old_4_an": fig_old_annuelle_baton(selected_rs2m[4], selected_annee, selected_label, titres_graphe[4] + " à RS2M ", titres_y[4]),
        "rs2m_old_4_tri": fig_old_trimestrielle(selected_rs2m[4], selected_annee, selected_label, titres_graphe[4] + " à RS2M ", titres_y[4]),
        "rs2m_old_4_tot": fig_old_total(selected_rs2m[4], selected_annee, titres_graphe[4] + " à RS2M ", titres_y[4]),
        "rs2m_old_4_comp": fig_old_annuelle_courbe(selected_rs2m[4], selected_annee, titres_graphe[4] + " à RS2M ", titres_y[4]),
        "rs2m_old_5_an": fig_old_annuelle_baton(selected_rs2m[5], selected_annee, selected_label, titres_graphe[5] + " à RS2M ", titres_y[5]),
        "rs2m_old_5_tri": fig_old_trimestrielle(selected_rs2m[5], selected_annee, selected_label, titres_graphe[5] + " à RS2M ", titres_y[5]),
        "rs2m_old_5tot": fig_old_total(selected_rs2m[5], selected_annee, titres_graphe[5] + " à RS2M ", titres_y[5]),
        "rs2m_old_5_comp": fig_old_annuelle_courbe(selected_rs2m[5], selected_annee, titres_graphe[5] + " à RS2M ", titres_y[5]),
        "rs2m_old_6_an": fig_old_annuelle_baton(selected_rs2m[6], selected_annee, selected_label, titres_graphe[6] + " à RS2M ", titres_y[6]),
        "rs2m_old_6_tri": fig_old_trimestrielle(selected_rs2m[6], selected_annee, selected_label, titres_graphe[6] + " à RS2M ", titres_y[6]),
        "rs2m_old_6_tot": fig_old_total(selected_rs2m[6], selected_annee, titres_graphe[6] + " à RS2M ", titres_y[6]),
        "rs2m_old_6_comp": fig_old_annuelle_courbe(selected_rs2m[6], selected_annee, titres_graphe[6] + " à RS2M ", titres_y[6]),
        "rs2m_old_7_an": fig_old_annuelle_baton(selected_rs2m[7], selected_annee, selected_label, titres_graphe[7] + " à RS2M ", titres_y[7]),
        "rs2m_old_7_tri": fig_old_trimestrielle(selected_rs2m[7], selected_annee, selected_label, titres_graphe[7] + " à RS2M ", titres_y[7]),
        "rs2m_old_7_tot": fig_old_total(selected_rs2m[7], selected_annee, titres_graphe[7] + " à RS2M ", titres_y[7]),
        "rs2m_old_7_comp": fig_old_annuelle_courbe(selected_rs2m[7], selected_annee, titres_graphe[7] + " à RS2M ", titres_y[7]),
        "rs2m_old_8_an": fig_old_annuelle_baton(selected_rs2m[8], selected_annee, selected_label, titres_graphe[8] + " à RS2M ", titres_y[8]),
        "rs2m_old_8_tri": fig_old_trimestrielle(selected_rs2m[8], selected_annee, selected_label, titres_graphe[8] + " à RS2M ", titres_y[8]),
        "rs2m_old_8_tot": fig_old_total(selected_rs2m[8], selected_annee, titres_graphe[8] + " à RS2M ", titres_y[8]),
        "rs2m_old_8_comp": fig_old_annuelle_courbe(selected_rs2m[8], selected_annee, titres_graphe[8] + " à RS2M ", titres_y[8]),
        "rs2m_old_9_an": fig_old_annuelle_baton(selected_rs2m[9], selected_annee, selected_label, titres_graphe[9] + " à RS2M ", titres_y[9]),
        "rs2m_old_9_tri": fig_old_trimestrielle(selected_rs2m[9], selected_annee, selected_label, titres_graphe[9] + " à RS2M ", titres_y[9]),
        "rs2m_old_9_tot": fig_old_total(selected_rs2m[9], selected_annee, titres_graphe[9] + " à RS2M ", titres_y[9]),
        "rs2m_old_9_comp": fig_old_annuelle_courbe(selected_rs2m[9], selected_annee, titres_graphe[9] + " à RS2M ", titres_y[9]),
        "rs2m_old_10_an": fig_old_annuelle_baton(selected_rs2m[10], selected_annee, selected_label, titres_graphe[10] + " à RS2M ", titres_y[10]),
        "rs2m_old_10_tri": fig_old_trimestrielle(selected_rs2m[10], selected_annee, selected_label, titres_graphe[10] + " à RS2M ", titres_y[10]),
        "rs2m_old_10_tot": fig_old_total(selected_rs2m[10], selected_annee, titres_graphe[10] + " à RS2M ", titres_y[10]),
        "rs2m_old_10_comp": fig_old_annuelle_courbe(selected_rs2m[10], selected_annee, titres_graphe[10] + " à RS2M ", titres_y[10]),

        # RST
        "rst_old_0_an": fig_old_annuelle_baton(selected_rst[0], selected_annee, selected_label, titres_graphe[0] + " à RST ", titres_y[0]),
        "rst_old_0_tri": fig_old_trimestrielle(selected_rst[0], selected_annee, selected_label, titres_graphe[0] + " à RST ", titres_y[0]),
        "rst_old_0_tot": fig_old_total(selected_rst[0], selected_annee, titres_graphe[0] + " à RST ", titres_y[0]),
        "rst_old_0_comp": fig_old_annuelle_courbe(selected_rst[0], selected_annee, titres_graphe[0] + " à RST ", titres_y[0]),
        "rst_old_1_an": fig_old_annuelle_baton(selected_rst[1], selected_annee, selected_label, titres_graphe[1] + " à RST ", titres_y[1]),
        "rst_old_1_tri": fig_old_trimestrielle(selected_rst[1], selected_annee, selected_label, titres_graphe[1] + " à RST ", titres_y[1]),
        "rst_old_1_tot": fig_old_total(selected_rst[1], selected_annee, titres_graphe[1] + " à RST ", titres_y[1]),
        "rst_old_1_comp": fig_old_annuelle_courbe(selected_rst[1], selected_annee, titres_graphe[1] + " à RST ", titres_y[1]),
        "rst_old_2_an": fig_old_annuelle_baton(selected_rst[2], selected_annee, selected_label, titres_graphe[2] + " à RST ", titres_y[2]),
        "rst_old_2_tri": fig_old_trimestrielle(selected_rst[2], selected_annee, selected_label, titres_graphe[2] + " à RST ", titres_y[2]),
        "rst_old_2_tot": fig_old_total(selected_rst[2], selected_annee, titres_graphe[2] + " à RST ", titres_y[2]),
        "rst_old_2_comp": fig_old_annuelle_courbe(selected_rst[2], selected_annee, titres_graphe[2] + " à RST ", titres_y[2]),
        "rst_old_3_an": fig_old_annuelle_baton(selected_rst[3], selected_annee, selected_label, titres_graphe[3] + " à RST ", titres_y[3]),
        "rst_old_3_tri": fig_old_trimestrielle(selected_rst[3], selected_annee, selected_label, titres_graphe[3] + " à RST ", titres_y[3]),
        "rst_old_3_tot": fig_old_total(selected_rst[3], selected_annee, titres_graphe[3] + " à RST ", titres_y[3]),
        "rst_old_3_comp": fig_old_annuelle_courbe(selected_rst[3], selected_annee, titres_graphe[3] + " à RST ", titres_y[3]),
        "rst_old_4_an": fig_old_annuelle_baton(selected_rst[4], selected_annee, selected_label, titres_graphe[4] + " à RST ", titres_y[4]),
        "rst_old_4_tri": fig_old_trimestrielle(selected_rst[4], selected_annee, selected_label, titres_graphe[4] + " à RST ", titres_y[4]),
        "rst_old_4_tot": fig_old_total(selected_rst[4], selected_annee, titres_graphe[4] + " à RST ", titres_y[4]),
        "rst_old_4_comp": fig_old_annuelle_courbe(selected_rst[4], selected_annee, titres_graphe[4] + " à RST ", titres_y[4]),
        "rst_old_5_an": fig_old_annuelle_baton(selected_rst[5], selected_annee, selected_label, titres_graphe[5] + " à RST ", titres_y[5]),
        "rst_old_5_tri": fig_old_trimestrielle(selected_rst[5], selected_annee, selected_label, titres_graphe[5] + " à RST ", titres_y[5]),
        "rst_old_5tot": fig_old_total(selected_rst[5], selected_annee, titres_graphe[5] + " à RST ", titres_y[5]),
        "rst_old_5_comp": fig_old_annuelle_courbe(selected_rst[5], selected_annee, titres_graphe[5] + " à RST ", titres_y[5]),
        "rst_old_6_an": fig_old_annuelle_baton(selected_rst[6], selected_annee, selected_label, titres_graphe[6] + " à RST ", titres_y[6]),
        "rst_old_6_tri": fig_old_trimestrielle(selected_rst[6], selected_annee, selected_label, titres_graphe[6] + " à RST ", titres_y[6]),
        "rst_old_6_tot": fig_old_total(selected_rst[6], selected_annee, titres_graphe[6] + " à RST ", titres_y[6]),
        "rst_old_6_comp": fig_old_annuelle_courbe(selected_rst[6], selected_annee, titres_graphe[6] + " à RST ", titres_y[6]),
        "rst_old_7_an": fig_old_annuelle_baton(selected_rst[7], selected_annee, selected_label, titres_graphe[7] + " à RST ", titres_y[7]),
        "rst_old_7_tri": fig_old_trimestrielle(selected_rst[7], selected_annee, selected_label, titres_graphe[7] + " à RST ", titres_y[7]),
        "rst_old_7_tot": fig_old_total(selected_rst[7], selected_annee, titres_graphe[7] + " à RST ", titres_y[7]),
        "rst_old_7_comp": fig_old_annuelle_courbe(selected_rst[7], selected_annee, titres_graphe[7] + " à RST ", titres_y[7]),
        "rst_old_8_an": fig_old_annuelle_baton(selected_rst[8], selected_annee, selected_label, titres_graphe[8] + " à RST ", titres_y[8]),
        "rst_old_8_tri": fig_old_trimestrielle(selected_rst[8], selected_annee, selected_label, titres_graphe[8] + " à RST ", titres_y[8]),
        "rst_old_8_tot": fig_old_total(selected_rst[8], selected_annee, titres_graphe[8] + " à RST ", titres_y[8]),
        "rst_old_8_comp": fig_old_annuelle_courbe(selected_rst[8], selected_annee, titres_graphe[8] + " à RST ", titres_y[8]),
        "rst_old_9_an": fig_old_annuelle_baton(selected_rst[9], selected_annee, selected_label, titres_graphe[9] + " à RST ", titres_y[9]),
        "rst_old_9_tri": fig_old_trimestrielle(selected_rst[9], selected_annee, selected_label, titres_graphe[9] + " à RST ", titres_y[9]),
        "rst_old_9_tot": fig_old_total(selected_rst[9], selected_annee, titres_graphe[9] + " à RST ", titres_y[9]),
        "rst_old_9_comp": fig_old_annuelle_courbe(selected_rst[9], selected_annee, titres_graphe[9] + " à RST ", titres_y[9]),
        "rst_old_10_an": fig_old_annuelle_baton(selected_rst[10], selected_annee, selected_label, titres_graphe[10] + " à RST ", titres_y[10]),
        "rst_old_10_tri": fig_old_trimestrielle(selected_rst[10], selected_annee, selected_label, titres_graphe[10] + " à RST ", titres_y[10]),
        "rst_old_10_tot": fig_old_total(selected_rst[10], selected_annee, titres_graphe[10] + " à RST ", titres_y[10]),
        "rst_old_10_comp": fig_old_annuelle_courbe(selected_rst[10], selected_annee, titres_graphe[10] + " à RST ", titres_y[10]),
    """

    #fusion avec graph de "Choix libre" (ci dessus) : 

        #DF
        "df_1": fig_df_1(),
        "df_2": fig_df_2_update(get_df_DF_annuel()),

        #DRFD
        "drfd_1": fig_drfd_1(),
        "drfd_2": fig_drfd_2(),
        "drfd_3": fig_drfd_3(),
        "drfd_4": fig_drfd_4(),



        #DIRE
        "dire_1": fig_dire_1(),
        "dire_2": fig_dire_2(),
        "dire_3": fig_dire_3(),
        "dire_4": fig_dire_4(),


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


        #DRH
        "drh_1": fig_drh_1(),
        "drh_2": fig_drh_2(),
        "drh_3": fig_drh_3(),
        "drh_4": fig_drh_4(),


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


        #CITI
        "dept_3": fig_dept_3(),
        "citi_1": fig_citi_1(),
        "citi_2": fig_citi_2(),
        "citi_3": fig_citi_3(),
        "citi_4": fig_citi_4(),
        "citi_5": fig_citi_5(),
        "citi_6": fig_citi_6(),
        "citi_7": fig_citi_7(),


        #EPH
        "dept_4": fig_dept_4(),
        "eph_1": fig_eph_1(),
        "eph_2": fig_eph_2(),
        "eph_3": fig_eph_3(),
        "eph_4": fig_eph_4(),
        "eph_5": fig_eph_5(),
        "eph_6": fig_eph_6(),
        "eph_7": fig_eph_7(),


        #INF
        "dept_5": fig_dept_5(),
        "inf_1": fig_inf_1(),
        "inf_2": fig_inf_2(),
        "inf_3": fig_inf_3(),
        "inf_4": fig_inf_4(),
        "inf_5": fig_inf_5(),
        "inf_6": fig_inf_6(),
        "inf_7": fig_inf_7(),


        #RS2M
        "dept_6": fig_dept_6(),
        "rs2m_1": fig_rs2m_1(),
        "rs2m_2": fig_rs2m_2(),
        "rs2m_3": fig_rs2m_3(),
        "rs2m_4": fig_rs2m_4(),
        "rs2m_5": fig_rs2m_5(),
        "rs2m_6": fig_rs2m_6(),
        "rs2m_7": fig_rs2m_7(),

        #RST
        "dept_7": fig_dept_7(),
        "rst_1": fig_rst_1(),
        "rst_2": fig_rst_2(),
        "rst_3": fig_rst_3(),
        "rst_4": fig_rst_4(),
        "rst_5": fig_rst_5(),
        "rst_6": fig_rst_6(),
        "rst_7": fig_rst_7(),

        "dept_8": fig_dept_8(),
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