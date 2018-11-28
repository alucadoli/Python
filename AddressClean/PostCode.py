#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
import json

proxies = {
  "https": "http://10.3.246.5:8500",
  "http": "http://10.3.246.5:8500"
}

addr='上海青浦拓青路88号'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'Hm_lvt_f9156f80cc764fbe69ecafe0e5202e63=1523152264; Hm_lpvt_f9156f80cc764fbe69ecafe0e5202e63=1523152264; UM_distinctid=162a2f31d1e2e5-0c9cf6e54c9d92-b34356b-144000-162a2f31d2649f; PHPSESSID=bktioe6kcjne6059131aj8av73; iptac-5C838FE1DDB7-FCZ1949N005=434f5250464353494e545c636e616c6c69404643535f4144--1523155850--2507--1522814673--fb4d5c647d65af49333313cf52a6b668f4210057a2990c81b81c605ec69e425c',
    'DNT': '1',
    'Host': 'cpdc.chinapost.com.cn',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://cpdc.chinapost.com.cn/web/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

payload = {
    'm': 'postsearch',
    'c': 'index',
    'a': 'ajax_addr',
    'searchkey': addr,
    'flag': '1523156224735',
    'provinceid': '310000',
    'cityid': '310100 - r',
    'areaid': '310116',
    'dosubmit': '1'
}

# url = 'http://cpdc.chinapost.com.cn/web/index.php?m=postsearch&c=index&a=ajax_addr&searchkey=%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%87%91%E6%B2%99%E6%B1%9F%E8%B7%AF1060%E5%8F%B7%E7%94%B3%E6%B1%89%E5%95%86%E5%8A%A1%E5%A4%A7%E5%8E%A6C%E5%BA%A71202%E5%AE%A4&flag=1523162978357&provinceid=310000&cityid=310000-r&areaid=310105&dosubmit=1'
r = requests.get("http://cpdc.chinapost.com.cn/web/index.php", headers=headers, params = payload,verify=False)

#r = requests.get(url,proxies=proxies, verify=False)
r.encoding = 'utf-8'
print(r.text)
ps = r.json()['rs'][0]['POSTCODE']
print(ps.split(' '))



