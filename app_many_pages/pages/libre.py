#fichier pour indicateurs avec sélection libre selon les departements.

import dash
from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from departements.departement_fig import * 


dash.register_page(
    __name__,
    title = "Choix libre des indicateurs",
    name = "Choix libre des indicateurs",
    order=9
)

layout = html.Div(children=[
    html.H1(children='Dans cette page, vous pouvez croiser les directions'),

    html.H2(children='sélection des departements'),

    #joue le rôle de variable globale 
    dcc.Store(id='old-value', data=[]),

     dbc.Checklist(
        options=[
            {"label": "ARTEMIS", "value": 1},
            {"label": "CITI", "value": 2},
            {"label": "EPH", "value": 3},
            {"label": "INF", "value": 4},
            {"label": "RS2M", "value": 5},
            {"label": "RST", "value": 6},
        ],
        id="checklist-input",
    ),

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
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    figure=fig_dept_3(),
                    config={'displaylogo': False}
                ),
                width="auto"
            )
        ]),

        id="collapse2",
        is_open=False,
    ),

    dbc.Collapse(
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    figure=fig_dept_4(),
                    config={'displaylogo': False}
                ),
                width="auto"
            )
        ]),

        id="collapse3",
        is_open=False,
    ),

    dbc.Collapse(
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    figure=fig_dept_5(),
                    config={'displaylogo': False}
                ),
                width="auto"
            )
        ]),

        id="collapse4",
        is_open=False,
    ),

    dbc.Collapse(
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    figure=fig_dept_6(),
                    config={'displaylogo': False}
                ),
                width="auto"
            )
        ]),

        id="collapse5",
        is_open=False,
    ),
    dbc.Collapse(
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    figure=fig_dept_7(),
                    config={'displaylogo': False}
                ),
                width="auto"
            )
        ]),

        id="collapse6",
        is_open=False,
    ),
])



@callback(
    Output("old-value", "data"),
    [Input("checklist-input", "value")],
    [State("old-value", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return value


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
