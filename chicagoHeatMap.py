import folium
from folium import plugins
import pandas as pd

chicago_crime_data=pd.read_csv("F:\cloudProject\Chicago_Crimes_2012_to_2017.csv")
chicagoData= chicago_crime_data.loc[:,['Latitude','Longitude','Year']]

print(chicagoData.apply(lambda x: sum(x.isnull())))
chicagoData['Latitude'] = chicagoData['Latitude'].fillna(chicagoData['Latitude'].mode()[0])
chicagoData['Longitude'] = chicagoData['Longitude'].fillna(chicagoData['Longitude'].mode()[0])

m = folium.Map([41.864073157, -87.706818608], zoom_start=11)


for index, row in chicagoData.iterrows():
    if(row['Year']==2015):
     folium.CircleMarker([row['Latitude'], row['Longitude']],
                        radius=15,
                       # popup=row['name'],
                        fill_color="#3db7e4", # divvy color
                       ).add_to(m)

stationArr = chicagoData[['Latitude', 'Longitude']].as_matrix()
m.add_children(plugins.HeatMap(stationArr, radius=15))
m.save('chicagoHeatmap.html')