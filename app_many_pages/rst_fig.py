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


valeur_drh_rst=valeur_tri[5]
valeur_dire1_rst = valeur_trim1[5]
valeur_dire3_rst = valeur_trim3[5]



list_fig_rst=[]
for i in range(4):
    fig_rst = go.Figure()
    fig_rst.add_trace(go.Bar(x=trimestre, y=valeur_daf[i][5]))

    fig_rst.update_layout(yaxis_title = y_axis_daf[i])
    list_fig_rst.append(fig_rst)

def fig_rst_1():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_drh_rst, name=y_axis_tri[0]))
    fig.update_layout(title='Les ressources humaines à RST', yaxis_title=y_axis_tri[0])

    return fig

def fig_rst_2():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire1_rst, name=y_axis_dire[0]))
    fig.update_layout(title='Les contrats de recherche à RST', yaxis_title=y_axis_dire[0])

    return fig

def fig_rst_3():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=trimestre, y=valeur_dire3_rst, name=y_axis_dire[2]))
    fig.update_layout(title='La contribution au financement de l\'école à RST', yaxis_title=y_axis_dire[2])

    return fig

def fig_rst_4():
    fig = list_fig_rst[0]
    fig.update_layout(title='Les dépenses de vacataires à RST')
    return fig

def fig_rst_5():
    fig = list_fig_rst[1]
    fig.update_layout(title='Les ressources propres à RST')
    return fig

def fig_rst_6():
    fig = list_fig_rst[2]
    fig.update_layout(title='Les ressources d\'état à RST')
    return fig
def fig_rst_7():
    fig = list_fig_rst[3]
    fig.update_layout(title='Le total des dépenses à RST')
    return fig
