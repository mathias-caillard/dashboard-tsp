from dash import Dash, html, dcc, Output, Input, State, ALL
import dash
import sys
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash_bootstrap_templates import load_figure_template
from config import chemin_absolu_rep_parent
from src.fig.df_fig import *
from flask import send_file
from src import config


 

sys.path.append(chemin_absolu_rep_parent + '\\src\\pages')   #pour pouvoir importer les variables entre fichiers dans /pages
sys.path.append(chemin_absolu_rep_parent + '\\src\\pages\\departements')   #pour pouvoir importer les variables entre fichiers dans /pages/departements


app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)   #, suppress_callback_exceptions=True
load_figure_template("bootstrap")
app._favicon = "favicon.ico"

# Définir une variable active_page initialement à la page d'accueil
active_page = "/"


annee = config.liste_annee_selection




#Importation des DATA
data_df = data.data.data_df
data_daf = data.data.data_daf
data_dire = data.data.data_dire
data_drfd = data.data.data_drfd
data_drh = data.data.data_drh

#Sidebar
offcanvas = html.Div(
    [
        dbc.Offcanvas(
            id="offcanvas",
            title="Options",
            is_open=False,
            backdrop=False,
            scrollable=True,
            close_button=False,
            style = {"marginTop" : "60px"},
            children = [
                html.H3(children='Sélection de l\'année',
                        style={'font-size': '18px'}),

                dcc.Dropdown(
                    id = "choix-annee",
                    options = annee,
                    multi = False,
                    value=annee[0],
                    persistence = True,
                ),
 

                dbc.Switch(
                    id="COP-switch",
                    label="Objectifs COP (IP Paris)",
                    value=False,
                ),
                dbc.Switch(
                    id="IMT-switch",
                    label="Objectifs IMT",
                    value=False,
                ),

                html.Hr(style={'borderTop': '2px solid #000000'}),


                dbc.Switch(
                    id="tri-switch",
                    label="afficher indicateurs trimestriels",
                    value=False,
                ),
                dbc.Switch(
                    id="ann-switch",
                    label="afficher indicateurs annuels",
                    value=False,
                ),

                html.Hr(style={'borderTop': '2px solid #000000'}),

                dbc.Switch(
                    id="école-switch",
                    label="indicateur périmètre école",
                    value=False,
                ),
                dbc.Switch(
                    id="dept-switch",
                    label="indicateur périmètre départemental",
                    value=False,
                ),
                    html.Hr(style={'borderTop': '2px solid #000000'}),
                    html.P('Télécharger les jeux de données : '),
                    html.A('indicateurs années 2023', href="/download/" + config.fichier_2023),
                    html.Br(),
                    html.A('indicateurs historiques', href="/download/" + config.fichier_historique),
                

            ],
        ),
    ],
)
 
 



app.layout = dbc.Container([

        dbc.NavbarSimple(
            children=[
                #Bouton pour afficher ou cacher la sidebar
             dbc.Button("Options", id="open-offcanvas", n_clicks=0, color = "secondary", style = {"margin-right" : "4rem"}),

        html.Div(
        [
                #Boutons pour les différentes pages
                dbc.Button(
                    f"{page['name']}", href=page["relative_path"], outline=False, color="dark", className="me-1 btn-sm" + (" active" if page["active"] else ""),  #btn-sm rend les boutons un peu plus petits
                    style = {'marginTop': '0px', 'flex': '1', 'height': '60px', 'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'},#, 'whiteSpace': 'nowrap'}
                    id={'type': 'tab-button', 'index': page["relative_path"]}  # Ajoutez cette ligne pour identifier le bouton d'onglet
                )

            for page in dash.page_registry.values()
            if not 'departements' in page['relative_path'] and not 'Accueil' in page['name'] and not "a-propos" in page["relative_path"]  # Filtrer les pages du dossier "pages" qui ne sont pas des departements, et la page accueil (qui est remplacé par le bouton tout à gauche)
	    
        ],
        className="d-flex me-auto justify-content-me-end"
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
                className="ms-auto"

            ),
	    
            #Boutons à propos
            dbc.NavItem(dbc.NavLink("À propos", href="/a-propos")),

            ], 
            className="navbar navbar-expand-lg navbar-light bg-light fixed-top",
            brand="Indicateurs de Télécom SudParis",
            brand_href="/",
            color="dark",
            dark=True,
	        fluid = True,
            style={'height': '60px', 'justifyContent': 'center', 'alignItems': 'center'},



	    ),


    dcc.Location(id='url', refresh=False),
    dbc.Container(id="page-content", className="pt-4"),
	dash.page_container,

    #Bouton permettant de remonter la page
	html.Div([
        dcc.Link('Remonter la page', href='#top')
    ], style={'position': 'fixed', 'bottom': '20px', 'right': '20px'}),
    offcanvas

	

],
style={'marginTop': '60px'},    #Contenu des pages sous la barre de navigation (et pas caché derrière)
fluid = True,
id = "output-container-"
)




@app.callback(
    Output('page-content', 'children'),
    Output({'type': 'tab-button', 'index': ALL}, 'className'),
    Input('url', 'pathname')
)

#Permet d'afficher la page désirée
def render_page_content(pathname):
    for page in dash.page_registry.values():
        if 'departements' not in page['relative_path'] and not 'Accueil' in page['name'] and "a-propos" not in page["relative_path"]:
            if page['relative_path'] == pathname:
                page['active'] = True
            else:
                page['active'] = False

    return html.Div([

    ]), [
               "me-1 btn-sm active" if page["active"] else "me-1 btn-sm"
               for page in dash.page_registry.values() if not 'departements' in page['relative_path'] and not 'Accueil' in page['name'] and "a-propos" not in page["relative_path"]
           ]


@app.callback(
    Output('output', 'children'),
    Input('input', 'value'),
    State('input', 'id')
)
# Fonction pour déterminer l'onglet actif en fonction du chemin relatif de la page
def update_active_tab(value, input_id):

    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate

    if input_id == ctx.triggered[0]['prop_id'].split('.')[0]:
        active_path = ctx.inputs[input_id]['pathname']

        for page in dash.page_registry.values():
            if page['relative_path'] == active_path:
                page['active'] = True

            else:
                page['active'] = False
        return active_path


    raise PreventUpdate





@app.callback(
    Output('output-container-', 'style'),
    Input('open-offcanvas', 'n_clicks'),
    [State("offcanvas", "is_open")],
)
#Pour afficher ou cacher la sidebar
def update_margin(n1, is_open):
    if not is_open and n1 != 0: 
        return {'margin-left': "25rem", 'marginTop': '60px'}
    return {'margin-left': "0px", 'marginTop': '60px'}


@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
#Pour afficher ou cacher la sidebar
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


#Permet à un utilisateur de télécharger les fichiers Excels.
server = app.server  # Get the underlying Flask server
@app.server.route("/download/<filename>")
def download_excel(filename):
    if filename == config.fichier_2023 :
        return send_file(config.excel_path, as_attachment=True)
    elif filename == config.fichier_historique : 
        return send_file(config.excel_path2, as_attachment=True)





if __name__ == '__main__':
	app.run_server(debug=True) #debug=True pour la version en production




