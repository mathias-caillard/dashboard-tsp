from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template




app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
load_figure_template("bootstrap")
app._favicon = "favicon.ico"

app.layout = dbc.Container([
	
        dbc.NavbarSimple(
            children=[
	

        html.Div(
        [
	
                dbc.Button(
                    f"{page['name']}", href=page["relative_path"], outline=True, color="primary", className="me-1",
                    style = {'marginTop': '0px'}
                )
                
            for page in dash.page_registry.values()
	    
        ]
    ),
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
            ], 
            className="navbar navbar-expand-lg navbar-light bg-light fixed-top",
            brand="Indicateurs de Télécom SudParis",
            brand_href="#",
            color="dark",
            dark=True,
	        fluid = True
	    ),
	    

	dash.page_container,
	

],
fluid = True,
)

if __name__ == '__main__':
	app.run_server(debug=True)