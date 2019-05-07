import pandas as pd
import matplotlib.pyplot as plt

chicago_crime_data=pd.read_csv("F:\cloudProject\Chicago_Crimes_2012_to_2017.csv")
boston_crime_data=pd.read_csv("F:\cloudProject\BostonCrimes.csv")
sf_crime_data=pd.read_csv("F:\cloudProject\sf.csv")

chicagoData= chicago_crime_data.loc[:,['Primary Type']]

bostonData= boston_crime_data.loc[:,['OFFENSE_CODE_GROUP']]

sfData=sf_crime_data.loc[:,['Category']]

#print(chicagoData.apply(lambda x: sum(x.isnull())))
#print(bostonData.apply(lambda x: sum(x.isnull())))
#print(sfData.apply(lambda x: sum(x.isnull())))


fig, axes = plt.subplots(3,1)
ax0, ax1, ax2 = axes.flatten()

prim_count1 = boston_crime_data['OFFENSE_CODE_GROUP'].value_counts(normalize=True)
prim_count1 = prim_count1[:10,]
rect1 = ax0.bar(prim_count1.index, prim_count1.values, label='Boston')
ax0.set_title('Boston Crimes')

prim_count = chicago_crime_data['Primary Type'].value_counts(normalize=True)
prim_count = prim_count[:10,]
rect2 = ax1.bar(prim_count.index, prim_count.values, label='Chicago')
ax1.set_title('Chicago Crimes')

prim_count2 = sf_crime_data['Category'].value_counts(normalize=True)
prim_count2 = prim_count2[:10,]
rect2 = ax2.bar(prim_count2.index, prim_count2.values, label='SF')
ax2.set_title('San Fransisco Crimes')

fig.tight_layout()
plt.show()
