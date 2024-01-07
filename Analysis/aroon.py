import pandas as pd 
import numpy as np 

from Data.dataset import DataFrames

historical_data=DataFrames.stock_historical_data()
current_data=DataFrames.stock_current_data()

class Aroon:
    def split_data_set(ticker,lookback,max_lookback,data):
        data=historical_data[ticker]
        data_list=data.values.tolist()
        return data_list

    def aroon_function(ticker,lookback,max_lookback,data):
        aroon_up_list=[] ; aroon_down_list=[]
        data_split_function=Aroon.split_data_set(ticker,lookback,max_lookback,data)
        
        lookback_list=[]
        
        for i,y in enumerate(data_split_function):
            lookback_list.append(data_split_function[lookback:max_lookback])
    
            lookback+=1
            max_lookback+=1

                
        for i,y in enumerate(lookback_list):


            days_from_max=25-y.index(np.max(y)) ; days_from_min=25-y.index(np.min(y))

            print(days_from_max)
            
            
            aroon_up=((25-days_from_max)/25)*100 ; aroon_down=((25-days_from_min)/25)*100
            
            
            aroon_up_list.append(aroon_up) ; aroon_down_list.append(aroon_down)
            
            
            
            aroon_up_array=pd.DataFrame(data={"Aroon Up":aroon_up_list[::-1]})
            aroon_down_array=pd.DataFrame(data={"Aroon Down":aroon_down_list[::-1]})
        
        
        return aroon_up_array[::-1],aroon_down_array[::-1]
    

