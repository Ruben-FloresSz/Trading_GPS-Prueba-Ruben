# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:01:21 2024

@author: rubof
"""

from src.modules import custom_functions as cf 

#Prueba de la función
stocks = cf.data_dict("Input\Data_and_Features")
BAC_df = stocks["BAC"].copy()
AAPL_df = stocks["AAPL"].copy()

#Prueba de la grafica
cf.candle_chart(BAC_df, ticker="BAC", title= "Bank of America Candlestick Chart", save_fig=True,
             save_path="Output")
cf.candle_chart(AAPL_df, ticker="APPL", title= "Apple Candlestick Chart", save_fig=True,
             save_path="Output")
