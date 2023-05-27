import dash
from dash import html, dcc, Input, Output, State, callback
from src.fig.drfd_fig import *
from src.data.data import *


dash.register_page(
    __name__,
    title = "DRFD",
    name = "DRFD",
    order=3,
    active= False
                   )

titres_graphe_drfd = titres_graphe[7:9]
titres_y_drfd = titres_y[7:9]


data_drfd_pond1 = ponderation_total(data.data.data_drfd[0])
data_drfd_pond2 = ponderation_total(data.data.data_drfd[1])
data_drfd_pond1.append(data_drfd_2023[0])
data_drfd_pond2.append(data_drfd_2023[1])


selected_data_drfd1 = data_drfd_pond1[-1]
selected_data_drfd2 = data_drfd_pond2[-1]
annee = config.liste_annee_maj
selected_annee = annee[-1]

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DRFD'),

    dcc.Graph(
        id='drfd-graph1',
        figure=fig_baton_total(selected_data_drfd1,selected_annee , titres_graphe_drfd[0], titres_y_drfd[0]),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='drfd-graph2',
        figure=fig_baton_total(selected_data_drfd2,selected_annee , titres_graphe_drfd[1], titres_y_drfd[1]),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph1',
        figure=fig_drfd_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph2',
        figure=fig_drfd_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph3',
        figure=fig_drfd_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_drfd_4(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1',
        figure=fig_old_drfd_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1_tri',
        figure=fig_old_drfd_1_tri(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph1_tot',
        figure=fig_old_drfd_1_tot(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph2',
        figure=fig_old_drfd_2(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3',
        figure=fig_old_drfd_3(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3_tri',
        figure=fig_old_drfd_3_tri(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph3_tot',
        figure=fig_old_drfd_3_tot(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='old-graph4',
        figure=fig_old_drfd_4(),
        config = {'displaylogo': False}
    ),
])

@callback(
    [Output('drfd-graph1', 'figure'), Output('drfd-graph2', 'figure')],
    Input('choix-annee', 'value')
)
def update_graph(selected_year):
    if selected_year == 2023:
        selected_data_drfd1 = data_drfd_pond1[-1]
        selected_data_drfd2 = data_drfd_pond2[-1]

        return fig_baton_total(selected_data_drfd1,selected_year , titres_graphe_drfd[0], titres_y_drfd[0]), \
               fig_baton_total(selected_data_drfd2,selected_year , titres_graphe_drfd[1], titres_y_drfd[1])

    else:
        selected_data_drfd1 = data_drfd_pond1[selected_year - annee[0]]
        selected_data_drfd2 = data_drfd_pond2[selected_year - annee[0]]
        return fig_baton_total(selected_data_drfd1,selected_year , titres_graphe_drfd[0], titres_y_drfd[0]), \
               fig_baton_total(selected_data_drfd2,selected_year , titres_graphe_drfd[1], titres_y_drfd[1])