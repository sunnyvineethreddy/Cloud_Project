
## Import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from os import path
from PIL import Image

## Reading Boston Crime data from the CSV file
df = pd.read_csv('Boston_Crime.csv')

df.OCCURRED_ON_DATE = pd.to_datetime(df.OCCURRED_ON_DATE, format = '%Y-%m-%d %H:%M:%S')

df.index = pd.DatetimeIndex(df.OCCURRED_ON_DATE)

df['time_hour'] = df['OCCURRED_ON_DATE'].apply(lambda x : x.hour)
df['month'] = df['OCCURRED_ON_DATE'].apply(lambda x : x.month)
df['year'] = df['OCCURRED_ON_DATE'].apply(lambda x : x.year)


df.head()

plt.figure(figsize=(11,5))
df.resample('M').size().plot(legend = False)
plt.title(" Number of crimes from August 2015 - Present")
plt.xlabel("Monthly ")
plt.ylabel("Crimes ")
plt.show()

plt.figure(figsize=(16,8))
sns.countplot(x='time_hour', data = df)
plt.ylabel('Number of Crimes')
plt.title('Boston: Hour wise # of Crimes Reported')
plt.show()

df['Details'] = df['OFFENSE_CODE_GROUP'] + ',' + df['OFFENSE_DESCRIPTION']
top_crimes = df.groupby(['Details']).count()
top_crimes = pd.DataFrame(top_crimes).nlargest(10,'DISTRICT').reset_index()
top_crimes = list(top_crimes['Details'])


df2 = df.groupby(['Details','month']).count()

DIMS = (25,15)
fig= plt.figure(figsize = DIMS)
ax1 = fig.add_subplot(111)
ax1.set_title('Major crimes (January - December)',fontsize=20)
ax1.set_ylabel('Details',fontsize=20)
ax1.set_xlabel('month',fontsize=20)

df2 = pd.DataFrame(df2).reset_index()
df2 = df2[df2['Details'].isin(top_crimes)]

df2 = df2.pivot_table(index='Details',columns='month',values='DISTRICT')
df2.fillna(0,inplace=True)

sns.heatmap(df2,cmap="Blues",annot=True,fmt='g')
plt.show()