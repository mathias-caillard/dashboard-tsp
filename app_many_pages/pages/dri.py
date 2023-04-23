import dash
from dash import html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd
from dri_fig import *

annee = range(2020, 2024)
valeur_evolution = valeur2
label_evolution = labels2


dash.register_page(
    __name__,
    title = "DRI",
    name = "DRI",
    order=7
                   )




layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la Direction des relations internationales'),

    #dcc.Graph(
    #    id='example-graph',
    #    figure=fig_dri_1(),
    #    config = {'displaylogo': False}
    #),

    #html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes
    #graphe redondant

    dcc.Graph(
        id='example-graph3',
        figure=fig_dri_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    html.H3("Sélectionnez une plage d'années :"),
    dcc.RangeSlider(
        id='annee-selector',
        min=min(annee),
        max=max(annee),
        value=[min(annee), max(annee)],
        marks={str(year): str(year) for year in annee},
        step=1
    ),

    dcc.Graph(
        id='example-graph2',
        figure=fig_dri_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_dri_4(),
        config = {'displaylogo': False}
    ),

    html.Div(children='''
        
    '''),

])

# Définir la fonction de rappel pour filtrer les données
@callback(
    Output('example-graph2', 'figure'),
    [Input('annee-selector', 'value')])
def update_graph(selected_years):
    filtered_data = valeur_evolution[4*(selected_years[0] - min(annee)) : 4*(selected_years[1] - min(annee) + 1)]
    filtered_label = label_evolution[4*(selected_years[0] - min(annee)) : 4*(selected_years[1] - min(annee) + 1)]
    # Utiliser les données filtrées pour mettre à jour le graphe en bâton
    fig2 = px.bar(x=filtered_label, y=filtered_data, color=filtered_data)

    # Ajout d'un titre
    fig2.update_layout(title="Evolution temporelle du nombre d'étudiants étrangers à Télécom Sudparis")
    return fig2