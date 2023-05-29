
from src.functions.fonctions_historique import *


dash.register_page(
    __name__,
    title = "Historique",
    name = "Choix libre",
    order=91,
    active= False

)

layout = dbc.Container(children=[
    html.H1(
        children='Dans cette page, vous pouvez afficher les graphes de votre choix sur les années précédentes',
        style={'text-align': 'justify'}
    ),

    dcc.Loading(id = "loading", color = "black", type = "circle"),

    html.H2(children='Sélection de la plage temporelle :'),
    dcc.RangeSlider(
        id='annee-selector',
        min=min(annee),
        max=max(annee),
        value=[min(annee), max(annee)],
        marks={str(year): str(year) for year in annee},
        step=1
    ),

    #joue le rôle de variable globale
    dcc.Store(id='current-value', data=[]),

    #Menu déourlant/moteur de recherche
    dcc.Dropdown(
        options=categories,
        id="checklist-input",
        multi=True,
        placeholder="Veuillez selectionner des graphes à afficher.",
        persistence = True,
        searchable=True,
        clearable=True


    ),

    # Boucle pour générer les graphiques

            
            dbc.Container(id="graph-container-historique",
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
    Output("current-value", "data"),
    [Input("checklist-input", "value")],
    [State("current-value", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return update_old_value_(value, old_value)


# Boucle pour générer les callbacks pour chaque département
for i, cat in enumerate(categories):
    cat_id = cat["value"]


    @callback(
        Output(f"current_collapse{i + 1}", "is_open"),
        [Input("checklist-input", "value")],
        [State(f"collapse{i + 1}", "is_open"), State("current-value", "data")],
        prevent_initial_call=True
    )
    def toggle_collapse(value, is_open, data, cat_id=cat_id):
        return toggle_collapse_(value, is_open, data, cat_id=cat_id)

@callback(
    [Output("graph-container-historique", "children"),
     Output("loading", "parent-style")], #Permet d'afficher un Spinner de Char
    [Input("annee-selector", "value"),
     Input("checklist-input", "value")]
)
def generate_graphs(selected_years, value):
    return generate_graphs_(selected_years, value, [])