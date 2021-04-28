import pyupbit

if __name__ == "__main__":
    tickers = pyupbit.get_tickers()
    print(tickers)

    tickers = pyupbit.get_tickers(fiat="KRW")
    print(tickers)

    price = pyupbit.get_current_price("KRW-XRP")
    print(price)

    price2 = pyupbit.get_current_price("BTC-XRP")
    print(price2)

    df = pyupbit.get_ohlcv("KRW-BTC")
    print(df)

    df2 = pyupbit.get_ohlcv("KRW-BTC", count=5)
    print(df2)

    orderbook = pyupbit.get_orderbook("KRW-BTC")

    print(type(orderbook))
    print(len(orderbook[0]['orderbook_units']))

    bids_asks = orderbook[0]['orderbook_units']
    print(orderbook)

    for bid_ask in bids_asks:
        print(bid_ask)