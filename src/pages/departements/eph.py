import dash
from dash import html, dcc
from src.fig.departement_fig import *
from src.fig.eph_fig import *
from dash import html, dcc, Output, Input, State, callback
from src.functions.fonctions_historique import *
from src.functions.fonction_figure import fig_dept_trim_baton





dash.register_page(
    __name__,
    title = "EPH",
    name = "EPH",
    order=13,
    active= False
                   )


def liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_annee) :
    return [
        dcc.Graph(
            id='dire1_bat_eph',
            figure=fig_dept_trim_baton("DIRE-01", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire2_bat_eph',
            figure=fig_dept_trim_baton("DIRE-02", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='dire3_bat_eph',
            figure=fig_dept_trim_baton("DIRE-03", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf1_bat_eph',
            figure=fig_dept_trim_baton("DAF-01", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf2_bat_eph',
            figure=fig_dept_trim_baton("DAF-02", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf3_bat_eph',
            figure=fig_dept_trim_baton("DAF-03", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf4_bat_eph',
            figure=fig_dept_trim_baton("DAF-04", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='daf5_bat_eph',
            figure=fig_dept_trim_baton("DAF-05", selected_annee, 2),
            config={'displaylogo': False}
        ),

        dcc.Graph(
            id='drh3_bat_eph',
            figure=fig_dept_trim_baton("DRH-03", selected_annee, 2),
            config={'displaylogo': False}
        ),

    ]



layout = dbc.Container(children=[
    html.H1(
        children='Bienvenue sur la page concernant le département EPH',
        style={'text-align': 'justify'}
    ),

    dcc.Loading(id = "loading-eph", color = "black", type = "circle"),


    #joue le rôle de variable globale
    dcc.Store(id='current-value-eph', data=[]),
    #Menu déourlant/moteur de recherche
    dcc.Dropdown(
        options=categories,
        id="checklist-input-eph",
        multi=True,
        placeholder="Veuillez selectionner des graphes à afficher.",
        persistence = True,
        value = [

        ],
        disabled = True,
        style={"display": "none"}
    ),
    # Boucle pour générer les graphiques       
            dbc.Container(id="graph-container-historique-eph",
                children=[],
                fluid = True),
    ],
fluid = True
)










#Mettre à jour les données du menu déroulant sélectionnées
@callback(
    Output("current-value-eph", "data"),
    [Input("checklist-input-eph", "value")],
    [State("current-value-eph", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return update_old_value_(value, old_value) #dans fonctions_historique.py


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories):
    cat_id = cat["value"]


    @callback(
        Output(f"current_collapse-eph{i + 1}", "is_open"),
        [Input("checklist-input-eph", "value")],
        [State(f"collapse-eph{i + 1}", "is_open"), State("current-value-eph", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        return toggle_collapse_(value, is_open, data, cat_id=cat_id)

@callback(
    [Output("graph-container-historique-eph", "children"),
     Output("loading-eph", "parent-style")], #Permet d'afficher un Spinner de Char
    [Input("choix-annee", "value"),
     Input("checklist-input-eph", "value"),
     ]
)

def generate_graphs(selected_year, value):
    return generate_graphs_(selected_year, value, baseline_graph = liste_graphes_pas_encore_dans_historique_mais_dans_onglet_donc_cette_liste_est_temporaire(selected_year))



"""
dcc.Graph(
        id='example-graph2',
        figure=fig_dept_4(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph3',
        figure=fig_eph_1(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='example-graph4',
        figure=fig_eph_2(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='example-graph5',
        figure=fig_eph_3(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='example-graph6',
        figure=fig_eph_4(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='example-graph7',
        figure=fig_eph_5(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='example-graph8',
        figure=fig_eph_6(),
        config = {'displaylogo': False}
    ),



    dcc.Graph(
        id='example-graph9',
        figure=fig_eph_7(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph1',
        figure=fig_old_df_eph_1(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph1_tri',
        figure=fig_old_df_eph_1_tri(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph1_tot',
        figure=fig_old_df_tot_eph_1(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph2',
        figure=fig_old_df_eph_2(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph3',
        figure=fig_old_daf_eph_1(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph3_tri',
        figure=fig_old_daf_eph_1_tri(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph3_tot',
        figure=fig_old_daf_tot_eph_1(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph4',
        figure=fig_old_daf_eph_2(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph5',
        figure=fig_old_daf_eph_3(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph5_tri',
        figure=fig_old_daf_eph_3_tri(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph5_tot',
        figure=fig_old_daf_tot_eph_3(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph6',
        figure=fig_old_daf_eph_4(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph7',
        figure=fig_old_daf_eph_5(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph7_tri',
        figure=fig_old_daf_eph_5_tri(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph7_tot',
        figure=fig_old_daf_tot_eph_5(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph8',
        figure=fig_old_daf_eph_6(),
        config = {'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph9',
        figure=fig_old_dire_eph_1(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph9_tri',
        figure=fig_old_dire_eph_1_tri(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph9_tot',
        figure=fig_old_dire_tot_eph_1(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph10',
        figure=fig_old_dire_eph_2(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph11',
        figure=fig_old_dire_eph_3(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph11_tri',
        figure=fig_old_dire_eph_3_tri(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph11_tot',
        figure=fig_old_dire_tot_eph_3(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph12',
        figure=fig_old_dire_eph_4(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph13',
        figure=fig_old_dire_eph_5(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph13_tri',
        figure=fig_old_dire_eph_5_tri(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph13_tot',
        figure=fig_old_dire_tot_eph_5(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph14',
        figure=fig_old_dire_eph_6(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph15',
        figure=fig_old_drfd_eph_1(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph15_tri',
        figure=fig_old_drfd_eph_1_tri(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph15_tot',
        figure=fig_old_drfd_tot_eph_1(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph16',
        figure=fig_old_drfd_eph_2(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph17',
        figure=fig_old_drfd_eph_3(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph17_tri',
        figure=fig_old_drfd_eph_3_tri(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph17_tot',
        figure=fig_old_drfd_tot_eph_3(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph18',
        figure=fig_old_drfd_eph_4(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph19',
        figure=fig_old_drh_eph_1(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph19_tri',
        figure=fig_old_drh_eph_1_tri(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph19_tot',
        figure=fig_old_drh_tot_eph_1(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph20',
        figure=fig_old_drh_eph_2(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph21',
        figure=fig_old_drh_eph_3(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph21_tri',
        figure=fig_old_drh_eph_3_tri(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph21_tot',
        figure=fig_old_drh_tot_eph_3(),
        config={'displaylogo': False}
    ),


    dcc.Graph(
        id='old-graph22',
        figure=fig_old_drh_eph_4(),
        config={'displaylogo': False}
    ),"""


"""
 "df_old_1_tri",
                 "df_old_1_tot",
                 "df_old_1_comp"
"""