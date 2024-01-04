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
                    html.H3(children="Company"),
                ])
            )
        ),
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
                    html.H2(id="STOCKTWONAME"),
                ])
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(id="STOCKTHREENAME"),
                ])
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(id="STOCKFOURNAME"),
                ])
            )
        ),
    ]),

    dbc.Row([

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(children="Price")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKONEPRICE")
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKTWOPRICE")
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKTHREEPRICE")
                ])
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKFOURPRICE")
                ])
            )
        ),



    ]),

    dbc.Row([

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(children="P/E")
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKONEP/E")
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKTWOP/E")
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKTHREEP/E")
                ])
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKFOURP/E")
                ])
            )
        ),



    ]),

    dbc.Row([

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(children="EPS")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKONEEPS")
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKTWOEPS")
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKTHREEEPS")
                ])
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKFOUREPS")
                ])
            )
        ),



    ]),

    dbc.Row([

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(children="Beta")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKONEBETA")
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKTWOBETA")
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKTHREEBETA")
                ])
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H3(id="STOCKFORUBETA")
                ])
            )
        ),



    ]),




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
    
    Output("STOCKONENAME","children"),
    Output("STOCKTWONAME","children"),
    Output("STOCKTHREENAME","children"),
    Output("STOCKFOURNAME","children"),


    Output("STOCKONEPRICE","children"),
    Output("STOCKTWOPRICE","children"),
    Output("STOCKTHREEPRICE","children"),
    Output("STOCKFOURPRICE","children"),



 
    Input("STOCK_IDS","value"),
    
)
def figure_stocks(ticker):
    stock_graph=px.line(historical_data,x="Date Date",y=ticker)

    if type(ticker) is not list and type(ticker) is not None:
        stock_one_label=ticker       
        stock_two_label="" ; stock_three_label="" ; stock_four_label=""
        company_df_1=current_data.loc[current_data["Company & Ticker"]==ticker]
        
        stock_one_price=company_df_1["Price"]
        stock_two_price=""
        stock_three_price=""
        stock_four_price=""


    if type(ticker) is None:
        stock_one_label="LABELTEST1" ; stock_two_label="" ; stock_three_label="" ; stock_four_label=""
    
    if type(ticker) is list:
        if len(ticker)==1:
            stock_one_label=ticker[0] ; stock_two_label=""; stock_three_label="" ; stock_four_label=""
            company_df_1=current_data.loc[current_data["Company & Ticker"]==ticker[0]]

            stock_one_price=company_df_1["Price"]
            stock_two_price=""
            stock_three_price=""
            stock_four_price=""
        


        if len(ticker)==2:
            stock_one_label=ticker[0] ; stock_two_label=ticker[1] ; stock_three_label="" ; stock_four_label=""
            company_df_1=current_data.loc[current_data["Company & Ticker"]==ticker[0]]
            company_df_2=current_data.loc[current_data["Company & Ticker"]==ticker[1]]

            stock_one_price=company_df_1["Price"]
            stock_two_price=company_df_2["Price"]
            stock_three_price=""
            stock_four_price=""
        
        
        if len(ticker)==3:
            stock_one_label=ticker[0] ; stock_two_label=ticker[1] ; stock_three_label=ticker[2] ; stock_four_label=""
            company_df_1=current_data.loc[current_data["Company & Ticker"]==ticker[0]]
            company_df_2=current_data.loc[current_data["Company & Ticker"]==ticker[1]]
            company_df_3=current_data.loc[current_data["Company & Ticker"]==ticker[2]]

            stock_one_price=company_df_1["Price"]
            stock_two_price=company_df_2["Price"]
            stock_three_price=company_df_3["Price"]
            stock_two_price=""
  
        
        
        if len(ticker)==4:
            stock_one_label=ticker[0] ; stock_two_label=ticker[1] ; stock_three_label=ticker[2] ; stock_four_label=ticker[3]
            company_df_1=current_data.loc[current_data["Company & Ticker"]==ticker[0]]
            company_df_2=current_data.loc[current_data["Company & Ticker"]==ticker[1]]
            company_df_3=current_data.loc[current_data["Company & Ticker"]==ticker[2]]
            company_df_4=current_data.loc[current_data["Company & Ticker"]==ticker[3]]

            stock_one_price=company_df_1["Price"]
            stock_two_price=company_df_2["Price"]
            stock_three_price=company_df_3["Price"]
            stock_four_price=company_df_4["Price"]

    return (stock_graph,stock_one_label,stock_two_label,stock_three_label,stock_four_label,
            stock_one_price,stock_two_price,stock_three_price,stock_four_price)
