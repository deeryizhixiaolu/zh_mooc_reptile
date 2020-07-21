import requests

payload = {"key1": "value1", "key2": "value2"}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

r1 = requests.post("http://httpbin.org/post", data="ABC")
print(r1.text)
