#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:39:22 2023

@author: nickzhou
"""

import math 
import numpy as np 
import scipy as sp 
import pandas as pd 
import matplotlib as mpl 
import seaborn as sns 
import matplotlib.pyplot as plt 
import matplotlib.cbook as cbook 
import random





vg = pd.read_csv("/Users/nickzhou/Downloads/Video_Games.csv") 
game_data = vg 

columns = vg.columns 
print(columns)
print(vg[['Name', 'Global_Sales']])
print(vg.describe()['Global_Sales'])
sorted_vg = vg.sort_values('Global_Sales', ascending = False)[['Name', 'Global_Sales']]

sorted_vg_2010 = vg.query('Year_of_Release >= 2010').sort_values('Global_Sales', 
                                                                 ascending = False)[['Name']]

print(sorted_vg_2010)

grouped_genre = vg.groupby('Genre')
print(vg['Genre'])
print(grouped_genre.get_group('Sports'), 'Grouped by genres')

"""
Input: dataframe column
Output: set containing all the distinct values of this column 
"""
def categorize(n): 
    thisset = set()
    for i in range(len(n)): 
        thisset.add(n[i])
    thisset.discard('nan')
    return thisset 

global_sales = vg['Global_Sales']
na_sales = vg['NA_Sales']
genres = vg['Genre'].drop_duplicates() 
print('genres: ', genres)

#x is the x value, comumn in the df, a string 
#y is the categories that determine color-coding 
        
"""
#basic scatterplot, nothing removed 

fig, ax = plt.subplots() 
ax.scatter(na_sales, global_sales, s = 1, c = 'red', vmin = 0, vmax = 100)

ax.set(xlim = (np.min(na_sales), np.max(na_sales)),
      ylim = (np.min(global_sales), np.max(global_sales)))
plt.show() 
"""

"""
Input: x, y, which are both lists or datasets
Output: a basic scatterplot 
"""
def basic_scatterplot(x, y):
    fig, ax = plt.subplots() 
    ax.scatter(x, y, s = 1, c = 'red', vmin = 0, vmax = 100)

    #ax.set(xlim = (np.min(x), np.max(x)),
          #ylim = (np.min(y), np.max(y)))
    plt.show()
    return 


named_publishers= vg.dropna(subset = ['Publisher'])

vg_GS_millions = vg[vg['Global_Sales'] > 1]
print(vg_GS_millions)

na_sales = vg_GS_millions['NA_Sales']
print(vg_GS_millions.size)
print(vg_GS_millions.index.size)


"""
Input: dataframe, columns wanted to include in final dataframe, column to sort, 
        and will return the highest n elements 
"""
def find_first_n(dataframe, sort_column, n, ascending): 
    df_sorted = dataframe.sort_values(sort_column, ascending = ascending)
    return df_sorted.iloc[0: n]

first_100_GS = find_first_n(vg, 'Global_Sales', 100, False)

def find_last_n(dataframe, sort_column, n, ascending): 
    return find_first_n(dataframe, sort_column, n, True)


#pie charts 


#publisher 

def total_by_category(dataframe, category):
    totals = dict()
    cats = dataframe.dropna(subset = [category])
    if category not in cats: 
        raise ValueError('category does not exist in this dataframe')     
    else:
    
        for i in cats[category]:
            if i in totals:
                totals[i] = totals[i] + 1
            else:
                totals[i] = 1 
    return totals

def trim(dictionary, count):
    for key in dictionary.keys():
        if (dictionary[key] <= count):
            del dictionary[key]
    return dictionary 


    
    

named_publishers = find_first_n(named_publishers, 'Global_Sales', 100, False)
#print(total_by_category(named_developers, 'Developer'))



def basic_pieChart(dictionary): 
    data_labels = dictionary.keys()
    data = dictionary.values() 
    fig = plt.figure(figsize = (10, 7))
    plt.pie(data, labels = data_labels)
    plt.show() 
    return 


def advanced_pyChart(dictionary, name, category):
    data_labels = dictionary.keys()
    data = dictionary.values() 
    
    wp = {'linewidth': 1, 'edgecolor': 'green'}
    def percentage(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return ''.format(pct, absolute) 
    def explode(values): 
        explosions = list()
        for i in range(len(values)): 
            explosions.extend([random.randrange(3) / 10])
        return explosions 
        
    fig, ax = plt.subplots(figsize = (10, 7))
    wedges, texts, autotexts = ax.pie(data, 
                                      autopct = '%1.1f%%',
                                      explode = explode(data),
                                      #labels = data_labels, 
                                      shadow = True, 
                                      startangle = 90, 
                                      wedgeprops = wp, 
                                      textprops = dict(color = 'black')
                                      )
    ax.legend(wedges, data_labels, 
              title = category, 
              loc = 'upper left', 
              bbox_to_anchor = (1, 0, 0.5, 1))
    plt.setp(autotexts, size = 8, weight = 'bold')
    ax.set_title(name)
    plt.show()
    return 
    
#genre 

"""
TRENDS: 
    
    Inputs: dataframe, column to examine
    Output: a linegraph detailing the trends of video games from year to year, 
    x axis = years
    y axis = column totals for that year 
    column must be a categorical variable 
    percent = percentage of games to consider for calculation 
