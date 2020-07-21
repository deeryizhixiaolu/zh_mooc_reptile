import requests

url = "http://www.amazon.cn/gp/product/B01M8L5Z3Y"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "cookie": "自己浏览器的信息（要先登入）"
}
r = requests.get(url, headers=headers)
r.raise_for_status()
r.encoding = r.apparent_encoding
print(r.text[1000:20001])
