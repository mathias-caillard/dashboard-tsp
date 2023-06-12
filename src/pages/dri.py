import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from  functions.fonction_figure import generate_graphs, fig_annuelle_baton, fig_trim_baton



dash.register_page(
    __name__,
    title = "DRI",
    name = "DRI",
    order=7,
    active= False
                   )


def liste_graphes_dri(selected_annee) :
    return [
        dcc.Graph(
            id='dri1_bat',
            figure=fig_trim_baton("DRI-01", selected_annee, "Temps", None),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dri2_bat',
            figure=fig_trim_baton("DRI-02", selected_annee, "Temps", None),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dri3_bat',
            figure=fig_trim_baton("DRI-03", selected_annee, "Temps", None),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dri4_bat',
            figure=fig_trim_baton("DRI-04", selected_annee, "Temps", None),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dri5_bat',
            figure=fig_trim_baton("DRI-05", selected_annee, "Temps", None),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dri6_tot',
            figure=fig_annuelle_baton("DRI-06", selected_annee, "", None),
            config={'displaylogo': False}
        ),

    ]

layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant la Direction des Relations Internationales',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-dri", color = "black", type = "circle"),


    # Boucle pour generer les graphiques
            dbc.Container(id="graph-container-historique-dri",
                children=[],
                fluid = True),
    ],
fluid = True
)

@callback(
    [Output("graph-container-historique-dri", "children"),
     Output("loading-dri", "parent-style")], #Permet d'afficher un Spinner de Char
    Input("choix-annee", "value")

)

def generate_graphs_dri(selected_year):
    return generate_graphs(selected_year, baseline_graph = liste_graphes_dri(selected_year))
