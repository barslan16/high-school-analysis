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
import pandas as pd


#It is the file where the graphics will be created.
graph_location="graphs/"

#===============================================================================#

#Average Efficiency Factors of High Schools
#vs
# Average Percentile of High Schools <br>According to High School Entrance Exam
#Province Factor Bubble Graph

#===============================================================================#

#round to two decimals
provinces["factor"]=[round(x,2) for x in provinces["factor"]]    
provinces["lowest_score"]=[round(x,2) for x in provinces["lowest_score"]]    

#use mono color
colors=[]
for i in range(len(provinces["factor"])):
    colors.append(1)

fig = px.scatter(provinces,
                 x="factor",
                 y="percentile_of_2019",
                 text="province",
                 size="high_school_quota_2019",
                 hover_name="province",
                 color=colors, 
                 color_continuous_scale="blues",  
                 range_color=(0,1),
                 log_y=True,
                 custom_data=['factor', 'lowest_score',"high_school_quota_2019","province"]
                 )


#html type: <br> = space ; <b> %{data} </b> = bold ;
#To add data to hover template,  custom data list must be added to px.scatter.
fig.update_traces(
    textposition='top center',
    hovertemplate="<br>".join([
        "<b> %{customdata[3]} </b>",
        "<br>"
        "Province Efficiency Factor: %{customdata[0]}",
        "Province Exam Score: %{customdata[1]}",
        "Province High School Quota: %{customdata[2]}",

    ])
)


fig.update_layout(

    xaxis_title=" Average Efficiency Factors of High Schools",
    yaxis_title=" Average Percentile of High Schools <br>According to High School Entrance Exam",

    font=dict(
        family=font,
        size=5.5,
        color="#011126"
    ),
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=1.00
    ),
    #background color
    paper_bgcolor="#FFFFFF",
    yaxis = dict(tickfont = dict(size=10)),
    xaxis = dict(tickfont = dict(size=10))
    
)


fig.update_xaxes(title_font_size=title_font_size)
fig.update_yaxes(title_font_size=title_font_size)

#don't show color axes 
fig.update_coloraxes(
    showscale=False,
    #colorbar_tickfont_size=22,
)


#if you are in spyder, check top right section and click Plots, you can see the graph!
fig.show()


#create html type graph
fig.write_image(graph_location+"graph_province_efficiency_factor_bubble.pdf")
#create pdf type graph
fig.write_html(graph_location+'graph_province_efficiency_factor_bubble.html', auto_open=auto_open)
