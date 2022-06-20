import requests
import pyupbit

url = "https://api.upbit.com/v1/market/all?isDetails=false"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

#print(response.text)

ticker_list = pyupbit.get_tickers()
#print(ticker_list)

ticker_list = pyupbit.get_tickers(fiat="KRW")
# 원화로 살 수 있는애들만 뽑을 수 있음
print(ticker_list)
# 뒤에 글자만 뽑아내기
coin_list = []
for ticker in ticker_list:
    #print(ticker[4:10])
    coin_list.append(ticker[4:10])
print(coin_list)