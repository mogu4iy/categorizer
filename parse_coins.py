from bs4 import BeautifulSoup
import requests
import json

url = "https://coinmarketcap.com"
file = r"coins.json"
file2 = r"coinsList.json"
tagLinks = [("https://coinmarketcap.com/view/defi/", "Defi"),
            ("https://coinmarketcap.com/view/collectibles-nfts/", "NFT"),
            ("https://coinmarketcap.com/view/polkadot-ecosystem/", "Polkadot Eco"),
            ("https://coinmarketcap.com/view/binance-smart-chain/", "BSC Eco")]
coinsCount = 1000


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
    with open(file2, "w") as coinsListFile:
        resultCoinsList = []
        for c in coinsJSON:
            resultCoinsList.extend(c)
        json.dump({"Cryptocurrencies": lowerList(resultCoinsList)},
                  coinsListFile)
    with open(file2, "r") as coinsListFile:
        coinsListJSON = json.load(coinsListFile)
        with open(file, "w") as coinsFile:
            resultCoinsList = []
            for c in coinsJSON:
                if c[0] == c[1]:
                    resultCoinsNamesList = lowerList([c[0]])
                else:
                    resultCoinsNamesList = lowerList([c[0], c[1]])
                coinNamesList = lowerList(c[0].split(' '))
                # for c in coinsJSON:
                #
                exceptCoinNames = []
                if len(coinNamesList) > 1:
                    coinName = coinNamesList[0]
                    if coinName not in coinsListJSON['Cryptocurrencies']:
                        resultCoinsNamesList.append(coinName)
                    else:
                        exceptCoinNames.append(coinName)
                resultCoinsList.append(
                    {'names': resultCoinsNamesList, 'fullName': resultCoinsNamesList[0], 'except': exceptCoinNames})
            json.dump({"Cryptocurrencies": resultCoinsList},
                      coinsFile)


# def parseTags():
#     with open(file, "r+") as coinFile:
#         coinsJSON = json.load(coinFile)
#         for tag in tagLinks:
#             coinsJSON["Cryptocurrencies"]["categories"][tag[1]] = []
#             page = requests.get(tag[0])
#             soup = BeautifulSoup(page.content, "html.parser")
#             cryptoCurrenciesTable = soup.find("table",
#                                               {"class": "cmc-table cmc-table___11lFC cmc-table-homepage___2_guh"})
#             coins = list(cryptoCurrenciesTable.children)[2].find_all("tr")
#             result = []
#             for coin in coins:
#                 if len(list(coin.children)) not in [5, 11]:
#                     continue
#                 if list(coin.children)[2].find_all("p"):
#                     coinName = list(coin.children)[2].find_all("p")[0].get_text()
#                 else:
#                     coinName = list(coin.children)[2].find_all("span")[1].get_text()
#                 result.append(coinName)
#                 if coinName in coinsJSON["Cryptocurrencies"]["list"]:
#                     coinsJSON["Cryptocurrencies"]["categories"][tag[1]].append(coinName)
#         coinFile.seek(0)
#         coinFile.write(json.dumps(coinsJSON))


def main():
    parseCoins()


if __name__ == '__main__':
    main()
