"""
Author: Evan Williams
Section Leader: Olivia Flores
Date: Nov 26, 2023
ISTA 350 Final Project

Desc: This file contains the function needed 
      to scrape the NBA 2021 stats per game, 
      the first 350 ranked players
"""

import pandas as pd

def read_file():
    """
    Name: read_file
    Type: Dataframe
    Purpose: Returns the proccesed dataframe for the 
                first 350 ranked NBA players and the 
                specific stats needed

    Parameters: None

    Return: A Dataframe
    """
    
    url = 'https://www.basketball-reference.com/leagues/NBA_2021_per_game.html'
    tables = pd.read_html(url)

    df = tables[0]
    new_df = pd.DataFrame()

    for i in range(0,350):

        if df.iloc[i][1] != 'Player':
            new_df.loc[i, 'Player'] = df.loc[i, 'Player']
            new_df.loc[i, 'Age'] = float(df.loc[i, 'Age'])
            new_df.loc[i, 'ORB'] = float(df.loc[i, 'ORB'])
            new_df.loc[i, 'MP'] = float(df.loc[i, 'MP'])
            new_df.loc[i, 'PTS'] = float(df.loc[i, 'PTS'])
            new_df.loc[i, 'FGA'] = float(df.loc[i, 'FGA'])
            new_df.loc[i, 'FG%'] = float(df.loc[i, 'FG%']) * 100
        else:
            pass

    new_df['FG%'] = new_df['FG%'].fillna(new_df['FG%'].mean()) 

    return new_df