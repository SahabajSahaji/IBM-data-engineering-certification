from bs4 import BeautifulSoup
import requests

#Specify the URL of the webpage you want to scrape

url='https://en.wikipedia.org/wiki/IBM'

# Add headers with User-Agent
headers={
    "User-Agent":"Mozilla/5.0"
}
#Send an HTTP GET request to the webpage
response=requests.get(url,headers=headers)

#Store teh HTML content in a variable
html_content=response.text

#Create a BeautifulSoup object to parse the HTML
soup=BeautifulSoup(html_content,'html.parser')

#Display a snippet of the HTML content
print(html_content[:500])