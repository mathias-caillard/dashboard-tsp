
from src.functions.fonctions_historique import *


dash.register_page(
    __name__,
    title = "Historique",
    name = "Choix libre",
    order=92,
    active= False

)

layout = dbc.Container(children=[
    html.H1(
        children='Dans cette page, vous pouvez afficher les graphes de votre choix.',
        style={'text-align': 'justify'}
    ),

    dcc.Loading(id = "loading-libre", color = "black", type = "circle"),


    #joue le rôle de variable globale
    dcc.Store(id='current-value-libre', data=[]),

    #Menu déourlant/moteur de recherche
    dcc.Dropdown(
        options=categories_libre,
        id="checklist-input-libre",
        multi=True,
        placeholder="Veuillez selectionner des graphes à afficher.",
        persistence = True,
        searchable=True,
        clearable=True


    ),

    # Boucle pour générer les graphiques

            
            dbc.Container(id="graph-container-libre",
                children=[],
                fluid = True),
            


            

    ],
fluid = True
)

"""
#Mettre à jour les données des graphes
@callback(
    Output('graph_test', 'figure'),
    [Input('annee-selector', 'value')])

def update_data(selected_years):

    global selected_global, selected_annee, selected_label

    filtered_data = [data_old[selected_years[0] - min(annee) : selected_years[1] - min(annee) + 1] for data_old in data_old_global]
    filtered_label = label[selected_years[0] - min(annee) : selected_years[1] - min(annee) + 1]

    selected_global = filtered_data
    selected_annee = [year for year in range(selected_years[0], selected_years[1] + 1)]
    selected_label = filtered_label

    #print(selected_annee)
    #print(selected_label)
    #print(selected_global)
    update_fig = fig_test(selected_global[0], selected_annee, selected_label)

    return update_fig
"""

"""
    dcc.Graph(
        id='graph_test',
        figure=fig_test(selected_global[0], selected_annee, selected_label),
        config = {'displaylogo': False}

    ),"""

#Mettre à jour les données du menu déroulant sélectionnées
@callback(
    Output("current-value-libre", "data"),
    [Input("checklist-input-libre", "value")],
    [State("current-value-libre", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return update_old_value_(value, old_value)


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories_libre):
    cat_id = cat["value"]


    @callback(
        Output(f"current_collapse-libre{i + 1}", "is_open"),
        [Input("checklist-input-libre", "value")],
        [State(f"collapse-libre{i + 1}", "is_open"), State("current-value-libre", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        return toggle_collapse_(value, is_open, data, cat_id=cat_id)

@callback(
    [Output("graph-container-libre", "children"),
     Output("loading-libre", "parent-style")], #Permet d'afficher un Spinner de Char
    [Input("choix-annee", "value"),
     Input("checklist-input-libre", "value")]
)
def generate_graphs(selected_years, value):
    return generate_graphs_libre(selected_years, value, [])



