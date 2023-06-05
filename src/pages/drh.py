import dash_bootstrap_components as dbc
import dash
from dash import html, dcc, Input, Output, callback
from src.functions.fonction_figure import generate_graphs, fig_annuelle_baton, fig_camembert, fig_trim_baton, fig_trim_courbe, couleurs, couleurs_all

dash.register_page(
    __name__,
    title = "DRH",
    name = "DRH",
    order=6,
    active= False
                   )


def liste_graphes_drh(selected_annee) :

    return [
        dcc.Graph(
            id='drh1_tot',
            figure=fig_annuelle_baton("DRH-01", selected_annee, "Services/Départements", couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh1_cam',
            figure=fig_camembert("DRH-01", selected_annee, couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh2_tot',
            figure=fig_annuelle_baton("DRH-02", selected_annee, "Services/Départements", couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh2_cam',
            figure=fig_camembert("DRH-02", selected_annee, couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_bat',
            figure=fig_trim_baton("DRH-03", selected_annee, "Départements", couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_cou',
            figure=fig_trim_courbe("DRH-03", selected_annee, couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_tot',
            figure=fig_annuelle_baton("DRH-03", selected_annee, "Départements", couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_cam',
            figure=fig_camembert("DRH-03", selected_annee, couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh4_tot',
            figure=fig_annuelle_baton("DRH-04", selected_annee, "Services/Départements", couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh4_cam',
            figure=fig_camembert("DRH-04", selected_annee, couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh5_tot',
            figure=fig_annuelle_baton("DRH-05", selected_annee, "Services/Départements", couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh5_cam',
            figure=fig_camembert("DRH-05", selected_annee, couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh6_tot',
            figure=fig_annuelle_baton("DRH-06", selected_annee, "Services/Départements", couleurs_all),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh6_cam',
            figure=fig_camembert("DRH-06", selected_annee, couleurs_all),
            config={'displaylogo': False}
        ),

    ]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant la Direction des Ressources Humaines',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-drh", color = "black", type = "circle"),

    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-drh",
                children=[],
                fluid = True),
    ],
fluid = True
)


@callback(
    [Output("graph-container-historique-drh", "children"),
     Output("loading-drh", "parent-style")], #Permet d'afficher un Spinner de Char
    Input("choix-annee", "value")

)

def generate_graphs_drh(selected_year):
    return generate_graphs(selected_year, baseline_graph = liste_graphes_drh(selected_year))

