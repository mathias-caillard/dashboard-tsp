import dash
from dash import html, dcc, callback, Output, Input, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src import config
from src.daf_fig import *
from src.data import *


dash.register_page(
    __name__,
    title = "DAF",
    name = "DAF",
    order=5,
    active= False
                   )

titres_graphe_daf = titres_graphe[1:4]
titres_y_daf = titres_y[1:4]

data_daf_pond1 = ponderation(data.data_daf[0])
data_daf_pond2 = ponderation(data.data_daf[1])
data_daf_pond3 = ponderation(data.data_daf[2])
data_daf_pond1_total = ponderation_total(data.data_daf[0])
data_daf_pond2_total = ponderation_total(data.data_daf[1])
data_daf_pond3_total = ponderation_total(data.data_daf[2])

data_daf_pond1.append(data_daf_2023[0])
data_daf_pond2.append(data_daf_2023[1])
data_daf_pond3.append(data_daf_2023[2])
data_daf_pond1_total.append(data_daf_2023_total[0])
data_daf_pond2_total.append(data_daf_2023_total[1])
data_daf_pond3_total.append(data_daf_2023_total[2])

selected_data_daf1 = data_daf_pond1[-1]
selected_data_daf2 = data_daf_pond2[-1]
selected_data_daf3 = data_daf_pond3[-1]
selected_data_daf1_total = data_daf_pond1_total[-1]
selected_data_daf2_total = data_daf_pond2_total[-1]
selected_data_daf3_total = data_daf_pond3_total[-1]

annee = config.liste_annee_maj
selected_annee = annee[-1]



layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DAF'),

    dcc.Graph(
        id='daf-graph1',
        figure=fig_baton_trimestre(selected_data_daf1, selected_annee, titres_graphe_daf[0], titres_y_daf[0]),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='daf-graph2',
        figure=fig_baton_total(selected_data_daf2_total, selected_annee, titres_graphe_daf[1], titres_y_daf[1]),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='daf-graph3',
        figure=fig_baton_departement(selected_data_daf3, selected_annee, titres_graphe_daf[2], titres_y_daf[2]),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='example-graph1',
        figure=fig_daf_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph2',
        figure=fig_daf_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph3',
        figure=fig_daf_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_daf_4(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph5',
        figure=fig_daf_5(),
        config = {'displaylogo': False}
    ),


    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph6',
        figure=fig_daf_6(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph7',
        figure=fig_daf_7(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph8',
        figure=fig_daf_8(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph9',
        figure=fig_daf_9(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1',
        figure=fig_old_daf_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1_tri',
        figure=fig_old_daf_1_tri(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1_tot',
        figure=fig_old_daf_1_tot(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph2',
        figure=fig_old_daf_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3',
        figure=fig_old_daf_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3_tri',
        figure=fig_old_daf_3_tri(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3_tot',
        figure=fig_old_daf_3_tot(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph4',
        figure=fig_old_daf_4(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph5',
        figure=fig_old_daf_5(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph5_tri',
        figure=fig_old_daf_5_tri(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph5_tot',
        figure=fig_old_daf_5_tot(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph6',
        figure=fig_old_daf_6(),
        config = {'displaylogo': False}
    ),
])


@callback(
    [Output('daf-graph1', 'figure'), Output('daf-graph2', 'figure'), Output('daf-graph3', 'figure')],
    Input('choix-annee', 'value')
)
def update_graph(selected_year):
    if selected_year == 2023:
        selected_data_daf1 = data_daf_pond1[-1]
        selected_data_daf2 = data_daf_pond2[-1]
        selected_data_daf3 = data_daf_pond3[-1]
        selected_data_daf1_total = data_daf_pond1_total[-1]
        selected_data_daf2_total = data_daf_pond2_total[-1]
        selected_data_daf3_total = data_daf_pond3_total[-1]

        return fig_baton_trimestre(selected_data_daf1, selected_year, titres_graphe_daf[0], titres_y_daf[0]), \
               fig_baton_total(selected_data_daf2_total, selected_year, titres_graphe_daf[1], titres_y_daf[1]), \
               fig_baton_departement(selected_data_daf3, selected_year, titres_graphe_daf[2], titres_y_daf[2])


    else:
        selected_data_daf1 = data_daf_pond1[selected_year - annee[0]]
        selected_data_daf2 = data_daf_pond2[selected_year - annee[0]]
        selected_data_daf3 = data_daf_pond3[selected_year - annee[0]]
        selected_data_daf1_total = data_daf_pond1_total[selected_year - annee[0]]
        selected_data_daf2_total = data_daf_pond2_total[selected_year - annee[0]]
        selected_data_daf3_total = data_daf_pond3_total[selected_year - annee[0]]
        return fig_baton_trimestre(selected_data_daf1, selected_year, titres_graphe_daf[0], titres_y_daf[0]), \
               fig_baton_total(selected_data_daf2_total, selected_year, titres_graphe_daf[1], titres_y_daf[1]), \
               fig_baton_departement(selected_data_daf3, selected_year, titres_graphe_daf[2], titres_y_daf[2])
