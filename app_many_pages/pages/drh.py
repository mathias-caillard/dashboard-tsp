import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
from drh_fig import *

dash.register_page(
    __name__,
    title = "DRH",
    name = "DRH",
    order=6
                   )



layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la Direction des ressources humaines'),

    dcc.Graph(
        id='example-graph',
        figure=fig_drh_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph2',
        figure=fig_drh_2(),
        config = {'displaylogo': False}
    )

])