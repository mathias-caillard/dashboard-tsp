import dash
from dash import html, dcc

dash.register_page(
    __name__,
    title = "A propos",
    name = "a-propos",
    order=10,
    active= False
                   )


layout = html.Div([
    html.H1("À propos"),
    html.P("Cette application a été développée dans le cadre d'un projet Cassiopée, à Télécom SudParis")
    ])