#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:28:32 2021

@author: Anil Sen & Beyza Arslan
"""

# =============================================================================
# Importing necessary libraries
# =============================================================================

import pandas as pd
import numpy as np

#for dataset
from data_filtering import highschool
from data_filtering import university_exam_data

#for regression/statistical analysis
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
from patsy import dmatrices

#for visualization
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

#for LaTex table
from stargazer.stargazer import Stargazer
from IPython.core.display import HTML

# =============================================================================
# =============================================================================
# EFFICIENCY FACTOR REGRESSION
# =============================================================================
# =============================================================================

#define location for output
graph_location="graphs/"
table_location="table/"


# =============================================================================
# Checking correlation and visualize
# =============================================================================

#create new dataframe and remove unnecessary columns
to_corr_check = highschool
to_corr_check = to_corr_check.drop(columns = ["factor", "bubblesize", "province", "lowest_score" ])

#find correlation coefficients
to_corr_check.corr()

#visualize
sns.heatmap(to_corr_check.corr())

#save as png file
plt.savefig(graph_location+'correlation-coefficients.png')

# =============================================================================
# Creating OLS Model for Efficiency Factor Regression
# =============================================================================

#remove 0 values of factor
highschool= highschool[highschool['factor'] != 0]

#insert log(percentile_of_2019) to dataframe
highschool.insert(5, "log_percentile_of_2019", np.log(highschool["percentile_of_2019"]))

#create OLS Model - Define Y and X variables
factor_model = ols('factor ~   log_percentile_of_2019  + C(high_school_type)  +   average_diploma_grade + high_school_with_prep + high_school_dormitory + gdpdata ', data=highschool)
y = highschool["factor"]
X = highschool[['log_percentile_of_2019','high_school_type' , "average_diploma_grade" , "high_school_with_prep" , "high_school_dormitory" , "gdpdata"]]

#fit Model
fitted_factor_model = factor_model.fit()
fitted_factor_model.get_robustcov_results().summary()


# =============================================================================
# Find Predicted Values
# =============================================================================

X = sm.add_constant(X)
predicted_values = fitted_factor_model.predict(X)

#visualize predicted vs real values
highschool = highschool.rename_axis('index1').reset_index()
highschool.insert(1, "predicted_factor", predicted_values)
highschool.insert(2, 'real_factor', highschool['factor'])
fig_prediction_vs_factor = px.line(highschool, x="index1", y=highschool.columns[1:3] )
fig_prediction_vs_factor.update_traces(mode="lines", hovertemplate=None)
fig_prediction_vs_factor.update_layout(hovermode="x")
fig_prediction_vs_factor.update_layout(
    xaxis_title="Indexes",
    yaxis_title="Predicted and Real Factor Value ",
    legend_title="Predicted vs Real",
        
    legend=dict(
        yanchor="bottom",
        y=0.01,
        xanchor="left",
        x=0.01
    ),
    font=dict(
        family="Roboto",  
        size=8,
        color="#011126"
    )
)
fig_prediction_vs_factor.show()
fig_prediction_vs_factor.write_html(graph_location+"prediction_vs_factor.html",auto_open=True) 
fig_prediction_vs_factor.write_image(graph_location+"prediction_vs_factor.pdf") #save as pdf file
# =============================================================================
# Hypothesis Testing and Check Multicollinearity
# =============================================================================

#find t-score
hypothesis = 'high_school_dormitory = 0' #can used with other hypothesis
t_test = fitted_factor_model.t_test(hypothesis)

#calculate VIF 
y, X = dmatrices('factor ~   log_percentile_of_2019  + high_school_type  +   average_diploma_grade + high_school_with_prep + high_school_dormitory + gdpdata ', data=highschool, return_type='dataframe')
vif_factor = pd.DataFrame()
vif_factor['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif_factor['variable'] = X.columns

# =============================================================================
# Create LaTex Table
# =============================================================================

stargazer = Stargazer([fitted_factor_model])
HTML(stargazer.render_html())
f = open(table_location+'my_factor_reg.tex', 'w')
f.write(stargazer.render_latex())
f.close()

# =============================================================================
# =============================================================================
# EXAM SCORE REGRESSION
# =============================================================================
# =============================================================================


# =============================================================================
# Creating OLS Model for Exam Score Regression
# =============================================================================

#remove 0 values of factor
university_exam_data= university_exam_data[university_exam_data['lowest_score'] != 0]

#insert log(percentile_of_2019) to dataframe
university_exam_data.insert(5, "log_percentile_of_2019", np.log(university_exam_data["percentile_of_2019"]))

#create OLS Model - Define Y and X variables
exam_model = ols('lowest_score ~   log_percentile_of_2019  + C(high_school_type)  + newly_graduated_student +  average_diploma_grade + high_school_with_prep + high_school_dormitory + gdpdata ', data=university_exam_data)
y_exam = university_exam_data["lowest_score"]
X_exam = university_exam_data[['log_percentile_of_2019','high_school_type' ,"newly_graduated_student", "average_diploma_grade" , "high_school_with_prep" , "high_school_dormitory" , "gdpdata"]]

#fit Model
fitted_exam_model = exam_model.fit()
fitted_exam_model.get_robustcov_results().summary()


# =============================================================================
# Find Predicted Values
# =============================================================================

X_exam = sm.add_constant(X_exam)
predicted_values_exam = fitted_exam_model.predict(X_exam)

#visualize predicted vs real values
university_exam_data = university_exam_data.rename_axis('index1').reset_index()
university_exam_data.insert(1, "predicted_exam_score", predicted_values_exam)
university_exam_data.insert(2, 'real_score', university_exam_data['lowest_score'])
fig_prediction_vs_exam = px.line(university_exam_data, x="index1", y=university_exam_data.columns[1:3] )
fig_prediction_vs_exam.update_traces(mode="lines", hovertemplate=None)
fig_prediction_vs_exam.update_layout(hovermode="x")
fig_prediction_vs_exam.update_layout(
    xaxis_title="Indexes",
    yaxis_title="Predicted and Real Exam Score",
    legend_title="Predicted vs Real",
        
    legend=dict(
        yanchor="bottom",
        y=0.01,
        xanchor="left",
        x=0.01
    ),
    font=dict(
        family="Roboto",  
        size=8,
        color="#011126"
    )
)
fig_prediction_vs_exam.show()
fig_prediction_vs_exam.write_html(graph_location+"prediction_vs_exam.html",auto_open=True)
fig_prediction_vs_exam.write_image(graph_location+"prediction_vs_exam.pdf") #save as pdf file

# =============================================================================
# Hypothesis Testing and Check Multicollinearity
# =============================================================================

#find t-score
hypothesis_exam = 'average_diploma_grade = 0' #can used with other hypothesis
t_test = fitted_exam_model.t_test(hypothesis_exam)

#calculate VIF 
y_exam, X_exam = dmatrices('lowest_score ~   log_percentile_of_2019  + C(high_school_type)  + newly_graduated_student +  average_diploma_grade + high_school_with_prep + high_school_dormitory + gdpdata ', data=university_exam_data, return_type='dataframe')
vif_exam = pd.DataFrame()
vif_exam['VIF'] = [variance_inflation_factor(X_exam.values, i) for i in range(X_exam.shape[1])]
vif_exam['variable'] = X_exam.columns

# =============================================================================
# Create LaTex Table
# =============================================================================

stargazer = Stargazer([fitted_exam_model])
HTML(stargazer.render_html())
f = open(table_location+'my_exam_reg.tex', 'w')
f.write(stargazer.render_latex())
f.close()



