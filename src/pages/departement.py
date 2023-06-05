import dash
from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from src.functions.fonction_figure import generate_graphs, fig_radar, fig_radar_all_dept


dash.register_page(
    __name__,
    title = "Comparaison départements",
    name = "Comparaison départements",
    order=8,
    active= False
                   )


def liste_graphes_departement(selected_annee) :
    return [
        dcc.Graph(
            id='radar_all_dept',
            figure=fig_radar_all_dept(selected_annee),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_artemis',
            figure=fig_radar(selected_annee, 0),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_citi',
            figure=fig_radar(selected_annee, 1),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_eph',
            figure=fig_radar(selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_inf',
            figure=fig_radar(selected_annee, 3),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_rs2m',
            figure=fig_radar(selected_annee, 4),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_rst',
            figure=fig_radar(selected_annee, 5),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='radar_tsp',
            figure=fig_radar(selected_annee, 6),
            config={'displaylogo': False}
        ),


]


layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page proposant une comparaison entre départements',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-dept", color = "black", type = "circle"),


    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-dept",
                children=[],
                fluid = True),
    ],
fluid = True
)


@callback(
    [Output("graph-container-historique-dept", "children"),
     Output("loading-dept", "parent-style")], #Permet d'afficher un Spinner de Char
    Input("choix-annee", "value"),

)

def generate_graphs_departement(selected_year):
    return generate_graphs(selected_year, baseline_graph = liste_graphes_departement(selected_year))


