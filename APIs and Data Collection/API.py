import requests

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}

r=requests.get(url_get,params=payload)

print(r.status_code)
print(r.text)
print(r.json)