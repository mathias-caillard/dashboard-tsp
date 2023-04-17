#fichier pour indicateurs avec sélection libre selon les departements.

import dash
from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from app_many_pages.df_fig import *
from app_many_pages.dire_fig import *
from app_many_pages.daf_fig import *
from app_many_pages.drfd_fig import *
from app_many_pages.drh_fig import *
from app_many_pages.dri_fig import *
from app_many_pages.departement_fig import *
from app_many_pages.artemis_fig import *
from app_many_pages.citi_fig import *
from app_many_pages.eph_fig import *
from app_many_pages.inf_fig import *
from app_many_pages.rs2m_fig import *
from app_many_pages.rst_fig import *







categories = [
    #DF
    {"label": html.Span(["DF - Nombre d\'étudiants"], style={'color': 'green'}), "value": "df_1"},
    {"label": html.Span(["DF - Nombre d\'UP"], style = {'color' : "green"}), "value": "df_2"},

    #DRFD
    {"label": html.Span(["DRFD - Publications"], style={'color': 'blue'}), "value": "drfd_1"},
    {"label": html.Span(["DRFD - Nombre de doctorants"], style={'color': 'blue'}), "value": "drfd_2"},
    {"label": html.Span(["DRFD - Evolutions des publications"], style={'color': 'blue'}), "value": "drfd_3"},
    {"label": html.Span(["DRFD - Evolution du nombre de doctorants"], style={'color': 'blue'}), "value": "drfd_4"},

    #DIRE
    {"label": html.Span(["DIRE - Suivi des contrats de recherches"], style={'color': 'purple'}), "value": "dire_1"},
    {"label": html.Span(["DIRE - Suivi des contrats de recherches, vision trimestrielle"], style={'color': 'purple'}), "value": "dire_2"},
    {"label": html.Span(["DIRE - Suivi des contrats de recherches, total école"], style={'color': 'purple'}), "value": "dire_3"},
    {"label": html.Span(["DIRE - Contribution au financement de l'école, graphe camembert"], style={'color': 'purple'}), "value": "dire_4"},


    #DAF
    {"label": html.Span(["DAF - Chiffre d\'affaire de la recherche"], style={'color': 'orange'}), "value": "daf_1"},
    {"label": html.Span(["DAF - Dépenses de vacataires"], style={'color': 'orange'}), "value": "diaf_2"},
    {"label": html.Span(["DAF - Dépenses de vacataires, vision trimestrielle"], style={'color': 'orange'}), "value": "daf_3"},
    {"label": html.Span(["DAF - Ressource propres"], style={'color': 'orange'}), "value": "daf_4"},
    {"label": html.Span(["DAF - Ressource propres, vision trimestrielle"], style={'color': 'orange'}), "value": "daf_5"},
    {"label": html.Span(["DAF - Ressource d\'état"], style={'color': 'orange'}), "value": "daf_6"},
    {"label": html.Span(["DAF - Ressource d\'état, vision trimestrielle"], style={'color': 'orange'}), "value": "daf_7"},
    {"label": html.Span(["DAF - Total des dépenses"], style={'color': 'orange'}), "value": "daf_8"},
    {"label": html.Span(["DAF - Total des dépenses, vision trimestrielle"], style={'color': 'orange'}), "value": "daf_9"},



   #DRH
    {"label": html.Span("DRH - Nombre de permanents", style={'color': 'black'}), "value": "drh_1"},
    {"label": html.Span("DRH - Répartition des permanents, vision trimestrielle", style={'color': 'black'}), "value": "drh_2"},
    {"label": html.Span("DRH - Nombre de non-permanents", style={'color': 'black'}), "value": "drh_3"},
    {"label": html.Span("DRH - Evolution du nombre de non-permanents", style={'color': 'black'}), "value": "drh_4"},

    #DRI
    {"label": html.Span("DRI - Chiffres sur l'international", style={'color': 'Maroon'}), "value": "dri_2"},
    {"label": html.Span("DRI - Evolution du nombre d\'étudiants étrangers, bâtons", style={'color': 'Maroon'}), "value": "dri_3"},
    {"label": html.Span("DRI - Evolution du nombre d\'étudiants étrangers, courbe", style={'color': 'Maroon'}), "value": "dri_4"},

    #ARTEMIS
    {"label": html.Span("ARTEMIS - Graphe radar année 2023", style={'color': 'Navy'}), "value": "dept_2"},
    {"label": html.Span("ARTEMIS - Graphe radar année 2023-2024", style={'color': 'Navy'}), "value": "dept_1"},
    {"label": html.Span("ARTEMIS - Ressources humaines", style={'color': 'Navy'}), "value": "artemis_1"},
    {"label": html.Span("ARTEMIS - Contrats de recherche", style={'color': 'Navy'}), "value": "artemis_2"},
    {"label": html.Span("ARTEMIS - Contribution au financement de l'école", style={'color': 'Navy'}), "value": "artemis_3"},
    {"label": html.Span("ARTEMIS - Dépense de vacataires", style={'color': 'Navy'}), "value": "artemis_4"},
    {"label": html.Span("ARTEMIS - Ressources propres", style={'color': 'Navy'}), "value": "artemis_5"},
    {"label": html.Span("ARTEMIS - Ressources d'états", style={'color': 'Navy'}), "value": "artemis_6"},
    {"label": html.Span("ARTEMIS - Total des dépenses", style={'color': 'Navy'}), "value": "artemis_7"},

    #CITI
    {"label": html.Span("CITI - Graphe radar année 2023", style={'color': 'Olive'}), "value": "dept_3"},
    {"label": html.Span("CITI - Ressources humaines", style={'color': 'Olive'}), "value": "citi_1"},
    {"label": html.Span("CITI - Contrats de recherche", style={'color': 'Olive'}), "value": "citi_2"},
    {"label": html.Span("CITI - Contribution au financement de l'école", style={'color': 'Olive'}), "value": "citi_3"},
    {"label": html.Span("CITI - Dépense de vacataires", style={'color': 'Olive'}), "value": "citi_4"},
    {"label": html.Span("CITI - Ressources propres", style={'color': 'Olive'}), "value": "citi_5"},
    {"label": html.Span("CITI - Ressources d'états", style={'color': 'Olive'}), "value": "citi_6"},
    {"label": html.Span("CITI - Total des dépenses", style = {'color':'Olive'}), "value": "citi_7"},

    #EPH
    {"label": html.Span("EPH - Graphe radar année 2023", style={'color': 'Salmon'}), "value": "dept_4"},
    {"label": html.Span("EPH - Ressources humaines", style={'color': 'Salmon'}), "value": "eph_1"},
    {"label": html.Span("EPH - Contrats de recherche", style={'color': 'Salmon'}), "value": "eph_2"},
    {"label": html.Span("EPH - Contribution au financement de l'école", style={'color': 'Salmon'}), "value": "eph_3"},
    {"label": html.Span("EPH - Dépense de vacataires", style={'color': 'Salmon'}), "value": "eph_4"},
    {"label": html.Span("EPH - Ressources propres", style={'color': 'Salmon'}), "value": "eph_5"},
    {"label": html.Span("EPH - Ressources d'états", style={'color': 'Salmon'}), "value": "eph_6"},
    {"label": html.Span("EPH - Total des dépenses", style={'color': 'Salmon'}), "value": "eph_7"},

    #INF
    {"label": html.Span("INF - Graphe radar année 2023", style={'color': 'MediumVioletRed'}), "value": "dept_5"},
    {"label": html.Span("INF - Ressources humaines", style={'color': 'MediumVioletRed'}), "value": "inf_1"},
    {"label": html.Span("INF - Contrats de recherche", style={'color': 'MediumVioletRed'}), "value": "inf_2"},
    {"label": html.Span("INF - Contribution au financement de l'école", style={'color': 'MediumVioletRed'}), "value": "inf_3"},
    {"label": html.Span("INF - Dépense de vacataires", style={'color': 'MediumVioletRed'}), "value": "inf_4"},
    {"label": html.Span("INF - Ressources propres", style={'color': 'MediumVioletRed'}), "value": "inf_5"},

    {"label": html.Span("INF - Ressources propres", style={'color': 'BlueViolet'}), "value": "inf_5"},
    {"label": html.Span("INF - Ressources d\'états", style={'color': 'BlueViolet'}), "value": "inf_6"},
    {"label": html.Span("INF - Total des dépenses", style={'color': 'BlueViolet'}), "value": "inf_7"},

    #RS2M
    {"label": html.Span("RS2M - Graphe radar année 2023", style={'color': 'Indigo'}), "value": "dept_6"},
    {"label": html.Span("RS2M - Ressources humaines", style={'color': 'Indigo'}), "value": "rs2m_1"},
    {"label": html.Span("RS2M - Contrats de recherche", style={'color': 'Indigo'}), "value": "rs2m_2"},
    {"label": html.Span("RS2M - Contribution au financement de l\'école", style={'color': 'Indigo'}), "value": "rs2m_3"},
    {"label": html.Span("RS2M - Dépense de vacataires", style={'color': 'Indigo'}), "value": "rs2m_4"},
    {"label": html.Span("RS2M - Ressources propres", style={'color': 'Indigo'}), "value": "rs2m_5"},
    {"label": html.Span("RS2M - Ressources d\'états", style={'color': 'Indigo'}), "value": "rs2m_6"},
    {"label": html.Span("RS2M - Total des dépenses", style={'color': 'Indigo'}), "value": "rs2m_7"},

    #RST
    {"label": html.Span("RST - Graphe radar année 2023", style={'color': 'DarkGreen'}), "value": "dept_7"},
    {"label": html.Span("RST - Ressources humaines", style={'color': 'DarkGreen'}), "value": "rst_1"},
    {"label": html.Span("RST - Contrats de recherche", style={'color': 'DarkGreen'}), "value": "rst_2"},
    {"label": html.Span("RST - Contribution au financement de l\'école", style={'color': 'DarkGreen'}), "value": "rst_3"},
    {"label": html.Span("RST - Dépense de vacataires", style={'color': 'DarkGreen'}), "value": "rst_4"},


    #RST
    {"label": html.Span("RST - Graphe radar année 2023", style={'color': 'SaddleBrown'}), "value": "dept_7"},
    {"label": html.Span("RST - Ressources humaines", style={'color': 'SaddleBrown'}), "value": "rst_1"},
    {"label": html.Span("RST - Contrats de recherche", style={'color': 'SaddleBrown'}), "value": "rst_2"},
    {"label": html.Span("RST - Contribution au financement de l\'école", style={'color': 'SaddleBrown'}), "value": "rst_3"},
    {"label": html.Span("RST - Dépense de vacataires", style={'color': 'SaddleBrown'}), "value": "rst_4"},
    {"label": html.Span("RST - Dépense de vacataires", style={'color': 'SaddleBrown'}), "value": "rst_4"},
    {"label": html.Span("RST - Ressources propres", style={'color': 'SaddleBrown'}), "value": "rst_5"},
    {"label": html.Span("RST - Ressources d\'états", style={'color': 'SaddleBrown'}), "value": "rst_6"},
    {"label": html.Span("RST - Total des dépenses", style={'color': 'SaddleBrown'}), "value": "rst_7"},

    {"label": html.Span("Graphes radar des départements", style={'color': 'DarkSlateGray'}), "value": "dept_8"},
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
        multi=True,

    ),

    # Boucle pour générer les graphiques
    dbc.Container(id="graph-container",
             children=[],
             fluid = True),






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
        



