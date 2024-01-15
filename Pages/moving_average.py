import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
import plotly.express as px

from Data.dataset import DataFrames
from Analysis.moving_average import MovingAverage

external_stylesheets=[dbc.themes.BOOTSTRAP]

dash.register_page(__name__,external_stylesheets=external_stylesheets)

historical_data=DataFrames.stock_historical_data()
current_data=DataFrames.stock_current_data()

historical_data_options_list=list(historical_data.columns.values)
historical_data_options_list=historical_data_options_list[1:]

layout=html.Div([

    html.H2("Moving Average"),

    html.H2(""),

    dbc.Row([
        dbc.Col(
            html.H2("Company")
        ),
        dbc.Col(
            html.H2("Look Back")
        ),
        dbc.Col(
            html.H2("Prediction Length")
        )

    ]),

    dbc.Row([
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Dropdown(id="MA_Stocks",options=historical_data_options_list,value=historical_data_options_list[0])
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Input(
                        id="prediction_id",type="number",value=30
                    )
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Input(
                        id="lookback_id",type="number",value=30
                    )
                ])
            )
        )
    ]),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Graph(id="Moving Average Figure")
                ])
            )
        )
    ]),

])

@callback(
    Output("Moving Average Figure","figure"),
    Input("MA_Stocks","value"),
    Input("lookback_id","value"),
    Input("prediction_id","value")
)

def moving_average_figure(ticker,lookback,prediction_length_integer):
    company_data=MovingAverage.moving_average_prediction(ticker,lookback,prediction_length_integer)[0]
    prediction_data=MovingAverage.moving_average_prediction(ticker,lookback,prediction_length_integer)[1]

    figure_normal_data=px.line(company_data,x="Date Date",y=ticker)
    figure_moving_average_data=px.line(prediction_data,x="Date",y="Moving Average List")
    figure_moving_average_data.update_traces(line_color="red")
    
    figure_moving_average=go.Figure(data=figure_normal_data.data+figure_moving_average_data.data)

    return figure_moving_average


