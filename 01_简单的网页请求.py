# -*-coding:utf-8-*-

import requests

# 模拟User-Agent用户标签的参数
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/79.0.3945.130 Safari/537.36"}

# 搜索的参数
p = {"wd": "传智播客"}

# 网址
url_temp = 'https://www.baidu.com/s?wd={}'.format("传智播客")

#获取页面
r = requests.get(url_temp, headers=headers)

# 判断是否连接成功
print(r.status_code)
# 打印页面的url地址
print(r.request.url)
