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
    fig = list_fig_eph[0]
    fig.update_layout(title='Les dépenses de vacataires à EPH')
    return fig

def fig_eph_5():
    fig = list_fig_eph[1]
    fig.update_layout(title='Les ressources propres à EPH')
    return fig

def fig_eph_6():
    fig = list_fig_eph[2]
    fig.update_layout(title='Les ressources d\'état à EPH')
    return fig

def fig_eph_7():
    fig = list_fig_eph[3]
    fig.update_layout(title='Le total des dépenses à EPH')
    return fig

