from numpy.core.defchararray import isdigit
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# import time

browser = webdriver.Chrome(ChromeDriverManager().install())


def contains_digits(temp):
    for ch in temp:
        if isdigit(ch):
            return True
    return False


dict = {}
initialised_dict = False
for day in range(20, 28):
    # if day == 21:
    #     break
    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-ianuarie-ora-13-00/")
    # table = browser.find_element(by=By.CLASS_NAME, value='//*[@class="entry-content"]')
    table = browser.find_element(by=By.XPATH, value="//table")

    list = table.text.split('\n')
    list = list[1:43]

    header_len = 5

    # print(len(list[0]))

    csv_list = []
    for string in list:
        separated = string.split(' ')
        # print(separated)
        # aux = []
        # aux.append(separated[0])
        # city = ""
        # idx = 1
        # num = ""
        # while True:
        #     try:
        #         num = int(separated[idx])
        #         break
        #     except:
        #         city += num
        #         idx = idx + 1
        # aux.append(city)
        # aux.append(num)
        # aux.append(separated[3:5])
        aux = []
        aux.append(separated[0])
        idx = 1
        city = ""
        while not (contains_digits(separated[idx])):
            city += separated[idx]
            idx = idx + 1

        aux.append(city)
        mylen = len(separated)
        for index in range(idx, len(separated)):
            aux.append(separated[index])

        csv_list.append(aux)

    # print(csv_list)

    headers = []
    for i in range(5):
        header_title = browser.find_element(by=By.XPATH, value=f'//table//td[{i + 1}]').text
        headers.append(header_title)

    if initialised_dict == False:
        initialised_dict = True
        dict = {i: [] for i in headers}

    for string in csv_list:
        for index in range(len(headers)):
            # print(len(headers))
            # print(len(string))
            dict[headers[index]].append(string[index])

    # print(dict)

df = pd.DataFrame(dict)
df.to_csv('ALL_DATA_GOV.csv')
browser.close()
