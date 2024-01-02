import dash
from dash import Dash,html,dash_table,dcc,Input,Output,State, callback
import dash_bootstrap_components as dbc
import plotly.express as px

from Data.dataset import DataFrames

current_data=DataFrames.stock_current_data()
historical_data=DataFrames.stock_historical_data()

historical_data_options_list=list(historical_data.columns.values)
historical_data_options_list=historical_data_options_list[1:]

external_stylesheets=[dbc.themes.BOOTSTRAP]

dash.register_page(__name__,path="/",external_stylesheets=external_stylesheets)

layout=html.Div([

    html.H2("Home"),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id="STOCKID",options=historical_data_options_list,value=historical_data_options_list[1]),
            dcc.Graph(id="STOCKGRAPH"),
            dcc.Store(id="STOCKSTOREID")
        
        ]),
    
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H2("Price",style={"textAlign":"center"}),
                    html.H3(id="price-company",style={"textAlign":"center"})
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("High",style={"textAlign":"center"}),
                    html.H3(id="high-company",style={"textAlign":"center"})
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("EPS",style={"textAlign":"center"}),
                    html.H3(id="eps-company",style={"textAlign":"center"})
                ])
            ),
        ]),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H2("Open",style={"textAlign":"center"}),
                    html.H3(id="open-company",style={"textAlign":"center"})
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("Low",style={"textAlign":"center"}),
                    html.H3(id="low-company",style={"textAlign":"center"})
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("Beta",style={"textAlign":"center"}),
                    html.H3(id="beta-company",style={"textAlign":"center"})
                ])
            ),
        ]),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H2("Close",style={"textAlign":"center"}),
                    html.H3(id="close-company",style={"textAlign":"center"})
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("P/E",style={"textAlign":"center"}),
                    html.H3(id="pe-company",style={"textAlign":"center"})
                ])
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H2("Sector",style={"textAlign":"center"}),
                    html.H3(id="sector-company",style={"textAlign":"center"})
                ])
            ),
        ]),
    ]),

])

@callback(
        Output("STOCKGRAPH","figure"),
        Output("price-company","children"),
        Output("high-company","children"),
        Output("eps-company","children"),
        Output("open-company","children"),
        Output("low-company","children"),
        Output("beta-company","children"),
        Output("close-company","children"),
        Output("pe-company","children"),
        Output("sector-company","children"),
        Input("STOCKID","value"),

)

def graph(ticker):
    stock_graph=px.line(historical_data,x="Date Date",y=ticker)
    stock_graph.update_xaxes(title_text="Date")
    
    company_df=current_data.loc[current_data["Company & Ticker"]==ticker]

    price_company=company_df["Price"]
    high_company=company_df["High"]
    eps_company=company_df["EPS"]
    open_company=company_df["Open"]
    low_company=company_df["Low"]
    beta_company=company_df["Beta"]
    close_company=company_df["Closing Price Yesterday"]
    pe_company=company_df["P/E"]
    market_company=company_df["Sector"]

    return stock_graph,price_company,high_company, eps_company,open_company,low_company,beta_company,close_company,pe_company,market_company
