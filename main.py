from bs4 import BeautifulSoup
import requests

website = requests.get("https://www.worldometers.info/coronavirus/").text

soup = BeautifulSoup(website, 'lxml')

info_boxes = soup.find_all('div', class_="maincounter-number")

for info in info_boxes:

    print(info.span.text)




