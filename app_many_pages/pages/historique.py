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

annee = [x for x in range(2015, 2020)]   #A MODIFIER PLUS TARD
trimestre = config.trimestre
titre = data.titres
label = [[str(year) + " - " + tri for tri in trimestre] for year in annee]


#Récupération des données
data_old_global = df_fig.data_old + daf_fig.data_old + dire_fig.data_old + drfd_fig.data_old + drh_fig.data_old

#Initialisation des paramètres
selected_global = data_old_global
selected_annee = annee
selected_label = label

def fig_test(donnes, annees, labels):
    donnee = []
    print(annees)
    print(donnes)
    for i, annee in enumerate(annees):
        print(i)
        donnee.append(
            go.Bar(
                x=[annees[i]],
                y=[donnes[i]],
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

    dcc.Graph(
        id='graph_test',
        figure=fig_test(selected_global[0], selected_annee, selected_label),
        config = {'displaylogo': False}

    ),




    ]

)


@callback(
    Output('my-updated-graph', 'data'),
    Output('my-updated-graph', 'labels'),
    [Input('annee-selector', 'value')])

def update_data(selected_years):
    global selected_global, selected_annee, selected_label

    filtered_data = [data_old[selected_years[0] - min(annee) : selected_years[1] - min(annee) + 1] for data_old in data_old_global]
    filtered_label = [tri[selected_years[0] - min(annee) : selected_years[1] - min(annee) + 1] for tri in label]

    selected_global = filtered_data
    selected_annee = selected_years
    selected_label = filtered_label

    print(selected_global[0])

    return filtered_data, filtered_label

