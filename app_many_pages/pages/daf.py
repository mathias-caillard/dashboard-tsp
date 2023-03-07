import dash
from dash import html, dcc

dash.register_page(
    __name__,
    title = "DAF",
    name = "DAF",
    order=5
                   )

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DAF'),

    html.Div(children='''
        Pas encore d\'indicateur a afficher
    '''),

])