from dash import Dash, html, dcc, Output, Input, callback, State, dash_table
import dash
import sys
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from config import chemin_absolu_rep_parent
from datetime import datetime, timedelta, date
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate
import pandas as pd
from app_many_pages.df_fig import *



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
            close_button=False,
            style = {"marginTop" : "60px"},
            children = [
     
                    dmc.DateRangePicker(
                    id="date-range-picker",
                    label="Plage temporelle",
                    description="En construction",
                    minDate=date(2010, 1, 1),
                    maxDate = date(2025,1,1),
                    value=[datetime.now().date() - timedelta(days=365*2), datetime.now().date()],
                    style={"width": 330},
                    inputFormat = "DD/MM/YYYY",
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
                    id="percentile25-switch",
                    label="25ème de percentile",
                    value=False,
                ),
                dbc.Switch(
                    id="médiane-switch",
                    label="médiane",
                    value=False,
                ),
                dbc.Switch(
                    id="percentile75-switch",
                    label="75ème de percentile",
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
                    label="indicateur périmmètre école",
                    value=False,
                ),
                dbc.Switch(
                    id="dept-switch",
                    label="indicateur périmètre départemental",
                    value=False,
                ),
                
                html.Hr(style={'borderTop': '2px solid #000000'}),
                

            ],
        ),
    ],
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








# Define the callback to update the bar chart when the date range is changed
@app.callback(
    Output("graph1_df", "figure"),
    Input("date-range-picker", "value"),
)
def update_bar_chart(value):
    # Convert the start_date and end_date strings to pandas Timestamps
    start_date = value[0]
    end_date = value[1]

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    df_melt = get_df_melt_df()

    # Filter the dataframe to include only rows where the date is within the selected range
    filtered_df = df_melt.loc[(df_melt["Date"] >= start_date) & (df_melt["Date"] <= end_date)]
    
    # Create and return the bar chart
    print(filtered_df, flush=True)
    fig = fig_df_1(filtered_df)
    return fig



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



