import dash
from dash import html, dcc

dash.register_page(
    __name__,
    title = "Direction des ressources humaines",
    name = "Direction des ressources humaines",
    order=6
                   )

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la Direction des ressources humaines'),

    html.Div(children='''
        Pas encore d\'indicateur a afficher
    '''),

])