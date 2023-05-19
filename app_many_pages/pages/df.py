import dash
from dash import html, dcc, dash_table, Output, Input, callback

from app_many_pages.df_fig import *
from app_many_pages.data import *






dash.register_page(
    __name__,
    title="DF",
    name="DF",
    order=2,
    active= False
    )

titres_y = data.titres_y
titres_graphe = data.titres_graphe
effectif_dept = data.effectif_dept
data_df_pond = ponderation_total(data.data_df[0])
data_df_pond.append([valeur_annuel[i]/effectif[i] for i in range(7)])

selected_data_df = data_df_pond[-1]
annee = config.liste_annee
selected_annee = annee[0]

layout = html.Div(children=[
    html.H1(
        children='Bienvenue sur la page concernant la Direction des formations',
        style={'text-align': 'justify'}
    ),

    html.H2(id="message_date"),

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
    Output('df_update_year', 'figure'),
    Input('choix-annee', 'value')
)
def update_output(selected_year):
    if selected_year == 2023:
        selected_data_df = data_df_pond[-1]
        return fig_baton_total(selected_data_df,selected_year , titres_graphe[0], titres_y[0])
    else:
        selected_data_df = data_df_pond[selected_year - annee[-1]]
        return fig_baton_total(selected_data_df,selected_year , titres_graphe[0], titres_y[0])


# Define the callback to update the bar chart when the date range is changed
@callback(
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
    #print(filtered_df, flush=True)
    fig = fig_df_1_update(filtered_df)
    return fig



# Define the callback to update the bar chart when the date range is changed
@callback(
    Output("graph2_df", "figure"),
    Input("date-range-picker", "value"),
)
def update_bar_chart(value):
    # Convert the start_date and end_date strings to pandas Timestamps
    start_date = value[0]
    end_date = value[1]

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    df = get_df_DF_annuel()

    # Filter the dataframe to include only rows where the date is within the selected range
    filtered_df = df.loc[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
    
    # Create and return the bar chart
    #print(filtered_df, flush=True)
    fig = fig_df_2_update(filtered_df)
    return fig


