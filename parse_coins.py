from bs4 import BeautifulSoup
import requests
import json
from coins_regex import configure_regex

url = "https://coinmarketcap.com"
file = r"coins.json"
file2 = r"coinsList.json"
coinsCount = 100
tagLinks = [("https://coinmarketcap.com/view/defi/", "Defi"),
            ("https://coinmarketcap.com/view/collectibles-nfts/", "NFT"),
            ("https://coinmarketcap.com/view/polkadot-ecosystem/", "Polkadot Eco"),
            ("https://coinmarketcap.com/view/binance-smart-chain/", "BSC Eco")]


def lowerList(listToLower):
    return list(map(lambda x: x.lower(), listToLower))


def parseCoins():
    coinsJSON = []
    for i in range(1, int(coinsCount / 100) + 1):
        link = url + f"?page={i}"
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        cryptoCurrenciesTable = soup.find("table", {"class": "cmc-table cmc-table___11lFC cmc-table-homepage___2_guh"})
        coins = list(cryptoCurrenciesTable.children)[2].find_all("tr")
        for coin in coins:
            if list(coin.children)[2].find_all("p"):
                coinNames = list(map(lambda tag: tag.get_text(), list(coin.children)[2].find_all("p")))
            else:
                coinNames = list(map(lambda tag: tag.get_text(), list(coin.children)[2].find_all("span")[1:]))
            coinsJSON.append(coinNames)
    coinsJSON = list(map(lowerList, coinsJSON))
    coinsList = []
    for coin in coinsJSON:
        coinsList.extend(coin)
    with open(file, "w") as coinsFile:
        resultCoinsList = []
        for c in coinsJSON:
            fullName = c[0]
            resultCoinsNamesList = lowerList([c[0], c[1]])
            coinNamesList = lowerList(c[0].split(' '))
            exceptCoinNames = []
            if len(coinNamesList) > 1:
                if coinNamesList[0] not in coinsList:
                    resultCoinsNamesList.append(coinNamesList[0])
                exceptCoinNames = coinNamesList
            resultCoinsNamesList = list(set(resultCoinsNamesList))
            resultCoinsList.append(
                {'names': resultCoinsNamesList, 'fullName': fullName, 'except': exceptCoinNames})
        json.dump({"Cryptocurrencies": resultCoinsList},
                  coinsFile)


def main():
    parseCoins()
    configure_regex()


if __name__ == '__main__':
    main()