"""
def get_trend(df, column, startyear, endyear, sales_metric, percent, name): 
    if startyear == None: 
        startyear = find_first_n(df, df.columns, 'Year_of_Release', 1, True)
    if endyear == None: 
        endyear = find_first_n(df, df.columns, 'Year_of_Release', 1, False)
    if percent == None:
        percent= 0.2 
    i = startyear
    yearly_data = {}
    yearly_cat_data = {}
    sorted_thing = df.sort_values('Year_of_Release', ascending = True).drop_duplicates(subset = ['Year_of_Release'])
    x2 = sorted_thing[['Year_of_Release']].dropna()
    x1 = x2[x2['Year_of_Release'] <= endyear]
    x = x1[x1['Year_of_Release'] >= startyear]
                                            
    categories = list(df[column].drop_duplicates().dropna())
    for cat in categories:
        yearly_cat_data[cat] = list()
    y = list() 
    def percentage(num, total): 
        if total == 0:
            return 0
        else:
            return num / total 
    
    while i <= endyear: 
        #find all games released in year i 
        games_this_year = df[df['Year_of_Release'] == i]
        if len(games_this_year.index) > 0:
            #if too few games, take them all. Else, take top x percent
            if len(games_this_year.index) <= 100:
                percent = 1 
            top_games = find_first_n(games_this_year, 
                         sales_metric, 
                         int(percent * len(games_this_year.index)), 
                         False)
            raw_totals = total_by_category(top_games, column)
            percentages = {}
            #calculate percent of games in top sales that were in this genre 
            #store them in dictionary 
            for j in categories:
                if j not in raw_totals.keys():
                    p = 0.0
                else:
                    p = percentage(raw_totals[j], len(top_games.index))
                percentages[j] = p
                
                l = yearly_cat_data[j] 
                l.extend([p])
                yearly_cat_data[j] = l
                #map: key = year, value = map<category, percent>
                yearly_data[i] = percentages         
        i = i + 1
        
            
    fig, ax = plt.subplots() 
    lines = [] 
    
        
    for i in categories:
        y = yearly_cat_data[i]
        lines += ax.plot(x, y, label = i)
    cutoff = int(len(lines) / 2)
    
    ax.legend(lines[:cutoff], categories[:cutoff], loc = 'upper center', frameon = False)
    from matplotlib.legend import Legend
    leg = Legend(ax, lines[cutoff:], categories[cutoff:], loc = 'upper left', frameon = False)
    ax.set_title(name)
    ax.add_artist(leg)
    plt.show()
    
    
    return yearly_data


d = {'hello': 1, 'goodbye': 2}

#Heatmap of publishers and their most popular genres 

game_data.groupby('Genre').sum()
sales_list = []
top_100_games_since_2010 = find_first_n(game_data[game_data['Year_of_Release'] >= 2010],
                                    'Global_Sales', 100, False)
genres = game_data[['Genre']].drop_duplicates().dropna().values.tolist()
genres_list = []
for i in genres:
    genres_list.extend(i)

map_df = top_100_games_since_2010.groupby('Genre').sum()[['NA_Sales', 'EU_Sales', 'JP_Sales']]

map_dataset = []
print(genres_list)
print(map_df)
for i in range(10):
    print(i)
    print(map_df.iloc[i].values.tolist())
    l = map_df.iloc[i].values.tolist()
    for j in range(len(l)):
        l[j] = round(l[j], 2)
    map_dataset.extend([l])
    

map_dataset.extend([[0.0, 0.0, 0.0]])
map_dataset.extend([[0.0, 0.0, 0.0]])


def get_regional_heatmap():
    fig, ax = plt.subplots()
    im = ax.imshow(map_dataset)
    ax.set_yticks(np.arange(len(genres_list)), labels = genres_list)
    ax.set_xticks(np.arange(3), labels = ['North America', 'Europe', 'Japan'])
    plt.setp(ax.get_xticklabels(), rotation = 45, ha = 'right', rotation_mode = 'anchor')
    for i in range(len(genres_list)):
        for j in range(len(['North America', 'Europe', 'Japan'])):
            text = ax.text(j, i, map_dataset[i][j], 
                           ha = 'center', va = 'center', color = 'white')
    ax.set_title('Regional Sales by Genre')
    fig.tight_layout
    plt.show()

get_regional_heatmap()


    



# calculate the lifetime of video games, regression on 

#Large regression model 

from statsmodels.formula.api import ols 


def linear_regression(df, independents, dependent):
    
    equation = dependent + ' ~'
    def classify_variables(df, variables):
        isCategorical = [False] * len(variables)
        for i in range(len(variables)):
            var = variables[i] 
            if df[var].iloc[0].__class__ == str or var.str.contains('Year_of_Release'):
                isCategorical[i] = True
            else:
                isCategorical[i] = False
        return isCategorical
    df2 = df.dropna(subset = independents.append(dependent))
    categoricals = classify_variables(df, independents)
    s = str()
    for i in independents:
        if i not in df.columns:
            raise ValueError('an iv is not in the dataset')
        else:
            if categoricals[i] == True:
                s += ' + C(' + independents[i] + ')'
            else:
                s = ' + ' + independents[i]
    fit = ols(s, data = df).fit()
    fit.summary()
    return 

ivs = ['Publisher', 'Genre', 'Rating']
fit = ols('Global_Sales ~ C(Publisher) + C(Genre) + C(Platform) + Critic_Score',
          data = game_data.dropna(subset = ['Publisher', 'Genre', 'Critic_Score', 'Platform', 'Global_Sales'])).fit()
print(fit.summary())

#linear_regression(game_data, ivs, 'Global_Sales')
                
                    
                
            
        

"""
Input: dataframe, column of dataframe, list of categories that fall under that column
output: dataframe that contains observations belonging to only these categories 
"""
def get_by_group(df, column, categories):
    s = str()
    for i in range(len(categories)):
        s2 = str()
        if i == 0:
            s2 = categories[0]
        else:
            s2 = '|' + categories[i]
    
        s = s + s2
    df2 = df.dropna(subset = [column])
    return df2[df2[column].str.contains(s)]






    

    



    
    
    

    


    


        





    

