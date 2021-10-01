import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

f=open("Result_data.csv","w",newline="")
obj=csv.writer(f)

browser=webdriver.Chrome('C:/Users/<name>/Downloads/chromedriver.exe')
browser.get('https://www.linkedin.com/uas/login')
uname=""
password=""
eid=browser.find_element_by_id('username')
eid.send_keys(uname)
eid=browser.find_element_by_id('password')
eid.send_keys(password)
eid.submit()



for pages in range(1,101):

    link="https://www.linkedin.com/search/results/people/?keywords=institute%20of%20engineering%20and%20management&origin=FACETED_SEARCH&page="+str(pages)+"&schoolFilter=%5B%2241153%22%5D"

    browser.get(link)
    src=browser.page_source

    soup=BeautifulSoup(src,"html.parser")

    block=soup.findAll('div',{'class':'entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light'})

    for divs in block:
        val1=divs.find('span',{"aria-hidden":"true"})
        #print(divs.find('span',{"aria-hidden":"true"}).text)
        #print(divs.find('div',{'class','entity-result__primary-subtitle t-14 t-black'}).text[1:])
        if val1:
            name=((val1.text).encode("ascii","ignore")).decode()
        else:
            name="None"

        val2=divs.find('div',{'class','entity-result__primary-subtitle t-14 t-black'})
        #print(val1.text,val2.text)
        if val2:
            occ=((val2.text[1:-1]).encode("ascii","ignore")).decode()
        else:
            occ="None"

            
        obj.writerow([name,occ])
	


f.close()
