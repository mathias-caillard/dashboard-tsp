import dash
from dash import html, dcc, callback, Output, Input, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src import config
from src.drh_fig import *
from src.data import *

dash.register_page(
    __name__,
    title = "DRH",
    name = "DRH",
    order=6,
    active= False
                   )

titres_graphe_drh = titres_graphe[9:11]
titres_y_drh = titres_y[9:11]


data_drh_1 = data.data_drh[0]
TAB = []
for data_annee in data_drh_1:
    tab=[]
    for data_dept in data_annee:
        tab.append(sum(data_dept)/4)
    TAB.append(tab)
data_drh_1=TAB
data_drh_2 = data.data_drh[1]
data_drh_1.append(data_drh_2023_1)
data_drh_2.append(data_drh_2023_2)


selected_data_drh1 = data_drh_1[-1]
selected_data_drh2 = data_drh_2[-1]
annee = config.liste_annee_maj
selected_annee = annee[-1]

layout = html.Div(children=[
    html.H1(
        children='Bienvenue sur la page concernant la Direction des ressources humaines',
        style={'text-align': 'justify'}
    ),

    dcc.Graph(
        id='drh-graph1',
        figure=fig_baton_total(selected_data_drh1,selected_annee , titres_graphe_drh[0], titres_y_drh[0]),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='drh-graph2',
        figure=fig_baton_trimestre(selected_data_drh2,selected_annee , titres_graphe_drh[1], titres_y_drh[1]),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph',
        figure=fig_drh_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph2',
        figure=fig_drh_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph3',
        figure=fig_drh_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_drh_4(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1',
        figure=fig_old_drh_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1_tri',
        figure=fig_old_drh_1_tri(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1_tot',
        figure=fig_old_drh_1_tot(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph2',
        figure=fig_old_drh_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3',
        figure=fig_old_drh_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3_tri',
        figure=fig_old_drh_3_tri(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3_tot',
        figure=fig_old_drh_3_tot(),
        config={'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph4',
        figure=fig_old_drh_4(),
        config = {'displaylogo': False}
    ),

])

@callback(
    [Output('drh-graph1', 'figure'), Output('drh-graph2', 'figure')],
    Input('choix-annee', 'value')
)
def update_graph(selected_year):
    if selected_year == 2023:
        selected_data_drh1 = data_drh_1[-1]
        selected_data_drh2 = data_drh_2[-1]

        return fig_baton_total(selected_data_drh1,selected_year , titres_graphe_drh[0], titres_y_drh[0]), \
               fig_baton_trimestre(selected_data_drh2,selected_year , titres_graphe_drh[1], titres_y_drh[1])

    else:
        selected_data_drh1 = data_drh_1[selected_year - annee[0]]
        selected_data_drh2 = data_drh_2[selected_year - annee[0]]
        return fig_baton_total(selected_data_drh1,selected_year , titres_graphe_drh[0], titres_y_drh[0]), \
               fig_baton_trimestre(selected_data_drh2, selected_year, titres_graphe_drh[1], titres_y_drh[1])