# Définissez le callback pour générer les graphiques par département
@callback(
    Output("graph-container", "children"),
    [Input("checklist-input", "value")]
)

def generate_graphs(value):
    # Liste des graphiques disponibles
    graphs = {
        #DF
        "df_1": fig_df_1(),
        "df_2": fig_df_2(),

        #DRFD
        "drfd_1": fig_drfd_1(),
        "drfd_2": fig_drfd_2(),
        "drfd_3": fig_drfd_3(),
        "drfd_4": fig_drfd_4(),

        #DIRE
        "dire_1": fig_dire_1(),
        "dire_2": fig_dire_2(),
        "dire_3": fig_dire_3(),
        "dire_4": fig_dire_4(),

        #DAF
        "daf_1": fig_daf_1(),
        "daf_2": fig_daf_2(),
        "daf_3": fig_daf_3(),
        "daf_4": fig_daf_4(),
        "daf_5": fig_daf_5(),
        "daf_6": fig_daf_6(),
        "daf_7": fig_daf_7(),
        "daf_8": fig_daf_8(),
        "daf_9": fig_daf_9(),

        #DRH
        "drh_1": fig_drh_1(),
        "drh_2": fig_drh_2(),
        "drh_3": fig_drh_3(),
        "drh_4": fig_drh_4(),

        #DRI
        "dri_2": fig_dri_2(),
        "dri_3": fig_dri_3(),
        "dri_4": fig_dri_4(),

        #ARTEMIS
        "dept_2": fig_dept_2(),
        "dept_1": fig_dept_1(),
        "artemis_1": fig_artemis_1(),
        "artemis_2": fig_artemis_2(),
        "artemis_3": fig_artemis_3(),
        "artemis_4": fig_artemis_4(),
        "artemis_5": fig_artemis_5(),
        "artemis_6": fig_artemis_6(),
        "artemis_7": fig_artemis_7(),

        #CITI
        "dept_3": fig_dept_3(),
        "citi_1": fig_citi_1(),
        "citi_2": fig_citi_2(),
        "citi_3": fig_citi_3(),
        "citi_4": fig_citi_4(),
        "citi_5": fig_citi_5(),
        "citi_6": fig_citi_6(),
        "citi_7": fig_citi_7(),

        #EPH
        "dept_4": fig_dept_4(),
        "eph_1": fig_eph_1(),
        "eph_2": fig_eph_2(),
        "eph_3": fig_eph_3(),
        "eph_4": fig_eph_4(),
        "eph_5": fig_eph_5(),
        "eph_6": fig_eph_6(),
        "eph_7": fig_eph_7(),

        #INF
        "dept_5": fig_dept_5(),
        "inf_1": fig_inf_1(),
        "inf_2": fig_inf_2(),
        "inf_3": fig_inf_3(),
        "inf_4": fig_inf_4(),
        "inf_5": fig_inf_5(),
        "inf_6": fig_inf_6(),
        "inf_7": fig_inf_7(),

        #RS2M
        "dept_6": fig_dept_6(),
        "rs2m_1": fig_rs2m_1(),
        "rs2m_2": fig_rs2m_2(),
        "rs2m_3": fig_rs2m_3(),
        "rs2m_4": fig_rs2m_4(),
        "rs2m_5": fig_rs2m_5(),
        "rs2m_6": fig_rs2m_6(),
        "rs2m_7": fig_rs2m_7(),

        #RST
        "dept_7": fig_dept_7(),
        "rst_1": fig_rst_1(),
        "rst_2": fig_rst_2(),
        "rst_3": fig_rst_3(),
        "rst_4": fig_rst_4(),
        "rst_5": fig_rst_5(),
        "rst_6": fig_rst_6(),
        "rst_7": fig_rst_7(),

        "dept_8": fig_dept_8(),
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

    new_graph_output = []

    i = 0
    while 2*i < len(graph_output) : 
        if (2*i + 1 < len(graph_output)) :

            graph1 = graph_output[2*i]
            graph2 = graph_output[2*i+1]
            
            new_graph_output.append(
                dbc.Row(children = [
                    dbc.Col(graph1, width = 6),
                    dbc.Col(graph2, width = 6)
                ])
            )
        
        else : 
            graph = graph_output[2*i]
            new_graph_output.append(
                dbc.Row(children = [
                    dbc.Col(graph)
                ])
            )
        i += 1


    return new_graph_output


"""
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

"""



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

"""

