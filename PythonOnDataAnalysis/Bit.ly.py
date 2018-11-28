#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#Obtain data and count on tag.
import pandas
import json
import matplotlib.pyplot as plt
from pylab import *
from collections import defaultdict

path = r"E:\PYProjects\PythonOnDataAnalysis\usagov_bitly_data2012-03-16-1331923249.txt"
#record txt to json
records = [json.loads(line) for line in open(path)]
#print(records)
#print(records[0]['tz'])
#get all time_zones records
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
#print(time_zones)
#count time_zones
def get_counts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

counts = get_counts(time_zones)
#print(counts['America/New_York'])

#get top 10 time_zones
def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

#print(top_counts(counts))
#Collections.Counter
from collections import Counter

counts = Counter(time_zones)
#print(counts.most_common(10))

#DataFrame
from pandas import DataFrame, Series

frame = DataFrame(records)
#print(frame)
#print(frame['tz'][:10])
tz_counts = frame['tz'].value_counts()
#print(tz_counts[:10])

#Fill missed records and generate the picture
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
#print(tz_counts[:10])

tz_counts[:10].plot(kind='barh', rot=0)
#Window show chart
#show()

#Extract keywords
results = Series([x.split()[0] for x in frame.a.dropna()])
# print(results[:5])
# print(results.value_counts()[:10])

#Count by Window/Non window
cframe = frame[frame.a.notnull()]
operation_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
#print(operation_system[:10])
#Group by
by_tz_os = cframe.groupby(['tz',operation_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
#print(agg_counts[:10])
indexer = agg_counts.sum(1).argsort()
#print(indexer[:10])
count_subset = agg_counts.take(indexer)[-10:]
#print(count_subset)
count_subset.plot(kind='barh', stacked=True)
#Another Stacked Barchart
normed_subset = count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind='barh',stacked=True)
show()
