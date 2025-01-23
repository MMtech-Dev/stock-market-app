import utils.dynamic_funcs as func
import Yahoo as yo
import alphavantage as alpha
from datetime import datetime, timedelta




# Function to manage and logic other integrated modules. 
def fetch_save_analyise(provider, symbol):
    """
    Fetches, saves, and analyzes stock market data from the selected provider.

    Parameters:
        provider (str): The selected stock data provider ('YAHOO' or 'ALPHAVANTAGE').
        symbol (str): The stock symbol to fetch data for.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """

    try:
        # First provider's selection logic
        if provider == 'YAHOO':

            # Prompting the user to set desired date range and intervals
            default_start = datetime.now() - timedelta(days=7)
            start = func.get_date("Enter the start date (YYYY-MM-DD) [default: 7 days ago]: ")
            if not start:
                start = default_start  # Use default if no input
                print(f"Start Date: {start}")
            end = func.get_date("Enter the end date (YYYY-MM-DD):") 
            if not start:
                start = default_start  # Use default if no input
                print(f"Start Date: {end}")
            interval = func.valid_intervals()
            
            print(f"Fetching data for {symbol} from Yahoo Finance...")
           
            # Fetching, saving, and analysing data for Yahoo
            data = yo.fetch_data(symbol=symbol, start=start, end=end, interval=interval)
            yo.save_to_csv(data, filename=f"{symbol}_data.csv")
            yo.data_analysis(file=f"{symbol}_data.csv")
            
            # Confirming data analysis completion
            print(f"📊 Data analysis for {symbol} completed.")

        # Second provider's selection logic    
        elif provider == 'ALPHAVANTAGE':
            
            # Prompting the user to set desired intervals
            interval = func.valid_intervals()
            
            print(f"Fetching data for {symbol} from Alphavantage...")
            
            # Fetching, saving, and analysing data for Alphavantage
            meta_data, time_series = alpha.get_stock_data(symbol=symbol, interval=interval)
            alpha.save_to_csv(time_series, filename=f"{symbol}_data.csv")
            alpha.data_analysis(file=f"{symbol}_data.csv")
            
            # Confirming data analysis completion
            print(f"📊 Data analysis for {symbol} completed.")

        
        # Confirmation message
        print(f"✅ Data for {symbol} successfully fetched and saved!")
        return True
    except Exception as e:
        print(f"⚠️ An error occurred while processing {symbol} with {provider}: {e}")
        import traceback
        traceback.print_exc()
        return False

# ---------------------------------
# Executing the program
# ---------------------------------    
if __name__ == '__main__':
    stock_providers = ['ALPHAVANTAGE', 'YAHOO']
    with open('data/stock_symbols.txt', 'r') as file:
        stock_symbols = [line.strip() for line in file]
    

    # Welcoming message
    print("\nWelcome to the Stock Market Data")
    print("In this program, user can choose between two of the wellknown Stock Market Data provider - Yahoo Finance and Alphavantage.")
    
    # ---------------------------------
    # Provider Selection Loop:
        # Allows the user to select a stock provider or go back to provider selection.
    # ---------------------------------

    while True:
        print(f"\nAvailable Stock Market Data Providers: {', '.join(stock_providers)}")
        selected_provider = input("Enter a provider (or type 'EXIT' to quit): ").upper()

        if selected_provider == 'EXIT':
            print("Exiting the program. Goodbye!")
            break

        if selected_provider not in stock_providers:
            print("⚠️ Invalid provider. Please choose from the list.")
            continue

        # ---------------------------------
        # Symbol Selection Loop:
            # Allows the user to select a stock symbol or go back to provider selection.
        # ---------------------------------

        while True:
            print(f"\nAvailable Stock Symbols: {', '.join(stock_symbols)}")
            selected_symbol = input("Enter a stock symbol (or type 'BACK' to choose another provider or 'EXIT' to quit): ").upper()

            if selected_symbol == 'EXIT':
                print("Exiting the program. Goodbye!")
                break
            
            if selected_symbol == 'BACK':
                print("Returning to provider selection...")
                break

            if selected_symbol not in stock_symbols:
                print("⚠️ Invalid stock symbol. Please choose from the list.")
                continue

            # Fetch and save data
            success = fetch_save_analyise(selected_provider, selected_symbol)
            if success:
                continue_choice = input("Do you want to fetch data for another stock? (yes/no/back): ").lower()
                if continue_choice in ['no', 'back']:
                    print("Returning to provider selection...")
                    break 

                elif continue_choice == 'yes':
                    continue
                
                else:
                    print("⚠️ Invalid choice. Returning to provider selection...")
                    break