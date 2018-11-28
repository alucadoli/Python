#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json
import time
import sys
import codecs

def trans(path,result):
    file = open(path + '.csv','w',newline='')
    writer = csv.writer(file,delimiter='\t')
    flag = True
    for line in result:
        dic = json.loads(line[0:-1])
        if flag:
            keys = list(dic.keys())
            print(keys)
            writer.writerow(keys)
            flag = False
        else:
            writer.writerow(list(dic.values()))
    file.close()


chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-extension')
chrome_options.add_argument('--test-type')
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(chrome_options=chrome_options)

# driver = webdriver.Chrome()
driver.get("https://cloud.cainiao.com/markets/cnwww/cncloud-dzk-detail-correct")
assert "地址" in driver.title
elem = driver.find_element_by_class_name("inputInput")
elem.clear()
elem.send_keys("addressList=北京市西城区广安门外大街西堤红山6号楼")
driver.find_element_by_class_name("inputBtn").click()

try:
    WebDriverWait(driver,2).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,'json')))
    #a = driver.find_element_by_xpath("//*[@class='hljs json']")
    result = driver.find_element_by_css_selector(".json").text
    # result = json.loads(a.text)
    print(result)
    trans(r'D:\PythonProjects\AddressClean\a',result)
finally:
    assert "No results found." not in driver.page_source
    driver.close()



