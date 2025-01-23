from datetime import datetime
import pandas as pd


# Prompting the user for date and verifying the correct format
def get_date(prompt="Enter a date (YYYY-MM-DD): "):
    while True:
        date_str = input(prompt)
        try:
            if not date_str:
                break
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            print("⚠️ Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Prompting the user for intervals and verifying
def valid_intervals(prompt="Please choose an interval.. ", valid_intervals = ['1m', '5m', '15m', '1d', '1wk', '1mo']):
    interval = input(f'{prompt}\nValid intervals: {valid_intervals}: ')
    if interval not in valid_intervals:
        print(f"⚠️ Invalid interval '{interval}'. Please choose from {valid_intervals}.")
        return None
    return interval

