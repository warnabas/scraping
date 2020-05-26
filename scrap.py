import requests
from lxml import etree
import lxml.html
import csv

def parse(url):
	name_of_csv = url.split('/')[-1].split('.')[0]
	try:
		api = requests.get(url)
	except:
		return
	tree = lxml.html.document_fromstring(api.text)
	text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
	text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
	print(text_original, text_translate)
	with open(f"{name_of_csv}.csv", 'w', newline='') as file:
		write = csv.writer(file)
		for i in range(len(text_original)):
			write.writerow(text_original[i])
			write.writerow(text_translate[i])

def main():
	parse("https://www.amalgama-lab.com/songs/t/tones_and_i/dance_monkey.html")

if __name__ == '__main__':
	main()