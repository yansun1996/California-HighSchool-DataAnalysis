import pandas as pn
import numpy as np
import math

def parser(): # takes in all verbal and math sat scores and by county by year and puts it into a dictionary
    fileList = ['sat00.xls','sat01.xls','sat02.xls','sat03.xls','sat04.xls','sat05.xls','sat06.xls','sat07.xls','sat08.xls','sat09.xls','sat10.xls','sat11.xls','sat12.xls','sat13.xls','sat14.xls','sat15.xls']
    structList = []
    structL = []
    structDict = {}
    #for fi in range(14):
    for fi in range(14):
   
        struct = pn.read_excel(fileList[fi])
        if fi < 14: # sat14 and sat15 are in a different format
            struct = struct[['Unnamed: 3', 'Unnamed: 9', 'Unnamed: 10']] #these correspond to county name, verbal score, math score
            struct = struct.loc[4:] # first few rows contain no useful info
            
            # clean out rows with missing data
            #origSize = len(struct['Unnamed: 3'])
            struct.index = range(len(struct))
            droplist = []
           # for i in range(len(struct)):
            for i,v in struct['Unnamed: 9'].items():
                # numbers are also formatted as strings and floats within even the same file...let's fix that
                try:
                    struct['Unnamed: 9'][i] = float(struct['Unnamed: 9'][i])
                    struct['Unnamed: 10'][i] = float(struct['Unnamed: 10'][i])
                except ValueError:
                    pass

                try:
                    if (math.isnan(struct['Unnamed: 9'][i])):
                        droplist.append(i)
                except TypeError:
                    pass

                if ((struct['Unnamed: 9'][i] == 0) or (type(struct['Unnamed: 9'][i]) != int and type(struct['Unnamed: 9'][i]) != float)):
                    droplist.append(i)
#                    if struct['Unnamed: 9'][i] != 0:
#                        print(type(struct['Unnamed: 9'][i]))

#        if fi >= 14:
#            struct = struct[['cname', 'AvgScrRead', 'AvgScrMath']] #these correspond to county name, verbal score, math score
#            struct = struct.loc[1:] # first row contain no useful info
#
#            # clean out rows with missing data
#            origSize = len(struct['cname'])
#            for i in range(1,1+origSize):
#                if (type(struct['AvgScrRead'][i]) != int or type(struct['AvgScrMath'][i]) != int):
#                    struct = struct.drop(i)

####        struct.columns = ['%s county_name'%fileList[fi][3:5],'%s verbal_score'%fileList[fi][3:5],'%s mat_score'%fileList[fi][3:5]]
        struct = struct.drop(droplist)
        struct.index = range(len(struct))
        structL.append(struct)
#        dic = struct.to_dict()
#        structList.append(dic)
#    for d in structList:
#        for k in d:
#            structDict[k] = d[k]
    return(structL)
def avg_by_year(structL):
    agg = 1;newlist = []
    for db in structL:
#        print(db['Unnamed: 9'])
        holder1 = db['Unnamed: 9'][0]
        holder2 = db['Unnamed: 10'][0]
        for i in range(len(db['Unnamed: 3'])):
            try:
                if db['Unnamed: 3'][i] == db['Unnamed: 3'][i+1]:
                    agg += 1
                    holder1 += db['Unnamed: 9'][i+1]
                    holder2 += db['Unnamed: 10'][i+1]
                    db = db.drop(i)
                else:
                    db['Unnamed: 9'][i] = holder1/agg
                    db['Unnamed: 10'][i] = holder2/agg
                    holder1 = db['Unnamed: 9'][i+1]
                    holder2 = db['Unnamed: 10'][i+1]
                    agg = 1

            except KeyError: # if we hit the last item in the list go ahead and average
                db['Unnamed: 9'][i] = holder1/agg
                db['Unnamed: 10'][i] = holder2/agg
        db.index = range(len(db))
        newlist.append(db)
    return(newlist)






structL = parser()
#print(structL)
new = avg_by_year(structL)
print(new)
