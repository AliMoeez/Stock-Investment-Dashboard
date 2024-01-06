import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
import plotly.express as px

from Data.dataset import DataFrames
from Analysis.aroon import Aroon

current_data=DataFrames.stock_current_data()
historical_data=DataFrames.stock_historical_data()

historical_data_options_list=list(historical_data.columns.values)
historical_data_options_list=historical_data_options_list[1:]

external_stylesheets=[dbc.themes.BOOTSTRAP]


dash.register_page(__name__,external_stylesheets=external_stylesheets)

layout=html.Div([

    html.H2("Aroon"),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Dropdown(id="STOCK_AROON_DROPDOWN",options=historical_data_options_list,value=historical_data_options_list[0])
                ])
            )
        )
    ]),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([ 
                    dcc.Graph(id="STOCK_AROON_GRAPH"),
                    dcc.Graph(id="STOCK_AROON_TREND_GRAPH")
                ])
            )
        )
    ])

])

@callback(
    Output("STOCK_AROON_GRAPH","figure"),
    Output("STOCK_AROON_TREND_GRAPH","figure"),
    Input("STOCK_AROON_DROPDOWN","value")
)

def aroon_graph(ticker):
    aroon_function=Aroon.aroon_function(ticker,25)
    aroon_up_function=aroon_function[0]
    aroon_down_function=aroon_function[1]

    aroon_figure=px.line(historical_data,x="Date Date",y=ticker)

    aroon_up_figure=px.line(aroon_up_function,x=aroon_up_function.index,y=aroon_up_function["Aroon Up"])
    aroon_down_figure=px.line(aroon_down_function,x=aroon_down_function.index,y=aroon_down_function["Aroon Down"])
    aroon_trend_figure=go.Figure(data=aroon_up_figure.data+aroon_down_figure.data)

    return aroon_figure,aroon_trend_figure