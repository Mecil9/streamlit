import pandas as pd
import yfinance as yf

import streamlit as st

st.write("""
# Simple Strock Price Apps

Shown are the stock colsing **price** and ***volumne*** of Googl!

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')

st.write("""
## Colsing Price
""")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
