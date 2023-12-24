import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import dash_bootstrap_components as dbc
import plotly.express as px

external_stylesheets=[dbc.themes.BOOTSTRAP]

dash.register_page(__name__,external_stylesheets=external_stylesheets)


layout=html.Div([

    html.H2("Moving Average")


])