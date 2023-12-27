import dash
from dash import Dash,html,dash_table,dcc,Input,Output,State, callback
import dash_bootstrap_components as dbc
import plotly.express as px

from Data.dataset import DataFrames

current_data=DataFrames.stock_current_data()
historical_data=DataFrames.stock_historical_data()

historical_data_options_list=list(historical_data.columns.values)

external_stylesheets=[dbc.themes.BOOTSTRAP]

ticker=None

dash.register_page(__name__,path="/",external_stylesheets=external_stylesheets)

@callback(
        Output("STOCKGRAPH","figure"),
        Input("STOCKID","value"),
)

def graph(ticker):
    stock_graph=px.line(historical_data,x="Date Date",y=ticker)
    return stock_graph



layout=html.Div([

    html.H2("Home"),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id="STOCKID",options=historical_data_options_list,value=historical_data_options_list[1]),
            dcc.Graph(id="STOCKGRAPH"),
        
        ]),
    
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H2("Price"),
                    html.H3("TEXT 1")
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("High"),
                    html.H3("TEXT 2")
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("EPS"),
                    html.H3("TEXT 3")
                ])
            ),
        ]),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H2("Open"),
                    html.H3("TEXT 4")
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("Low"),
                    html.H3("TEXT 5")
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("Daily Trading Volume"),
                    html.H3("TEXT 6")
                ])
            ),
        ]),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H2("Close"),
                    html.H3("TEXT 7")
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("P/E"),
                    html.H3("TEXT 8")
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("Market Capitalization"),
                    html.H3("TEXT 9")
                ])
            ),
        ]),
    ]),

])
