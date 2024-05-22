"""
Author: Evan Williams
Section Leader: Olivia Flores
Date: Nov 26, 2023
ISTA 350 Final Project

Desc: This file contains the function needed 
      to produce image3 of my final project
"""

from read_file import *
import matplotlib.pyplot as plt

def make_plot(df):
    """
    Name: make_plot
    Type: Void
    Purpose: Creates the plot for image2, 
             which is a histogram using Age 
             and offensive rebounds as data.

    Parameters: df - The dataframe of NBA player data

    Return: None
    """

    x = 'Age'
    y = 'ORB'
    fig = plt.figure(figsize= (13,9))
    plt.hist(list(df[x]), color='maroon', rwidth=0.8)

    #### Misc changes to plot ####
    ax = plt.gca()
    
    # Colors and Font Sizes
    ax.spines['bottom'].set_color('red')
    ax.spines['top'].set_color('red')
    ax.spines['right'].set_color('red')
    ax.spines['left'].set_color('red')
    ax.set_facecolor("gainsboro")
    fig.patch.set_facecolor("darkgray")
    plt.xticks(fontsize=14, rotation='horizontal', color='mediumblue')
    plt.yticks(fontsize=14, color='mediumblue')
    plt.ylabel('Offensive Rebounds Per Game (ORB)', fontsize=18, color='mediumblue')
    plt.xlabel('Age (Years)', fontsize=18, color='mediumblue')
    plt.title('Correlation between Age and Offensive Rebounds', fontsize=18, color='mediumblue')

def main():
    """
    Name: main
    Type: Void
    Description: This function uses read_file 
                 to get the data and makes the 
                 third image with it.

    :return: Nothing
    """

    df = read_file()

    make_plot(df)

    plt.show()

main()