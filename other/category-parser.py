import math

import requests
from bs4 import BeautifulSoup
import json

workers = ['Bohdan', 'Yaroslav', 'Sasha', 'Roman', 'Ivan']

req = {
    'url': 'https://stockmoonapi.herokuapp.com/stock_apis_BE/category/',
    'cookies': [
        {'name': 'csrftoken',
         'value': 'fDOPEy1hwsvLiFqGaB82JMtox5wPZHOzsEoQm11PO3GIKNRR9ZuNoyWr7pITTRS7',
         'domain': 'stockmoonapi.herokuapp.com',
         'path': '/'},
        {'name': 'sessionid',
         'value': '0tdasqaf72fny0sinoadl91whff57xsl',
         'domain': 'stockmoonapi.herokuapp.com',
         'path': '/'}
    ]

}
URL = 'https://stockmoonapi.herokuapp.com/stock_apis_BE/category/'
COOKIES = [
    {'name': 'csrftoken',
     'value': 'fDOPEy1hwsvLiFqGaB82JMtox5wPZHOzsEoQm11PO3GIKNRR9ZuNoyWr7pITTRS7',
     'domain': 'stockmoonapi.herokuapp.com',
     'path': '/'},
    {'name': 'sessionid',
     'value': '0tdasqaf72fny0sinoadl91whff57xsl',
     'domain': 'stockmoonapi.herokuapp.com',
     'path': '/'}
]

INPUT_FILE = r'categories.json'


def pageParser(page):
    returnList = []
    categoriesList = page.find('table', {'id': 'result_list'}).find('tbody').find_all('th', {'class': 'field-__str__'})
    for category in categoriesList:
        c = category.find('a').text
        returnList.append(c)
    return returnList


def main():
    with open(INPUT_FILE, "r") as file:
        previousCategories = json.load(file)
        with requests.Session() as s:
            c = requests.cookies.RequestsCookieJar()
            for cookie in COOKIES:
                c.set(**cookie)
            s.cookies = c
            r = s.get(URL)
            soup = BeautifulSoup(r.content, "html.parser")
            pages = soup.find('p', {'class': 'paginator'})
            lastPageIndex = pages.find('a', {'class': 'end'})
            print(f'We have categories on {lastPageIndex.text} pages')
            # page = s.get(url, params={'p': 1})
            # print(BeautifulSoup(page.content, 'html.parser').find('table', {'id': 'result_list'}))
            # page = s.get(url, params={'p': 2})
            # print(BeautifulSoup(page.content, 'html.parser').find('table', {'id': 'result_list'}))
            # for i in range(1, int(lastPageIndex.text)):
            i = 1
            workerIndex = 0
            while i <= int(lastPageIndex.text):
                with open(f'{workers[workerIndex]}.json', "w") as outputFile:
                    print(f'{workers[workerIndex]} file -----------------')
                    workerCount = 0
                    output = previousCategories
                    while workerCount < 1800 and i <= int(lastPageIndex.text):
                        page = s.get(url, params={'p': i})
                        pageHtml = BeautifulSoup(page.content, 'html.parser')
                        lastCount = count
                        categories = getCategories(pageHtml)
                        for category in categories:
                            output[f'categoriesList{math.floor(workerCount / 100)}'].append(
                                {"name": category, "categories": []})
                        workerCount += count - lastCount
                        print(f'page {i} is done, workerCount :{workerCount}, globalCount :{count}')
                        i += 1
                    print(
                        f'{workers[workerIndex]} file is done, workerCount :{workerCount}, globalCount :{count} -------------')
                    json.dump(output, outputFile)
                workerIndex += 1


if __name__ == '__main__':
    main()
