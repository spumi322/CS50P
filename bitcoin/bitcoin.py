import requests
import sys


# command-line argument the number of Bitcoins, n
if len(sys.argv) != 2:
    sys.exit("Missing or too many command-line arguments")
else:
    try:
        n = sys.argv[1]
        n = float(n)
        if type(n) != float:
            raise ValueError
    except ValueError:
        sys.exit("Command-line argument is not a number")

# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object
try:
    request_from_api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    bitcoin_rate = request_from_api["bpi"]["USD"]["rate_float"]
    print(f"${bitcoin_rate * n:,.4f}")
except requests.RequestException:
    sys.exit("API request error")
