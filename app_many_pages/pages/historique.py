import dash
from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc


dash.register_page(
    __name__,
    title = "Historique",
    name = "Historique",
    order=91,
    active= False

)

annee = range(2015, 2023)


layout = dbc.Container(children=[
    html.H1(
        children='Dans cette page, vous pouvez afficher les graphes de votre choix sur les années précédentes',
        style={'text-align': 'justify'}
    ),

    html.H2(children='Sélections de la plage temporelle:'),
    dcc.RangeSlider(
        id='annee-selector',
        min=min(annee),
        max=max(annee),
        value=[min(annee), max(annee)],
        marks={str(year): str(year) for year in annee},
        step=1
    ),


    html.H2(children='Sélections des graphes à afficher:'),


    ]

)