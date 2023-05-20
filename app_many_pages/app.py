from dash import Dash, html, dcc, Output, Input, State, ALL
import dash
import sys

import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash_bootstrap_templates import load_figure_template
from config import chemin_absolu_rep_parent
from datetime import datetime, timedelta, date
import dash_mantine_components as dmc
from app_many_pages.df_fig import *



sys.path.append(chemin_absolu_rep_parent + '\\app_many_pages\\pages')   #pour pouvoir importer les variables entre fichiers dans /pages
sys.path.append(chemin_absolu_rep_parent + '\\app_many_pages\\pages\\departements')   #pour pouvoir importer les variables entre fichiers dans /pages/departements


app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)   #, suppress_callback_exceptions=True
load_figure_template("bootstrap")
app._favicon = "favicon.ico"

# Définir une variable active_page initialement à la page d'accueil
active_page = "/"

annee = config.liste_annee




#Importation des DATA
data_df = data.data_df
data_daf = data.data_daf
data_dire = data.data_dire
data_drfd = data.data_drfd
data_drh = data.data_drh


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
     
                html.Hr(style={'borderTop': '2px solid #000000'}),

                html.H3(children='Sélection de l\'année',
                        style={'font-size': '18px'}),

                dcc.Dropdown(
                    id = "choix-annee",
                    options = annee,
                    multi = False,
                    value=annee[0]
                ),

                html.Hr(style={'borderTop': '2px solid #000000'}),

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
                

            ],
        ),
    ],
)
 
 



app.layout = dbc.Container([
     

	
        dbc.NavbarSimple(
            children=[
     

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
            if not 'departements' in page['relative_path'] and not 'Accueil' in page['name']  # Filtrer les pages du dossier "pages" qui ne sont pas des departements, et la page accueil (qui est remplacé par le bouton tout à gauche)
	    
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
	    

            dbc.NavItem(dbc.NavLink("À propos", href="/apropos")),

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
def render_page_content(pathname):
    for page in dash.page_registry.values():
        if 'departements' not in page['relative_path'] and not 'Accueil' in page['name']:
            if page['relative_path'] == pathname:
                page['active'] = True
            else:
                page['active'] = False

    return html.Div([

    ]), [
               "me-1 btn-sm active" if page["active"] else "me-1 btn-sm"
               for page in dash.page_registry.values() if not 'departements' in page['relative_path'] and not 'Accueil' in page['name']
           ]


@app.callback(
    Output('output', 'children'),
    Input('input', 'value'),
    State('input', 'id')
)
# Fonction pour déterminer l'onglet actif en fonction du chemin relatif de la page
def update_active_tab(value, input_id):
    print("TEST")

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

        return f'Output: {active_path}'

    raise PreventUpdate





@app.callback(
    Output('output-container-', 'style'),
    Input('open-offcanvas', 'n_clicks'),
    [State("offcanvas", "is_open")],
)
def update_margin(n1, is_open):
    if not is_open and n1 != 0: 
        return {'margin-left': "25rem", 'marginTop': '60px'}
    return {'margin-left': "0px", 'marginTop': '60px'}


@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open




@app.callback(
    Output("message_date", "children"),
    Input("date-range-picker", "value"),
)
def test(dates) :
    prefixe = "intervalle dates : "
    # Input string in yyyy-mm-dd format
    input_str1 = dates[0]

    # Convert to datetime object
    dt_obj = datetime.strptime(input_str1, '%Y-%m-%d')

    # Convert back to string in dd/mm/yyyy format
    output_str1 = dt_obj.strftime('%d/%m/%Y')

        # Input string in yyyy-mm-dd format
    input_str2 = dates[1]

    # Convert to datetime object
    dt_obj = datetime.strptime(input_str2, '%Y-%m-%d')

    # Convert back to string in dd/mm/yyyy format
    output_str2 = dt_obj.strftime('%d/%m/%Y')

    datesModified = [output_str1, output_str2]


    return prefixe + "   -   ".join(datesModified)



if __name__ == '__main__':
	app.run_server(debug=True)



