import json

COINS_FILE = r"coins.json"
COINS_REGEX_FILE = r"coinsRegex.json"
coins_regex = lambda coinList: '(' + '|'.join(
    [rf"((\b({coin})(\w(\w)+)+)|((\w(\w)+)+({coin})\b))|(\b({coin})\b)" for coin in coinList]) + ')'


def configure_regex():
    with open(COINS_FILE, "r") as coinsListFile:
        coinsListJSON = json.load(coinsListFile)['Cryptocurrencies']
        with open(COINS_REGEX_FILE, "w") as coinsRegexListFile:
            coinsRegexList = []
            for coin in coinsListJSON:
                coinsRegexList.append({"regex": coins_regex(coin['names']), "fullName": coin['fullName']})
            json.dump({"Cryptocurrencies": coinsRegexList},
                      coinsRegexListFile)
