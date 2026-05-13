import requests

url='https://WWW.ibm.com/'
r=requests.get(url)
print(r.status_code)
#print(r.request.headers)
#print(r.request.body)
header=r.request.headers
print(header['User-Agent'])