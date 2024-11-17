import pandas as pd

def fetch_polling_data():
    url = "https://projects.fivethirtyeight.com/polls-page/data/president_primary_polls.csv"
    polling_data = pd.read_csv(url)
    polling_data.to_csv("data/polling_data_raw.csv", index=False)
    print("Polling data saved to 'data/polling_data_raw.csv'.")

if __name__ == "__main__":
    fetch_polling_data()