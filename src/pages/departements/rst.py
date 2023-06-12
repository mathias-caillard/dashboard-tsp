import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from    functions.fonction_figure import generate_graphs, fig_dept_trim_baton, fig_radar



dash.register_page(
    __name__,
    title = "RST",
    name = "RST",
    order=16,
    active= False
                   )

def liste_graphes_rst(selected_annee) :
    return [
        dcc.Graph(
            id='radar_rst',
            figure=fig_radar(selected_annee, 5),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire1_bat_rst',
            figure=fig_dept_trim_baton("DIRE-01", selected_annee, 5),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire2_bat_rst',
            figure=fig_dept_trim_baton("DIRE-02", selected_annee, 5),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire3_bat_rst',
            figure=fig_dept_trim_baton("DIRE-03", selected_annee, 5),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf1_bat_rst',
            figure=fig_dept_trim_baton("DAF-01", selected_annee, 5),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf2_bat_rst',
            figure=fig_dept_trim_baton("DAF-02", selected_annee, 5),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf3_bat_rst',
            figure=fig_dept_trim_baton("DAF-03", selected_annee, 5),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf4_bat_rst',
            figure=fig_dept_trim_baton("DAF-04", selected_annee, 5),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf5_bat_rst',
            figure=fig_dept_trim_baton("DAF-05", selected_annee, 5),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_bat_rst',
            figure=fig_dept_trim_baton("DRH-03", selected_annee, 5),
            config={'displaylogo': False}
        ),

    ]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant le département RST',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-rst", color = "black", type = "circle"),


    # Boucle pour generer les graphiques
            dbc.Container(id="graph-container-historique-rst",
                children=[],
                fluid = True),
    ],
fluid = True
)


@callback(
    [Output("graph-container-historique-rst", "children"),
     Output("loading-rst", "parent-style")], #Permet d'afficher un Spinner de Char
    Input("choix-annee", "value")

)

def generate_graphs_rst(selected_year):
    return generate_graphs(selected_year, baseline_graph = liste_graphes_rst(selected_year))

