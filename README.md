# Stock Market Data

This project is a Python-based command-line app designed to fetch, save, and analyze stock market data from two major providers: **Yahoo Finance** and **AlphaVantage**. It was created as a learning project to demonstrate skills in Python programming, working with APIs, and data visualization.

---

## **What This App Does**

- Lets users choose between Yahoo Finance and AlphaVantage to fetch stock market data.
- Allows input for specific stock symbols, date ranges, and time intervals.
- Saves the fetched data in CSV format for later use.
- Displays visualizations of stock performance, such as closing prices over time.

---

## **How to Use It**

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/stock-market-app.git
   cd stock-market-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python main.py
   ```

4. Follow the prompts:
   - Choose a data provider (Yahoo Finance or AlphaVantage).
   - Enter a stock symbol from the list.
   - Provide additional inputs, such as date range and interval (as applicable).

---

## **Key Features**

- **Dynamic Inputs:** Set date ranges, intervals, and stock symbols.
- **Multi-Provider Support:** Integrates two stock market data providers.
- **Data Visualization:** Generates a line chart for stock closing prices.
- **Error Handling:** Includes prompts and clear feedback for invalid inputs.

---

## **File Organization**

```
📂 stock-market-app
├── README.md              # Project description
├── requirements.txt       # Dependencies
├── main.py                # Main app script
├── Yahoo.py               # Yahoo Finance integration
├── alphavantage.py        # AlphaVantage integration
├── dynamic_func.py        # Helper functions
└── data/                  # Folder for CSV files
```

---

## **Things I Learned**

1. How to integrate multiple APIs into a single project.
2. Using `pandas` for data manipulation and `matplotlib` for visualization.
3. Writing modular code for better maintainability.
4. Error handling to improve user experience.

---

## **What’s Next?**

- Add dynamic stock symbol loading from APIs.
- Implement comparison features for multiple stocks or providers.
- Create a simple GUI using a framework like Tkinter.

---

## **Contact**

Feel free to reach out with any questions or suggestions:
- GitHub: MMtech-Dev - https://github.com/MMtech-Dev/portfo 
- Portfolio: https://mmtech.eu.pythonanywhere.com

