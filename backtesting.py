import pyupbit
import numpy as np
from pandas import DataFrame

def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-PLA")
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],
                      df['close'] / df['target'] - fee,
                      1)

    ror = df['ror'].cumprod()[-2]
    return ror


    # PLA
if __name__ == "__main__":
    df = pyupbit.get_ohlcv('KRW-PLA')
    print(df.tail())

    df['range'] = (df['high'] - df['low']) * 0.5
    df['range_shift1'] = df['range'].shift(1)
    df['target'] = df['open'] + df['range'].shift(1)
    # numpy.where(조건, 조건이 참 일 때의 값, 조건이 거짓일 때의 값)
    fee = 0.005

    df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'], 1)
    df['hpr'] = df['ror'].cumprod()
    df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
    print("MDD(%): ", df['dd'].max())

    ror = df['ror'].cumprod()[-2]

    for k in np.arange(0.1, 1.0, 0.1):
        ror = get_ror(k)
        print("%.1f %f" % (k, ror))

    df.to_excel("KRW-PLA.xlsx")
    print(ror)

    print("MDD: ", df['dd'].max())
    print("HPR: ", df['hpr'][-2])
    df.to_excel("larry_ma.xlsx")

    # data = {'빗썸': [100, 100, 100],'코빗': [90, 110, 120]}

    # df.to_excel("trade.xlsx")

    # df = DataFrame(data)
    # df['최저가'] = np.where(df['빗썸'] < df['코빗'], '빗썸', '코빗')
    # df.to_excel("거래소.xlsx")