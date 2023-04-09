#fichier pour indicateurs avec sélection libre selon les departements.

import dash
from dash import html, dcc, Output, Input, State, callback
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd
import dash_bootstrap_components as dbc
from df_fig import fig_nb_etudiants


dash.register_page(
    __name__,
    title = "Choix libre des indicateurs",
    name = "Choix libre des indicateurs",
    order=9
                   )

layout = html.Div(children=[
    html.H1(children='Dans cette page, vous pouvez croiser les directions'),

    html.H2(children='sélection des departements'),
    dcc.Checklist(['ARTEMIS', 'CITI', 'EPH', 'INF','RS2M','RST']),


    dbc.Button(
            "Open collapse",
            id="collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
                
            dcc.Graph(
                figure=fig_nb_etudiants(),
                config = {'displaylogo': False}
                ),

            id="collapse",
            is_open=False,
        ),
])


@callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)


def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

