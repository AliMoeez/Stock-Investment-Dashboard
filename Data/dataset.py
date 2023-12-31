import pandas as pd 
pd.set_option('display.max_columns',None)

class DataFrames:
    def stock_current_data():
        sheet_name="StockCurrentData"
        url=f"https://docs.google.com/spreadsheets/d/1W6n_aDhthFVHLmUQ762NaCWa-nvRRxQjFqe5zhxUzAk/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        df=pd.read_csv(url)
        return df


    def stock_historical_data():
        sheet_name="StockHistoricalData"
        url=f"https://docs.google.com/spreadsheets/d/1W6n_aDhthFVHLmUQ762NaCWa-nvRRxQjFqe5zhxUzAk/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        df=pd.read_csv(url)
        df_new=df.drop([0,1])
        return df



