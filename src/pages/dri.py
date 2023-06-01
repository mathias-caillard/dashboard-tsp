import dash
from dash import html, dcc, Input, Output, callback, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src import config
import random as rd
from src.fig.dri_fig import *
from src.data.data import *
from src.functions.fonction_figure import fig_annuelle_baton, fig_camembert, fig_trim_baton, fig_trim_courbe, couleurs, couleurs_all
from src.functions.fonctions_historique import *

annee = range(2020, 2024)
valeur_evolution = valeur2
label_evolution = labels2

selected_data = data_dri_2023
label_dri = labels
y_axis_dri = y_axis2


dash.register_page(
    __name__,
    title = "DRI",
    name = "DRI",
    order=7,
    active= False
                   )


def liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_annee) :
    return [
        dcc.Graph(
            id='dri1_bat',
            figure=fig_trim_baton("DRI-01", selected_annee, "Temps", None),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dri2_bat',
            figure=fig_trim_baton("DRI-02", selected_annee, "Temps", None),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dri3_bat',
            figure=fig_trim_baton("DRI-03", selected_annee, "Temps", None),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dri4_bat',
            figure=fig_trim_baton("DRI-04", selected_annee, "Temps", None),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dri5_bat',
            figure=fig_trim_baton("DRI-05", selected_annee, "Temps", None),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dri6_tot',
            figure=fig_annuelle_baton("DRI-06", selected_annee, "", None),
            config={'displaylogo': False}
        ),

    ]

layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant la Direction des Relations Internationales',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-dri", color = "black", type = "circle"),



    #joue le rôle de variable globale
    dcc.Store(id='current-value-dri', data=[]),
    #Menu déourlant/moteur de recherche
    dcc.Dropdown(
        options=categories_historique,
        id="checklist-input-dri",
        multi=True,
        placeholder="Veuillez selectionner des graphes à afficher.",
        persistence = True,
        value = [

        ],
        disabled = True,
        style={"display": "none"}
    ),
    # Boucle pour générer les graphiques
            dbc.Container(id="graph-container-historique-dri",
                children=[],
                fluid = True),
    ],
fluid = True
)




#Mettre à jour les données du menu déroulant sélectionnées
@callback(
    Output("current-value-dri", "data"),
    [Input("checklist-input-dri", "value")],
    [State("current-value-dri", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return update_old_value_(value, old_value) #dans fonctions_historique.py


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories_historique):
    cat_id = cat["value"]


    @callback(
        Output(f"current_collapse-dri{i + 1}", "is_open"),
        [Input("checklist-input-dri", "value")],
        [State(f"collapse-dri{i + 1}", "is_open"), State("current-value-dri", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        return toggle_collapse_(value, is_open, data, cat_id=cat_id)

@callback(
    [Output("graph-container-historique-dri", "children"),
     Output("loading-dri", "parent-style")], #Permet d'afficher un Spinner de Char
    [Input("choix-annee", "value"),
     Input("checklist-input-dri", "value"),
     ]
)

def generate_graphs(selected_year, value):
    return generate_graphs_(selected_year, value, baseline_graph = liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_year))
