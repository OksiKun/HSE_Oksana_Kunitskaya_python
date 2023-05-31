# импортирование необходимых библиотек

import json
import requests
from bs4 import BeautifulSoup as BS
import datetime
from decimal import Decimal


# переменная, в которой сохранена ссылка с нужной таблицей данных
url = 'https://www.cbr.ru/hd_base/metall/metall_base_new/?UniDbQuery.Posted=True&UniDbQuery.From=12.04.2009&UniDbQuery.To=22.04.2023&UniDbQuery.Gold=true&UniDbQuery.so=1'

class ParserCBRF:

    def start(x):
        data = BS(requests.get(x).text)
        data = data.findAll('td')
        clear_data = {}                   # в переменной сохраняется пустой словарь
        clear_data2 = {}
        clear_data3 = {}
        for i in range(0, len(data), 2):
            clear_data[data[i].text] = data[i+1].text
        with open('serializ_data.json', 'w+') as outfile:
            json.dump(clear_data, outfile)
        for i in clear_data:
            x = datetime.date(int(i[-4:]),int(i[3:5]),int(i[0:2]))
            clear_data3[x] = clear_data[i]
            clear_data2 = clear_data2 | clear_data3
        for i in clear_data2:
            clear_data2[i] = clear_data2[i].replace(' ', '')
            clear_data2[i] = clear_data2[i].replace(',', '.')
            clear_data2[i] = Decimal(clear_data2[i])
        clear_data4 = []

        def dict_to_list_of_tuple(newList):
            newList = []
            for key in clear_data2:
                value = clear_data2[key]
                nTuple = (key, value)
                newList.append(nTuple)
            return newList

        newList = dict_to_list_of_tuple(clear_data2)
        clear_data4.append(newList[0])
        def del_spaces(u, newList):
            u = 1
            for i in range(len(newList) - 1):
                if newList[i][0] - datetime.timedelta(days=1) != newList[i + 1][0]:
                    newList.append((newList[i][0] - datetime.timedelta(days=1), newList[i + 1][1]))
                    newList.sort(reverse=True)
                    u = 0
                    break
            return (u, newList)

        x = del_spaces(0, newList)
        while del_spaces(0, newList)[0] == 0:
            del_spaces(0, newList)
        else:
            x = newList

        return x

x = ParserCBRF.start(url)


print(x)
















