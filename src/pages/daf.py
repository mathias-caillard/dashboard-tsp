import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from   functions.fonction_figure import generate_graphs, fig_annuelle_baton, fig_camembert, fig_trim_baton,fig_trim_courbe, couleurs



dash.register_page(
    __name__,
    title = "DAF",
    name = "DAF",
    order=5,
    active= False
                   )

def liste_graphes_daf(selected_annee) :
     return [
         dcc.Graph(
             id='daf1_bat',
             figure=fig_trim_baton("DAF-01", selected_annee, "Départements", couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf1_cou',
             figure=fig_trim_courbe("DAF-01", selected_annee, couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf1_tot',
             figure=fig_annuelle_baton("DAF-01", selected_annee, "Départements", couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf1_cam',
             figure=fig_camembert("DAF-01", selected_annee, couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf2_bat',
             figure=fig_trim_baton("DAF-02", selected_annee, "Départements", couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf2_cou',
             figure=fig_trim_courbe("DAF-02", selected_annee, couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf2_tot',
             figure=fig_annuelle_baton("DAF-02", selected_annee, "Départements", couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf2_cam',
             figure=fig_camembert("DAF-02", selected_annee, couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf3_bat',
             figure=fig_trim_baton("DAF-03", selected_annee, "Départements", couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf3_cou',
             figure=fig_trim_courbe("DAF-03", selected_annee, couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf3_tot',
             figure=fig_annuelle_baton("DAF-03", selected_annee, "Départements", couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf3_cam',
             figure=fig_camembert("DAF-03", selected_annee, couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf4_bat',
             figure=fig_trim_baton("DAF-04", selected_annee, "Départements", couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf4_cou',
             figure=fig_trim_courbe("DAF-04", selected_annee, couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf4_tot',
             figure=fig_annuelle_baton("DAF-04", selected_annee, "Départements", couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf4_cam',
             figure=fig_camembert("DAF-04", selected_annee, couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf5_bat',
             figure=fig_trim_baton("DAF-05", selected_annee, "Départements", couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf5_cou',
             figure=fig_trim_courbe("DAF-05", selected_annee, couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf5_tot',
             figure=fig_annuelle_baton("DAF-05", selected_annee, "Départements", couleurs),
             config={'displaylogo': False}
         ),


         dcc.Graph(
             id='daf6_tot',
             figure=fig_annuelle_baton("DAF-06", selected_annee, "Départements", couleurs),
             config={'displaylogo': False}
         ),

         dcc.Graph(
             id='daf6_cam',
             figure=fig_camembert("DAF-06", selected_annee, couleurs),
             config={'displaylogo': False}
         )
    ]

layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant la DAF',
        style={'text-align': 'justify'}
    ),
    dcc.Loading(id = "loading-daf", color = "black", type = "circle"),

    # Boucle pour generer les graphiques
            dbc.Container(id="graph-container-historique-daf",
                children=[],
                fluid = True),
    ],
fluid = True
)

@callback(
    [Output("graph-container-historique-daf", "children"),
     Output("loading-daf", "parent-style")], #Permet d'afficher un Spinner de Char
    Input("choix-annee", "value")

)

def generate_graphs_daf(selected_year):
    return generate_graphs(selected_year, baseline_graph = liste_graphes_daf(selected_year))

