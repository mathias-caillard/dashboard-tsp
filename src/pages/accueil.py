import dash
from dash import html


dash.register_page(
    __name__,
    path='/',
    order = 1,
    active= False)

layout = html.Div(children=[
    html.H1(children='Bienvenue sur l\'application de visualisation des indicateurs de Télécom SudParis'),



])

