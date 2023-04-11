import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app_many_pages import config
import random as rd
from drh_fig import trimestre, valeur_tri,y_axis_tri
from dire_fig import valeur_trim1, valeur_trim3, y_axis as y_axis_dire
from daf_fig import valeur_tri as valeur_daf, y_axis_tri as y_axis_daf

valeur_drh_citi=valeur_tri[1]
valeur_dire1_citi = valeur_trim1[1]
valeur_dire3_citi = valeur_trim3[1]



list_fig_citi=[]
for i in range(4):
    fig_citi = go.Figure()
    fig_citi.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][1]))

    fig_citi.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_citi.append(fig_citi)

def fig_citi_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_citi, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à CITI', yaxis_title=y_axis_tri[0])

    return fig

def fig_citi_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_citi, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à CITI', yaxis_title=y_axis_dire[0])

    return fig

def fig_citi_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_citi, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à CITI', yaxis_title=y_axis_dire[2])

    return fig

def fig_citi_4():
    return list_fig_citi[0]

def fig_citi_5():
    return list_fig_citi[1]

def fig_citi_6():
    return list_fig_citi[2]

def fig_citi_7():
    return list_fig_citi[3]

