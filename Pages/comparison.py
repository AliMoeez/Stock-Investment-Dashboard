import dash
from dash import Dash,html,dash_table,dcc,Input,Output,State,callback
import dash_bootstrap_components as dbc
import plotly.express as px

from Data.dataset import DataFrames

current_data=DataFrames.stock_current_data()
historical_data=DataFrames.stock_historical_data()

historical_data_options_list=list(historical_data.columns.values)
historical_data_options_list=historical_data_options_list[1:]

external_stylesheets=[dbc.themes.BOOTSTRAP]

dash.register_page(__name__,external_stylesheets=external_stylesheets)


layout=html.Div([

    html.H2("Comparsion Page"),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Dropdown(id="STOCK_IDS",options=historical_data_options_list,value=historical_data_options_list[0],multi=True)
                ])
            )
        ),
    ]),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Graph(id="STOCKGRAPHTOTAL")
                ])
            )
        )
    ]),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKONENAME"),
                ])
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(""),
                ])
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(""),
                ])
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(""),
                ])
            )
        ),
    ])




])

@callback(
   Output("STOCK_IDS","value"),
   Input("STOCK_IDS","value"),
   State("STOCK_IDS","value"), 
)

def max_dropdown_values(selection,current):
    if len(selection)>4:
        return current[:-1]
    return selection


@callback(
    Output("STOCKGRAPHTOTAL","figure"),
    Output("STOCKONENAME","value"),
    #"""    Output("STOCKTWONAME","value"),
    #Output("STOCKTHREENAME","value"),
    #Output("STOCKFOURNAME","value"),"""
    Input("STOCK_IDS","value"),
    
)
def figure_stocks(ticker):
    stock_graph=px.line(historical_data,x="Date Date",y=ticker)

    stock_one_label=ticker

    return stock_graph,stock_one_label