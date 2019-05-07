import pandas as pd
import matplotlib.pyplot as plt

chicago_crime_data=pd.read_csv("F:\cloudProject\Chicago_Crimes_2012_to_2017.csv")
boston_crime_data=pd.read_csv("F:\cloudProject\BostonCrimes.csv")
sf_crime_data=pd.read_csv("F:\cloudProject\sf.csv")

chicagoData= chicago_crime_data.loc[:,['Year']]

bostonData= boston_crime_data.loc[:,['YEAR']]

sfData=sf_crime_data.loc[:,['Date']]
sfData['Date'] = pd.to_datetime(sfData.Date,format='%m/%d/%Y')
sf_crime_data['Date']=  pd.to_datetime(sf_crime_data.Date,format='%m/%d/%Y')
for i in (sfData,sf_crime_data):
    i['year']=i.Date.dt.year
    i['month']=i.Date.dt.month
    i['day']=i.Date.dt.day

fig, axes = plt.subplots(3,1)
ax0, ax1, ax2 = axes.flatten()

prim_count1 = boston_crime_data['YEAR'].value_counts(normalize=True)
prim_count1 = prim_count1[:10,]
rect1 = ax0.bar(prim_count1.index, prim_count1.values, label='Boston')
ax0.set_title('Boston Year Chart')

prim_count = chicago_crime_data['Year'].value_counts(normalize=True)
prim_count = prim_count[:10,]
rect2 = ax1.bar(prim_count.index, prim_count.values, label='Chicago')
ax1.set_title('Chicago Year Chart')

prim_count2 = sf_crime_data['year'].value_counts(normalize=True)
prim_count2 = prim_count2[:10,]
rect2 = ax2.bar(prim_count2.index, prim_count2.values, label='SF')
ax2.set_title('San Fransisco Year Chart')

fig.tight_layout()
plt.show()


