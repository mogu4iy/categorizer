from categorizer import categorize
from datetime import datetime


def Average(lst):
    return sum(lst) / len(lst)


if __name__ == '__main__':
    tags = ['XMR/BTC', 'BTC Options OI held', 'DOGEBTC (TradingView)', 'BTCB', 'get-more-btc', 'filbtc',
            'BTCADA (TradingView)', 'bitcoin cash prices', 'bitcoin btc/btcp makes bitcoin cash increase',
            'bitcoin cash increase']
    start_time = datetime.now()
    result = categorize(tags)
    result_time = (datetime.now() - start_time).microseconds / 1000
    print(f"Time to categorize {len(tags)} Tags : ", result_time, "milliseconds")
    print("Time per Tag : ", result_time / len(tags), "milliseconds")
    print("tags :\n", tags)
    print("categories :\n", result)
