import dash
from dash import html, dcc
from src.fig.departement_fig import *
from src.fig.eph_fig import *
from dash import html, dcc, Output, Input, State, callback
from src.functions.fonctions_historique import *
from src.functions.fonction_figure import generate_graphs, fig_dept_trim_baton, fig_radar





dash.register_page(
    __name__,
    title = "EPH",
    name = "EPH",
    order=13,
    active= False
                   )


def liste_graphes_eph(selected_annee) :
    return [
        dcc.Graph(
            id='radar_eph',
            figure=fig_radar(selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire1_bat_eph',
            figure=fig_dept_trim_baton("DIRE-01", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire2_bat_eph',
            figure=fig_dept_trim_baton("DIRE-02", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire3_bat_eph',
            figure=fig_dept_trim_baton("DIRE-03", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf1_bat_eph',
            figure=fig_dept_trim_baton("DAF-01", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf2_bat_eph',
            figure=fig_dept_trim_baton("DAF-02", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf3_bat_eph',
            figure=fig_dept_trim_baton("DAF-03", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf4_bat_eph',
            figure=fig_dept_trim_baton("DAF-04", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf5_bat_eph',
            figure=fig_dept_trim_baton("DAF-05", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_bat_eph',
            figure=fig_dept_trim_baton("DRH-03", selected_annee, 2),
            config={'displaylogo': False}
        ),

    ]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant le département EPH',
        style={'text-align': 'justify'}
    ),

    dcc.Loading(id = "loading-eph", color = "black", type = "circle"),


    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-eph",
                children=[],
                fluid = True),
    ],
fluid = True
)


@callback(
    [Output("graph-container-historique-eph", "children"),
     Output("loading-eph", "parent-style")], #Permet d'afficher un Spinner de Char
    Input("choix-annee", "value")

)

def generate_graphs_eph(selected_year):
    return generate_graphs(selected_year, baseline_graph = liste_graphes_eph(selected_year))

