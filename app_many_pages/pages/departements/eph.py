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
    title = "EPH",
    name = "EPH",
    order=12
                   )



valeur_drh_eph=valeur_tri[2]
valeur_dire1_eph = valeur_trim1[2]
valeur_dire3_eph = valeur_trim3[2]



list_fig_eph=[]
for i in range(4):
    fig_eph = go.Figure()
    fig_eph.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][2]))

    fig_eph.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_eph.append(fig_eph)

def fig_eph_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_eph, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à EPH', yaxis_title=y_axis_tri[0])

    return fig

def fig_eph_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_eph, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à EPH', yaxis_title=y_axis_dire[0])

    return fig

def fig_eph_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_eph, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à EPH', yaxis_title=y_axis_dire[2])

    return fig

def fig_eph_4():
    return list_fig_eph[0]

def fig_eph_5():
    return list_fig_eph[1]

def fig_eph_6():
    return list_fig_eph[2]

def fig_eph_7():
    return list_fig_eph[3]




layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant le département EPH'),

    dcc.Graph(
        id='example-graph2',
        figure=fig_dept_4(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='example-graph3',
        figure=fig_eph_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_eph_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph5',
        figure=fig_eph_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph6',
        figure=fig_eph_4(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph7',
        figure=fig_eph_5(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph8',
        figure=fig_eph_6(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='example-graph9',
        figure=fig_eph_7(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    html.Div(children='''

    '''),

])