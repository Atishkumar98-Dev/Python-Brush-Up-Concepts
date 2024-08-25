import requests
from bs4 import BeautifulSoup

page = requests.get('https://mausam.imd.gov.in/')
soup = BeautifulSoup(page.content,'html.parser')
print(soup)