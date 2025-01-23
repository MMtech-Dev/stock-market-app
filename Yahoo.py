import yfinance as yf
import pandas as pd
import csv
import matplotlib.pyplot as plt


# Function to fetch and clean data
def fetch_data(symbol, start, end, interval):
    try:
        
        # Fetch data
        raw_data = yf.download(symbol, start=start, end=end, interval=interval)
        
        if raw_data.empty:
            print(f"⚠️ No data found for {symbol}. Returning empty DataFrame.")
            return pd.DataFrame(columns=['Date', 'Open', 'Close', 'High', 'Low', 'Volume', 'Symbol'])
        
        # Clean the data: Rename columns to remove tuple structure
        cleaned_data = raw_data.copy()
        cleaned_data.columns = [col if isinstance(col, str) else col[0] for col in raw_data.columns]
        
        # Reset index to make 'Date' a column
        cleaned_data.reset_index(inplace=True)
        cleaned_data['Symbol'] = symbol  # Add stock symbol as a column
        
        return cleaned_data
    except Exception as e:
        print(f"⚠️ Error fetching data for {symbol}: {e}")
        return None

# Function to save cleaned data to a CSV file
def save_to_csv(data, filename='yahoo.csv'):
    if data is None or data.empty:
        print('⚠️ No data available to save.')
        return

    try:
        # Write to CSV
        with open(filename, 'a', newline='') as yahoo:  # 'a' mode to append data
            writer = csv.writer(yahoo)
            
            # Write header only if the file is empty
            if yahoo.tell() == 0:
                writer.writerow(['Symbol', 'Date', 'Open', 'Close', 'High', 'Low', 'Volume'])
            
            # Write rows
            for _, row in data.iterrows():
                writer.writerow([
                    row['Symbol'], 
                    row['Date'], 
                    row['Open'], 
                    row['Close'], 
                    row['High'], 
                    row['Low'], 
                    row['Volume']
                ])
        
        print(f"✅ Data successfully saved to {filename}")
    except Exception as e:
        print(f'⚠️ Error saving data to CSV: {e}')

# Data analysis function
def data_analysis(file, figsize=(12,6), color="blue", title="Stock Closing Price Over Time"):
    try:
        df = pd.read_csv(file, parse_dates=['Date'])

        if df.empty:
            print(f"⚠️ Error: The file '{file}' contains no data.")
            return
        df.set_index('Date', inplace=True)

        df['Close'].plot(figsize=figsize, color=color, title=title)
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.grid(visible=True)
        plt.show()

    except FileNotFoundError:
        print(f"⚠️ Error: The file '{file}' does not exist.")
    except KeyError:
        print("Make sure the file contains 'Date' and 'Close' columns.")
    except Exception as e:
        print(f"Unexpected error: {e}")
