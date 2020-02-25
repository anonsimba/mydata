#!/usr/bin/env python
# importing pandas package 
import sys
import pandas as pd 
from textblob import TextBlob
import requests
import argparse

# making data frame from csv file 
data = pd.read_csv("/var/www/html/upload/data.csv")  ##change 

# replacing blank spaces with '_' 
data.columns =[column.replace(" ", "_") for column in data.columns] 
data.columns=[x.lower() for x in data.columns]
# filtering with query method 
data=data.apply(lambda x: x.astype(str).str.lower()) ##tolowercaseallvalues


#search=raw_input("Enter Values to Filter:") # chnage it wi
search= sys.argv[1].lower()
blob = TextBlob(search)
keywords=blob.words
print keywords


result=[]
for i in keywords:
	idx = data.apply(lambda ts: any(ts == i), axis=1)
	result.append(data[idx])
#print result
df1=pd.concat(result,axis=0)
print df1
'''
new_df = result[0]
for i in result[1:]:
	new_df=new_df.merge(i,how='outer')
print new_df
'''
csv=df1.to_csv()
text_file = open("data.csv", "w")
text_file.write(csv)
text_file.close()
print(len(result))



