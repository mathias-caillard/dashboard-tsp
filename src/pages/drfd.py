import dash
from dash import html, dcc, Input, Output, State, callback
from src.fig.drfd_fig import *
from src.data.data import *
from src.functions.fonction_figure import fig_annuelle_baton, fig_camembert, fig_trim_baton
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
from flask import Flask, session
from src.functions.fonctions_historique import *
from src.functions.fonction_figure import *

from src.data.data import *
import dash
from dash import html, dcc, dash_table, Output, Input, callback

from src.fig.df_fig import *

from src.data.data import new_donnee, new_titre_y, new_labels, dict_titres
from src.data.data import *
from src.functions.fonction_figure import fig_annuelle_baton, fig_camembert, fig_trim_baton, couleurs


dash.register_page(
    __name__,
    title = "DRFD",
    name = "DRFD",
    order=3,
    active= False
                   )
def liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_annee) :
    return [
dcc.Graph(
        id='drfd1_tot',
        figure=fig_annuelle_baton("DRFD-01", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='drfd1_cam',
        figure=fig_camembert("DRFD-01", selected_annee, couleurs),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='drfd2_tot',
        figure=fig_annuelle_baton("DRFD-02", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='drfd2_cam',
        figure=fig_camembert("DRFD-02", selected_annee, couleurs),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='drfd3_tot',
        figure=fig_annuelle_baton("DRFD-03", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}
    ),


]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant la DRFD',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-drfd", color = "black", type = "circle"),


    #joue le rôle de variable globale
    dcc.Store(id='current-value-drfd', data=[]),
    #Menu déourlant/moteur de recherche
    dcc.Dropdown(
        options=categories,
        id="checklist-input-drfd",
        multi=True,
        placeholder="Veuillez selectionner des graphes à afficher.",
        persistence = True,
        value = [

        ],
        disabled = True,
        style={"display": "none"}
    ),
    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-drfd",
                children=[],
                fluid = True),
    ],
fluid = True
)










#Mettre à jour les données du menu déroulant sélectionnées
@callback(
    Output("current-value-drfd", "data"),
    [Input("checklist-input-drfd", "value")],
    [State("current-value-drfd", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return update_old_value_(value, old_value) #dans fonctions_historique.py


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories):
    cat_id = cat["value"]


    @callback(
        Output(f"current_collapse-drfd{i + 1}", "is_open"),
        [Input("checklist-input-drfd", "value")],
        [State(f"collapse-drfd{i + 1}", "is_open"), State("current-value-drfd", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        return toggle_collapse_(value, is_open, data, cat_id=cat_id)

@callback(
    [Output("graph-container-historique-drfd", "children"),
     Output("loading-drfd", "parent-style")], #Permet d'afficher un Spinner de Char
    [Input("choix-annee", "value"),
     Input("checklist-input-drfd", "value"),
     ]
)

def generate_graphs(selected_year, value):
    return generate_graphs_(selected_year, value, baseline_graph = liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_year))


"""
"drfd_old_1_comp",
            "drfd_old_1_tri",
            "drfd_old_1_tot",
            "drfd_old_2_comp",
            "drfd_old_2_tri",
            "drfd_old_2_tot"
"""


