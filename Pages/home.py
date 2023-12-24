import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import dash_bootstrap_components as dbc
import plotly.express as px

from Data.dataset import DataFrames

current_data=DataFrames.stock_current_data()
historical_data=DataFrames.stock_historical_data()


external_stylesheets=[dbc.themes.BOOTSTRAP]

dash.register_page(__name__,path="/",external_stylesheets=external_stylesheets)

layout=html.Div([



    html.H2("Home"),

    dcc.Dropdown(id="STOCKID",options=[
        
    ]).

    dcc.Graph(id="STOCKGRAPH"),


])

@callback(
        Output("STOCKGRAPH","figure"),
        Input("STOCKID","value")
)

def graph(ticker):
    stock_graph=px.line(historical_data,y="Date Date Date",x=ticker)
    return stock_graph


