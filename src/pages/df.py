import dash
from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from src.fig import daf_fig, df_fig, dire_fig, drfd_fig, drh_fig, dri_fig, artemis_fig, citi_fig, eph_fig, inf_fig, rs2m_fig, rst_fig
from src import config
import data
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
    title="DF",
    name="DF",
    order=2,
    active= False
    )


def liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_annee) :
    return [
    dcc.Graph(
        id='df1_bat',
        figure=fig_annuelle_baton("DF-01", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}

    ),


    dcc.Graph(
        id='df1_cam',
        figure=fig_camembert("DF-01", selected_annee, couleurs),
        config = {'displaylogo': False}

    ),


    dcc.Graph(
        id='df2_bat',
        figure=fig_trim_baton("DF-02", selected_annee, "Temps", None),
        config = {'displaylogo': False}

    ),


    dcc.Graph(
        id='df3_bat',
        figure=fig_trim_baton("DF-03", selected_annee, "Temps", None),
        config = {'displaylogo': False}

    ),


    dcc.Graph(
        id='df4_bat',
        figure=fig_trim_baton("DF-04", selected_annee, "Temps", None),
        config={'displaylogo': False}

    ),


    dcc.Graph(
        id='df5_bat',
        figure=fig_trim_baton("DF-05", selected_annee, "Temps", None),
        config={'displaylogo': False}

    ),


    dcc.Graph(
        id='df6_bat',
        figure=fig_trim_baton("DF-06", selected_annee, "Temps", None),
        config={'displaylogo': False}

    )
]



layout = dbc.Container(children=[
    dcc.Loading(id = "loading-df", color = "black", type = "circle"),
    html.H2(children='Sélection de l\'année :'),
                    dcc.Dropdown(
                    id = "annee-selector-df",
                    options = annee,
                    multi = False,
                    value=annee[0]
                ),
    #joue le rôle de variable globale
    dcc.Store(id='current-value-df', data=[]),
    #Menu déourlant/moteur de recherche
    dcc.Dropdown(
        options=categories,
        id="checklist-input-df",
        multi=True,
        placeholder="Veuillez selectionner des graphes à afficher.",
        persistence = True,
        value = [
                 "df_old_1_tri",
                 "df_old_1_tot",
                 "df_old_1_comp",
                 "df_1",
                 "df_2"
        ],
        disabled = True,
        style={"display": "none"}
    ),
    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-df",
                children=[],
                fluid = True),
    ],
fluid = True
)










#Mettre à jour les données du menu déroulant sélectionnées
@callback(
    Output("current-value-df", "data"),
    [Input("checklist-input-df", "value")],
    [State("current-value-df", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return update_old_value_(value, old_value) #dans fonctions_historique.py


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories):
    cat_id = cat["value"]


    @callback(
        Output(f"current_collapse-df{i + 1}", "is_open"),
        [Input("checklist-input-df", "value")],
        [State(f"collapse-df{i + 1}", "is_open"), State("current-value-df", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        return toggle_collapse_(value, is_open, data, cat_id=cat_id)

@callback(
    [Output("graph-container-historique-df", "children"),
     Output("loading-df", "parent-style")], #Permet d'afficher un Spinner de Char
    [Input("annee-selector-df", "value"),
     Input("checklist-input-df", "value"),
     ]
)

def generate_graphs(selected_year, value):
    return generate_graphs_(selected_year, value, baseline_graph = liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_year))





