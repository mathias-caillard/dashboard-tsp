import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd



dash.register_page(
    __name__,
    title = "CITI",
    name = "CITI",
    order=11
                   )

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant le département CITI'),



    html.Div(children='''

    '''),

])