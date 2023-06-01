import dash
from dash import html, dcc
from src.fig.departement_fig import *
import dash
from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from src.functions.fonction_figure import fig_annuelle_baton, fig_camembert, fig_trim_baton, fig_radar, fig_radar_all_dept, couleurs
from src.functions.fonctions_historique import *

dash.register_page(
    __name__,
    title = "Comparaison départements",
    name = "Comparaison départements",
    order=8,
    active= False
                   )


def liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_annee) :
    return [
        dcc.Graph(
            id='radar_all_dept',
            figure=fig_radar_all_dept(selected_annee),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_artemis',
            figure=fig_radar(selected_annee, 0),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_citi',
            figure=fig_radar(selected_annee, 1),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_eph',
            figure=fig_radar(selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_inf',
            figure=fig_radar(selected_annee, 3),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_rs2m',
            figure=fig_radar(selected_annee, 4),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_rst',
            figure=fig_radar(selected_annee, 5),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_tsp',
            figure=fig_radar(selected_annee, 6),
            config={'displaylogo': False}
        ),


]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page proposant une comparaison entre départements',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-dept", color = "black", type = "circle"),


    #joue le rôle de variable globale
    dcc.Store(id='current-value-dept', data=[]),
    #Menu déourlant/moteur de recherche
    dcc.Dropdown(
        options=categories_historique,
        id="checklist-input-dept",
        multi=True,
        placeholder="Veuillez selectionner des graphes à afficher.",
        persistence = True,
        value = [
            #A completer une fois historique full
        ],
        disabled = True,
        style={"display": "none"}
    ),
    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-dept",
                children=[],
                fluid = True),
    ],
fluid = True
)










#Mettre à jour les données du menu déroulant sélectionnées
@callback(
    Output("current-value-dept", "data"),
    [Input("checklist-input-dept", "value")],
    [State("current-value-dept", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return update_old_value_(value, old_value) #dans fonctions_historique.py


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories_historique):
    cat_id = cat["value"]


    @callback(
        Output(f"current_collapse-dept{i + 1}", "is_open"),
        [Input("checklist-input-dept", "value")],
        [State(f"collapse-dept{i + 1}", "is_open"), State("current-value-dept", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        return toggle_collapse_(value, is_open, data, cat_id=cat_id)

@callback(
    [Output("graph-container-historique-dept", "children"),
     Output("loading-dept", "parent-style")], #Permet d'afficher un Spinner de Char
    [Input("choix-annee", "value"),
     Input("checklist-input-dept", "value"),
     ]
)

def generate_graphs(selected_year, value):
    return generate_graphs_(selected_year, value, baseline_graph = liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_year))




"""
dcc.Graph(
        id='example-graph',
        figure=fig_dept_1(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph2',
        figure=fig_dept_2(),
        config = {'displaylogo': False}
    ),

   

    dcc.Graph(
        id='example-graph3',
        figure=fig_dept_3(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph4',
        figure=fig_dept_4(),
        config = {'displaylogo': False}
    ),

   

    dcc.Graph(
        id='example-graph5',
        figure=fig_dept_5(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph6',
        figure=fig_dept_6(),
        config = {'displaylogo': False}
    ),

   

    dcc.Graph(
        id='example-graph7',
        figure=fig_dept_7(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph8',
        figure=fig_dept_8(),
        config = {'displaylogo': False}
    ),
"""