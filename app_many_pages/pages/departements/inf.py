import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd
from departement_fig import *


dash.register_page(
    __name__,
    title = "INF",
    name = "INF",
    order=13
                   )

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant le département INF'),



    html.Div(children='''

    '''),

])