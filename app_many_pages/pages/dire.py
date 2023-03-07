import dash
from dash import html, dcc

dash.register_page(
    __name__,
    title = "DIRE",
    name = "DIRE",
    order=4
                   )

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DIRE'),

    html.Div(children='''
        Pas encore d\'indicateur a afficher
    '''),

])