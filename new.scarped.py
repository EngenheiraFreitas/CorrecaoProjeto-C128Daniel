import pandas as pd
import time 
from bs4 import BeautifulSoup
from selenium import webdriver

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("D:\Projeto 127\chromedriver_win32")
browser.get(START_URL)

scarped_data = []

def scrape_more_data():
    soup = BeautifulSoup(browser.page_source, "html.parser")

    bright_star_table = soup.find_all("table", attrs={"class", "wikitable"})

    temp_list = []

    table_rows = bright_star_table.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td') 
        temp_list.append(table_cols)
    scarped_data.append(temp_list)
        
stars_data = []

for i in range(0,len(scarped_data)):

    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]

    required_data = [Star_names,Distance,Mass,Radius,Lum]
    stars_data.append(required_data)

headers = ['Star_names','Distance','Mass','Radius','Lum']

star_df_1 = pd.DataFrame(stars_data, columns=headers)

star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")