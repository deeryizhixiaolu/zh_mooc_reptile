import requests
# 带上浏览器信息
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
r = requests.get("https://item.jd.com/2967929.html", headers=headers)
print(r.status_code)
print(r.text)
