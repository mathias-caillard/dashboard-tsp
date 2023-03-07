import dash
from dash import html, dcc

dash.register_page(
    __name__,
    title = "DRFD",
    name = "DRFD",
    order=3
                   )

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DRFD'),

    html.Div(children='''
        Pas encore d\'indicateur a afficher
    '''),

])