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


CMA = load_prices("CMA")
print(CMA[:3])

print(CMA[1]["Name"])
