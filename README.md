NBAStats
===

This is a Python module I have put together to make it easier and faster to parse NBA statistics. 

version 1.0.1

My apologies for the lack of documentation within the package and on here.  That will be coming quickly.

To get started, install the module using the following:
```$ easy_install nbastats```
or 
```$ pip install nbastats```

*This module requires the most recent versions of `pandas` and `requests`.*

Once you have `NBAStats` installed, load it into your python environment using:

```python

import nbastats.nbastats as nbastats
```

Once you have the package imported, you can use the following commands to collect data:

##Shot Chart Data

If you wish to see detailed information on a single players shot chart, use the `ShotChart` method. To use this method, you first need the unique id number of the player you are interested in. You can obtain this by finding the player's profile page on `http://stats.nba.com` and looking in the address bar. You may have to click the "stats" tab when you find the players page. For this example, I'll use Paul George. His NBA ID is `202331`.
```python
george = nbastats.ShotChart('202331')
george.shotchart().head(2)
```
This code returns the following pandas dataframe: 

| index | GRID_TYPE	| GAME_ID | GAME_EVENT_ID | PLAYER_ID | PLAYER_NAME | TEAM_ID | TEAM_NAME | PERIOD | MINUTES_REMAINING | SECONDS_REMAINING | EVENT_TYPE | ACTION_TYPE | SHOT_TYPE | SHOT_ZONE_BASIC | SHOT_ZONE_AREA | SHOT_ZONE_RANGE | SHOT_DISTANCE | LOC_X | LOC_Y | SHOT_ATTEMPTED_FLAG | SHOT_MADE_FLAG |
| :----: | ---- | ---- | :----: | :----: | :----: | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0	| Shot Chart Detail	| 0021300001 | 5 |  202331 | Paul George | 1610612754 | Indiana Pacers | 1 | 11 | 30 | Made Shot | Pullup Jump shot | 2PT Field Goal | Mid-Range | Right Side Center(RC) | 16-24 ft. | 19 | 105 | 164 | 1 | 1 |
| 1	  | Shot Chart Detail | 0021300001 | 16 | 202331 | Paul George | 1610612754 | Indiana Pacers	| 1	| 10 | 11 | Made Shot | Layup Shot | 2PT Field Goal | Restricted Area | Center(C) | Less Than 8 ft. | 1 | -10 | 3 | 1 | 1 |

There are a couple things to note. First, invoking `nbastats.ShotChart('202331')` creates an object that has to unique methods. each of these returns specific data in a `Pandas` dataframe. You can manipulate and adjust all of the data just as you would with a normal `Pandas` dataframe.

###Methods

####`.shotchart()`
This method of the returns detailed information about all of a players shots that you have chosen. The table above is an example of the type of data that this method returns.

####`.leagueaverage()`
This method returns a table with league averages for shots taken and made from each of the identified zones on the court. This is not player specific information. It is league specific. If you invoke this method for different players during the same time period, the results should be identical.

###Customization
There are quite a few ways to customize the actual data that is collected from the website by adjusting the current code. Each of the potential changes are described below. Some variables have a discrete number of options. The options are listed underneath their respective variables. Default values are in **bold**.

* `playerid` - no default value; Required
* `leagueid`
	* **00**
	* 20
* `season` - Input in format of 20XX-XX
	* **2013-14**
* `seasontype`
	* **Regular Season**
	* Playoffs
	* All Star
* `teamid` - Only useful if a player played on more than one team during a season. Allows you to pull all of the shots taken during a specific season while playing for a specific team. 
	* **blank**
* `gameid` - Used to select shots taken during a specific game
	* **blank**
* `outcome` - Selects shot taken during games with a specific outcome. 
	* W
	* L
	* **blank**
* `location` - Selects shots taken during games played at different locations
	* Home
	* Road
	* **blank**
* `month` - Selects shots taken during a specific month. 
	* **0** (all months)
* `seasonsegment` - Selects shots taken during a segment of the season
	* Post All-Star
	* Pre All-Star
	* **blank**
* `datefrom` - Selects shots taken after a specific date; 2004-01-01 format
	* **blank**
* `dateto` - Selects shots taken before a specific date; 2004-01-01 format
	* **blank**
* `opponentteamid` - Selects shots taken against a specific team
	* **blank**
* `vsconf` - Selects shots taken against a specific conference
	* East
	* West
	* **blank**
* `vsdiv` - Selects shots taken against a specific division
	* Atlantic
	* Central
	* Northwest
	* Pacific
	* Southeast
	* Southwest
	* East
	* West
	* **blank**
* `position` - Selects shots taken when labeled as specific position; not useful
	* Guard
	* Center
	* Forward
	* **blank**
* `gamesegment` - Selects shots taken during a specific segment of a game
	* First Half
	* Overtime
	* Second Half
	* **blank**
* `period` - Selects shots taken during specific periods of games
	* **0** returns all shots
	* Takes values 0-9
* `lastngames` - Selects shots taken during past N games; Will not aggregate across seasons
	* **0** returns all games
* `aheadbehind` - Selects shots taken during specific situations in a game
	* Ahead or Behind
	* Ahead or Tied
	* Behind or Tied
	* **blank**
* `contextmeasure` - Description
	* FGM
	* FGA
	* FG_PCT
	* FG3M
	* FG3A
	* FG3_PCT
	* PF
	* EFG_PCT
	* TS_PCT
	* PTS_FB
	* PTS_OFF_TOV
	* PTS_2ND_CHANCE
	* **blank**
* `clutchtime` - Selects shots taken during specific "clutch" times during a game
	* Last 5 Minutes
	* Last 4 Minutes
	* Last 3 Minutes
	* Last 2 Minutes
	* Last 1 Minute
	* Last 30 Seconds
	* Last 10 Seconds
	* **blank**


When you adjust these values, be sure the selected value is included as a string. For example, to select all of Paul George's shots taken during the last minute of every game he played during the 2012-13 season, you would run the following code:
```python
george = nbastats.ShotChart('202331', season='2012-13', clutchtime='Last 1 Minute')
george.shotchart()
```
***
##BoxScore Data
***
##Player Game Logs
***
##Play By Play Data
***
##Lineup Data
