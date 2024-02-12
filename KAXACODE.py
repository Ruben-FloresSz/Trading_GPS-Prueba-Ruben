import pandas as pd
import os
import mplfinance as mpf


stocks = "Input\Data_and_Features"
list_stocks = os.listdir(stocks)

repositorio_stocks = {}

for ticker in list_stocks:
    path = os.path.join(stocks, ticker)
    ticker_name = os.path.splitext(ticker)[0]
    repositorio_stocks[ticker_name] = pd.read_csv(path)

BAC_df = repositorio_stocks["BAC"].copy()

db_dict = {
    "m_date" : "date",
    "c_adjusted_open": "Open",
    "c_adjusted_high": "High",
    "c_adjusted_low": "Low",
    "m_adjusted_close": "Close",
    "m_volume": "Volume",
    "m_close": "Adj Close"
    }

BAC_df = BAC_df.rename(columns = db_dict)
BAC_df['date'] = pd.to_datetime(BAC_df['date'])
BAC_df = BAC_df.set_index('date')

mpf.plot(BAC_df,type='candle', volume=True, title='Bank Of America Stocks January 2022 - December 2023', figsize=(10, 6), style= "charles")

BAC_Nov = BAC_df['2023-11-01':'2023-11-30']
mpf.plot(BAC_Nov,type='candle', volume=True, title='Bank Of America Stocks - November 2023', figsize=(10, 6))