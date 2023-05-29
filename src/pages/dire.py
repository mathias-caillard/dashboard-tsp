import dash
from dash import html, dcc, callback, Output, Input, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as subplt
from src import config
import dash_bootstrap_components as dbc
from src.fig.dire_fig import *
from src.data.data import *
from src.functions.fonction_figure import fig_annuelle_baton, fig_camembert, fig_trim_baton, fig_trim_courbe, couleurs
from src.functions.fonctions_historique import *


dash.register_page(
    __name__,
    title = "DIRE",
    name = "DIRE",
    order=4,
    active= False
                   )

titres_graphe_dire = titres_graphe[4:7]
titres_y_dire = titres_y[4:7]

data_dire_pond1 = ponderation(data.data.data_dire[0])
data_dire_pond2 = ponderation(data.data.data_dire[1])
data_dire_pond3 = ponderation(data.data.data_dire[2])
data_dire_pond1_total = ponderation_total(data.data.data_dire[0])
data_dire_pond2_total = ponderation_total(data.data.data_dire[1])
data_dire_pond3_total = ponderation_total(data.data.data_dire[2])

data_dire_pond1.append(data_dire_2023[0])
data_dire_pond2.append(data_dire_2023[1])
data_dire_pond3.append(data_dire_2023[2])
data_dire_pond1_total.append(data_dire_2023_total[0])
data_dire_pond2_total.append(data_dire_2023_total[1])
data_dire_pond3_total.append(data_dire_2023_total[2])

selected_data_dire1 = data_dire_pond1[-1]
selected_data_dire2 = data_dire_pond2[-1]
selected_data_dire3 = data_dire_pond3[-1]
selected_data_dire1_total = data_dire_pond1_total[-1]
selected_data_dire2_total = data_dire_pond2_total[-1]
selected_data_dire3_total = data_dire_pond3_total[-1]


def liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_annee) :
    return [
        dcc.Graph(
            id='dire1_bat',
            figure=fig_trim_baton("DIRE-01", selected_annee, "Départements", couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire1_cou',
            figure=fig_trim_courbe("DIRE-01", selected_annee, couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire1_cam',
            figure=fig_camembert("DIRE-01", selected_annee, couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire2_bat',
            figure=fig_trim_baton("DIRE-02", selected_annee, "Départements", couleurs),
            config={'displaylogo': False}
        ),

            dcc.Graph(
                id='dire2_cou',
                figure=fig_trim_courbe("DIRE-02", selected_annee, couleurs),
                config={'displaylogo': False}
            ),

            dcc.Graph(
                id='dire2_cam',
                figure=fig_camembert("DIRE-02", selected_annee, couleurs),
                config={'displaylogo': False}
            ),

            dcc.Graph(
                id='dire3_bat',
                figure=fig_trim_baton("DIRE-03", selected_annee, "Départements", couleurs),
                config={'displaylogo': False}
            ),

                dcc.Graph(
                    id='dire3_cou',
                    figure=fig_trim_courbe("DIRE-03", selected_annee, couleurs),
                    config={'displaylogo': False}
                ),

                dcc.Graph(
                    id='dire3_cam',
                    figure=fig_camembert("DIRE-03", selected_annee, couleurs),
                    config={'displaylogo': False}
                )

        ]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant la DIRE',
        style={'text-align': 'justify'}
        ),
            dcc.Loading(id = "loading-dire", color = "black", type = "circle"),

            #joue le rôle de variable globale
            dcc.Store(id='current-value-dire', data=[]),
            #Menu déourlant/moteur de recherche
            dcc.Dropdown(
                options=categories,
                id="checklist-input-dire",
                multi=True,
                placeholder="Veuillez selectionner des graphes à afficher.",
                persistence = True,
                value = [

                ],
                disabled = True,
                style={"display": "none"}
            ),
            # Boucle pour générer les graphiques
                    dbc.Container(id="graph-container-historique-dire",
                        children=[],
                        fluid = True),
            ],
        fluid = True
        )










#Mettre à jour les données du menu déroulant sélectionnées
@callback(
            Output("current-value-dire", "data"),
            [Input("checklist-input-dire", "value")],
            [State("current-value-dire", "data")],
            prevent_initial_call=True
        )
def update_old_value(value, old_value):
            return update_old_value_(value, old_value) #dans fonctions_historique.py


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories):
    cat_id = cat["value"]


    @callback(
                Output(f"current_collapse-dire{i + 1}", "is_open"),
                [Input("checklist-input-dire", "value")],
                [State(f"collapse-dire{i + 1}", "is_open"), State("current-value-dire", "data")],
                prevent_initial_call=True
            )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        return toggle_collapse_(value, is_open, data, cat_id=cat_id)

@callback(
            [Output("graph-container-historique-dire", "children"),
             Output("loading-dire", "parent-style")], #Permet d'afficher un Spinner de Char
            [Input("choix-annee", "value"),
             Input("checklist-input-dire", "value"),
             ]
        )

def generate_graphs(selected_year, value):
    return generate_graphs_(selected_year, value, baseline_graph = liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_year))





"""
dcc.Graph(
        id='dire-graph1',
        figure=fig_baton_trimestre(selected_data_dire1,selected_annee , titres_graphe_dire[0], titres_y_dire[0]),
        config = {'displaylogo': False}
        ),




    dcc.Graph(
        id='dire-graph2',
        figure= fig_baton_total(selected_data_dire2_total,selected_annee , titres_graphe_dire[1], titres_y_dire[1]),
        config = {'displaylogo': False}
        ),



    dcc.Graph(
        id='dire-graph3',
        figure=fig_baton_departement(selected_data_dire3,selected_annee , titres_graphe_dire[2], titres_y_dire[2]),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='example-graph1',
        figure=fig_dire_1(),
        config = {'displaylogo': False}
        ),




    dcc.Graph(
        id='example-graph2',
        figure=fig_dire_2(),
        config = {'displaylogo': False}
        ),



    dcc.Graph(
        id='example-graph3',
        figure=fig_dire_3(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph4',
        figure=fig_dire_4(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph1',
        figure=fig_old_dire_1(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph1_tri',
        figure=fig_old_dire_1_tri(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph1_tot',
        figure=fig_old_dire_1_tot(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph2',
        figure=fig_old_dire_2(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph3',
        figure=fig_old_dire_3(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph3_tri',
        figure=fig_old_dire_3_tri(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph3_tot',
        figure=fig_old_dire_3_tot(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph4',
        figure=fig_old_dire_4(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph5',
        figure=fig_old_dire_5(),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='old-graph5_tri',
        figure=fig_old_dire_5_tri(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph5_tot',
        figure=fig_old_dire_5_tot(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph6',
        figure=fig_old_dire_6(),
        config = {'displaylogo': False}
    ),
"""

"""
"dire_old_1_tri",
            "dire_old_1_tot",
            "dire_old_1_comp",
            "dire_old_2_tri",
            "dire_old_2_tot",
            "dire_old_2_comp",
            "dire_old_3_tri",
            "dire_old_3_tot",
            "dire_old_3_comp",
"""