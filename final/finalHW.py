# импортирование необходимых библиотек

import json
import requests
from bs4 import BeautifulSoup as BS
import datetime
from decimal import Decimal


# переменная, в которой сохранена ссылка с нужной таблицей данных
url = 'https://www.cbr.ru/hd_base/metall/metall_base_new/?UniDbQuery.Posted=True&UniDbQuery.From=12.04.2023&UniDbQuery.To=22.04.2023&UniDbQuery.Gold=true&UniDbQuery.so=1'

def serialization(x):
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
    def del_spaces(clear_data2):
        b = list(clear_data2.keys())[0]
        clear_data4 = {}
        a = 0
        for i in clear_data2:
            x = int(str(b - i)[0])
            if x > 1:
                b = b - datetime.timedelta(1)
                clear_data4[b] = clear_data2[i]
                break
            else:
                clear_data4[i] = clear_data2[i]
                b = i
        if list(clear_data4.keys())[-1] == list(clear_data2.keys())[-1]:
            return clear_data4
        else:
            del_spaces(clear_data2)
    return clear_data4


serializ_data = serialization(url)
print(serializ_data)

















