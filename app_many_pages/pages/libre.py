#fichier pour indicateurs avec sélection libre selon les departements.

import dash
from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc

from app_many_pages.departement_fig import *

categories = [
            {"label": "ARTEMIS - Graphe radar année 2023", "value": 1},
            {"label": "CITI - Graphe radar année 2023", "value": 2},
            {"label": "EPH - Graphe radar année 2023", "value": 3},
            {"label": "INF - Graphe radar année 2023", "value": 4},
            {"label": "RS2M - Graphe radar année 2023", "value": 5},
            {"label": "RST - Graphe radar année 2023", "value": 6},
        ]

dash.register_page(
    __name__,
    title = "Choix libre des indicateurs",
    name = "Choix libre des indicateurs",
    order=9,

)

layout = dbc.Container(children=[
    html.H1(children='Dans cette page, vous pouvez afficher les graphes de votre choix'),

    html.H2(children='Sélections des graphes à afficher'),

    #joue le rôle de variable globale 
    dcc.Store(id='old-value', data=[]),

    dcc.Dropdown(
        options=categories,
        id="checklist-input",
        multi=True
    ),

    # Boucle pour générer les graphiques
    html.Div(id="graph-container",
             children=[]),




    #ARTEMIS
    dbc.Collapse(
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    figure=fig_dept_1(),
                    config={'displaylogo': False}
                ),
                width="auto"
            ),
            dbc.Col(
                dcc.Graph(
                    figure=fig_dept_2(),
                    config={'displaylogo': False}
                ),
                width="auto"
            ),

        ]),

        id="collapse1",
        is_open=False,
    ),

    #CITI
    dbc.Collapse(

                dcc.Graph(
                    figure=fig_dept_3(),
                    config={'displaylogo': False}
                ),

        id="collapse2",
        is_open=False,
    ),

    dbc.Collapse(

                dcc.Graph(
                    figure=fig_dept_4(),
                    config={'displaylogo': False}
                ),

        id="collapse3",
        is_open=False,
    ),

    dbc.Collapse(

                dcc.Graph(
                    figure=fig_dept_5(),
                    config={'displaylogo': False}
                ),

        id="collapse4",
        is_open=False,
    ),

    dbc.Collapse(
                dcc.Graph(
                    figure=fig_dept_6(),
                    config={'displaylogo': False}
                ),

        id="collapse5",
        is_open=False,
    ),
    dbc.Collapse(

                dcc.Graph(
                    figure=fig_dept_7(),
                    config={'displaylogo': False}
                ),

        id="collapse6",
        is_open=False,
    ),





],


fluid = True)




@callback(
    Output("old-value", "data"),
    [Input("checklist-input", "value")],
    [State("old-value", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return value

"""
# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories):
    cat_id = cat["value"]

    @callback(
        Output(f"collapse{i + 1}", "is_open"),
        [Input("checklist-input", "value")],
        [State(f"collapse{i + 1}", "is_open"), State("old-value", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        if (cat_id in value and cat_id in data) or (cat_id not in value and cat_id not in data):
            return is_open
        return not is_open
        
"""

"""
# Définissez le callback pour générer les graphiques par département
@callback(
    Output("graph-container", "children"),
    [Input("checklist-input", "value")]
)

def generate_graphs(value):
    # Liste des graphiques disponibles
    graphs = {
        1: fig_dept_2(),
        2: fig_dept_3(),
        3: fig_dept_4(),
        4: fig_dept_5(),
        5: fig_dept_6(),
        6: fig_dept_7(),
    }
    if value is None:
        value = []
    # Création de la liste des IDs de collapse ouverts
    open_collapse_ids = ["collapse{}".format(val) for val in value]

    # Génération des graphiques et des collapses
    graph_output = []
    for val in value:

        graph_output.append(
            dbc.Collapse(
                dcc.Graph(
                    figure=graphs[val],
                    config={'displaylogo': False}
                ),
                id="collapse{}".format(val),
                is_open=("collapse{}".format(val) in open_collapse_ids)
            )
        )

    return graph_output
"""


#ARTEMIS
@callback(
    Output("collapse1", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse1", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_1(value, is_open, data):
    if (1 in value and 1 in data) or (1 not in value and 1 not in data) : 
        return is_open
    return not is_open

#CITI
@callback(
    Output("collapse2", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse2", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_2(value, is_open, data):
    if (2 in value and 2 in data) or (2 not in value and 2 not in data) : 
        return is_open
    return not is_open

#EPH
@callback(
    Output("collapse3", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse3", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_3(value, is_open, data):
    if (3 in value and 3 in data) or (3 not in value and 3 not in data) : 
        return is_open
    return not is_open

#INF
@callback(
    Output("collapse4", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse4", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_4(value, is_open, data):
    if (4 in value and 4 in data) or (4 not in value and 4 not in data) : 
        return is_open
    return not is_open

#RS2M
@callback(
    Output("collapse5", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse5", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_5(value, is_open, data):
    if (5 in value and 5 in data) or (5 not in value and 5 not in data) : 
        return is_open
    return not is_open

#RST
@callback(
    Output("collapse6", "is_open"),
    [Input("checklist-input", "value")],
    [State("collapse6", "is_open"), State("old-value", "data")],
    prevent_initial_call=True
)
def toggle_collapse_6(value, is_open, data):
    if (6 in value and 6 in data) or (6 not in value and 6 not in data) : 
        return is_open
    return not is_open



