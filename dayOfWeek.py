import pandas as pd
import matplotlib.pyplot as plt

chicago_crime_data=pd.read_csv("F:\cloudProject\Chicago_Crimes_2012_to_2017.csv")
boston_crime_data=pd.read_csv("F:\cloudProject\BostonCrimes.csv")
sf_crime_data=pd.read_csv("F:\cloudProject\sf.csv")



bostonData= boston_crime_data.loc[:,['DAY_OF_WEEK']]

sfData=sf_crime_data.loc[:,['DayOfWeek']]

fig, axes = plt.subplots(2,1)
ax0, ax2 = axes.flatten()

prim_count1 = bostonData['DAY_OF_WEEK'].value_counts(normalize=True)
prim_count1 = prim_count1[:7,]
rect1 = ax0.bar(prim_count1.index, prim_count1.values, label='Boston')
ax0.set_title('Boston Day of Week')


prim_count2 = sfData['DayOfWeek'].value_counts(normalize=True)
prim_count2 = prim_count2[:7,]
rect2 = ax2.bar(prim_count2.index, prim_count2.values, label='SF')
ax2.set_title('San Fransisco Day of Week')

fig.tight_layout()
plt.show()
