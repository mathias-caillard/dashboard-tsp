import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as subplt
from app_many_pages import config
import dash_bootstrap_components as dbc
from dire_fig import *


dash.register_page(
    __name__,
    title = "DIRE",
    name = "DIRE",
    order=4
                   )



layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DIRE'),

    dcc.Graph(
        id='example-graph1',
        figure=fig_dire_1(),
        config = {'displaylogo': False}
        ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='example-graph2',
        figure=fig_dire_2(),
        config = {'displaylogo': False}
        ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph3',
        figure=fig_dire_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_dire_4(),
        config = {'displaylogo': False}
    ),

])