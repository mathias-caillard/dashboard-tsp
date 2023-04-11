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


valeur_drh_inf=valeur_tri[3]
valeur_dire1_inf = valeur_trim1[3]
valeur_dire3_inf = valeur_trim3[3]



list_fig_inf=[]
for i in range(4):
    fig_inf = go.Figure()
    fig_inf.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][3]))

    fig_inf.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_inf.append(fig_inf)

def fig_inf_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_inf, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à INF', yaxis_title=y_axis_tri[0])

    return fig

def fig_inf_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_inf, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à INF', yaxis_title=y_axis_dire[0])

    return fig

def fig_inf_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_inf, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à INF', yaxis_title=y_axis_dire[2])

    return fig

def fig_inf_4():
    return list_fig_inf[0]

def fig_inf_5():
    return list_fig_inf[1]

def fig_inf_6():
    return list_fig_inf[2]

def fig_inf_7():
    return list_fig_inf[3]
