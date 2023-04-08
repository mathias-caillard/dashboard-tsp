#fichier pour indicateurs avec sélection libre selon les departements.

import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd


dash.register_page(
    __name__,
    title = "Choix libre des indicateurs",
    name = "Choix libre des indicateurs",
    order=9
                   )



layout = html.Div(children=[
    html.H1(children='Dans cette page, vous pouvez croiser les directions'),

    html.H2(children='sélection des departements'),
    dcc.Checklist(['ARTEMIS', 'CITI', 'EPH', 'INF','RS2M','RST'])


])