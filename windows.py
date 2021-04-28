import requests
import datetime
import pandas as pd
import pybithumb
import datetime
import time

if __name__ == "__main__":

    tickers = pybithumb.get_tickers()

    detail = pybithumb.get_market_detail("BTC")
    #print(detail)

    orderbook = pybithumb.get_orderbook("BTC")
    #print(orderbook)

    ms = int(orderbook["timestamp"])
    dt = datetime.datetime.fromtimestamp(ms/1000)

    # 매수
    bids = orderbook['bids']
    # 매도
    asks = orderbook['asks']

    for bid, ask in zip(bids, asks):
        price_bid = bid['price']
        quant_bid = bid['quantity']

        price_ask = ask['price']
        quant_ask = ask['quantity']
        print("매수호가: ", price_bid, "매수잔량: ", quant_bid, "매도호가: ", price_ask, "매도잔량: ", quant_ask)

    all = pybithumb.get_current_price("ALL")
    for ticker, data in all.items():
        print(ticker, data['closing_price'])


    while True:
        price = pybithumb.get_current_price("BTC")
        try:
            print(price / 10)
        except:
            print("에러 발생", price)
            time.sleep(0.2)


    # for k in orderbook:
    #     print(k)

    # for ticker in tickers:
    #     price = pybithumb.get_current_price(ticker)
    #     print(ticker, price)
    #     time.sleep(0.1)