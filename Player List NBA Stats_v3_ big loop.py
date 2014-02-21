from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
from string import *
import csv
import sys
from bs4 import BeautifulSoup as Soup
import time
import datetime
import os

starttime = time.time()
#Defining the 'GetStats' Function
def getstats():
    gamedates = soup.find_all(id="dojox_grid__View_2")
    gamelist = gamedates[0].find_all("a")
    gameinfo = []
    for game in gamelist:
        gameid = game.get('href')
        gameid = gameid.split("=")
        gameid = gameid[1]
        gamedate = game.text.split('-')[0].rstrip()
        teams = game.text.split('-')[1].lstrip()
        tm = teams.split(" ")[0]
        opp = teams.split(" ")[2]
        if teams.split(" ")[1] =='@':
            home = 'Away'
        else:
            home = 'Home'
        gameinfo.append((gameid,gamedate,tm,opp,home))

    playerstats = soup.find_all(id="dojox_grid__View_3")
    gamelogs = playerstats[0].find_all("table")
    playerinfo=[]
    for game in gamelogs:
        stats = game.find_all('td')
        winloss = stats[0].text
        minutes = stats[1].text
        fgm = stats[2].text
        fga = stats[3].text
        fgpercent = stats[4].text
        threefgm = stats[5].text
        threefga = stats[6].text
        threefgpercent = stats[7].text
        ftm = stats[8].text
        fta = stats[9].text
        ftpercent = stats[10].text
        oreb = stats[11].text
        dreb = stats[12].text
        reb = stats[13].text
        ast = stats[14].text
        stl = stats[15].text
        blk = stats[16].text
        turnover = stats[17].text
        pfouls = stats[18].text
        points  = stats[19].text
        plusminus = stats[20].text
        playerinfo.append((winloss,minutes,fgm,fga,threefgm,threefga,ftm,fta,oreb,dreb,ast,stl,blk,turnover,pfouls,points))

    x=0
    while x <len(playerinfo):
        csvout.writerow((pid,pname,gameinfo[x][0],gameinfo[x][1],gameinfo[x][2],gameinfo[x][3],gameinfo[x][4],playerinfo[x][0],playerinfo[x][1],playerinfo[x][2],playerinfo[x][3],playerinfo[x][4],playerinfo[x][5],playerinfo[x][6],playerinfo[x][7],playerinfo[x][8],playerinfo[x][9],playerinfo[x][10],playerinfo[x][11],playerinfo[x][12],playerinfo[x][13],playerinfo[x][14],playerinfo[x][15]))
        x+=1


#Collect Link List for all players

"""This section starts by going to the player list on NBA.com. It selects all historical players, creates separate lists of both IDs and Names. Onces it's completed the list, it merges the two list into a dictionary, removing any duplicates that may exist"""
first_url = "http://stats.nba.com/players.html"
driver = webdriver.Chrome()
page = driver.get(first_url)
driver.find_element_by_link_text("All Historical Players").click()
time.sleep(5)
soup = Soup(driver.page_source)
LinkList = soup.find_all("a", class_="playerlink")
EndofLoop = len(LinkList)

playerlist=[]
playerid=[]

for link in LinkList[0:EndofLoop]:
    playerlist.append(link.text)
    linkname=link.get('href')
    splitlink=linkname.split("=")
    playerid.append(splitlink[1])

playerdict = dict(zip(playerid,playerlist))

#Start Cycle through all Players

"""Creates a unique CSV file for each player in the dictionary created in the previous step. Identifies the total number of games each person has played. Loops through all the games played by that player, running the GetStats function on each page"""
for pid,pname in playerdict.items():
    base_url = "http://stats.nba.com/playerGameLogs.html?PlayerID="+pid+"&rowsPerPage=100&pageNo=1"
    filename = time.strftime(pname+"-"+pid+"%m" "-" "%m" "-" "%Y" +".csv")
    f = open("B:\\Dropbox\\NBAStats\\"+filename, "wb")
    csvout = csv.writer(f)
    csvout.writerow(("PlayerID", "PlayerName","GameID", "Date","Team","Opponent","Home/Away", 'winloss','minutes','fgm','fga','threefgm','threefga','ftm','fta','oreb','dreb','ast','stl','blk','turnover','pfouls','points'))
    page = driver.get(base_url)

    time.sleep(10)

    soup = Soup(driver.page_source)

    limit = soup.find(class_="dojoxGridDescription")
    try:
        limit = limit.text.split(" ")[4]
        limit = int(limit)
        if limit%100 >0:
            limit = limit/100 + 1
        else:
                limit = limit/100
    except AttributeError:
            limit = 1

    getstats()


    looping = 2
    while looping <= limit:
        new_url = "http://stats.nba.com/playerGameLogs.html?PlayerID="+pid+"&rowsPerPage=100&pageNo=" + str(looping)
        page = driver.get(new_url)
        time.sleep(5)
        soup = Soup(driver.page_source)
        getstats() 
        looping+=1

    f.close()

driver.close()

print time.time() - starttime, "seconds"
