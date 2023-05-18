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
couleurs_trimestres = config.couleurs_trimestres

titres_y = data.titres_y
titres_graphe = data.titres_graphe
effectif_dept = data.effectif_dept
label = [[str(year) + " - " + tri for tri in trimestre] for year in annee]


#Récupération des données
data_old_global = df_fig.data_old + daf_fig.data_old + dire_fig.data_old + drfd_fig.data_old + drh_fig.data_old

#Initialisation des paramètres
selected_global = data_old_global
selected_annee = annee
selected_label = label


#Catégories du menu déroulant
categories = [
    # DF
    {"label": "DF - " + titres_graphe[0] + ", vision annuelle", "value": "df_old_1_an"},
    {"label": "DF - " + titres_graphe[0] + ", vision trimestrielle", "value": "df_old_1_tri"},
    {"label": "DF - " + titres_graphe[0] + ", total annuel", "value": "df_old_1_tot"},
    {"label": "DF - " + titres_graphe[0] + ", comparaison annuelle par trimestre", "value": "df_old_1_comp"},

    #DAF
    {"label": "DAF - " + titres_graphe[1] + ", vision annuelle", "value": "daf_old_1_an"},
    {"label": "DAF - " + titres_graphe[1] + ", vision trimestrielle", "value": "daf_old_1_tri"},
    {"label": "DAF - " + titres_graphe[1] + ", total annuel", "value": "daf_old_1_tot"},
    {"label": "DAF - " + titres_graphe[1] + ", comparaison annuelle par trimestre", "value": "daf_old_1_comp"},
    {"label": "DAF - " + titres_graphe[2] + ", vision annuelle", "value": "daf_old_2_an"},
    {"label": "DAF - " + titres_graphe[2] + ", vision trimestrielle", "value": "daf_old_2_tri"},
    {"label": "DAF - " + titres_graphe[2] + ", total annuel", "value": "daf_old_2_tot"},
    {"label": "DAF - " + titres_graphe[2] + ", comparaison annuelle par trimestre", "value": "daf_old_2_comp"},
    {"label": "DAF - " + titres_graphe[3] + ", vision annuelle", "value": "daf_old_3_an"},
    {"label": "DAF - " + titres_graphe[3] + ", vision trimestrielle", "value": "daf_old_3_tri"},
    {"label": "DAF - " + titres_graphe[3] + ", total annuel", "value": "daf_old_3_tot"},
    {"label": "DAF - " + titres_graphe[3] + ", comparaison annuelle par trimestre", "value": "daf_old_3_comp"},

    #DIRE
    {"label": "DIRE - " + titres_graphe[4] + ", vision annuelle", "value": "dire_old_1_an"},
    {"label": "DIRE - " + titres_graphe[4] + ", vision trimestrielle", "value": "dire_old_1_tri"},
    {"label": "DIRE - " + titres_graphe[4] + ", total annuel", "value": "dire_old_1_tot"},
    {"label": "DIRE - " + titres_graphe[4] + ", comparaison annuelle par trimestre", "value": "dire_old_1_comp"},
    {"label": "DIRE - " + titres_graphe[5] + ", vision annuelle", "value": "dire_old_2_an"},
    {"label": "DIRE - " + titres_graphe[5] + ", vision trimestrielle", "value": "dire_old_2_tri"},
    {"label": "DIRE - " + titres_graphe[5] + ", total annuel", "value": "dire_old_2_tot"},
    {"label": "DIRE - " + titres_graphe[5] + ", comparaison annuelle par trimestre", "value": "dire_old_2_comp"},
    {"label": "DIRE - " + titres_graphe[6] + ", vision annuelle", "value": "dire_old_3_an"},
    {"label": "DIRE - " + titres_graphe[6] + ", vision trimestrielle", "value": "dire_old_3_tri"},
    {"label": "DIRE - " + titres_graphe[6] + ", total annuel", "value": "dire_old_3_tot"},
    {"label": "DIRE - " + titres_graphe[6] + ", comparaison annuelle par trimestre", "value": "dire_old_3_comp"},

    #DRFD
    {"label": "DRFD - " + titres_graphe[7] + ", vision annuelle", "value": "drfd_old_1_an"},
    {"label": "DRFD - " + titres_graphe[7] + ", vision trimestrielle", "value": "drfd_old_1_tri"},
    {"label": "DRFD - " + titres_graphe[7] + ", total annuel", "value": "drfd_old_1_tot"},
    {"label": "DRFD - " + titres_graphe[7] + ", comparaison annuelle par trimestre", "value": "drfd_old_1_comp"},
    {"label": "DRFD - " + titres_graphe[8] + ", vision annuelle", "value": "drfd_old_2_an"},
    {"label": "DRFD - " + titres_graphe[8] + ", vision trimestrielle", "value": "drfd_old_2_tri"},
    {"label": "DRFD - " + titres_graphe[8] + ", total annuel", "value": "drfd_old_2_tot"},
    {"label": "DRFD - " + titres_graphe[8] + ", comparaison annuelle par trimestre", "value": "drfd_old_2_comp"},

    #DRH
    {"label": "DRH - " + titres_graphe[9] + ", vision annuelle", "value": "drh_old_1_an"},
    {"label": "DRH - " + titres_graphe[9] + ", vision trimestrielle", "value": "drh_old_1_tri"},
    {"label": "DRH - " + titres_graphe[9] + ", total annuel", "value": "drh_old_1_tot"},
    {"label": "DRH - " + titres_graphe[9] + ", comparaison annuelle par trimestre", "value": "drh_old_1_comp"},
    {"label": "DRH - " + titres_graphe[10] + ", vision annuelle", "value": "drh_old_2_an"},
    {"label": "DRH - " + titres_graphe[10] + ", vision trimestrielle", "value": "drh_old_2_tri"},
    {"label": "DRH - " + titres_graphe[10] + ", total annuel", "value": "drh_old_2_tot"},
    {"label": "DRH - " + titres_graphe[10] + ", comparaison annuelle par trimestre", "value": "drh_old_2_comp"},


    #ARTEMIS

    #CITI

    #EPH

    #INF

    #RS2M

    #RST

]

