
## Import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from os import path
from PIL import Image

## Reading Chicago Crime data from the CSV file
df = pd.read_csv('Chicago_Crimes_2012_to_2017.csv')
# print(df['Primary Type'].value_counts())
# print(df['Year'].value_counts())

## Plot these for better visualization
# crime_type_df = pd.Series(df['Primary Type'].value_counts(ascending=True))

## Some formatting to make it look nicer
## Plotting Frequency of Crimes
# fig=plt.figure(figsize=(18, 16))
# plt.title("Frequency of Crimes Per Crime Type")
# plt.xlabel("Frequency of Crimes")
# plt.ylabel("Type of Crime")
# my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']
# ax = crime_type_df.plot(kind='barh', color = my_colors)
# ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# plt.show()

## Count number of reported crimes for each year
# print(df['Year'].value_counts())

## Plot these for better visualization
# crime_year_df = df['Year'].value_counts(ascending=True)

## Some formatting to make it look nicer
# fig=plt.figure(figsize=(10, 8))
# plt.title("Frequency of Crimes Per Year in Chicago")
# plt.xlabel("Frequency of Crimes")
# plt.ylabel("Year")
# ax = crime_year_df.plot(kind='barh')
# ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
# plt.show()

df.Date = pd.to_datetime(df.Date, format = '%m/%d/%Y %I:%M:%S %p')

df.index = pd.DatetimeIndex(df.Date)

df['time_hour'] = df['Date'].apply(lambda x : x.hour)
df['month'] = df['Date'].apply(lambda x : x.month)
df['year'] = df['Date'].apply(lambda x : x.year)

df = df[df['year']!= 2017]

df.head()

plt.figure(figsize=(11,5))
df.resample('M').size().plot(legend = False)
plt.title(" Number of crimes from 2012-2016")
plt.xlabel("months ")
plt.ylabel("Crimes ")
plt.show()

plt.figure(figsize=(16,8))
sns.countplot(x='time_hour', data = df)
plt.ylabel('Number of Crimes')
plt.title('CHICAGO: Hour wise # of Crimes Reported')
plt.show()

crimes_count_date = df.pivot_table('ID', aggfunc=np.size,columns='Primary Type', index = df.index.date, fill_value=0)
crimes_count_date.index = pd.DatetimeIndex(crimes_count_date.index)
plot = crimes_count_date.rolling(365).sum().plot(figsize=(12,30),subplots=True,layout=(-1,3),sharex=False, sharey=False)
plt.show()


df['Details'] = df['Primary Type'] + ',' + df['Description']
top_crimes = df.groupby(['Details'])['Arrest'].count()
top_crimes = pd.DataFrame(top_crimes).nlargest(10,'Arrest').reset_index()
top_crimes = list(top_crimes['Details'])


df2 = df.groupby(['Details','month'])['Arrest'].count()

DIMS = (25,15)
fig= plt.figure(figsize = DIMS)
ax1 = fig.add_subplot(111)
ax1.set_title('Major crimes (January - December)',fontsize=20)
ax1.set_ylabel('Details',fontsize=20)
ax1.set_xlabel('month',fontsize=20)

df2 = pd.DataFrame(df2).reset_index()
df2 = df2[df2['Details'].isin(top_crimes)]

df2 = df2.pivot_table(index='Details',columns='month',values='Arrest')
df2.fillna(0,inplace=True)

sns.heatmap(df2,cmap="Blues",annot=True,fmt='g')
plt.show()