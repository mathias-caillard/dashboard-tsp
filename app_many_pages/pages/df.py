import dash
from dash import html, dcc, dash_table, Output, Input, callback
from app_many_pages.df_fig import *





dash.register_page(
    __name__,
    title="DF",
    name="DF",
    order=2,
    active= False
    )


layout = html.Div(children=[
    html.H1(children='Bienvenue sur la page concernant la Direction des formations'),

    html.H2(id="message_date"),

    dcc.Graph(
        id='graph1_df',
        figure=fig_df_1(),
        config = {'displaylogo': False}

    ),

    html.Hr(style={'borderTop': '2px solid #000000'}),  # Ligne horizontale pour mieux séparer les graphes


    dcc.Graph(
        id='graph2_df',
        figure=fig_df_2_update(get_df_DF_annuel()),
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
        id='example-graph4',
        figure=fig_old_df_2(),
        config = {'displaylogo': False}
    ),
])


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


