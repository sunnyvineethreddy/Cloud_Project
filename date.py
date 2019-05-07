import pandas as pd
import matplotlib.pyplot as plt

chicago_crime_data=pd.read_csv("F:\cloudProject\Chicago_Crimes_2012_to_2017.csv")
boston_crime_data=pd.read_csv("F:\cloudProject\BostonCrimes.csv")
sf_crime_data=pd.read_csv("F:\cloudProject\sf.csv")

chicagoData= chicago_crime_data.loc[:,['Date']]
bostonData= boston_crime_data.loc[:,['OCCURRED_ON_DATE']]
sfData=sf_crime_data.loc[:,['Date']]

print(chicagoData.apply(lambda x: sum(x.isnull())))
print(bostonData.apply(lambda x: sum(x.isnull())))
print(sfData.apply(lambda x: sum(x.isnull())))


chicagoData['Date'] = pd.to_datetime(chicagoData.Date,format='%m/%d/%Y %I:%M:%S %p')
chicago_crime_data['Date']=  pd.to_datetime(chicago_crime_data.Date,format='%m/%d/%Y %I:%M:%S %p')
for i in (chicagoData,chicago_crime_data):
    i['year']=i.Date.dt.year
    i['month']=i.Date.dt.month
    i['day']=i.Date.dt.day
    i['Hour']=i.Date.dt.hour

sfData['Date'] = pd.to_datetime(sfData.Date,format='%m/%d/%Y')
sf_crime_data['Date']=  pd.to_datetime(sf_crime_data.Date,format='%m/%d/%Y')
for i in (sfData,sf_crime_data):
    i['year']=i.Date.dt.year
    i['month']=i.Date.dt.month
    i['day']=i.Date.dt.day



fig, axes = plt.subplots(2,1)
ax1, ax2 = axes.flatten()



prim_count = chicagoData['day'].value_counts(normalize=True)
prim_count = prim_count[:31,]
rect2 = ax1.bar(prim_count.index, prim_count.values, label='Chicago')
ax1.set_title('Chicago Crime Date')

prim_count2 = sfData['day'].value_counts(normalize=True)
prim_count2 = prim_count2[:31,]
rect2 = ax2.bar(prim_count2.index, prim_count2.values, label='SF')
ax2.set_title('San Fransisco Crime Date')

fig.tight_layout()
plt.show()