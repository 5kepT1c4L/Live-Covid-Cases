from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime


def program():

    while 1:

        global now

        website = requests.get("https://www.worldometers.info/coronavirus/").text

        soup = BeautifulSoup(website, 'lxml')

        info_boxes = soup.find_all('div', class_="maincounter-number")

        def print_values():

            global now
            
            now = datetime.now()
            
            print("Updated at: {}".format(now.strftime("%I:%M:%S")))
            
            print("----------------------------------------------------\n")

            print("Current COVID-19 Cases: {}\n".format(info_boxes[0].span.text))

            print("COVID-19 Deaths: {}\n".format(info_boxes[1].span.text))

            print("Patients Recovered: {}\n".format(info_boxes[2].span.text))

            print("<-------------------------------------------------->\n\n")
        
        print_values()

        del info_boxes

        del now

        time.sleep(180)


program()




