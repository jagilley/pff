

from urllib.request import urlopen
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


# URL to Format
#url_template = "https://www.pro-football-reference.com/years/{year}/games.htm"

# Iterate Player Data Frame for Each Year Specified
def getoffensedata(player):
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

    column_headers = ['Player', 'Tm', 'Cmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'SkYds', 'PassLng', 'Rate', 'RushAtt', 'RushYds', 'RushTD', 'RushLng', 'Tgt', 'Rec', 'RecYds', 'RecTD', 'RecLng', 'Fmb', 'FL']
    statdataframe= pd.DataFrame(columns=column_headers)

    for a in linx:
        url = a

        html = urlopen(url).read()

        soup = BeautifulSoup(html)
        stattables = soup.findAll('div', {"id": "all_player_offense"})
        if not stattables:
            return statdataframe

        # look= soup.findAll('thead')
        headz = stattables[0].findAll('tr')[1]
        #column_headers = [th.getText() for th in stattables[0].findAll('tr')[1].findAll('th')]

        data_rows = stattables[0].findAll('tbody', limit=1)[0].findAll('tr', {"class": None})[0:]

        player_data = [[td.getText() for td in data_rows[i].findAll(['th', 'td'])]
                       for i in range(len(data_rows))]
        fakedf=pd.DataFrame(player_data, columns=column_headers)
        statdataframe = pd.concat([statdataframe, fakedf])
    retval= statdataframe[statdataframe['Player'].str.contains(player)]
    return retval


def getoffensedata_week(player, week):
    nfl_df = pd.DataFrame()


    url = "https://www.pro-football-reference.com/years/2020/week_" + week + ".htm"

    html = urlopen(url).read()

    soup = BeautifulSoup(html)


    tagz= soup.findAll('td', {"class": "right gamelink"})
    linx=[]
    for tag in tagz:
        linxtag=tag.findAll('a')
        linxtag="https://www.pro-football-reference.com" + linxtag[0].attrs['href']
        linx.append(linxtag)

    column_headers = ['Player', 'Tm', 'Cmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'SkYds', 'PassLng', 'Rate', 'RushAtt', 'RushYds', 'RushTD', 'RushLng', 'Tgt', 'Rec', 'RecYds', 'RecTD', 'RecLng', 'Fmb', 'FL']
    statdataframe= pd.DataFrame(columns=column_headers)

    for a in linx:
        url = a

        html = urlopen(url).read()

        soup = BeautifulSoup(html)
        stattables = soup.findAll('div', {"id": "all_player_offense"})
        if not stattables:
            return statdataframe

        # look= soup.findAll('thead')
        headz = stattables[0].findAll('tr')[1]
        #column_headers = [th.getText() for th in stattables[0].findAll('tr')[1].findAll('th')]

        data_rows = stattables[0].findAll('tbody', limit=1)[0].findAll('tr', {"class": None})[0:]

        player_data = [[td.getText() for td in data_rows[i].findAll(['th', 'td'])]
                       for i in range(len(data_rows))]
        fakedf=pd.DataFrame(player_data, columns=column_headers)
        statdataframe = pd.concat([statdataframe, fakedf])
    retval= statdataframe[statdataframe['Player'].str.contains(player)]
    return retval


