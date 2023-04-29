import dash
from dash import html, dcc, dash_table
from app_many_pages.df_fig import *





dash.register_page(
    __name__,
    title="DF",
    name="DF",
    order=2
    )


layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la Direction des formations'),

    html.H2(id="message_date"),

    dcc.Graph(
        id='graph1_df',
        #figure=fig_df_1(get_df_raw_df()),
        config = {'displaylogo': False}

    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes




    dcc.Graph(
        id='example-graph2',
        figure=fig_df_2(),
        config = {'displaylogo': False}
    ),
])


