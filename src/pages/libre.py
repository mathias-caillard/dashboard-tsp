
from src.functions.fonctions_choix_libre import *


dash.register_page(
    __name__,
    title = "Choix libre",
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

#Mettre à jour les données du menu déroulant sélectionnées
@callback(
    Output("current-value-libre", "data"),
    [Input("checklist-input-libre", "value")],
    [State("current-value-libre", "data")],
    prevent_initial_call=True
)
def update_old_value(value, old_value):
    return value


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
        if (cat_id in value and cat_id in data) or (cat_id not in value and cat_id not in data):
            return is_open
        return not is_open


@callback(
    [Output("graph-container-libre", "children"),
     Output("loading-libre", "parent-style")], #Permet d'afficher un Spinner de Char
    [Input("choix-annee", "value"),
     Input("checklist-input-libre", "value")]
)
def generate_graphs(selected_years, value):
    return generate_graphs_libre(selected_years, value, [])



