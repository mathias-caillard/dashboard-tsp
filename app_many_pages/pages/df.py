import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    title="Direction des formations",
    name="Direction des formations",
    order=2
    )

layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la Direction des formations'),

    html.Div(children='''
        Pas encore d\'indicateur a afficher
    ''')
    
  

])


"""
@callback(
    Output(component_id='analytics-output', component_property='children'),
    Input(component_id='analytics-input', component_property='value')
)
def update_city_selected(input_value):
    return f'You selected: {input_value}'
"""