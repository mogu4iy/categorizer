import json
import re

COINS_FILE = r"coins.json"
COINS_RE = lambda coin: rf"((\b({coin})(\w(\w)+)+)|((\w(\w)+)+({coin})\b))|(\b({coin})\b)"


def lowerList(listToLower):
    return list(map(lambda x: x.lower(), listToLower))


def categorize(tagsList):
    with open(COINS_FILE, "r") as coinsListFile:
        coinsListJSON = json.load(coinsListFile)['Cryptocurrencies']
        categories = []
        for tag in lowerList(tagsList):
            tagCategories = []
            exceptCategories = []
            for coin in coinsListJSON:
                for c in coin['names']:
                    pattern = re.compile(COINS_RE(c))
                    result = re.search(pattern, tag)
                    if result:
                        exceptCategories.extend(coin['except'])
                        tagCategories.append({'fullName': coin['fullName'], 'result': result, 'foundBy': c})
                        break
            for t in tagCategories:
                for otherTag in tagCategories:
                    if otherTag != t:
                        if t['foundBy'] in otherTag['foundBy']:
                            tagMatch = t['result'].span()
                            otherTagMatch = otherTag['result'].span()
                            if tagMatch[0] >= otherTagMatch[0] & tagMatch[1] <= otherTagMatch[1]:
                                tagCategories.remove(t)
            resultCategories = [c['fullName'] for c in tagCategories]
            categories.extend(resultCategories)
        return list(set(categories))
