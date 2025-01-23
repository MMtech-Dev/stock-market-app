import pandas as pd     
import matplotlib.pyplot as plt
import requests
import csv

# Function to fetch stock data 
def get_stock_data(symbol='AAPL', interval='5min', apikey='I0ITDWRVIF6BMLGL'):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=I0ITDWRVIF6BMLGL'
    r = requests.get(url)
    r.encoding
    data = r.json()
    
    if not data:
        print(f"⚠️ No data found for {symbol}. Returning empty DataFrame.")
        return pd.DataFrame(columns=['Date', 'Open', 'Close', 'High', 'Low', 'Volume', 'Symbol'])

    # Extract the data
    meta_data = data.get('Meta Data', {})
    time_series = data.get('Time Series (5min)', {})

    return meta_data, time_series

# Function to write data to csv file
def save_to_csv(time_series, filename='storge.csv'):
    if not time_series:
        print("⚠️ No data available to save.")
        return
    with open(filename, 'a', newline='') as stock:
        writer = csv.writer(stock)
        writer.writerow(['Time Stamp', 'Open', 'High', 'Low', 'Close', 'Volume'])

        for timestamp, values in time_series.items():
            writer.writerow([
                timestamp,              
                values["1. open"],        
                values["2. high"],        
                values["3. low"],         
                values["4. close"],       
                values["5. volume"] ])      
        print(f"✅ Stock data saved to {filename} successfully!")


# Data analysis function
def data_analysis(file):
    try:
        df = pd.read_csv(file)
        df["Time Stamp"] = pd.to_datetime(df["Time Stamp"])
        df.set_index("Time Stamp", inplace=True)

        df['Close'].plot(figsize=(12,6) , color="blue", title="Stock Closing Price Over Time")
        plt.xlabel('Time')
        plt.ylabel('Price (USD)')
        plt.grid(visible=True)
        plt.show()

    except FileNotFoundError:
        print(f"⚠️ Error: The file '{file}' does not exist.")
    except KeyError:
        print("Make sure the file contains 'Time Stamp' and 'Close' columns.")
    except Exception as e:
        print(f"Unexpected error: {e}")
