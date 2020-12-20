#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 04:20:00 2018
@author: Degentleman
"""

from urllib.request import urlopen
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


# URL to Format
#url_template = "https://www.pro-football-reference.com/years/{year}/games.htm"

# Iterate Player Data Frame for Each Year Specified

nfl_df = pd.DataFrame()


url = "https://www.pro-football-reference.com/boxscores/"

html = urlopen(url).read()

soup = BeautifulSoup(html)


tagz= soup.findAll('td', {"class": "right gamelink"})
linx=[]
for tag in tagz:
    linxtag=tag.findAll('a')
    linxtag="https://www.pro-football-reference.com" + linxtag[0].attrs['href']
    linx.append(linxtag)

column_headers = ['Player', 'Tm', 'Cmp', 'Att', 'Yds', 'TD', 'Int', 'Sk', 'Yds', 'Lng', 'Rate', 'Att', 'Yds', 'TD', 'Lng', 'Tgt', 'Rec', 'Yds', 'TD', 'Lng', 'Fmb', 'FL']
statdataframe= pd.DataFrame(columns=column_headers)

for a in linx:
    url = a

    html = urlopen(url).read()

    soup = BeautifulSoup(html)
    stattables = soup.findAll('div', {"id": "all_player_offense"})
    # look= soup.findAll('thead')
    headz = stattables[0].findAll('tr')[1]
    column_headers = [th.getText() for th in stattables[0].findAll('tr')[1].findAll('th')]

    data_rows = stattables[0].findAll('tbody', limit=1)[0].findAll('tr', {"class": None})[0:]

    player_data = [[td.getText() for td in data_rows[i].findAll(['th', 'td'])]
                   for i in range(len(data_rows))]
    fakedf=pd.DataFrame(player_data, columns=column_headers)
    statdataframe = pd.concat([statdataframe, fakedf])
print("poopyfarts")

