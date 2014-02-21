def run():
    global soup
    global csvout
    
    ##Putting the games by ID into the Sheet
    gamedates = soup.find_all(id="dojox_grid__View_2")
    gamelist = gamedates[0].find_all("a")
    gameinfo = []
    for game in gamelist:
        gameid = game.get('href')
        gameid = gameid.split("=")
        gameid = gameid[1]
        gameinfo.append((gameid,game.text))

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
    while x <99:
        csvout.writerow((gameinfo[x][0],gameinfo[x][1],playerinfo[x][0],playerinfo[x][1],playerinfo[x][2],playerinfo[x][3],playerinfo[x][4],playerinfo[x][5],playerinfo[x][6],playerinfo[x][7],playerinfo[x][8],playerinfo[x][9],playerinfo[x][10],playerinfo[x][11],playerinfo[x][12],playerinfo[x][13],playerinfo[x][14],playerinfo[x][15]))
        x+=1
