import pyupbit
import datetime
import time


def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

def get_yesterday_ma5(ticker):
     df = pyupbit.get_ohlcv(ticker)
     close = df['close']
     ma = close.rolling(window=5).mean()
     return ma[-2]


if __name__ == "__main__":
    now = datetime.datetime.now()
    mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
    ma5 = get_yesterday_ma5("KRW-BTC")
    target_price = get_target_price('KRW-BTC')
    print(target_price)

    while True:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.delta(seconds=10):
            target_price = get_target_price('BTC')
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            ma5 = get_yesterday_ma5("BTC")
            print(target_price)

        current_price = pyupbit.get_current_price('KRW-BTC')
        #print(current_price)

        time.sleep(1)
# while True:
#     price = pyupbit.get_current_price("KRW-BTC")
#     print(price)
#     time.sleep(0.2)
