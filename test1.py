import pandas as pd 

from Data.dataset import DataFrames

historical_data=DataFrames.stock_historical_data()
current_data=DataFrames.stock_current_data()


choice="Amazon AMZN"

df1=current_data.loc[current_data["Company & Ticker"]==choice]

print(df1["Number of Shares"])
