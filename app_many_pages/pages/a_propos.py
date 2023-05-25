import dash
from dash import html, dcc

dash.register_page(
    __name__,
    title = "A propos",
    name = "a-propos",
    order=17,
    active= False
                   )


layout = html.Div([
    html.H1("À propos"),
    html.P("Cette application a été développée en 2023 par JACQUET Marin et CAILLARD Mathias, deux étudiant en 2ème année à Télécom SudParis. Le projet a étéencadré par Bruno DEFUDE par Benoît JEAN dans le cadre d'un 'projet Cassiopée'"),
    html.P("Contact : "),
    html.A("marin.jacquet@telecom-sudparis.com", href="mailto:marin.jacquet@telecom-sudparis.eu"),
    html.Br(),
    html.A("mathias.caillard@telecom-sudparis.com", href="mailto:mathias.caillard@telecom-sudparis.eu"),
    html.Br(),

    ])