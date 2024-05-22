"""
Author: Evan Williams
Section Leader: Olivia Flores
Date: Nov 26, 2023
ISTA 350 Final Project

Desc: This file contains the function needed 
      to produce image1 of my final project
"""

from read_file import *
import matplotlib.pyplot as plt, numpy as np

def make_plot(df):
    """
    Name: make_plot
    Type: Void
    Purpose: Creates the plot for image1, which is a scatter 
             plot using Minutes played and points per game 
             as data

    Parameters: df - The dataframe of NBA player data

    Return: None
    """

    x = 'MP'
    y = 'PTS'
    df.plot.scatter(x=x, y=y, c='maroon')

    #### Misc changes to plot ####
    ax = plt.gca()
    fig = plt.gcf()

    # Line of Regression
    m, b = np.polyfit(list(df[x]), list(df[y]), 1)
    ax.plot(list(df[x]), m*df[x]+b)

    # Colors and Font Sizes
    ax.spines['bottom'].set_color('red')
    ax.spines['top'].set_color('red')
    ax.spines['right'].set_color('red')
    ax.spines['left'].set_color('red')
    ax.set_facecolor("gainsboro")
    fig.patch.set_facecolor("darkgrey")
    plt.xticks(fontsize=14, rotation='horizontal', color='mediumblue')
    plt.yticks(fontsize=14, color='mediumblue')
    plt.ylabel('Points Per Game (PTS)', fontsize=18, color='mediumblue')
    plt.xlabel('Minutes Per Game (MP)', fontsize=18, color='mediumblue')
    plt.title('Correlation between Minutes per game and Points per game', fontsize=18, color='mediumblue')


def main():
    """
    Name: main
    Type: Void
    Description: This function uses read_file 
                 to get the data and makes the 
                 first image with it.

    :return: Nothing
    """

    df = read_file()

    make_plot(df)

    plt.show()

main()