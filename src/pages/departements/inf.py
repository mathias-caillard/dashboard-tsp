import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from    functions.fonction_figure import generate_graphs, fig_dept_trim_baton, fig_radar


dash.register_page(
    __name__,
    title = "INF",
    name = "INF",
    order=14,
    active= False

),



def liste_graphes_inf(selected_annee) :
    return [
        dcc.Graph(
            id='radar_inf',
            figure=fig_radar(selected_annee, 3),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire1_bat_inf',
            figure=fig_dept_trim_baton("DIRE-01", selected_annee, 3),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire2_bat_inf',
            figure=fig_dept_trim_baton("DIRE-02", selected_annee, 3),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire3_bat_inf',
            figure=fig_dept_trim_baton("DIRE-03", selected_annee, 3),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf1_bat_inf',
            figure=fig_dept_trim_baton("DAF-01", selected_annee, 3),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf2_bat_inf',
            figure=fig_dept_trim_baton("DAF-02", selected_annee, 3),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf3_bat_inf',
            figure=fig_dept_trim_baton("DAF-03", selected_annee, 3),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf4_bat_inf',
            figure=fig_dept_trim_baton("DAF-04", selected_annee, 3),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf5_bat_inf',
            figure=fig_dept_trim_baton("DAF-05", selected_annee, 3),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_bat_inf',
            figure=fig_dept_trim_baton("DRH-03", selected_annee, 3),
            config={'displaylogo': False}
        ),
    ]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant le département INF',
        style={'text-align': 'justify'}
    ),

    dcc.Loading(id = "loading-inf", color = "black", type = "circle"),


    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-inf",
                children=[],
                fluid = True),
    ],
fluid = True
)


@callback(
    [Output("graph-container-historique-inf", "children"),
     Output("loading-inf", "parent-style")], #Permet d'afficher un Spinner de Char
    Input("choix-annee", "value")

)

def generate_graphs_inf(selected_year):
    return generate_graphs(selected_year, baseline_graph = liste_graphes_inf(selected_year))

