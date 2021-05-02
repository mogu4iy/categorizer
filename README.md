# Mogu4iy Categorizer

Simple python cryptoCurrencies categorizer, based on regex.
# Usage
#### Prepare to use
If you want to update coinsList and coinsRegex:

```sh
pip install requirements.txt
python parse_coins.py
```

To test Mogu4iy Catogorizer

```sh
python test_categorizer.py **list of tags or nothing(default list will be used)**
```
#### Production

For production use categorizer.py
Input : list of tags
Output : list of categories
##### Example : 
tags :
 ['XMR/BTC', 'BTC Options OI held', 'DOGEBTC (TradingView)', 'BTCB', 'get-more-btc', 'filbtc', 'BTCADA (TradingView)', 'bitcoin cash prices', 'bitcoin btc/btcp makes bitcoin cash incre
ase', 'bitcoin cash increases']
categories :
 ['bitcoin', 'bitcoin cash', 'cardano', 'dogecoin', 'filecoin', 'monero', 'bitcoin bep2']

