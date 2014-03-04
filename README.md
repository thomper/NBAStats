NBAStats
===

This is a series of Python scripts I have put together to collect individual player data from the NBA. The scripts are set to collect and save the data to a series of `.csv` files.

Update:

Finished version 1.0.0 of package and uploaded to pypi.python.org. My apologies for the lack of documentation within the package and on here.  That will be coming quickly.

To get started:
`easy_install nbastats`
or 
`pip install nbastats`

*This should install `pandas` and `requests` dependencies if you don't already have them or have not updated to the most recent version*

Once you have it installed, use:

`import nbastats.nbastats as nbastats`

Once you have the package imported, it has the following modules:

`ShotChart`

`BoxScore`

`GameLog`

`PlayByPlay`

`Lineups`
