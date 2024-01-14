import pandas as pd 
import numpy as np 
import datetime

from Data.dataset import DataFrames

historical_data=DataFrames.stock_historical_data()
current_data=DataFrames.stock_current_data()

class MovingAverage:
    
    def data_collection(ticker):
        data_set=historical_data[ticker].to_list()
        return data_set[::-1]
    
    def moving_average_prediction(ticker,moving_average_lookback,prediction_length):
        data=MovingAverage.data_collection(ticker)
        data_copy=data[:]
        moving_average_prediction_list=[]
        for i in range(moving_average_lookback):
            ma_calculation=np.average(data_copy[0:prediction_length])
            data_copy.insert(0,ma_calculation)
            moving_average_prediction_list.append(ma_calculation)
        date_data_list=historical_data["Date Date"].to_list()[::-1]
        date_final=datetime.datetime.strptime(date_data_list[0],"%m/%d/%Y %H:%M:%S")
        
        for i in range(prediction_length):
            date_final=date_final+datetime.timedelta(days=1)
    
        moving_average_dataframe=pd.DataFrame(data={
            "Date": date_final,
            "Moving Average List": moving_average_prediction_list
        }) 

        print(moving_average_dataframe)

        return historical_data[["Date Date",ticker]],moving_average_dataframe

ma=MovingAverage
ma.moving_average_prediction("Amazon AMZN",10,10)




