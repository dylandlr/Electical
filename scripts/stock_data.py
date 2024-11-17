from alpha_vantage.timeseries import TimeSeries
import pandas as pd

def fetch_stock_data():
    API_KEY = "your_alpha_vantage_api_key" # todo: use .env file instead
    ts = TimeSeries(key=API_KEY, output_format="pandas") # todo: use .env file instead

    # Example: Fetch S&P 500 data
    data, _ = ts.get_daily(symbol="^GSPC", outputsize="compact")
    data.to_csv("data/stock_data_raw.csv")
    print("Stock market data saved to 'data/stock_data_raw.csv'.")

if __name__ == "__main__":
    fetch_stock_data()