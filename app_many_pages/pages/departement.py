import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import random as rd
import plotly.graph_objects as go
import plotly.subplots as subplt
from app_many_pages import config
from departements.departement_fig import * 

dash.register_page(
    __name__,
    title = "Comparaison départements",
    name = "Comparaison départements",
    order=8
                   )


layout = html.Div(
    style={},
    children=[
    html.H1(children='Bienvenue sur la page concernant les départements de Télécom SudParis'),

    dcc.Graph(
        id='example-graph',
        figure=fig_dept_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  #Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph2',
        figure=fig_dept_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  #Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph3',
        figure=fig_dept_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  #Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_dept_4(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  #Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph5',
        figure=fig_dept_5(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  #Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph6',
        figure=fig_dept_6(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  #Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph7',
        figure=fig_dept_7(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph8',
        figure=fig_dept_8(),
        config = {'displaylogo': False}
    ),


    html.Div(children='''

    '''),

])