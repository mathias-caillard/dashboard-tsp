import dash
from dash import dcc, html, Dash
from dash.dependencies import Input, Output
import os

# Création de l'application
app = Dash(__name__, use_pages=True)
app._favicon = "favicon.ico"

# Création du menu de navigation
nav_items = []
for page in dash.page_registry.values():
    nav_items.append(
        dcc.Link(
            page['name'],
            href=page["relative_path"],
            className="nav-link",
            style= {"margin-right": "10px"}  # Ajouter un espace entre les liens
        )
    )
nav = html.Nav(
    children=[


        html.Div(
            nav_items,
            className="collapse navbar-collapse",
            id="navbarNav",
            style = {}

        )
    ],
    className="navbar navbar-expand-lg navbar-light bg-light fixed-top",
    style={"position": "fixed", "width": "100%", "z-index": "100",
           "background-color": "white", "color": "blue",
           "box-shadow": "2px 2px 5px grey", "top": "0"}  #fixed rends la barre de navigation  visible quand on scroll
            #top=0 permet de coller la barre de navigation en haut
)

# Définition du layout de l'application
app.layout = html.Div([
    nav,
    dash.page_container
])




if __name__ == '__main__':
    app.run_server(debug=True)