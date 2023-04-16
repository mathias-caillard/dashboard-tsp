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


valeur_drh_rs2m=valeur_tri[4]
valeur_dire1_rs2m = valeur_trim1[4]
valeur_dire3_rs2m = valeur_trim3[4]



list_fig_rs2m=[]
for i in range(4):
    fig_rs2m = go.Figure()
    fig_rs2m.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][4]))

    fig_rs2m.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_rs2m.append(fig_rs2m)

def fig_rs2m_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_rs2m, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à RS2M', yaxis_title=y_axis_tri[0])

    return fig

def fig_rs2m_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_rs2m, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à RS2M', yaxis_title=y_axis_dire[0])

    return fig

def fig_rs2m_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_rs2m, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à RS2M', yaxis_title=y_axis_dire[2])

    return fig

def fig_rs2m_4():
    fig = list_fig_rs2m[0]
    fig.update_layout(title='Les dépenses de vacataires à RS2M')
    return fig

def fig_rs2m_5():
    fig = list_fig_rs2m[1]
    fig.update_layout(title='Les ressources propres à RS2M')
    return fig

def fig_rs2m_6():
    fig = list_fig_rs2m[2]
    fig.update_layout(title='Les ressources d\'état à RS2M')
    return fig

def fig_rs2m_7():
    fig = list_fig_rs2m[3]
    fig.update_layout(title='Le total des dépenses à RS2M')
    return fig
