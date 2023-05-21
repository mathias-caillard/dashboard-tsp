import dash
from dash import html, dcc, callback, Output, Input, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as subplt
from app_many_pages import config
import dash_bootstrap_components as dbc
from app_many_pages.dire_fig import *
from app_many_pages.data import *


dash.register_page(
    __name__,
    title = "DIRE",
    name = "DIRE",
    order=4,
    active= False
                   )

titres_graphe_dire = titres_graphe[4:7]
titres_y_dire = titres_y[4:7]

data_dire_pond1 = ponderation(data.data_dire[0])
data_dire_pond2 = ponderation(data.data_dire[1])
data_dire_pond3 = ponderation(data.data_dire[2])
data_dire_pond1_total = ponderation_total(data.data_dire[0])
data_dire_pond2_total = ponderation_total(data.data_dire[1])
data_dire_pond3_total = ponderation_total(data.data_dire[2])

data_dire_pond1.append(data_dire_2023[0])
data_dire_pond2.append(data_dire_2023[1])
data_dire_pond3.append(data_dire_2023[2])
data_dire_pond1_total.append(data_dire_2023_total[0])
data_dire_pond2_total.append(data_dire_2023_total[1])
data_dire_pond3_total.append(data_dire_2023_total[2])

selected_data_dire1 = data_dire_pond1[-1]
selected_data_dire2 = data_dire_pond2[-1]
selected_data_dire3 = data_dire_pond3[-1]
selected_data_dire1_total = data_dire_pond1_total[-1]
selected_data_dire2_total = data_dire_pond2_total[-1]
selected_data_dire3_total = data_dire_pond3_total[-1]

annee = config.liste_annee_maj
selected_annee = annee[-1]

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DIRE'),

    dcc.Graph(
        id='dire-graph1',
        figure=fig_dire_1(),
        config = {'displaylogo': False}
        ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='dire-graph2',
        figure=fig_dire_2(),
        config = {'displaylogo': False}
        ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='dire-graph3',
        figure=fig_dire_3(),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='example-graph1',
        figure=fig_dire_1(),
        config = {'displaylogo': False}
        ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='example-graph2',
        figure=fig_dire_2(),
        config = {'displaylogo': False}
        ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph3',
        figure=fig_dire_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_dire_4(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1',
        figure=fig_old_dire_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1_tri',
        figure=fig_old_dire_1_tri(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1_tot',
        figure=fig_old_dire_1_tot(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph2',
        figure=fig_old_dire_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3',
        figure=fig_old_dire_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3_tri',
        figure=fig_old_dire_3_tri(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3_tot',
        figure=fig_old_dire_3_tot(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph4',
        figure=fig_old_dire_4(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph5',
        figure=fig_old_dire_5(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph5_tri',
        figure=fig_old_dire_5_tri(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph5_tot',
        figure=fig_old_dire_5_tot(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph6',
        figure=fig_old_dire_6(),
        config = {'displaylogo': False}
    ),
])

@callback(
    [Output('dire-graph1', 'figure'), Output('dire-graph2', 'figure'), Output('dire-graph3', 'figure')],
    Input('choix-annee', 'value')
)
def update_graph(selected_year):
    if selected_year == 2023:
        selected_data_dire1 = data_dire_pond1[-1]
        selected_data_dire2 = data_dire_pond2[-1]
        selected_data_dire3 = data_dire_pond3[-1]
        selected_data_dire1_total = data_dire_pond1_total[-1]
        selected_data_dire2_total = data_dire_pond2_total[-1]
        selected_data_dire3_total = data_dire_pond3_total[-1]



        return fig_baton_trimestre(selected_data_dire1,selected_year , titres_graphe_dire[0], titres_y_dire[0]), \
               fig_baton_total(selected_data_dire2_total,selected_year , titres_graphe_dire[1], titres_y_dire[1]), \
               fig_baton_departement(selected_data_dire3,selected_year , titres_graphe_dire[2], titres_y_dire[2])


    else:
        selected_data_dire1 = data_dire_pond1[selected_year - annee[0]]
        selected_data_dire2 = data_dire_pond2[selected_year - annee[0]]
        selected_data_dire3 = data_dire_pond3[selected_year - annee[0]]
        selected_data_dire1_total = data_dire_pond1_total[selected_year - annee[0]]
        selected_data_dire2_total = data_dire_pond2_total[selected_year - annee[0]]
        selected_data_dire3_total = data_dire_pond3_total[selected_year - annee[0]]
        return fig_baton_trimestre(selected_data_dire1,selected_year , titres_graphe_dire[0], titres_y_dire[0]), \
               fig_baton_total(selected_data_dire2_total,selected_year , titres_graphe_dire[1], titres_y_dire[1]), \
               fig_baton_departement(selected_data_dire3,selected_year , titres_graphe_dire[2], titres_y_dire[2])

