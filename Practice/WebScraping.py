import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://pokemondb.net/type"

headers={
    "User-Agent":"Mozilla/5.0"
}
response=requests.get(url,headers=headers)
#print(response.text)
html_content=response.text
soup=BeautifulSoup(html_content,'html.parser')

tables=soup.find_all('table')
rows=tables[0].find_all('tr')

for row in rows:
    cols=row.find_all('td')

    if (cols!=0):
        data_dict={"col1":cols[1].contents,
               "col2":cols[2].contents,
               "col2":cols[3].contents}
        df1=pd.DataFrame(data_dict,index=0)
        df=pd.concat([df,df1],ignore_index=True)
    

print(df)