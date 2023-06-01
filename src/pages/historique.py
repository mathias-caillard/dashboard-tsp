import dash
from src.functions.fonctions_historique import *


dash.register_page(
    __name__,
    title = "Historique",
    name = "Historique",
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
        min=min(annees),
        max=max(annees),
        value=[min(annees), max(annees)],
        marks={str(year): str(year) for year in annees},
        step=1
    ),

    #joue le rôle de variable globale
    dcc.Store(id='current-value', data=[]),

    #Menu déourlant/moteur de recherche
    dcc.Dropdown(
        options=categories_historique,
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
for i, cat in enumerate(categories_historique):
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
    return generate_graphs_historique(selected_years, value, [])



