#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:32:15 2023

@author: nickzhou
"""

import VideoGame as vg
import pandas as pd

game_data = pd.read_csv("/Users/nickzhou/Downloads/Video_Games.csv") 


global_sales = game_data['Global_Sales']
na_sales = game_data['NA_Sales']

#games that have sold over $1M worldwide 
millionaire_games = game_data[game_data['Global_Sales'] > 1]
multimillionaire_games = game_data[game_data['Global_Sales'] > 10]

top_100_sales = vg.find_first_n(game_data, 'Global_Sales', 100, False)
totals = vg.total_by_category(top_100_sales, 'Publisher')

print(totals)

print(game_data.sort_values('Year_of_Release', ascending = False)['Year_of_Release'])

recent_games = game_data[game_data['Year_of_Release'] >= 2016]
print(recent_games.sort_values('Global_Sales', ascending = False))

#vg.advanced_pyChart(vg.total_by_category(recent_games, 'Publisher'))

#print(vg.find_first_n(game_data, game_data.columns, 'Year_of_Release', 100, False))

recent_games_top_sales = recent_games.sort_values('Global_Sales', ascending = False)
recent_games_top_sales = vg.find_first_n(recent_games_top_sales, 
                                         'Global_Sales', 100, False)

games_since_2010 = game_data[game_data['Year_of_Release'] >= 2010]

"""
#recent games by publisher 
vg.advanced_pyChart(vg.total_by_category(recent_games_top_sales, 'Publisher'), 
                    '100 Best Selling Games Past 2016', 'Publisher')

#recent games by genre 
vg.advanced_pyChart(vg.total_by_category(recent_games_top_sales, 'Genre'), 
                    '100 Best Selling Games Past 2016 by Genre', 'Genres')
latest_year = 2020
earliest_year = 1980

vg.get_trend(game_data, 'Genre', 1980, 2016, 'Global_Sales', 0.2, 'Genre Popularity Over Time')
"""
vg.get_trend(game_data, 'Genre', 2010, 2016, 'Global_Sales', 0.2, 'Recent Genre Popularity')

top_100_recent_games = vg.find_first_n(game_data[game_data['Year_of_Release'] >= 2010],
                                    'Global_Sales', 100, False)

vg.advanced_pyChart(vg.total_by_category(top_100_recent_games, 'Publisher'), 
                    'Top Games Since 2010 by Publisher', 'Publisher')

games_since_2010.dropna(how = 'all')

print(vg.find_first_n(game_data, 'User_Count', 100, False))

vg.basic_scatterplot(game_data.dropna(subset = ['User_Count', 'Global_Sales'])[['User_Count']], 
                     game_data.dropna(subset = ['User_Count', 'Global_Sales'])[['Global_Sales']])

#interstingly, no correlation between user count and global sales 


all_publishers = vg.total_by_category(game_data, 'Publisher')
all_publishers_2010 = vg.total_by_category(game_data[game_data['Year_of_Release'] >=2010], 
                                           'Publisher')


prolific_publishers = {}
prolific_publishers_2010 = {}
for i in all_publishers.keys():
    if all_publishers[i] > 400:
        prolific_publishers[i] = all_publishers[i]

for i in all_publishers_2010.keys():
    if all_publishers_2010[i] > 100:
        prolific_publishers_2010[i] = all_publishers_2010[i]
        
print(prolific_publishers_2010.keys())

        
vg.total_by_category(game_data[game_data['Year_of_Release'] >= 2010], 'Publisher')

prolific_pubs_data = vg.get_by_group(game_data, 
                                     'Publisher', 
                                     list(prolific_publishers.keys()))

prolific_pubs_data_2010 = vg.get_by_group(game_data[game_data['Year_of_Release'] >=2010],
                                          'Publisher', 
                                          list(prolific_publishers_2010.keys()))




from statsmodels.formula.api import ols 

fit = ols('Global_Sales ~ C(Publisher) + C(Genre) + Critic_Score',
          data = prolific_pubs_data.dropna(subset = ['Publisher', 'Genre', 'Rating', 'Global_Sales'])).fit()
#print(fit.summary())


fit = ols('Global_Sales ~ C(Publisher) + C(Genre) + + C(Platform) + Critic_Score',
          data = top_100_recent_games.dropna(subset = ['Publisher', 'Genre', 'Platform', 'Critic_Score', 'Global_Sales'])).fit()

#print(fit.summary())

fit = ols('JP_Sales ~ C(Publisher) + C(Genre) + + C(Platform) + Critic_Score',
          data = prolific_pubs_data_2010.dropna(subset = ['Publisher', 'Genre', 'Platform', 'Critic_Score', 'JP_Sales'])).fit()

print(fit.summary())


vg.total_by_category(top_100_recent_games, 'Genre')


top_100_recent_games_JP = vg.find_first_n(game_data[game_data['Year_of_Release'] >= 2010],
                                    'JP_Sales', 100, False)

top_100_recent_games_EU = vg.find_first_n(game_data[game_data['Year_of_Release'] >= 2010],
                                    'EU_Sales', 100, False)

top_100_recent_games_NA = vg.find_first_n(game_data[game_data['Year_of_Release'] >= 2010],
                                    'NA_Sales', 100, False)


vg.advanced_pyChart(vg.total_by_category(top_100_recent_games_EU, 'Genre'), 
                    'Most Popular Genres in EU Since 2010 ', 'Genre')


vg.advanced_pyChart(vg.total_by_category(top_100_recent_games_JP, 'Genre'), 
                    'Popular Genres in Japan', 
                    'Genre')

vg.advanced_pyChart(vg.total_by_category(top_100_recent_games_EU, 'Genre'), 
                    'Popular Genres in Europe', 
                    'Genre')

vg.advanced_pyChart(vg.total_by_category(top_100_recent_games_NA, 'Genre'), 
                    'Popular Genres in North America', 
                    'Genre')



















        
    
        
        
    
    








