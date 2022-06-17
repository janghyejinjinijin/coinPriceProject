import requests

url = "https://api.upbit.com/v1/ticker"

param = {"markets":"KRW-BTC"}

#headers = {"Accept": "application/json"}

response = requests.get(url, params=param)
#print(response)
upbitResult = response.json() #제이슨파일로 변환

print(upbitResult[0]['trade_price'])#현재가
print(upbitResult[0]['high_price'])#24시간거래량
print(upbitResult[0]["low_price"])#24시간거래량
print(upbitResult[0]["acc_trade_price_24h"])#24시간거래량
print(upbitResult[0]["acc_trade_volume"])#24시간거래량
print(upbitResult[0]["trade_volume"])#24시간거래량
print(upbitResult[0]["signed_change_rate"])#부호가 있는 변화율