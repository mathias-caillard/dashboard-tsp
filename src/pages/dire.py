import dash
from dash import html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
from src.functions.fonction_figure import generate_graphs, fig_annuelle_baton, fig_camembert, fig_trim_baton, fig_trim_courbe, couleurs


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

            # Boucle pour générer les graphiques
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





"""
dcc.Graph(
        id='dire-graph1',
        figure=fig_baton_trimestre(selected_data_dire1,selected_annee , titres_graphe_dire[0], titres_y_dire[0]),
        config = {'displaylogo': False}
        ),




    dcc.Graph(
        id='dire-graph2',
        figure= fig_baton_total(selected_data_dire2_total,selected_annee , titres_graphe_dire[1], titres_y_dire[1]),
        config = {'displaylogo': False}
        ),



    dcc.Graph(
        id='dire-graph3',
        figure=fig_baton_departement(selected_data_dire3,selected_annee , titres_graphe_dire[2], titres_y_dire[2]),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='example-graph1',
        figure=fig_dire_1(),
        config = {'displaylogo': False}
        ),




    dcc.Graph(
        id='example-graph2',
        figure=fig_dire_2(),
        config = {'displaylogo': False}
        ),



    dcc.Graph(
        id='example-graph3',
        figure=fig_dire_3(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph4',
        figure=fig_dire_4(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph1',
        figure=fig_old_dire_1(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph1_tri',
        figure=fig_old_dire_1_tri(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph1_tot',
        figure=fig_old_dire_1_tot(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph2',
        figure=fig_old_dire_2(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph3',
        figure=fig_old_dire_3(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph3_tri',
        figure=fig_old_dire_3_tri(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph3_tot',
        figure=fig_old_dire_3_tot(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph4',
        figure=fig_old_dire_4(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph5',
        figure=fig_old_dire_5(),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='old-graph5_tri',
        figure=fig_old_dire_5_tri(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph5_tot',
        figure=fig_old_dire_5_tot(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph6',
        figure=fig_old_dire_6(),
        config = {'displaylogo': False}
    ),
"""

"""
"dire_old_1_tri",
            "dire_old_1_tot",
            "dire_old_1_comp",
            "dire_old_2_tri",
            "dire_old_2_tot",
            "dire_old_2_comp",
            "dire_old_3_tri",
            "dire_old_3_tot",
            "dire_old_3_comp",
"""