import pandas as pd
import numpy as np
import pickle

# important columns to extract from excel file
myList = [1, 2, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45]
# read from excel file
df = pd.read_excel("finData.xls", usecols = myList)
# filter only CA data
df = df[df.State == 'CA']
df = df[df.Area_name != 'California']
result = list(df.iterrows())
countyList = list(df.Area_name.unique())
yearList = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
for i in range(0, len(result)):
    result[i][1].Area_name = result[i][1].Area_name.split(',')[0]
df2 = pd.DataFrame(np.zeros((len(countyList), len(yearList))), index = countyList, columns = yearList)
myYear = ['Unemployment_rate_2007', 'Unemployment_rate_2008', 'Unemployment_rate_2009', 'Unemployment_rate_2010', 'Unemployment_rate_2011', 'Unemployment_rate_2012', 'Unemployment_rate_2013', 'Unemployment_rate_2014', 'Unemployment_rate_2015', 'Unemployment_rate_2016']
for i in range(0, len(countyList)):
    tempList = list(result[i][1].aggregate(myYear))
    for j in range(0, len(yearList)):
        df2.iloc[i,j] = tempList[j]
# pickle file name
filename = "unemploymentDataFile"
filehandler = open(filename,"wb")
pickle.dump(df2,filehandler)
filehandler.close()





