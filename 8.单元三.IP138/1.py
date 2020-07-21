import requests

text = "202.204.80.112"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
}
url = "https://m.ip138.com/iplookup.asp?ip={}".format(text)
html = requests.get(url, headers=headers)
html.encoding = html.apparent_encoding
print(html.text)
