import pandas as pd 
import numpy as np 

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
        return data[::-1],moving_average_prediction_list
