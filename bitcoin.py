import sys
import requests


if len(sys.argv) ==2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command line argument is not a number")
        sys.exit(1)
else:
    print("missing command line argument")
    sys.exit(1)
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    res = r.json()
    bit = res['bpi']['USD']['rate_float']
    amount = bit * value
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("invalid way")
    sys.exit(1)
