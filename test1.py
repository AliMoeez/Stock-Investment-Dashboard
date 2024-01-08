import pandas as pd 
import numpy as np

from Data.dataset import DataFrames

historical_data=DataFrames.stock_historical_data()
current_data=DataFrames.stock_current_data()

ticker="Amazon AMZN"

def split_data_set(ticker,lookback,max_lookback):
    data=historical_data[ticker]
    data_list=data.values.tolist()
    return data_list[::-1]

def aroon_function(ticker,lookback,max_lookback):
    aroon_up_list=[] ; aroon_down_list=[]
    data_split_function=split_data_set(ticker,lookback,max_lookback)
    
    lookback_list=[]
    
    for i,y in enumerate(data_split_function):
        lookback_list.append(data_split_function[lookback:max_lookback])

        lookback+=1
        max_lookback+=1

  #  print(lookback_list)

            
    for i,y in enumerate(lookback_list):

      #  print(y,np.max(y),y.index(np.max(y)),25-y.index(np.max(y)))


        days_from_max=y.index(np.max(y)) ; days_from_min=y.index(np.min(y))

        
        
        aroon_up=((25-days_from_max)/25)*100 ; aroon_down=((25-days_from_min)/25)*100

      #  print(aroon_up)
        
        
        
        
        aroon_up_list.append(aroon_up) ; aroon_down_list.append(aroon_down)

        if len(aroon_up_list)==len(historical_data["Date Date"]):
            aroon_up_array=pd.DataFrame(data={"Date":historical_data["Date Date"],"Aroon Up":aroon_up_list[::-1]})
            aroon_down_array=pd.DataFrame(data={"Date":historical_data["Date Date"],"Aroon Down":aroon_down_list[::-1]})
    
    
    return aroon_up_array[::-1],aroon_down_array[::-1]

au=aroon_function(ticker,0,25)[0]
ad=aroon_function(ticker,0,25)[1]

print(au)

