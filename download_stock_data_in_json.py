# pip install requests
# pip install json
# pip install datetime

import requests
import json
from datetime import datetime

# Configuration
api_key = "VZZC0B2JZBILVC05"
symbol = "XOM" # Stock ticker
start_date = datetime.strptime("1970-01-01", "%Y-%m-%d") # Starting date
end_date = datetime.strptime("2010-12-31", "%Y-%m-%d") # End date
output_filename = "xom_stock_monthly_1970_2010.json" # name of output file

# daily data is paid => monthly data

# Request Monthly Adjusted Data
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey={api_key}"

response = requests.get(url)
data = response.json()

# Check for errors
if "Monthly Adjusted Time Series" not in data:
    print("Error")
    print("API response:", data)
    exit()

# Parse and Filter Dates
monthly_data = data["Monthly Adjusted Time Series"]

formatted_data = [
    {
        "date": date,
        **{k: float(v) for k, v in values.items()}
    }
    for date, values in monthly_data.items()
]

filtered_data = [
    entry for entry in formatted_data
    if start_date <= datetime.strptime(entry["date"], "%Y-%m-%d") <= end_date
]

# Save to JSON File 
with open(output_filename, "w") as f:
    json.dump(filtered_data, f, indent=4)

print(f"saved {len(filtered_data)} monthly records to {output_filename}")

