# -*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup

# 获取请求
re = requests.get("https://www.autohome.com.cn/all/")

# 转换编码
re.encoding = "gbk"

# 获取BeautifulSoup解析对象
soup = BeautifulSoup(re.text, "html.parser")

# 指定一个唯一性的id
li_list = soup.find(id="auto-channel-lazyload-article").find_all("li")

# 将所需的标签查找出来
for li in li_list:
    title = li.find("h3")
    if not title:
        continue
    # print(title.text)

    summary = li.find("p")
    # print(summary.text)

    url = li.find("a").get("href")
    img = li.find("img").get("src")
    print(title.text, url, summary, img)

