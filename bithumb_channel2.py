from pybithumb import WebSocketManager

if __name__ == "__main__":
    wm = WebSocketManager("ticker", [f"BTC_KRW"], ["24H", "MID"])
    data = wm.get()

    print(data)