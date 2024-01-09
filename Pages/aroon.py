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
    aroon_function=Aroon.aroon_function(ticker,0,25,historical_data[ticker])
    aroon_up_function=aroon_function[0]
    aroon_down_function=aroon_function[1]

    aroon_figure=px.line(historical_data,x="Date Date",y=ticker)
    aroon_figure.update_xaxes(visible=False)
    aroon_figure.update_layout(margin=dict(b=10))

    aroon_up_figure=px.line(aroon_up_function,x=aroon_up_function["Date"],y=aroon_up_function["Aroon Up"])
    aroon_up_figure.update_traces(line_color="green")
    
    aroon_down_figure=px.line(aroon_down_function,x=aroon_down_function["Date"],y=aroon_down_function["Aroon Down"])
    aroon_down_figure.update_traces(line_color="red")

    aroon_trend_figure=go.Figure(data=aroon_up_figure.data+aroon_down_figure.data)
    aroon_trend_figure.update_layout(height=150,margin=dict(t=10))

    """
    aroon_figure.update_xaxes(
            range=aroon_trend_figure['layout']['xaxis']['range'],
        ),
    
    aroon_figure.update_yaxes(
            range=aroon_trend_figure['layout']['yaxis']['range'],
        ),

    aroon_trend_figure.update_xaxes(
            range=aroon_figure['layout']['xaxis']['range'],
        ),
    
    aroon_trend_figure.update_yaxes(
            range=aroon_figure['layout']['yaxis']['range'],
        ),"""

    '''aroon_trend_figure.update_layout(
            x_axis=dict(range=aroon_figure['layout']['xaxis']['range'])''',
    '''y_axis=dict(range=aroon_figure['layout']['yaxis']['range'])
    )'''

   # aroon_trend_figure.on_relayout(update_both_plots(aroon_trend_figure,aroon_figure))
   # aroon_function.on_relayout(update_both_plots(aroon_trend_figure,aroon_figure))

   # aroon_figure.on_relayout(aroon_graph,aroon_trend_figure)
   # aroon_trend_figure.on_relayout(aroon_graph,aroon_figure)

    return aroon_figure,aroon_trend_figure

@callback(
    Output("STOCK_AROON_GRAPH","relayoutData"),
    Output("STOCK_AROON_TREND_GRAPH","relayoutData"),
    Input("STOCK_AROON_GRAPH","relayoutData"),
    Input("STOCK_AROON_TREND_GRAPH","relayoutData")
)

def both_pan(fig1,fig2):
    if fig1 is not None:
        return fig1,fig1
    elif fig2 is not None:
        return fig2,fig2
    else:
        return None,None