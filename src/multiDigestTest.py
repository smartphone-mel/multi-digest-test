import requests
import json
from bs4 import BeautifulSoup
import itertools

def fGetData(sValue):
    r = requests.get(sValue)

    #print('. Request:')
    #print(type(r.text))
    #print('\n' + r.text)

    soup_html = BeautifulSoup(r.text, "html.parser")
    #print(soup_html.prettify())

    #print('\n - lxml:')
    #soup_lxml = BeautifulSoup(r.text, "lxml")
    #print(soup_lxml.prettify())

    print('\n\n. HTML Searching:')
    #print('h1: ' + soup_html.find('h1').text)
    print('h1!')
    list_h1 = soup_html.find_all('h1')
    for item_h1 in list_h1:
        if (item_h1.text != None and item_h1.text.strip() != ''):
            print(item_h1.text.strip())
    #print('h2: ' + soup_html.find('h2').text)
    print('\nh2!')
    list_h2 = soup_html.find_all('h2')
    for item_h2 in list_h2:
        if (item_h2.text != None and item_h2.text.strip() != ''):
            print(item_h2.text.strip())
    #list_p = soup_html.find_all('tag-item', {'class': 'class-name'})
    #for item_p in list_p:
    #    if (item_p.text != None and item_p.text.strip() != ''):
    #        print(item_p.text)
    #print(soup_html.find_all('div', {'class': 'footer'})[0].text)

rEntries = open(r'entries.json')
content = json.loads(rEntries.read())
for item in content:
    print(item)
    fGetData(item)
    print('----------\n')
