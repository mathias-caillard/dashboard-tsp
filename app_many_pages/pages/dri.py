import dash
from dash import html, dcc

dash.register_page(
    __name__,
    title = "Direction des relations internationales",
    name = "Direction des relations internationales",
    order=7
                   )

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la Direction des relations internationales'),

    html.Div(children='''
        Pas encore d\'indicateur a afficher
    '''),

])