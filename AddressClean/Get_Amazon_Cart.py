#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import re
import requests
from openpyxl import Workbook

cookies = {
    'at-main': 'Atza|IwEBILcrBKqoXHN6OvOXPqCFksETXdtBm1HWBka2PzoHJ8aidowa9mZ55pxIHaSutvmW6fr9PT7S-KLcnVbiBjAuJga7GwIwo8LOD-IppzCbmSz55rOIAqEu1OApCPYeoopKppSsxnMN0a7Ha7m5iJBJUmJls2sGJfrvWJp_rQOLF_hkzQAzvgTlTDSXLEhukAg1lXimp_npZNAQZnNDGm9ZITFztfeTgL_WzJcdsrMRGKMx1ygNm8CqzuieuUbT6vJYFC4vLYwHzARqQiS1sEgGDOIUjBhABn9bIbBcI0cH8AQHwMEK775SV5IregwZD-n746COSP2iGY7KRa7eEujmgAQX2v2C2Cz8YjEs-VOMcTHn4A6MpIh-jyGPI9zEpsh2qAgsF93uqKlVRA69awqXU_Ty',
    'sess-at-main': 'Kfv9KcWPDpbeV1QZaPhjc8ehJfHs4/rpQUjbcqrQj4k=',
    'iptac-5C838FE1DDB7-FCZ1949N005': '434f5250464353494e545c636e616c6c69404643535f4144--1475981659--998--1475978787--5337704213f378dd95777aa9bb9af90cf8404f8eac225589b192c62efc6bd1d2',
    'x-wl-uid': '1PwPZS9aI4Fm5Bdk1NcCVzflCBltjjE87iXlbNb0Q8Fgi0+2tsXIX84yYkLGVVIlAlATq3C89ExcQv+nnTDCdVkOaLdEFRwre5BfYvCrx7Hb9ryicWNAUOwRXgD46CY0QToDIHq+7700=',
    's_vnum': '1910136570625%26vn%3D1',
    's_cc': 'true',
    's_ppv': '70',
    's_nr': '1478136594516-New',
    's_dslv': '1478136594517',
    's_sq': '%5B%5BB%5D%5D',
    'amznacsleftnav-ef038fa0-d309-3fa8-843e-1e812feab80d': '1',
    'amznacsleftnav-63dedfe9-e28c-317a-8418-05517718ca4b': '1',
    'session-id': '451-9993811-5050868',
    'ubid-acbcn': '451-7049889-8146733',
    'x-acbcn': '8eHClVFKa8@jiKarjb7ZDMIyFaGL1E@o',
    'UM_distinctid': '16136b8e58d2a9-038635c6fdd23d-4323461-151800-16136b8e58e2a0',
    'session-id-time': '2082729601l',
    'session-token': '+Pvmk8ljn2g4ZMn+3QsNDA9chO5QXxyKO9xVqVuYe3hF0t9GokSxL0PHw04RMwyLecfqlBoXe8GNbNLDgQdSA/DSJK1WjOpmMiKKxgVBRZMWkOEbdHsXZtMFHaxDhSNkR1mSxLtzPGdDh2joOF8uFm6nWFGTTqbDU70mlqRq9wJ2XZ4lE4s43qJ0XJoxYx3Qp236O64QYSio+nkcolkClL6a3cVwLTJftFHIajn7sE8I/D54y8fuTssXe50szAk1gNURiJaqDhA=',
    'CNZZDATA1256793290': '1627048477-1517041249-null%7C1525774159',
    'csm-hit': 'Q1K19W39PVKFG3ZDEGG0+s-24A6S81VM79G58XYZDNJ|1525785371017'
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'DNT': '1',
    'Referer': 'https://www.amazon.cn/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}

proxies = {
    "https": "http://10.3.246.5:8500"
}

response = requests.get('https://www.amazon.cn/gp/cart/view.html/ref=nav_cart', proxies = proxies,headers=headers, cookies=cookies,verify=False)


html = response.text
# print(html)
it = r'<span class="aok-offscreen">(.*?)<\/span>'
pr = r'<span class="a-size-medium a-color-price sc-price sc-white-space-nowrap sc-product-price sc-price-sign a-text-bold">(.*?)<\/span>'
item = re.findall(it,html,re.S|re.M)
price = re.findall(pr,html,re.S|re.M)
list1 = dict(zip(item,price))

wb = Workbook()
ws = wb.active
ws.title = 'Books'
jg = {'Book' : '','Price' : ''}
ws.append(list(jg.keys()))


for k,v in list1.items():
    jg['Book'] = k
    jg['Price'] = v
    ws.append(list(jg.values()))
wb.save(r"C:\PYProjects\AddressClean\books.xlsx")

