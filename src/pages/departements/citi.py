import dash
from dash import html, dcc
from src.fig.departement_fig import *
from src.fig.citi_fig import *
from dash import html, dcc, Output, Input, State, callback
from src.functions.fonctions_historique import *
from src.functions.fonction_figure import generate_graphs, fig_dept_trim_baton, fig_radar



dash.register_page(
    __name__,
    title = "CITI",
    name = "CITI",
    order=12,
    active= False
                   )


def liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_annee) :
    return [
        dcc.Graph(
            id='radar_citi',
            figure=fig_radar(selected_annee, 1),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire1_bat_citi',
            figure=fig_dept_trim_baton("DIRE-01", selected_annee, 1),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire2_bat_citi',
            figure=fig_dept_trim_baton("DIRE-02", selected_annee, 1),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire3_bat_citi',
            figure=fig_dept_trim_baton("DIRE-03", selected_annee, 1),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf1_bat_citi',
            figure=fig_dept_trim_baton("DAF-01", selected_annee, 1),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf2_bat_citi',
            figure=fig_dept_trim_baton("DAF-02", selected_annee, 1),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf3_bat_citi',
            figure=fig_dept_trim_baton("DAF-03", selected_annee, 1),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf4_bat_citi',
            figure=fig_dept_trim_baton("DAF-04", selected_annee, 1),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf5_bat_citi',
            figure=fig_dept_trim_baton("DAF-05", selected_annee, 1),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_bat_citi',
            figure=fig_dept_trim_baton("DRH-03", selected_annee, 1),
            config={'displaylogo': False}
        ),

 
]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant le département CITI',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-citi", color = "black", type = "circle"),


    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-citi",
                children=[],
                fluid = True),
    ],
fluid = True
)



@callback(
    [Output("graph-container-historique-citi", "children"),
     Output("loading-citi", "parent-style")], #Permet d'afficher un Spinner de Char
    Input("choix-annee", "value")

)

def generate_graphs_citi(selected_year):
    return generate_graphs(selected_year, baseline_graph = liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_year))


