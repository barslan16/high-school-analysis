# -*- coding: utf-8 -*-
"""
@author: Anil Sen & Beyza Arslan
"""



#call required elements from graph_design
from graph_design import font,title_font_size,auto_open
#call data from data_filtering
from data_filtering import highschool
#visualization library
import plotly.express as px

#It is the file where the graphics will be created.
graph_location="graphs/"


#===============================================================================#

#High School's Efficiency Factor
#vs
#High School
#High School Efficiency Factor Bar Graph

#===============================================================================#


#use mono color
colors=[]
for i in range(len(highschool["factor"])):
    colors.append(1)



fig = px.bar(highschool,
             y="factor",
             x="high_school_name",
             color=colors, 
             color_continuous_scale="blues",
             )

fig.update_layout(
    yaxis_title="High School's Efficiency Factor",
    xaxis_title="High School",
    uniformtext_minsize=6,
    uniformtext_mode='hide',
    barmode='stack',
    xaxis={'categoryorder':'total descending'},
    font=dict(
        family=font,        
        size=4,
        color="#011126"
    ),
    legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=1.00
    )
)


#don't show color axes 
fig.update_coloraxes(showscale=False)


fig.update_xaxes(title_font_size=title_font_size)
fig.update_yaxes(title_font_size=title_font_size)


#if you are in spyder, check top right section and click Plots, you can see the graph!
fig.show()

#create html type graph
fig.write_html(graph_location+'graph_high_school_efficiency_factor_bar.html', auto_open=auto_open)
#create pdf type graph
fig.write_image(graph_location+"graph_high_school_efficiency_factor_bar.pdf")