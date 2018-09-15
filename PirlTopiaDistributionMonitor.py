import requests
r = requests.get("https://www.cryptopia.co.nz/Exchange/GetCurrencyDistribution?currencyId=690&count=100&_=1536900000001")

Distribution = r.json()
print(Distribution["Distribution"])