def fig_old_annuelle_baton(donnees, years, labels, titre_graphe, titre_y):
    Y=[]
    for i, year in enumerate(years):
        Y.append(
            go.Bar(
                x=labels[i],
                y=donnees[i],
                name=str(year),
                width=0.8,
            )
        )
    fig = go.Figure(data=Y)
    # Ajout d'un titre
    fig.update_layout(title=titre_graphe + " de " + str(years[0]) + " à " + str(years[-1]) + ", vision annuelle",
                      xaxis_title="Temps",
                      yaxis_title=titre_y)
    return fig

def fig_old_trimestrielle(donnees, years, labels, titre_graphe, titre_y):
    Y = []
    for i, year in enumerate(years):
        Y.append(
            go.Bar(
                x=labels[i],
                y=donnees[i],
                name=str(year),
                marker=dict(color=couleurs_trimestres),
                width=0.8,
            )
        )
    fig = go.Figure(data=Y)
    # Ajout d'un titre
    fig.update_layout(title=titre_graphe + " de " + str(years[0]) + " à " + str(years[-1]) + ", vision trimestrielle",
                      xaxis_title="Temps",
                      yaxis_title=titre_y)
    return fig

def fig_old_total(donnees, years, titre_graphe, titre_y):
    Y = []
    for i, year in enumerate(years):
        Y.append(
            go.Bar(
                x=[str(year)],
                y=[sum(donnees[i])],
                name=str(year),
            )
        )
    fig = go.Figure(data=Y)
    # Ajout d'un titre
    fig.update_layout(title=titre_graphe + " de " + str(years[0]) + " à " + str(years[-1]) + ", total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre_y)
    return fig

def fig_old_annuelle_courbe(donnees, years, titre_graphe, titre_y):
    fig = go.Figure()
    for i in range(len(years)):
        fig.add_trace(go.Scatter(x=trimestre, y=donnees[i], name="Année " + str(years[i])))

    fig.update_layout(title=titre_graphe + " de " + str(years[0]) + " à " + str(years[-1]) +", comparaison annuelle par trimestre",
                      xaxis_title="Trimestre",
                      yaxis_title=titre_y)
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
        "df_old_1_an": fig_old_annuelle_baton(selected_global[0], selected_annee, selected_label, titres_graphe[0], titres_y[0]),
        "df_old_1_tri": fig_old_trimestrielle(selected_global[0], selected_annee, selected_label, titres_graphe[0], titres_y[0]),
        "df_old_1_tot": fig_old_total(selected_global[0], selected_annee, titres_graphe[0], titres_y[0]),
        "df_old_1_comp": fig_old_annuelle_courbe(selected_global[0], selected_annee, titres_graphe[0], titres_y[0]),

        #DAF
        "daf_old_1_an": fig_old_annuelle_baton(selected_global[1], selected_annee, selected_label, titres_graphe[1],titres_y[1]),
        "daf_old_1_tri": fig_old_trimestrielle(selected_global[1], selected_annee, selected_label, titres_graphe[1],titres_y[1]),
        "daf_old_1_tot": fig_old_total(selected_global[1], selected_annee, titres_graphe[1], titres_y[1]),
        "daf_old_1_comp": fig_old_annuelle_courbe(selected_global[1], selected_annee, titres_graphe[1], titres_y[1]),
        "daf_old_2_an": fig_old_annuelle_baton(selected_global[2], selected_annee, selected_label, titres_graphe[2],titres_y[2]),
        "daf_old_2_tri": fig_old_trimestrielle(selected_global[2], selected_annee, selected_label, titres_graphe[2],titres_y[2]),
        "daf_old_2_tot": fig_old_total(selected_global[2], selected_annee, titres_graphe[2], titres_y[2]),
        "daf_old_2_comp": fig_old_annuelle_courbe(selected_global[2], selected_annee, titres_graphe[2], titres_y[2]),
        "daf_old_3_an": fig_old_annuelle_baton(selected_global[3], selected_annee, selected_label, titres_graphe[3], titres_y[3]),
        "daf_old_3_tri": fig_old_trimestrielle(selected_global[3], selected_annee, selected_label, titres_graphe[3], titres_y[3]),
        "daf_old_3_tot": fig_old_total(selected_global[3], selected_annee, titres_graphe[3], titres_y[3]),
        "daf_old_3_comp": fig_old_annuelle_courbe(selected_global[3], selected_annee, titres_graphe[3], titres_y[3]),

        #DIRE
        "dire_old_1_an": fig_old_annuelle_baton(selected_global[4], selected_annee, selected_label, titres_graphe[4], titres_y[4]),
        "dire_old_1_tri": fig_old_trimestrielle(selected_global[4], selected_annee, selected_label, titres_graphe[4], titres_y[4]),
        "dire_old_1_tot": fig_old_total(selected_global[4], selected_annee, titres_graphe[4], titres_y[4]),
        "dire_old_1_comp": fig_old_annuelle_courbe(selected_global[4], selected_annee, titres_graphe[4], titres_y[4]),
        "dire_old_2_an": fig_old_annuelle_baton(selected_global[5], selected_annee, selected_label, titres_graphe[5], titres_y[5]),
        "dire_old_2_tri": fig_old_trimestrielle(selected_global[5], selected_annee, selected_label, titres_graphe[5], titres_y[5]),
        "dire_old_2_tot": fig_old_total(selected_global[5], selected_annee, titres_graphe[5], titres_y[5]),
        "dire_old_2_comp": fig_old_annuelle_courbe(selected_global[5], selected_annee, titres_graphe[5], titres_y[5]),
        "dire_old_3_an": fig_old_annuelle_baton(selected_global[6], selected_annee, selected_label, titres_graphe[6], titres_y[6]),
        "dire_old_3_tri": fig_old_trimestrielle(selected_global[6], selected_annee, selected_label, titres_graphe[6], titres_y[6]),
        "dire_old_3_tot": fig_old_total(selected_global[6], selected_annee, titres_graphe[6], titres_y[6]),
        "dire_old_3_comp": fig_old_annuelle_courbe(selected_global[6], selected_annee, titres_graphe[6], titres_y[6]),

        #DRFD
        "drfd_old_1_an": fig_old_annuelle_baton(selected_global[7], selected_annee, selected_label, titres_graphe[7], titres_y[7]),
        "drfd_old_1_tri": fig_old_trimestrielle(selected_global[7], selected_annee, selected_label, titres_graphe[7], titres_y[7]),
        "drfd_old_1_tot": fig_old_total(selected_global[7], selected_annee, titres_graphe[7], titres_y[7]),
        "drfd_old_1_comp": fig_old_annuelle_courbe(selected_global[7], selected_annee, titres_graphe[7], titres_y[7]),
        "drfd_old_2_an": fig_old_annuelle_baton(selected_global[8], selected_annee, selected_label, titres_graphe[8], titres_y[8]),
        "drfd_old_2_tri": fig_old_trimestrielle(selected_global[8], selected_annee, selected_label, titres_graphe[8], titres_y[8]),
        "drfd_old_2_tot": fig_old_total(selected_global[8], selected_annee, titres_graphe[8], titres_y[8]),
        "drfd_old_2_comp": fig_old_annuelle_courbe(selected_global[8], selected_annee, titres_graphe[8], titres_y[8]),

        #DRH
        "drh_old_1_an": fig_old_annuelle_baton(selected_global[9], selected_annee, selected_label, titres_graphe[9], titres_y[9]),
        "drh_old_1_tri": fig_old_trimestrielle(selected_global[9], selected_annee, selected_label, titres_graphe[9], titres_y[9]),
        "drh_old_1_tot": fig_old_total(selected_global[9], selected_annee, titres_graphe[9], titres_y[9]),
        "drh_old_1_comp": fig_old_annuelle_courbe(selected_global[9], selected_annee, titres_graphe[9], titres_y[9]),
        "drh_old_2_an": fig_old_annuelle_baton(selected_global[10], selected_annee, selected_label, titres_graphe[10], titres_y[10]),
        "drh_old_2_tri": fig_old_trimestrielle(selected_global[10], selected_annee, selected_label, titres_graphe[10], titres_y[10]),
        "drh_old_2_tot": fig_old_total(selected_global[10], selected_annee, titres_graphe[10], titres_y[10]),
        "drh_old_2_comp": fig_old_annuelle_courbe(selected_global[10], selected_annee, titres_graphe[10], titres_y[10]),

        # ARTEMIS

        # CITI

        # EPH

        # INF

        # RS2M

        # RST

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



