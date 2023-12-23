import pandas as pd 

def stock_current_data():
    sheet_name="StockCurrentData"
    url=f"https://docs.google.com/spreadsheets/d/1W6n_aDhthFVHLmUQ762NaCWa-nvRRxQjFqe5zhxUzAk/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df=pd.read_csv(url)
    print(df)
    return df

stock_current_data()

def stock_historical_data():
    sheet_name="StockHistoricalData"
    url=f"https://docs.google.com/spreadsheets/d/1W6n_aDhthFVHLmUQ762NaCWa-nvRRxQjFqe5zhxUzAk/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df=pd.read_csv(url)
    print(df)
    return df

stock_historical_data()

