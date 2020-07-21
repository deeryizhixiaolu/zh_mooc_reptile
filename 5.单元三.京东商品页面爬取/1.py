import requests

url = "http://item.jd.com/2967929.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "cookie": "自己浏览器的信息（要先登入）"
}
r = requests.get(url, headers=headers)  # 因为京东啊，亚马逊都有反爬，所以要加入头部信息
r.raise_for_status()
r.encoding = r.apparent_encoding
print(r.text[:1001])
