import pandas as pd
import requests

url="https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon"
headers={
    "User-Agent":"Mozilla/5.0"
}
html=requests.get(url,headers=headers).text

tables=pd.read_html(html)

df1=tables[1]

print(df1.head())