import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
from daf_fig import * 


dash.register_page(
    __name__,
    title = "DAF",
    name = "DAF",
    order=5
                   )


layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DAF'),

    dcc.Graph(
        id='example-graph',
        figure=fig_daf_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-grap2',
        figure=fig_daf_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-grap3',
        figure=fig_daf_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-grap4',
        figure=fig_daf_4(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-grap5',
        figure=fig_daf_5(),
        config = {'displaylogo': False}
    ),


    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-grap4',
        figure=fig_daf_6(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-grap5',
        figure=fig_daf_7(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-grap4',
        figure=fig_daf_8(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-grap5',
        figure=fig_daf_9(),
        config = {'displaylogo': False}
    ),
    html.Div(children='''
        
    '''),

])