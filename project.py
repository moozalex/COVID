import pandas as pd
covid = pd.read_csv('time-series-19-covid-combined_csv.csv')
import matplotlib.pyplot as plt


for i in range(5):
    if covid.iloc[i,0] == '1/22/20':
        print(covid.iloc[i,1])
        print(covid.iloc[i,2])


#Printing Columns

#print(covid.head(3))
#print(covid.columns)
#print(covid['ObservationDate'][0:5])
#print(covid.ObservationDate)
#print(covid[['ObservationDate', 'Confirmed']])


#Printing Rows
#print(covid.iloc[1])
#print(covid.iloc[1:4])

#3rd row, 3rd column. 
#print(covid.iloc[2,2])

# for index, row in covid.iterrows():
#     print(index, row['Province/State'])

#mean and standard deviation
#print(covid.describe())

#print(covid.sort_values('Province/State', ascending=False))

#this didn't work as expected
#print(covid.sort_values(['SNo', 'Province/State'], ascending=[1,0]))


#print(covid.columns)

#print(covid.loc[(covid['Province/State'] == 'Wuhan') & (covid['Confirmed'] >= 0) & (covid['Deaths']) >= 0])

covid['Month'] = covid['Date'].str[0:1]
covid['Month'] = covid['Month'].astype('int32')

#Sort by Date
covid = covid.sort_values(by='Date')
print(covid)

#covid['Date'] = covid.astype('datetime64[ns]')
#covid["Date"] = pd.to_datetime(covid["Date"]).dt.date
#print(covid)


#print(covid.query("Month == 4")['Confirmed'].sum())
print(covid.loc[covid['Date'] == "1/31/20", 'Confirmed'].sum())
print(covid.loc[covid['Date'] == "2/29/20", 'Confirmed'].sum())

print(covid.loc[covid['Date'] == "3/31/20", 'Confirmed'].sum())
print(covid.loc[covid['Date'] == "4/18/20", 'Confirmed'].sum())


#covid.sort_values("Confirmed", inplace = True)
#covid.drop_duplicates(subset = "Confirmed", keep = False, inplace = True)

print(covid)

# months = range(1,5)
# plt.bar(months, results['Confirmed'])
# plt.ticklabel_format(style = 'plain')
# plt.show()
