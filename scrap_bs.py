import requests
from bs4 import BeautifulSoup as BS

#s = requests.Session()
#get CSRF
#auth_html = s.get(url)
#auth_bs = BS(auth_html.content, 'html.parser')
#csrf = auth_bs.select('input[name=YII_CSRF_TOKEN]')[0]['value']
#print(csrf)
#затем  делаем пост запрос через answer = s.post('url-login', data={тут словарь требуемый от пользователя})
#ans_bs = BS(answer.content, 'html.parser')

url = #название
r = requests.get(url)
html = BS(r.content, 'html.parser')

for element in html.select('.lent-block'): #заходим в нужный блок
	title = element.select('.lent-title > a') #выбираем все нужные тэги
	print(title[0].text)