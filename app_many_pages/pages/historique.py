import dash
from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from app_many_pages import data, daf_fig, df_fig, dire_fig, drfd_fig, drh_fig, dri_fig, artemis_fig, citi_fig, eph_fig, inf_fig, rs2m_fig, rst_fig
from app_many_pages import config
import plotly.express as px
import plotly.graph_objects as go


dash.register_page(
    __name__,
    title = "Historique",
    name = "Historique",
    order=91,
    active= False

)


annee = config.list_annee
trimestre = config.trimestre
titre = data.titres
label = [[str(year) + " - " + tri for tri in trimestre] for year in annee]


#Récupération des données
data_old_global = [df_fig.data_old + daf_fig.data_old + dire_fig.data_old + drfd_fig.data_old + drh_fig.data_old]

#Initialisation des paramètres
selected_global = data_old_global
selected_annee = annee
selected_label = label


#Catégories du menu déroulant
categories = [
    # DF
    {"label": "DF - Total des indicateurs en heures équivalentes - Graphe bâton", "value": "df_old_1"}

]



def fig_test(donnes, annees, labels):
    donnee = []
    for i, annee in enumerate(annees):

        donnee.append(
            go.Bar(
                x=labels[i],
                y=donnes[i],
                name=str(annee),
                width=0.8,
            )
        )

    fig = go.Figure(data=donnee)

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes de " + str(annees[0]) + " à " + str(annees[-1]) + ", graphique en bâton",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig



layout = dbc.Container(children=[
    html.H1(
        children='Dans cette page, vous pouvez afficher les graphes de votre choix sur les années précédentes',
        style={'text-align': 'justify'}
    ),

    html.H2(children='Sélections de la plage temporelle:'),
    dcc.RangeSlider(
        id='annee-selector',
        min=min(annee),
        max=max(annee),
        value=[min(annee), max(annee)],
        marks={str(year): str(year) for year in annee},
        step=1
    ),


    html.H2(children='Sélections des graphes à afficher:'),

    #joue le rôle de variable globale
    dcc.Store(id='current-value', data=[]),

    #Menu déouralnt/moteur de recherche
    dcc.Dropdown(
        options=categories,
        id="checklist-input",
        multi=True,

    ),

    # Boucle pour générer les graphiques
        dbc.Container(id="graph-container-historique",
            children=[],
            fluid = True),






    ],
fluid = True
)

"""
#Mettre à jour les données des graphes
@callback(
    Output('graph_test', 'figure'),
    [Input('annee-selector', 'value')])

def update_data(selected_years):

    global selected_global, selected_annee, selected_label

    filtered_data = [data_old[selected_years[0] - min(annee) : selected_years[1] - min(annee) + 1] for data_old in data_old_global]
    filtered_label = label[selected_years[0] - min(annee) : selected_years[1] - min(annee) + 1]

    selected_global = filtered_data
    selected_annee = [year for year in range(selected_years[0], selected_years[1] + 1)]
    selected_label = filtered_label

    #print(selected_annee)
    #print(selected_label)
    #print(selected_global)
    update_fig = fig_test(selected_global[0], selected_annee, selected_label)

    return update_fig
"""

"""
    dcc.Graph(
        id='graph_test',
        figure=fig_test(selected_global[0], selected_annee, selected_label),
        config = {'displaylogo': False}

    ),"""

#Mettre à jour les données du menu déroulant sélectionnées
@callback(
    Output("current-value", "data"),
    [Input("checklist-input", "value")],
    [State("current-value", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return value


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories):
    cat_id = cat["value"]


    @callback(
        Output(f"current_collapse{i + 1}", "is_open"),
        [Input("checklist-input", "value")],
        [State(f"collapse{i + 1}", "is_open"), State("current-value", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        if (cat_id in value and cat_id in data) or (cat_id not in value and cat_id not in data):
            return is_open
        return not is_open

@callback(
    Output("graph-container-historique", "children"),
    [Input("annee-selector", "value"),
     Input("checklist-input", "value")]
)
def generate_graphs(selected_years, value):
    #update_data([selected_annee[0], selected_annee[-1]])

    global selected_global, selected_annee, selected_label

    filtered_data = [data_old[selected_years[0] - min(annee): selected_years[1] - min(annee) + 1] for data_old in
                     data_old_global]
    filtered_label = label[selected_years[0] - min(annee): selected_years[1] - min(annee) + 1]

    selected_global = filtered_data
    selected_annee = [year for year in range(selected_years[0], selected_years[1] + 1)]
    selected_label = filtered_label

    # Liste des graphiques disponibles
    graphs = {
        # DF
        "df_old_1": fig_test(selected_global[0], selected_annee, selected_label),

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
                is_open=("collapse{}".format(val) in open_collapse_ids),

            )
        )

    new_graph_output = []

    i = 0
    while 2 * i < len(graph_output):
        if (2 * i + 1 < len(graph_output)):

            graph1 = graph_output[2 * i]
            graph2 = graph_output[2 * i + 1]

            new_graph_output.append(
                dbc.Row(children=[
                    dbc.Col(graph1, width=6),
                    dbc.Col(graph2, width=6)
                ])
            )
            new_graph_output.append(
                html.Hr(style={'borderTop': '2px solid #000000'}))  # Ligne horizontale pour mieux séparer les graphes)

        else:
            graph = graph_output[2 * i]
            new_graph_output.append(
                dbc.Row(children=[
                    dbc.Col(graph)
                ])
            )
            new_graph_output.append(
                html.Hr(style={'borderTop': '2px solid #000000'}))  # Ligne horizontale pour mieux séparer les graphes)
        i += 1

    return new_graph_output



