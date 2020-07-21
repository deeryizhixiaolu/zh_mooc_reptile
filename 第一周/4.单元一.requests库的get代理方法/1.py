import requests

# 使用代理网站的IP地址
# https://www.kuaidaili.com/free/
# pxs = {"http": "http://user:pass@10.10.10.1:1234",
#        "https": "https://10.10.10.1:4321"}

pxs = {
    "http": "120.83.101.166:9999"
}

r = requests.request("GET", "https://www.baidu.com", proxies=pxs)
print(r.text)
