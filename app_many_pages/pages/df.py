import dash
from dash import html, dcc
from app_many_pages.df_fig import fig_nb_etudiants





dash.register_page(
    __name__,
    title="DF",
    name="DF",
    order=2
    )


layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la Direction des formations'),

    dcc.Graph(
        id='example-graph',
        figure=fig_nb_etudiants(),
        config = {'displaylogo': False}

    ),
])


