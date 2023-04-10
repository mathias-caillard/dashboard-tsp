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
    title = "RST",
    name = "RST",
    order=15
                   )

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant le département RST'),



    html.Div(children='''

    '''),

])