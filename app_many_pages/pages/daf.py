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

    html.Div(children='''
        
    '''),

])