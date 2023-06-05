import dash_bootstrap_components as dbc
import dash
from dash import html, dcc, Output, Input, callback
from src.functions.fonction_figure import generate_graphs, fig_annuelle_baton, fig_camembert, fig_trim_baton, couleurs





dash.register_page(
    __name__,
    title="DF",
    name="DF",
    order=2,
    active= False
    )


def liste_graphes_df(selected_annee) :
    return [
    dcc.Graph(
        id='df1_tot',
        figure=fig_annuelle_baton("DF-01", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='df1_cam',
        figure=fig_camembert("DF-01", selected_annee, couleurs),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='df2_bat',
        figure=fig_trim_baton("DF-02", selected_annee, "Temps", None),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='df3_bat',
        figure=fig_trim_baton("DF-03", selected_annee, "Temps", None),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='df4_bat',
        figure=fig_trim_baton("DF-04", selected_annee, "Temps", None),
        config={'displaylogo': False}
    ),

    dcc.Graph(
        id='df5_bat',
        figure=fig_trim_baton("DF-05", selected_annee, "Temps", None),
        config={'displaylogo': False}
    ),

    dcc.Graph(
        id='df6_bat',
        figure=fig_trim_baton("DF-06", selected_annee, "Temps", None),
        config={'displaylogo': False}
    )
]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant la Direction des Formations',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-df", color = "black", type = "circle"),

    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-df",
                children=[],
                fluid = True),
    ],
fluid = True
)

@callback(
    [Output("graph-container-historique-df", "children"),
     Output("loading-df", "parent-style")], #Permet d'afficher un Spinner de Char
    Input("choix-annee", "value"),

)

def generate_graphs_df(selected_year):
    return generate_graphs(selected_year, baseline_graph = liste_graphes_df(selected_year))
