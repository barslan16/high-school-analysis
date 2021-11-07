# -*- coding: utf-8 -*-
"""
@author: Anil Sen & Beyza Arslan
"""
#call required elements from graph_design
from graph_design import font, title_font_size,auto_open
#call data from data_filtering
from data_filtering import provinces

#visualization library
import plotly.express as px

import json

import pandas as pd
import numpy as np


#It is the file where the graphics will be created.
graph_location="graphs/"

#===============================================================================#

#Province Efficieny Factor Turkey Map

#===============================================================================#


# coordinates of the borders of the provinces necessary for drawing map
with open('Data/tr-cities-utf8.json', encoding="utf-8") as response:
    counties = json.load(response)

#some datas about provinces (population,region etc.)
provinces_data="Data/tr_provinces_dem_data.xlsx"
eachcitydf = pd.read_excel(provinces_data, "Sheet1")


#create dataframe for drawing map
eachcitydf["id"] = eachcitydf["id"].astype(str)
factorofprovinces=[]
for i in eachcitydf["province"]:
    if len(np.where(provinces["province"] == i)[0])>0:

        factorofprovinces.append(provinces["factor"][np.where(provinces["province"] == i)[0][0]])
    else:
        factorofprovinces.append(75)

#round to two decimals
eachcitydf["factor"]=[round(x,2) for x in factorofprovinces]    


#draw Turkey Map
fig = px.choropleth(eachcitydf,
                    #coordinates of the borders of the provinces 
                    geojson=counties, 
                    color="factor",
                    color_continuous_scale="blues",            
                    range_color=(0,200),
                    hover_name="province",
                    #keyword to match GeoJson
                    locations = "id",
                    scope="asia",
                    #Turkey's center coordinate
                    center = {"lat": 39.925533, "lon": 32.866287},
                    #projection type
                    projection="mercator",
                    #custom data for hover template
                    custom_data=['factor', 'population',"province","region"]

)

#html type: <br> = space ; <b> %{data} </b> = bold ;
#To add data to hover template,  custom data list must be added to px.choropleth
fig.update_traces(
    hovertemplate="<br>".join([
        "<b> %{customdata[2]} </b>",
        "<br>"
        "Province Efficiency Factor: %{customdata[0]}",
        "Province Population: %{customdata[1]}",
        "Province Region: %{customdata[3]}",

    ])
)


fig.update_layout(
    margin={"r":0,"t":0,"l":0,"b":0},
    font=dict(
        family=font,
        size=10,
        color="#011126"
        )
    
)

#update map
fig.update_geos(
    fitbounds="locations",
    showframe=False,
    showcoastlines=False,
    visible=False,
    showsubunits=False,
    showlakes=True,
    #Neighboring countries were made invisible and locations were brought into focus.
    subunitwidth=0
)


fig.update_coloraxes(
    colorbar_tickmode="array",
    colorbar_ticklabelposition="outside",
    colorbar_ypad=30,
    colorbar_title="<br>   <br>Efficiency  <br>Factor",
    colorbar_title_side="bottom",
    colorbar_title_font_size=12,
    colorbar_thickness=13,
    colorbar_len=0.6,
    colorbar_showtickprefix="first"
)


#if you are in spyder, check top right section and click Plots, you can see the graph!
fig.show()

#create html type graph
fig.write_image(graph_location+"graph_province_efficieny_factor_map.pdf")

#create pdf type graph
fig.write_html(graph_location+'graph_province_efficieny_factor_map.html', auto_open=auto_open)

