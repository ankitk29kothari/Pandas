import pandas
#import pandas libarary
#pip install pandas on cmd

#reading file in the same folder or provide the path
df=pandas.read_excel("input.xlsx",index_col='switch')

#use this oine if your headingg is not placed in by deafult o position
'''df=pandas.read_excel("input.xlsx",header=1)'''
a=(df.loc['Txn23'])
print(a)
print('---')
print(a['output'])
print(a[2])

