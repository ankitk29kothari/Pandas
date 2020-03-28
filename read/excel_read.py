import pandas


# change header value resoective to header position,index col to find values
df=pandas.read_excel("input.xlsx",index_col='switch',header=0)
print(df.ix[2])

#df=pandas.read_csv("input.xlsx",index_col='switch',header=0)
#df = pd.read_html(r"C:\Users\KNRT5884\Downloads\ExcelLisTic.xls",header=1)
## this will print coluns only
#print(df.columns)
print("_________________")
#extracing diff diff rows
s=df['fping']
c=df['command']
io=df['input']


#itteration diff rows with same col no.
for i,j,k in zip(s,c,io):
	#print(i,j,io)
	pass

# finding value & print its correspond rows
a=(df.loc['PZRN059'])
print(a)

print("_________________")
print(a['input'])