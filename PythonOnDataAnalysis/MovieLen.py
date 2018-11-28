#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pandas as pd

#load data to dicts
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('movielens/users.dat',sep='::',header=None,names=unames,engine = 'python')

rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('movielens/ratings.dat',sep='::',header=None, names=rnames,engine = 'python')

mnames = ['movie_id','title','genres']
movies = pd.read_table('movielens/movies.dat',sep='::',header=None, names=mnames,engine = 'python')

# print(users[:5])
# print(ratings[:5])
# print(movies[:5])

#merge multiple tables
data = pd.merge(pd.merge(ratings,users),movies)
#print(data.ix[0])

#Pivot_table  => dataframe
mean_ratings = data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')
#print(mean_ratings[:5])

#filter out rating less than 250 and get index.
ratings_by_title = data.groupby('title').size()
#print(ratings_by_title[:10])
active_titles = ratings_by_title.index[ratings_by_title >= 250]
#print(active_titles)

#Get lines thru index
mean_ratings = mean_ratings.ix[active_titles]
#print(mean_ratings)

#Get the favority movies of female
top_female_ratings = mean_ratings.sort_values(by='F',ascending=False)
#print(top_female_ratings[:10])

#Calculate the differences rating Method 1
mean_ratings['diff'] = mean_ratings['M'] = mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
#print(sorted_by_diff[:10])
#get male -- desort.
#print(sorted_by_diff[::-1][:10])
#Diff without sexy
ratings_std_by_title = data.groupby('title')['rating'].std()
ratings_std_by_title = ratings_std_by_title.ix[active_titles]
print(ratings_std_by_title.sort_values(ascending=False)[:10])
