import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from functions.fonction_figure import generate_graphs, fig_annuelle_baton, fig_camembert, couleurs


dash.register_page(
    __name__,
    title = "DRFD",
    name = "DRFD",
    order=3,
    active= False
                   )
def liste_graphes_drfd(selected_annee) :
    return [
dcc.Graph(
        id='drfd1_tot',
        figure=fig_annuelle_baton("DRFD-01", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='drfd1_cam',
        figure=fig_camembert("DRFD-01", selected_annee, couleurs),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='drfd2_tot',
        figure=fig_annuelle_baton("DRFD-02", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='drfd2_cam',
        figure=fig_camembert("DRFD-02", selected_annee, couleurs),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='drfd3_tot',
        figure=fig_annuelle_baton("DRFD-03", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}
    ),
]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant la DRFD',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-drfd", color = "black", type = "circle"),

    # Boucle pour generer les graphiques
            dbc.Container(id="graph-container-historique-drfd",
                children=[],
                fluid = True),
    ],
fluid = True
)


@callback(
    [Output("graph-container-historique-drfd", "children"),
     Output("loading-drfd", "parent-style")], #Permet d'afficher un Spinner de Char
    Input("choix-annee", "value")

)

def generate_graphs_drfd(selected_year):
    return generate_graphs(selected_year, baseline_graph = liste_graphes_drfd(selected_year))




