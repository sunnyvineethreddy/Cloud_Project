
## Import necessary packages
import pandas as pd
import matplotlib.pyplot as plt

## Reading Chicago Crime data from the CSV file
df = pd.read_csv('KCPD_Crime_Data_2018.csv')
# print(df['Primary Type'].value_counts())
# print(df['Year'].value_counts())

## Plot these for better visualization
crime_type_df = pd.Series(df['Description'].value_counts(ascending=True))

## Some formatting to make it look nicer
## Plotting Frequency of Crimes
fig=plt.figure(figsize=(18, 16))
plt.title("Frequency of Crimes Per Crime Type")
plt.xlabel("Frequency of Crimes")
plt.ylabel("Type of Crime")
my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']
ax = crime_type_df.plot(kind='barh', color = my_colors)
ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

plt.show()


