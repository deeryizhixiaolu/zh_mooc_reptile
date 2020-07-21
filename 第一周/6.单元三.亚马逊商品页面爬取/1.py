import requests

# 带上浏览器信息


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "Cookie": "你浏览器的信息"}
r = requests.get("https://www.amazon.cn/gp/product/B01M8L5Z3Y", headers=headers)
r.encoding = r.apparent_encoding
print(r.status_code)
print(r.text)
