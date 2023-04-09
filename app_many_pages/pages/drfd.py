import random

import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config, effectifs
from drfd_fig import *


dash.register_page(
    __name__,
    title = "DRFD",
    name = "DRFD",
    order=3
                   )



layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DRFD'),

    dcc.Graph(
        id='example-graph1',
        figure=fig_drfd_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph2',
        figure=fig_drfd_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph3',
        figure=fig_drfd_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_drfd_4(),
        config = {'displaylogo': False}
    ),

])