import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd



dash.register_page(
    __name__,
    title = "RS2M",
    name = "RS2M",
    order=14
                   )

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant le département RS2M'),



    html.Div(children='''

    '''),

])