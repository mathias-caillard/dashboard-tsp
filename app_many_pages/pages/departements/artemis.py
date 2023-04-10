import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd
from departement_fig import *
from drh_fig import trimestre, valeur_tri,y_axis_tri
from dire_fig import valeur_trim1, valeur_trim3, y_axis as y_axis_dire
from daf_fig import valeur_tri as valeur_daf, y_axis_tri as y_axis_daf



dash.register_page(
    __name__,
    title = "ARTEMIS",
    name = "ARTEMIS",
    order=10
                   )



valeur_drh_artemis=valeur_tri[0]
valeur_dire1_artemis = valeur_trim1[0]
valeur_dire3_artemis = valeur_trim3[0]



list_fig_artemis=[]
for i in range(4):
    fig_artemis = go.Figure()
    fig_artemis.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][0]))

    fig_artemis.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_artemis.append(fig_artemis)

def fig_artemis_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_artemis, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à ARTEMIS', yaxis_title=y_axis_tri[0])

    return fig

def fig_artemis_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_artemis, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à ARTEMIS', yaxis_title=y_axis_dire[0])

    return fig

def fig_artemis_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_artemis, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à ARTEMIS', yaxis_title=y_axis_dire[2])

    return fig

def fig_artemis_4():
    return list_fig_artemis[0]

def fig_artemis_5():
    return list_fig_artemis[1]

def fig_artemis_6():
    return list_fig_artemis[2]

def fig_artemis_7():
    return list_fig_artemis[3]

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant le département ARTEMIS'),

    dcc.Graph(
        id='example-graph',
        figure=fig_dept_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph2',
        figure=fig_dept_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='example-graph3',
        figure=fig_artemis_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_artemis_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph5',
        figure=fig_artemis_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph6',
        figure=fig_artemis_4(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph7',
        figure=fig_artemis_5(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph8',
        figure=fig_artemis_6(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='example-graph9',
        figure=fig_artemis_7(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    html.Div(children='''

    '''),

])