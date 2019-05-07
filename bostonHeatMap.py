import folium
from folium import plugins
import pandas as pd
boston_crime_data=pd.read_csv("F:\cloudProject\BostonCrimes.csv")
bostonData= boston_crime_data.loc[:,['Lat','Long','YEAR']]
print(bostonData.apply(lambda x: sum(x.isnull())))

bostonData['Lat'] = bostonData['Lat'].fillna(bostonData['Lat'].mode()[0])
bostonData['Long'] = bostonData['Long'].fillna(bostonData['Long'].mode()[0])

m = folium.Map([42.3601, -71.0589], zoom_start=11)

for index, row in bostonData.iterrows():
    if(row['YEAR']==2015):
     folium.CircleMarker([row['Lat'], row['Long']],
                        radius=15,
                       # popup=row['name'],
                        fill_color="#3db7e4", # divvy color
                       ).add_to(m)

stationArr = bostonData[['Lat', 'Long']].as_matrix()
m.add_children(plugins.HeatMap(stationArr, radius=15))
m.save('bostonHeatmap.html')