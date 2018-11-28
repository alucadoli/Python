#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

names1880 = pd.read_csv(r'names/yob1880.txt', names = ['name','sex','births'])
#show sum of births by sex
#print(names1880.groupby('sex').births.sum())
#Merge all files
years = range(1880,2011)
pieces = []
columns = ['name','sex','births']

for year in years:
    path = r'names/yob%d.txt' % year
    frame = pd.read_csv(path,names = columns)

    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces,ignore_index=True)

#pivot table
total_births = names.pivot_table('births',index='year',columns='sex',aggfunc=sum)
#total_births.plot(title='Total births by sex and year')
#show()

#pertagate of infant
def add_prop(group):
    births = group.births.astype(float)

    group['prop'] = births / births.sum()
    return group

names = names.groupby(['year','sex']).apply(add_prop)
#print(names)
#Check Data Valid
np.allclose(names.groupby(['year','sex']).prop.sum(),1)
#pop up sub collection
def get_top1000(group):
    return group.sort_values(by='births',ascending=False)[:1000]

grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)
#print(top1000)
pieces = []
for year,group in names.groupby(['year','sex']):
    pieces.append(group.sort_values(by='births',ascending=False)[:1000])
top1000 = pd.concat(pieces,ignore_index=True)
#print(top1000)

#Analysis trend of naming
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
total_births = top1000.pivot_table('births',index='year',columns='name',aggfunc=sum)
#print(total_births)
# subset = total_births[['John','Harry','Mary','Marilyn']]
# subset.plot(subplots=True,figsize=(12,10),grid=False,title='Numbe of births per year')
# show()

#Evaluate the growth of divsity naming
#

#考虑占总出生人数前50%的不同名字的数量。
# df = boys[boys.year == 2010]
# #Find the number of sum of prop equal 50%
# prop_cumsum = df.sort_values(by='prop',ascending=False).prop.cumsum()
# prop_cumsum.searchsorted(0.5)

# df = boys[boys.year == 1900]
# in1900 = df.sort_values(by='prop',ascending=False).prop.cumsum()
# in1900.searchsorted(0.5)+1

#Function that calc
def get_quantile_count(group,q=0.5):
    group = group.sort_values(by="prop",ascending=False)
    return group.prop.cumsum().searchsorted(q)+1

diversity = top1000.groupby(['year','sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
#print(diversity.head())
print(diversity)
# diversity.plot(title='Number of popular names in top 50%')
# show()

##Last letter of name
#Get last letter
get_last_letter = lambda x:x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'
table = names.pivot_table('births',index=last_letters,columns=['sex','year'],aggfunc=sum)
print(table)