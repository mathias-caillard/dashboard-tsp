import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd
from dri_fig import *



dash.register_page(
    __name__,
    title = "DRI",
    name = "DRI",
    order=7
                   )




layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la Direction des relations internationales'),

    dcc.Graph(
        id='example-graph',
        figure=fig_dri_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph3',
        figure=fig_dri_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph2',
        figure=fig_dri_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_dri_4(),
        config = {'displaylogo': False}
    ),

    html.Div(children='''
        
    '''),

])