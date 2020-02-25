#!/usr/bin/python
# importing pandas package 
import pandas as pd 
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
path='/var/www/html/upload'
files = os.listdir(path)
for file in files:
   os.rename(os.path.join(path, file), os.path.join(path,'myfile'))
data = pd.read_excel("/var/www/html/upload/myfile")  ##change to webapi url

# replacing blank spaces with '_' 
data.columns =[column.replace(" ", "_") for column in data.columns] 


#write to csv

csv=data.to_csv()
text_file = open("/var/www/html/upload/data.csv", "w")
text_file.write(csv)
text_file.close()

'''
csv=data.to_csv()
text_file = open("/var/www/html/data.csv", "w")
text_file.write(csv)
text_file.close()
'''
