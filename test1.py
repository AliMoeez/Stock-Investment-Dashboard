import pandas as pd 
import numpy as np

from Data.dataset import DataFrames

historical_data=DataFrames.stock_historical_data()
current_data=DataFrames.stock_current_data()

ticker="Amazon AMZN"

def split_data_set(ticker,lookback):
    data=historical_data[ticker]
    data_list=data.values.tolist()
    data_list=data_list[::-1]
    list_data=[data_list[i:i+lookback] for i in range(0,len(data_list),lookback)]
    return list_data

def aroon_function(ticker,lookback):
    aroon_up_list=[] ; aroon_down_list=[]
    data_split_function=split_data_set(ticker,lookback)
    for i,y in enumerate(data_split_function):
        days_from_max=lookback-y.index(np.max(y)) ; days_from_min=lookback-y.index(np.min(y))
        aroon_up=((lookback-days_from_max)/lookback)*100 ; aroon_down=((lookback-days_from_min)/lookback)*100
        aroon_up_list.append(aroon_up) ; aroon_down_list.append(aroon_down)
        aroon_up_array=pd.DataFrame(data={"Aroon Up":aroon_up_list[::-1]})
        aroon_down_array=pd.DataFrame(data={"Aroon Down":aroon_down_list[::-1]})
    return aroon_up_array,aroon_down_array

au=aroon_function(ticker,25)[0]
ad=aroon_function(ticker,25)[1]


print(au.index.tolist())

