import json

import requests
import pytest

a = {
    "apikey": "Lyp1smApghxvY28UbdMZICbPyBTWpR94",
    "q": "Minsk"
}
b = {
    "onDate": "2017-1-1"
}
c = {
    "startDate": "2016-6-1",
    "endDate": "2016-6-30",
}
# host = 'http://www.nbrb.by/API/ExRates/Rates'
#
# response = requests.get(host + '/145', params=b)
# print response
# cur_json = response.json()
# print cur_json
# current = json.dumps(cur_json)
# print cur_json['Cur_OfficialRate']

host1 = 'http://www.nbrb.by/API/ExRates/Rates/Dynamics/145'
response1 = requests.get(host1, params=c)
cur_json1 = response1.json()
print type(cur_json1)
print cur_json1
cur_list = []
for i in cur_json1:
    cur_list.append(i['Cur_OfficialRate'])
print cur_list




# host = 'http://dataservice.accuweather.com/locations/v1/cities/search'
#
# response = requests.get(host, params=a)
# location = response.json()
# print type(location)
# for i in location:
#     print i
#     print
# print location[0]['LocalizedName']