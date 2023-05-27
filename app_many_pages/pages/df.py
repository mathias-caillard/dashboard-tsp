import dash
from dash import html, dcc, dash_table, Output, Input, callback

from app_many_pages.df_fig import *

from app_many_pages.data import new_donnee, new_titre_y, new_labels, dict_titres
from app_many_pages.data import *
from app_many_pages.fonction_figure import fig_annuelle_baton, fig_camembert, fig_trim_baton, couleurs







dash.register_page(
    __name__,
    title="DF",
    name="DF",
    order=2,
    active= False
    )

donnee_annee = data_complete_pondere[-1]

data_df_pond = ponderation_total(data.data_df[0])
data_df_pond.append([valeur_annuel[i]/effectif[i] for i in range(7)])

selected_data_df = data_df_pond[-1]
annee = config.liste_annee_maj

selected_annee = annee[-1]

layout = html.Div(children=[
    html.H1(
        children='Bienvenue sur la page concernant la Direction des formations',
        style={'text-align': 'justify'}
    ),

    html.H2(id="message_date"),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='df1_bat',
        figure=fig_annuelle_baton("DF-01", selected_annee, "Départements", couleurs),
        config = {'displaylogo': False}

    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='df1_cam',
        figure=fig_camembert("DF-01", selected_annee, couleurs),
        config = {'displaylogo': False}

    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='df2_bat',
        figure=fig_trim_baton("DF-02", selected_annee, "Temps", None),
        config = {'displaylogo': False}

    ),

    dcc.Graph(
        id='df_update_year',
        figure=fig_baton_total(selected_data_df,selected_annee , titres_graphe[0], titres_y[0]),
        config={'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='graph1_df',
        figure=fig_df_1(),
        config = {'displaylogo': False}

    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='graph2_df_update',
        figure=fig_df_2_update(get_df_DF_annuel()),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='graph2_df_',
        figure=fig_df_2(),
        config = {'displaylogo': False}
    ),



    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='example-graph3',
        figure=fig_old_df_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph3_tri',
        figure=fig_old_tri_df_1(),
        config = {'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph3_tot',
        figure=fig_old_df_1_tot(),
        config={'displaylogo': False}
    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes

    dcc.Graph(
        id='example-graph4',
        figure=fig_old_df_2(),
        config = {'displaylogo': False}
    ),
])


@callback(
    Output('df1_bat', 'figure'),
    Input('choix-annee', 'value')
)
def update_graphes(selected_year):
    donnee_annee = data_complete_pondere[selected_year - annee[0]]
    return fig_annuelle_baton("DF-01", selected_year, "Départements", couleurs)



"""
@callback(
    Output('df_update_year', 'figure'),
    Input('choix-annee', 'value')
)
def update_output(selected_year):
    if selected_year == 2023:
        selected_data_df = data_df_pond[-1]
        return fig_baton_total(selected_data_df,selected_year , titres_graphe[0], titres_y[0])
    else:
        selected_data_df = data_df_pond[selected_year - annee[0]]
        return fig_baton_total(selected_data_df,selected_year , titres_graphe[0], titres_y[0])

"""




