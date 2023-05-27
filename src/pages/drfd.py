import dash
from dash import html, dcc, Input, Output, State, callback
from src.fig.drfd_fig import *
from src.data.data import *
from src.functions.fonction_figure import fig_annuelle_baton, fig_camembert, fig_trim_baton


dash.register_page(
    __name__,
    title = "DRFD",
    name = "DRFD",
    order=3,
    active= False
                   )

"""
titres_graphe_drfd = titres_graphe[7:9]
titres_y_drfd = titres_y[7:9]

data_drfd_pond1 = ponderation_total(data.data_drfd[0])
data_drfd_pond2 = ponderation_total(data.data_drfd[1])
data_drfd_pond1.append(data_drfd_2023[0])
data_drfd_pond2.append(data_drfd_2023[1])

selected_data_drfd1 = data_drfd_pond1[-1]
selected_data_drfd2 = data_drfd_pond2[-1]
"""

annee = config.liste_annee_maj
selected_annee = annee[-1]

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la DRFD'),

    dcc.Graph(
        id='drfd1_bat',
        figure=fig_annuelle_baton("DRFD-01", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='drfd1_cam',
        figure=fig_camembert("DRFD-01", selected_annee, couleurs),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='drfd2_bat',
        figure=fig_annuelle_baton("DRFD-02", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='drfd2_cam',
        figure=fig_camembert("DRFD-02", selected_annee, couleurs),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='drfd3_bat',
        figure=fig_annuelle_baton("DRFD-03", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


])

@callback(
    [Output('drfd1_bat', 'figure'), Output('drfd1_cam', 'figure'),
     Output('drfd2_bat', 'figure'), Output('drfd2_cam', 'figure'),
     Output('drfd3_bat', 'figure')
     ],
    Input('choix-annee', 'value')
)
def update_graphes(selected_year):
    list_fig = []
    list_fig.append(fig_annuelle_baton("DRFD-01", selected_year, "Départements", couleurs))
    list_fig.append(fig_camembert("DRFD-01", selected_year, couleurs))
    list_fig.append(fig_annuelle_baton("DRFD-02", selected_year, "Départements", couleurs))
    list_fig.append(fig_camembert("DRFD-02", selected_year, couleurs))
    list_fig.append(fig_annuelle_baton("DRFD-03", selected_year, "Départements", couleurs))

    return list_fig


"""
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
"""