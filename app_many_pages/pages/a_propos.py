import dash
from dash import html, dcc

dash.register_page(
    __name__,
    title = "A propos",
    name = "A propos",
    order=10,
    active= False
                   )


layout = html.Div(children=[
    html.H1(
        children='A propos',
        style={'text-align': 'justify'}
    ),
])