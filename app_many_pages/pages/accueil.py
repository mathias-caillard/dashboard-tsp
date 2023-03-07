import dash
from dash import html, dcc

dash.register_page(__name__, path='/', order = 1)

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page d\'accueil'),

    html.Div(children='''
        Vous pouvez naviguer entre les pages en cliquant sur les liens ci-dessus
    '''),

])