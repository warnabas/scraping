import requests
from bs4 import BeautifulSoup as BS

url = 'https://stopgame.ru/review/new/stopchoice'
r = requests.get(url)
html = BS(r.content, 'html.parser')

for element in html.select('.lent-block'): #заходим в нужный блок
	title = element.select('.lent-title > a') #выбираем все нужные тэги
	print(title[0].text)