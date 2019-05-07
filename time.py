import pandas as pd
import matplotlib.pyplot as plt

chicago_crime_data=pd.read_csv("F:\cloudProject\Chicago_Crimes_2012_to_2017.csv")
boston_crime_data=pd.read_csv("F:\cloudProject\BostonCrimes.csv")
sf_crime_data=pd.read_csv("F:\cloudProject\sf.csv")

chicagoData= chicago_crime_data.loc[:,['Date']]

bostonData= boston_crime_data.loc[:,['HOUR']]

sfData=sf_crime_data.loc[:,['Time']]

sfData['Time'] = sfData['Time'].map(lambda x: str(x)[:-3])

#print(chicagoData.apply(lambda x: sum(x.isnull())))
#print(bostonData.apply(lambda x: sum(x.isnull())))
#print(sfData.apply(lambda x: sum(x.isnull())))


chicagoData['Date'] = pd.to_datetime(chicagoData.Date,format='%m/%d/%Y %I:%M:%S %p')
chicago_crime_data['Date']=  pd.to_datetime(chicago_crime_data.Date,format='%m/%d/%Y %I:%M:%S %p')
for i in (chicagoData,chicago_crime_data):
    i['year']=i.Date.dt.year
    i['month']=i.Date.dt.month
    i['day']=i.Date.dt.day
    i['Hour']=i.Date.dt.hour



fig, axes = plt.subplots(3,1)
ax0, ax1, ax2 = axes.flatten()

prim_count1 = boston_crime_data['HOUR'].value_counts(normalize=True).sort_index()
prim_count1 = prim_count1[:24,]
rect1 = ax0.bar(prim_count1.index, prim_count1.values, label='Boston')
ax0.set_title('Boston Hour Chart')

prim_count = chicago_crime_data['Hour'].value_counts(normalize=True).sort_index()
prim_count = prim_count[:24,]
rect2 = ax1.bar(prim_count.index, prim_count.values, label='Chicago')
ax1.set_title('Chicago Hour chart')

prim_count2 = sfData['Time'].value_counts(normalize=True).sort_index()
prim_count2 = prim_count2[:24,]
rect2 = ax2.bar(prim_count2.index, prim_count2.values, label='SF')
ax2.set_title('San Fransisco hour chart')

fig.tight_layout()
plt.show()
