import streamlit
stock = streamlit.Ticker("AAPL")
print(stock.history(period="1d"))