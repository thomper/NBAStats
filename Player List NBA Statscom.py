from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
from string import *
import csv
import sys
from bs4 import BeautifulSoup as Soup

f = open("PlayerListNBAdotcom.csv", "wb")
csvout = csv.writer(f)
csvout.writerow(("A", "B", "C", "D"))
base_url = "http://stats.nba.com/players.html"
driver = webdriver.Chrome()
page = driver.get(base_url)
driver.find_element_by_link_text("All Historical Players").click()


soup = Soup(driver.page_source)
LinkList = soup.find_all("a", class_="playerlink")
EndofLoop = len(LinkList)

player=[]
playerid=[]

for link in LinkList[0:EndofLoop]:
    linktext=link.text
    linkname=link.get('href')
    player.append(linktext)
    playerid.append(linkname)
    csvout.writerow((linktext,linkname))


playergamelog=[]
for x in playerid:
    link 



   
driver.quit()

f.close()

import datetime
import os
import time
os.rename("PlayerListNBAdotcom.csv", time.strftime("PlayerListNBAdotcom " "%m" "-" "%d" "-" "%Y" +".csv"))

