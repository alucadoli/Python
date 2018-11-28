#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
import re
from bs4 import BeautifulSoup

req_url_base = r"http://d2.sku117.biz/pw/"
req_url_init = r"http://d2.sku117.biz/pw/thread.php?fid=17&page="
# req_url_init = r"http://s2.lulujjs.info/pw/thread.php?fid=17&page="

def get_txt(txt_title,txt_id,txt_url):
    txt = {}
    txt['title'] = ''
    txt['id'] = str(txt_id)
    res = requests.get(txt_url)
    soups = BeautifulSoup(res.content,"html.parser")
    txt['title'] = txt_title
    content = soups.find('div', class_='tpc_content')
    if(content):
        fo = open('{0:0>8}-{1}.txt'.format(txt['id'],txt['title']),"ab+")
        fo.write((txt['title']+"\r\n").encode('UTF-8'))
        fo.write((content.text + "\r\n").encode('UTF-8'))
        fo.close()
        print('Notes ',txt_title,'下载完毕！')



def get_pages(url_page):
    cookies = {
        '__cfduid': 'd71a44ed47f328923d9434eec131842621527081834',
        'UM_distinctid': '1638d2ba13a382-0e6d09b6f577b-737356c-151800-1638d2ba13b2e1',
        'aafaf_lastpos': 'F17',
        'aafaf_threadlog': '%2C17%2C',
        'aafaf_ol_offset': '97',
        'aafaf_lastvisit': '4%091527083725%09%2Fpw%2Fthread.php%3Ffid%3D17',
        'CNZZDATA1261158850': '3797371-1527077318-%7C1527082736',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'DNT': '1',
        'Referer': 'http://d2.sku117.com/pw/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = (
        ('fid', '17'),
    )

    r = requests.get(url_page, headers=headers, params=params, cookies=cookies)
    # r = requests.get(url_page)
    soup = BeautifulSoup(r.content, 'html.parser')
    note_list = soup.find_all(href=re.compile("read.php"), id=True)
    for list in note_list:
        txt_url = req_url_base + list.attrs['href']
        txt_id = list.attrs['id'][-7:]
        txt_title = list.text
        get_txt(txt_title, txt_id, txt_url)

for i in range(342,600):
    req_url_page = req_url_init+str(i)
    try:
        print('当前页数为',
        get_pages(req_url_page)
    except Exception as e:
        print('Error!',e)






