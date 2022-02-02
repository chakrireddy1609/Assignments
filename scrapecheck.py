import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.saucedemo.com/")
soup = BeautifulSoup(response.content,'html.parser')
count = soup.find_all('li',{'class':'feature'})
title = count[0].find('span',{'class':'title'}).get_text()

for i in range(len(count)):
    print(count[i].find('span',{'class':'title'}).get_text())

