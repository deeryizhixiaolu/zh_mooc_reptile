import requests

r = requests.get("https://www.baidu.com/")
print(r.status_code)
type(r)
print(r.headers)
r.encoding = r.apparent_encoding
print(r.text)
