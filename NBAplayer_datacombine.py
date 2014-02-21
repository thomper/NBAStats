import csv
from string import *
import time
import sys

##Begin Aggregate Data
infile = open('B:\\Desktop\\NBA_PLAYERS.txt','r')
players = []
for line in infile:
    players.append(line.strip())
del infile

aggdatfile = open('B:\\Dropbox\\NBAStats\\_AggregatePlayerData.csv','wb')
csvout = csv.writer(aggdatfile)
csvout.writerow(("PlayerID", "PlayerName","GameID", "Date","Team","Opponent","Home/Away", 'winloss','minutes','fgm','fga','threefgm','threefga','ftm','fta','oreb','dreb','ast','stl','blk','turnover','pfouls','points'))

for player in players:
    datfile = open('B:\\Dropbox\\NBAStats\\'+player,'r')
    dump = datfile.readline().strip()
    for line in datfile:
        aggdatfile.write(line)


##Begin create list of games
import pandas
alldata = pandas.read_csv('B:\\Dropbox\\NBAStats\\AggregatePlayerData.csv')
games = alldata['GameID']
games = set(games)


##Loading data into Pandas for analysis
import pandas as pd
playerdat = pd.read_csv('B:\\Dropbox\\NBAStats\\AggregatePlayerData.csv') ##Opens CSV File
playerdat.Date = numpy.datetime64(playerdat.Date) ##Converts String Date into datetime object

