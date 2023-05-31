import dash
from dash import html, dcc, callback, Output, Input, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src import config
from src.fig.drh_fig import *
from src.data.data import *
from src.functions.fonction_figure import fig_annuelle_baton, fig_camembert, fig_trim_baton, fig_trim_courbe, couleurs, couleurs_all
from src.functions.fonctions_historique import *

dash.register_page(
    __name__,
    title = "DRH",
    name = "DRH",
    order=6,
    active= False
                   )

titres_graphe_drh = titres_graphe[9:11]
titres_y_drh = titres_y[9:11]


data_drh_1 = data.data.data_drh[0]
TAB = []
for data_annee in data_drh_1:
    tab=[]
    for data_dept in data_annee:
        tab.append(sum(data_dept)/4)
    TAB.append(tab)
data_drh_1=TAB
data_drh_2 = data.data.data_drh[1]
data_drh_1.append(data_drh_2023_1)
data_drh_2.append(data_drh_2023_2)


selected_data_drh1 = data_drh_1[-1]
selected_data_drh2 = data_drh_2[-1]



def liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_annee) :

    return [
        dcc.Graph(
            id='drh1_tot',
            figure=fig_annuelle_baton("DRH-01", selected_annee, "Services/Départements", couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh1_cam',
            figure=fig_camembert("DRH-01", selected_annee, couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh2_tot',
            figure=fig_annuelle_baton("DRH-02", selected_annee, "Services/Départements", couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh2_cam',
            figure=fig_camembert("DRH-02", selected_annee, couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_bat',
            figure=fig_trim_baton("DRH-03", selected_annee, "Départements", couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_cou',
            figure=fig_trim_courbe("DRH-03", selected_annee, couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_tot',
            figure=fig_annuelle_baton("DRH-03", selected_annee, "Départements", couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_cam',
            figure=fig_camembert("DRH-03", selected_annee, couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh4_tot',
            figure=fig_annuelle_baton("DRH-04", selected_annee, "Services/Départements", couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh4_cam',
            figure=fig_camembert("DRH-04", selected_annee, couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh5_tot',
            figure=fig_annuelle_baton("DRH-05", selected_annee, "Services/Départements", couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh5_cam',
            figure=fig_camembert("DRH-05", selected_annee, couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh6_tot',
            figure=fig_annuelle_baton("DRH-06", selected_annee, "Services/Départements", couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh6_cam',
            figure=fig_camembert("DRH-06", selected_annee, couleurs_all),
            config={'displaylogo': False}
        ),

    ]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant la Direction des Ressources Humaines',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-drh", color = "black", type = "circle"),


    #joue le rôle de variable globale
    dcc.Store(id='current-value-drh', data=[]),
    #Menu déourlant/moteur de recherche
    dcc.Dropdown(
        options=categories,
        id="checklist-input-drh",
        multi=True,
        placeholder="Veuillez selectionner des graphes à afficher.",
        persistence = True,
        value = [

                 
        ],
        disabled = True,
        style={"display": "none"}
    ),
    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-drh",
                children=[],
                fluid = True),
    ],
fluid = True
)










#Mettre à jour les données du menu déroulant sélectionnées
@callback(
    Output("current-value-drh", "data"),
    [Input("checklist-input-drh", "value")],
    [State("current-value-drh", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return update_old_value_(value, old_value) #dans fonctions_historique.py


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories):
    cat_id = cat["value"]


    @callback(
        Output(f"current_collapse-drh{i + 1}", "is_open"),
        [Input("checklist-input-drh", "value")],
        [State(f"collapse-drh{i + 1}", "is_open"), State("current-value-drh", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        return toggle_collapse_(value, is_open, data, cat_id=cat_id)

@callback(
    [Output("graph-container-historique-drh", "children"),
     Output("loading-drh", "parent-style")], #Permet d'afficher un Spinner de Char
    [Input("choix-annee", "value"),
     Input("checklist-input-drh", "value"),
     ]
)

def generate_graphs(selected_year, value):
    return generate_graphs_(selected_year, value, baseline_graph = liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_year))


"""
dcc.Graph(
        id='drh-graph1',
        figure=fig_baton_total(selected_data_drh1,selected_annee , titres_graphe_drh[0], titres_y_drh[0]),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='drh-graph2',
        figure=fig_baton_trimestre(selected_data_drh2,selected_annee , titres_graphe_drh[1], titres_y_drh[1]),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='example-graph',
        figure=fig_drh_1(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='example-graph2',
        figure=fig_drh_2(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph3',
        figure=fig_drh_3(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph4',
        figure=fig_drh_4(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph1',
        figure=fig_old_drh_1(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph1_tri',
        figure=fig_old_drh_1_tri(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph1_tot',
        figure=fig_old_drh_1_tot(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph2',
        figure=fig_old_drh_2(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph3',
        figure=fig_old_drh_3(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph3_tri',
        figure=fig_old_drh_3_tri(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph3_tot',
        figure=fig_old_drh_3_tot(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph4',
        figure=fig_old_drh_4(),
        config = {'displaylogo': False}
    ),

"""

"""
"drh_old_1_tri",
                 "drh_old_1_tot",
                 "drh_old_1_comp",
                "drh_old_2_tri",
                 "drh_old_2_tot",
                 "drh_old_2_comp",
"""