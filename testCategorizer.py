from categorizer import categorize


if __name__ == '__main__':
    tags = ['XMR/BTC', 'BTC Options OI held', 'DOGEBTC (TradingView)', 'BTCB', 'get-more-btc', 'filbtc',
            'BTCADA (TradingView)', 'bitcoin cash prices']
    result = categorize(tags)
    print("tags :\n", tags)
    print("categories :\n", result)