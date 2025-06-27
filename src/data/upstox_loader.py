import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
hist_url = os.getenv('HISTORICAL_URL')

df = pd.DataFrame()

def fetch_upstox_data(instrument, unit, interval, to_date, from_date):
    """
    Fetch historical candle data from Upstox API.
    Args:
        instrument (str): Instrument identifier.
        unit (str): Time unit (e.g., 'minutes', 'hours').
        interval (str): Interval for the data.
        to_date (str): End date for the data in 'YYYY-MM-DD' format.
        from_date (str): Start date for the data in 'YYYY-MM-DD' format.
    """
    global df
    if not hist_url:
        print("HISTORICAL_URL is not set in the environment variables.")
        return
    
    url = f'{hist_url}/historical-candle/{instrument}/{unit}/{interval}/{to_date}/{from_date}'
    headers = {
    'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'candles' in data['data']:
            candles = data['data']['candles']
            columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'open_interest']
            df = pd.DataFrame(candles, columns=columns)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df.set_index('timestamp', inplace=True)
            # print(df.head())
    return response.status_code

def main():
    instrument = 'NSE_EQ%7CINE848E01016'
    unit = 'minutes'
    interval = '1'
    to_date = '2025-06-27'
    from_date = '2025-05-28'

    status_code = fetch_upstox_data(instrument, unit, interval, to_date, from_date)
    if status_code == 200:
        print("Data fetched successfully.")
        print(df.head())  # Display the first few rows of the DataFrame
    else:
        print(f"Failed to fetch data. Status code: {status_code}")

if __name__ == "__main__":
    main()