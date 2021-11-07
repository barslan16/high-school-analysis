# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 01:13:01 2021

@author: Anil Sen & Beyza Arslan

"""

#call required elements from graph_design
from graph_design import font, color_discrete_sequence_bubble, title_font_size,auto_open
#call data from data_filtering
from data_filtering import highschool
#visualization library
import plotly.express as px


#It is the file where the graphics will be created.
graph_location="graphs/"


#===============================================================================

#Average Score of High Schools According to the 2019 University Entrance Exam
#vs
#Percentile of High Schools According to the 2019 High School Entrance Exam
#High School Exam Bubble Graph

#===============================================================================

fig = px.scatter(highschool,
                 x="lowest_score", 
                 y="percentile_of_2019", 
                 color="high_school_type",
                 size="high_school_quota_2019",
                 hover_name="high_school_name",
                 color_discrete_sequence=color_discrete_sequence_bubble,
                 #set max bubble size
                 size_max=20,
                 log_y=True,
                 log_x=True,
                 #custom data for hover template
                 custom_data=['high_school_name', 'high_school_quota_2019', 'high_school_type'])

fig.update_layout(
    xaxis_title="Average Score of High Schools According to the 2019 University Entrance Exam",
    yaxis_title="Percentile of High Schools According to the 2019 High School Entrance Exam",
    legend_title=" High School Type",
        
    legend=dict(
        yanchor="bottom",
        y=0.01,
        xanchor="left",
        x=0.01
    ),
    font=dict(
        family=font,  
        size=8,
        color="#011126"
    )
)

#html type: <br> = space ; <b> %{data} </b> = bold ;
#to add data to hover template,  custom data list must be added to px.scatter
fig.update_traces(
    hovertemplate="<br>".join([
        "<b> %{customdata[0]} </b>",
        "<br>"
        "Average University Entrance Exam Score: %{x}",
        "High School Percentile: %{y}",
        "High School Type: %{customdata[2]}",
        "High School Quota: %{customdata[1]}",
    ])
)

#set font size
fig.update_xaxes(title_font_size=title_font_size)
fig.update_yaxes(title_font_size=title_font_size)

#dont show color axes
fig.update_coloraxes(showscale=False)

#if you are in spyder, check top right section and click Plots, you can see the graph!
fig.show()

#create html type graph
fig.write_html(graph_location+'graph_high_school_exam_bubble.html', auto_open=auto_open)
#create pdf type graph
fig.write_image(graph_location+"graph_high_school_exam_bubble.pdf")
