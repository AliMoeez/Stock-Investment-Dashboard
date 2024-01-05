import pandas as pd 
import numpy as np

from Data.dataset import DataFrames

historical_data=DataFrames.stock_historical_data()
current_data=DataFrames.stock_current_data()


print(historical_data)

ticker="AMAZON AMZN"

print(historical_data["Amazon AMZN"])

company_df=historical_data.loc[historical_data["Company & Ticker"]==ticker]

