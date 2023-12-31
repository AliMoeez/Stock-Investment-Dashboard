import pandas as pd 

from Data.dataset import DataFrames

historical_data=DataFrames.stock_historical_data()
current_data=DataFrames.stock_current_data()


choice="APPLE AAPL"

df1=current_data.loc[current_data["Company & Ticker"]==choice]

#print(df1["Open"][0])

#print(f'${df1["Open"][0]}')


high_company="$"+str(df1["High"][1])

print(high_company)

high_company=f'${df1["High"][0]}'
print(high_company,"HIGH")

eps_company=f'${df1["EPS"][1]}'
print(eps_company,"EPS")

open_company=f'${df1["Open"][1]}'
print(open_company,"OPEN")

low_company=f'${df1["Low"][1]}'
print(low_company,"LOW")

beta_company=df1["Beta"][1]
print(beta_company,"BETA")

close_company=f'${df1["Closing Price Yesterday"][1]}'
print(close_company,"CLOSE")

pe_company=df1["P/E"][0]
print(pe_company,"PE")

market_company=f'${df1["Market Capitalization"][1]:,}'
print(market_company,"MARKET")
