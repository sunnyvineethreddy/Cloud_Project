import folium
from folium import plugins
import pandas as pd

sf_crime_data=pd.read_csv("F:\cloudProject\sf.csv")

sfData=sf_crime_data.loc[:,['X','Y','Date']]

sfData['Date'] = pd.to_datetime(sfData.Date,format='%m/%d/%Y')
sf_crime_data['Date']=  pd.to_datetime(sf_crime_data.Date,format='%m/%d/%Y')
for i in (sfData,sf_crime_data):
    i['year']=i.Date.dt.year
    i['month']=i.Date.dt.month
    i['day']=i.Date.dt.day

m = folium.Map([-122.374019331833, 37.729203356539], zoom_start=11)

for index, row in sfData.iterrows():
    if(row['year']==2012 and row['month']==12):
     folium.CircleMarker([row['X'], row['Y']],
                        radius=15,
                       # popup=row['name'],
                        fill_color="#3db7e4", # divvy color
                       ).add_to(m)

stationArr = sfData[['X', 'Y']].as_matrix()
m.add_children(plugins.HeatMap(stationArr, radius=15))
m.save('sfHeatmap.html')