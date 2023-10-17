#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:48:28 2023

@author: nickzhou
"""
import pandas as pd
import VideoGame as vg 


game_data = pd.read_csv("/Users/nickzhou/Downloads/Video_Games.csv") 

def millionaire_games():
    return game_data[game_data['Global_Sales'] > 1]

def multimillionaire_games():
    return game_data[game_data['Global_Sales'] > 10]

def top_100_sales_all_time():
    return vg.find_first_n(game_data, 'Global_Sales', 100, False)

def recent_games():
    return game_data[game_data['Year_of_Release'] >= 2010]

def very_recent_games():
    return game_data[game_data['Year_of_Release'] >= 2016]

def  top_100_recent_games():
    return vg.find_first_n(game_data[game_data['Year_of_Release'] >= 2010],
                                        'Global_Sales', 100, False)


def prolific_publishers_all_time(threshold):
    return 


    
    