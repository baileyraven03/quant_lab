# To run: python quant_lab/src/quantlab/returns.py

import csv
import datetime as dt


def load_prices(Name):
    path = "quant_lab/data/individual_stocks_5yr/individual_stocks_5yr/" + Name + "_data.csv"
    stock = []
    with open(path, newline="") as file:
        full_csv = csv.DictReader(file)
        for row in full_csv:
            stock.append({
                "Date": dt.datetime.strptime(row['date'], '%Y-%m-%d'),
                "Open": float(row['open']),
                "High": float(row['high']),
                "Low": float(row['low']),
                "Close": float(row['close']),
                "Volume": float(row['volume']),
                "Name": row['Name']
            })

        print("You have successfully loaded the " +
              str(stock[0]["Name"] + " stock values."))
        return stock


def simple_returns(stock):
    opens = [row["Open"] for row in stock]
    closes = [row["Close"] for row in stock]
    dates = [row["Date"] for row in stock]
    daily_returns = [[dates[i], closes[i] - opens[i]]
                     for i in range(len(opens))]
    total_return = sum([row[1] for row in daily_returns])
    return daily_returns, total_return


CMA = load_prices("CMA")

CMA_daily, CMA_total = simple_returns(CMA)
