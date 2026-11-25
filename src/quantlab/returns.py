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


def weekly_returns(stock):
    daily_returns, _ = simple_returns(stock)

    weekly_returns_by_day = {}
    weekly_totals = {}
    for dates, returns in daily_returns:
        year, week, _ = dates.isocalendar()

        key = (year, week)
        if key not in weekly_returns_by_day:
            weekly_returns_by_day[key] = [returns]
            weekly_totals[key] = returns

        else:
            weekly_totals[key] = weekly_totals[key] + returns
            weekly_returns_by_day[key].append(returns)
    #  Checking Functionality
    for key in weekly_returns_by_day:
        if sum(weekly_returns_by_day[key]) != weekly_totals[key]:
            print("Incorrect!")

    return weekly_totals, weekly_returns_by_day


def yearly_returns(stock):
    weekly_totals, _ = weekly_returns(stock)
    yearly_returns = {}
    for (year, week), value in weekly_totals.items():
        key = year
        if key not in yearly_returns:
            yearly_returns[key] = value
        else:
            yearly_returns[key] += value
    return yearly_returns


def call_all_functions(stock):
    prices = load_prices(stock)
    daily, total = simple_returns(prices)
    weekly_total, daily_by_week_returns = weekly_returns(prices)
    yearly = yearly_returns(prices)
    stock = {
        "prices": prices,
        "daily": daily,
        "total": total,
        "weekly_totals": weekly_total,
        "daily_by_week": daily_by_week_returns,
        "yearly": yearly,
    }
    return stock


CMA = call_all_functions("CMA")

AAPL = load_prices("AAPL")

AAPL_daily, AAPL_total = simple_returns(AAPL)
AAPL_weekly_total, AAPL_daily_by_week_returns = weekly_returns(AAPL)
AAPL_yearly = yearly_returns(AAPL)

print(CMA["yearly"])
