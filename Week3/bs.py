from bs4 import BeautifulSoup
import requests
import pandas as pd
r = requests.get("https://bnr.ro/Cursul-de-schimb--7372-Mobile.aspx?pid=7372")
link = BeautifulSoup(r.text, "html.parser")
# print(link)
header = []
dataset = []
title = link.findAll('div', attrs={'class': 'contentDiv'})
for i in title:
    for tr_index in i.find_all('table'):
        for td_index in tr_index.find_all('tr'):
            td_list = []
            if td_index.find_all('th'):
                # print(td_index.find_all('th'))
                # for th_index in td_index.find_all('th'):
                # print(th_index.get_text())
                header = [th_index.get_text() for th_index in td_index.find_all('th')]
            for index, td_value in enumerate(td_index.find_all('td')):
                #print(index, td_value)
                if index == 0:
                    td_list.append(td_value.get_text())
                else:
                    td_list.append(float(td_value.get_text().replace(',', '.')))
            dataset.append(td_list)

print(header)
df=pd.DataFrame(dataset,columns=header)
df.to_csv("CursBnr.csv",header=header)
