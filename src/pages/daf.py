import dash
from dash import html, dcc, callback, Output, Input, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src import config
from src.fig.daf_fig import *
from src.data.data import *
from src.functions.fonction_figure import fig_annuelle_baton, fig_camembert, fig_trim_baton,fig_trim_courbe, couleurs
from src.functions.fonctions_historique import *


dash.register_page(
    __name__,
    title = "DAF",
    name = "DAF",
    order=5,
    active= False
                   )

titres_graphe_daf = titres_graphe[1:4]
titres_y_daf = titres_y[1:4]

data_daf_pond1 = ponderation(data.data.data_daf[0])
data_daf_pond2 = ponderation(data.data.data_daf[1])
data_daf_pond3 = ponderation(data.data.data_daf[2])
data_daf_pond1_total = ponderation_total(data.data.data_daf[0])
data_daf_pond2_total = ponderation_total(data.data.data_daf[1])
data_daf_pond3_total = ponderation_total(data.data.data_daf[2])

data_daf_pond1.append(data_daf_2023[0])
data_daf_pond2.append(data_daf_2023[1])
data_daf_pond3.append(data_daf_2023[2])
data_daf_pond1_total.append(data_daf_2023_total[0])
data_daf_pond2_total.append(data_daf_2023_total[1])
data_daf_pond3_total.append(data_daf_2023_total[2])

selected_data_daf1 = data_daf_pond1[-1]
selected_data_daf2 = data_daf_pond2[-1]
selected_data_daf3 = data_daf_pond3[-1]
selected_data_daf1_total = data_daf_pond1_total[-1]
selected_data_daf2_total = data_daf_pond2_total[-1]
selected_data_daf3_total = data_daf_pond3_total[-1]


def liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_annee) :
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
             id='daf6_bat',
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


    #joue le rôle de variable globale
    dcc.Store(id='current-value-daf', data=[]),
    #Menu déourlant/moteur de recherche
    dcc.Dropdown(
        options=categories,
        id="checklist-input-daf",
        multi=True,
        placeholder="Veuillez selectionner des graphes à afficher.",
        persistence = True,
        value = [


        ],
        disabled = True,
        style={"display": "none"}
    ),
    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-daf",
                children=[],
                fluid = True),
    ],
fluid = True
)










#Mettre à jour les données du menu déroulant sélectionnées
@callback(
    Output("current-value-daf", "data"),
    [Input("checklist-input-daf", "value")],
    [State("current-value-daf", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return update_old_value_(value, old_value) #dans fonctions_historique.py


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories):
    cat_id = cat["value"]


    @callback(
        Output(f"current_collapse-daf{i + 1}", "is_open"),
        [Input("checklist-input-daf", "value")],
        [State(f"collapse-daf{i + 1}", "is_open"), State("current-value-daf", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        return toggle_collapse_(value, is_open, data, cat_id=cat_id)

@callback(
    [Output("graph-container-historique-daf", "children"),
     Output("loading-daf", "parent-style")], #Permet d'afficher un Spinner de Char
    [Input("choix-annee", "value"),
     Input("checklist-input-daf", "value"),
     ]
)

def generate_graphs(selected_year, value):
    return generate_graphs_(selected_year, value, baseline_graph = liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_year))



"""
dcc.Graph(
        id='daf-graph1',
        figure=fig_baton_trimestre(selected_data_daf1, selected_annee, titres_graphe_daf[0], titres_y_daf[0]),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='daf-graph2',
        figure=fig_baton_total(selected_data_daf2_total, selected_annee, titres_graphe_daf[1], titres_y_daf[1]),
        config = {'displaylogo': False}
    ),

  
    dcc.Graph(
        id='daf-graph3',
        figure=fig_baton_departement(selected_data_daf3, selected_annee, titres_graphe_daf[2], titres_y_daf[2]),
        config = {'displaylogo': False}
    ),

    dcc.Graph(
        id='example-graph1',
        figure=fig_daf_1(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='example-graph2',
        figure=fig_daf_2(),
        config = {'displaylogo': False}
    ),

   

    dcc.Graph(
        id='example-graph3',
        figure=fig_daf_3(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph4',
        figure=fig_daf_4(),
        config = {'displaylogo': False}
    ),

  
    dcc.Graph(
        id='example-graph5',
        figure=fig_daf_5(),
        config = {'displaylogo': False}
    ),




    dcc.Graph(
        id='example-graph6',
        figure=fig_daf_6(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph7',
        figure=fig_daf_7(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='example-graph8',
        figure=fig_daf_8(),
        config = {'displaylogo': False}
    ),

  
    dcc.Graph(
        id='example-graph9',
        figure=fig_daf_9(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph1',
        figure=fig_old_daf_1(),
        config = {'displaylogo': False}
    ),

    
    dcc.Graph(
        id='old-graph1_tri',
        figure=fig_old_daf_1_tri(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph1_tot',
        figure=fig_old_daf_1_tot(),
        config = {'displaylogo': False}
    ),

   

    dcc.Graph(
        id='old-graph2',
        figure=fig_old_daf_2(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph3',
        figure=fig_old_daf_3(),
        config = {'displaylogo': False}
    ),

    
    dcc.Graph(
        id='old-graph3_tri',
        figure=fig_old_daf_3_tri(),
        config = {'displaylogo': False}
    ),

  

    dcc.Graph(
        id='old-graph3_tot',
        figure=fig_old_daf_3_tot(),
        config = {'displaylogo': False}
    ),

   
    dcc.Graph(
        id='old-graph4',
        figure=fig_old_daf_4(),
        config = {'displaylogo': False}
    ),

  

    dcc.Graph(
        id='old-graph5',
        figure=fig_old_daf_5(),
        config = {'displaylogo': False}
    ),

   

    dcc.Graph(
        id='old-graph5_tri',
        figure=fig_old_daf_5_tri(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph5_tot',
        figure=fig_old_daf_5_tot(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='old-graph6',
        figure=fig_old_daf_6(),
        config = {'displaylogo': False}
    ),
"""

"""
"daf_old_1_tri",
                "daf_old_1_comp",
                "daf_old_1_tot",
                "daf_old_2_tri",
                "daf_old_2_comp",
                "daf_old_2_tot",
                "daf_old_3_tri",
                "daf_old_3_comp",
                "daf_old_3_tot",
"""