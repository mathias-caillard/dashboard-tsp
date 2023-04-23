from dash import Dash, html, dcc, Output, Input, callback, State
import dash
import sys
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from config import chemin_absolu_rep_parent



sys.path.append(chemin_absolu_rep_parent + '\\app_many_pages\\pages')   #pour pouvoir importer les variables entre fichiers dans /pages
sys.path.append(chemin_absolu_rep_parent + '\\app_many_pages\\pages\\departements')   #pour pouvoir importer les variables entre fichiers dans /pages/departements


app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)   #, suppress_callback_exceptions=True
load_figure_template("bootstrap")
app._favicon = "favicon.ico"





offcanvas = html.Div(
    [
        dbc.Offcanvas(
            id="offcanvas",
            title="Options",
            is_open=False,
            backdrop=False,
            scrollable=True,
            style = {"marginTop" : "60px"}
        ),
    ]
)




app.layout = dbc.Container([
     

	
        dbc.NavbarSimple(
            children=[
     

             dbc.Button("Options", id="open-offcanvas", n_clicks=0, color = "secondary", style = {"margin-right" : "15rem"}),
	

        
	

        html.Div(
        [
                #Boutons pour les différentes pages
                dbc.Button(
                    f"{page['name']}", href=page["relative_path"], outline=False, color="dark", className="me-1 btn-sm",  #btn-sm rend les boutons un peu plus petits
                    style = {'marginTop': '0px', 'flex': '1', 'height': '50px', 'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'whiteSpace': 'nowrap'}
                )

            for page in dash.page_registry.values()
            if not 'departements' in page['relative_path'] and not 'Accueil' in page['name']  # Filtrer les pages du dossier "pages" qui ne sont pas des departements, et la page accueil (qui est remplacé par le bouton tout à gauche)
	    
        ],
        className="d-flex"
    ),
            #Menu déroulant pour les departements

            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem(page['name'], href=page['relative_path'])
                    for page in dash.page_registry.values()
                    if 'departements' in page['relative_path']  # Filtrer les pages du dossier "departements"
                ],
                nav=True,
                in_navbar=True,
                label="Départements",  # Texte du bouton de menu déroulant
                color="dark",

            ),
	    

            dbc.NavItem(dbc.NavLink("À propos", href="#")),

            ], 
            className="navbar navbar-expand-lg navbar-light bg-light fixed-top",
            brand="Indicateurs de Télécom SudParis",
            brand_href="/",
            color="dark",
            dark=True,
	        fluid = True,
            style={'height': '60px'},



	    ),
	    

	dash.page_container,
	html.Div([
        dcc.Link('Remonter la page', href='#top')
    ], style={'position': 'fixed', 'bottom': '20px', 'right': '20px'}),
    offcanvas

	

],
style={'marginTop': '60px'},    #Contenu des pages sous la barre de navigation (et pas caché derrière)
fluid = True,
id = "output-container-"
)




@callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


@app.callback(
    Output('output-container-', 'style'),
    Input('open-offcanvas', 'n_clicks'),
    [State("offcanvas", "is_open")],
)
def update_margin(n1, is_open):
    if n1 % 2 == 1 : 
        return {'margin-left': "25rem", 'marginTop': '60px'}
    return {'margin-left': "0px", 'marginTop': '60px'}





if __name__ == '__main__':
	app.run_server(debug=True)



