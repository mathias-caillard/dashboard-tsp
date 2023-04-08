from dash import Dash, html, dcc
import dash
import os
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from config import chemin_absolu_rep_parent




app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
load_figure_template("bootstrap")
app._favicon = "favicon.ico"

app.layout = dbc.Container([
	
        dbc.NavbarSimple(
            children=[
	

        html.Div(
        [
                #Boutons pour les différentes pages
                dbc.Button(
                    f"{page['name']}", href=page["relative_path"], outline=True, color="primary", className="me-1 btn-sm",  #btn-sm rend les boutons un peu plus petits
                    style = {'marginTop': '0px', 'flex': '1', 'height': '50px', 'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'whiteSpace': 'nowrap'}
                )

            for page in dash.page_registry.values()
            if not 'departement' in page['relative_path']  # Filtrer les pages du dossier "pages" qui ne sont pas des departements
	    
        ],
        className="d-flex"
    ),
            #Menu déroulant pour les départements

            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem(page['name'], href=page['relative_path'])
                    for page in dash.page_registry.values()
                    if 'departements' in page['relative_path']  # Filtrer les pages du dossier "departments"
                ],
                nav=True,
                in_navbar=True,
                label="Départements",  # Texte du bouton de menu déroulant
                color="dark",

            )

            ], 
            className="navbar navbar-expand-lg navbar-light bg-light fixed-top",
            brand="Indicateurs de Télécom SudParis",
            brand_href="#",
            color="dark",
            dark=True,
	        fluid = True,
            style={'height': '60px'},



	    ),
	    

	dash.page_container,
	

],
style={'marginTop': '60px'},    #Contenu des pages sous la barre de navigation (et pas caché derrière)
fluid = True,
)

if __name__ == '__main__':
	app.run_server(debug=True)



"""dbc.NavItem(dbc.NavLink("Page 1", href="#")),
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Plus de pages", header=True),
                        dbc.DropdownMenuItem("Page 2", href="#"),
                        dbc.DropdownMenuItem("Page 3", href="#"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="...",
                ),"""