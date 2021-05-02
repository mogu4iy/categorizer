import json
import re

COINS_REGEX_FILE = r"coinsRegex.json"


def lowerList(listToLower):
    return list(map(lambda x: x.lower(), listToLower))


def subSet(category1, category2):
    return category1['searchResult'][0] <= category2['searchResult'][0] and \
           category1['searchResult'][-1] >= category2['searchResult'][-1] and \
           category2['fullName'] in category1['fullName']


def categorize(tagsList):
    with open(COINS_REGEX_FILE, "r") as coinsListFile:
        coinsListJSON = json.load(coinsListFile)['Cryptocurrencies']
        tagsString = "|".join(lowerList(tagsList))
        tagCategories = []
        for coin in coinsListJSON:
            result = re.search(coin['regex'], tagsString)
            if result:
                tagCategories.append({'fullName': coin['fullName'], 'searchResult': result.span()})
        for i in range(len(tagCategories) - 1):
            for j in range(i+1, len(tagCategories)):
                if subSet(tagCategories[j], tagCategories[i]):
                    tagCategories.remove(tagCategories[i])

        return list(set(coinName['fullName'] for coinName in tagCategories))
