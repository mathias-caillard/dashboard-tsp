import dash
from dash import html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
from   functions.fonction_figure import generate_graphs, fig_annuelle_baton, fig_camembert, fig_trim_baton, fig_trim_courbe, couleurs


dash.register_page(
    __name__,
    title = "DIRE",
    name = "DIRE",
    order=4,
    active= False
                   )

def liste_graphes_dire(selected_annee) :
    return [
        dcc.Graph(
            id='dire1_bat',
            figure=fig_trim_baton("DIRE-01", selected_annee, "Départements", couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire1_cou',
            figure=fig_trim_courbe("DIRE-01", selected_annee, couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire1_tot',
            figure=fig_annuelle_baton("DIRE-01", selected_annee, "Départements", couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire1_cam',
            figure=fig_camembert("DIRE-01", selected_annee, couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire2_bat',
            figure=fig_trim_baton("DIRE-02", selected_annee, "Départements", couleurs),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire2_tot',
            figure=fig_annuelle_baton("DIRE-02", selected_annee, "Départements", couleurs),
            config={'displaylogo': False}
        ),

            dcc.Graph(
                id='dire2_cou',
                figure=fig_trim_courbe("DIRE-02", selected_annee, couleurs),
                config={'displaylogo': False}
            ),

            dcc.Graph(
                id='dire2_cam',
                figure=fig_camembert("DIRE-02", selected_annee, couleurs),
                config={'displaylogo': False}
            ),

            dcc.Graph(
                id='dire3_bat',
                figure=fig_trim_baton("DIRE-03", selected_annee, "Départements", couleurs),
                config={'displaylogo': False}
            ),

        dcc.Graph(
            id='dire3_tot',
            figure=fig_annuelle_baton("DIRE-03", selected_annee, "Départements", couleurs),
            config={'displaylogo': False}
        ),

                dcc.Graph(
                    id='dire3_cou',
                    figure=fig_trim_courbe("DIRE-03", selected_annee, couleurs),
                    config={'displaylogo': False}
                ),

                dcc.Graph(
                    id='dire3_cam',
                    figure=fig_camembert("DIRE-03", selected_annee, couleurs),
                    config={'displaylogo': False}
                )

        ]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant la DIRE',
        style={'text-align': 'justify'}
        ),
            dcc.Loading(id = "loading-dire", color = "black", type = "circle"),

            # Boucle pour generer les graphiques
                    dbc.Container(id="graph-container-historique-dire",
                        children=[],
                        fluid = True),
            ],
        fluid = True
        )


@callback(
            [Output("graph-container-historique-dire", "children"),
             Output("loading-dire", "parent-style")], #Permet d'afficher un Spinner de Char
            Input("choix-annee", "value"),
        )

def generate_graphs_dire(selected_year):
    return generate_graphs(selected_year, baseline_graph = liste_graphes_dire(selected_year))


