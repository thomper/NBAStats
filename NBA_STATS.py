from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
from string import *
import csv
import sys
from bs4 import BeautifulSoup as Soup

import xml.etree.ElementTree as ET

#f = open("PlayerListNBAdotcom.csv", "wb")
#csvout = csv.writer(f)
#csvout.writerow(("A", "B", "C", "D"))
base_url = "http://stats.nba.com/players.html"
driver = webdriver.Chrome()
page = driver.get(base_url)
driver.find_element_by_link_text("All Historical Players").click()


sourcecode = driver.page_source

text = open("sourcecode.txt", "w")
text.write(sourcecode)
text.close()

##sys.setrecursionlimit(5500)

##parse = ET.fromstring(driver.page_source)
##for link in parse.iter('href'):
##     csvout.writerow(link.find(".//href[@class_='playerlink']"))

####soup = Soup(driver.page_source)
####LinkList = soup.find_all("a", class_="playerlink")
##
######    print RowEntry
####
####for x in LinkList:
####     csvout.writerow(x.string)
##
##
##
##csvout.writerow((Team,Conference,GamesPlayed,PointsPerGame,FieldGoalsMade,FieldGoalsAttempted,FieldGoalPercentage,FreeThrowsMade,FreeThrowsAtetempted,FreeThrowPercentage,ThreePointersMade,ThreePointersAttempted,ThreePointerPercentage))




#f.close()

#import datetime
#import os
#import time
#os.rename("PlayerListNBAdotcom.csv", time.strftime("PlayerListNBAdotcom " "%m" "-" "%d" "-" "%Y" +".csv"))

