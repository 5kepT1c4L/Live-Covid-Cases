from bs4 import BeautifulSoup
import requests
import time

def program():

    while 1:

        website = requests.get("https://www.worldometers.info/coronavirus/").text

        soup = BeautifulSoup(website, 'lxml')

        info_boxes = soup.find_all('div', class_="maincounter-number")

        def print_values():

            epoch_time = 1631673866

            local_time = time.ctime(epoch_time)

            print("Updated at: {}".format(local_time))
            
            print("----------------------------------------------------\n")

            print("Current COVID-19 Cases: {}\n".format(info_boxes[0].span.text))

            print("COVID-19 Deaths: {}\n".format(info_boxes[1].span.text))

            print("Patients Recovered: {}\n".format(info_boxes[2].span.text))

            print("<-------------------------------------------------->\n\n")
        
        print_values()

        time.sleep(180)


program()




