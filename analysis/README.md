# Analysis Part

## Data Filtering
[`data/public_high_schools_data.xlsx`](https://github.com/asen16/high-schools-analysis/blob/main/analysis/data/public_high_schools_data.xlsx) is the data reached as a result of cleaning and merging operations. Data sets of provinces, high schools and students were created by filtering this data:
 - [`data/provinces_dataset.xlsx`](https://github.com/asen16/high-schools-analysis/blob/main/analysis/data/provinces_dataset.xlsx)
 - [`data/high_school_dataset.xlsx`](https://github.com/asen16/high-schools-analysis/blob/main/analysis/data/high_school_dataset.xlsx)
 -  [`data/university_exam_dataset.xlsx`](https://github.com/asen16/high-schools-analysis/blob/main/analysis/data/university_exam_dataset.xlsx)


Change directory:

  ```pyfunctiontypecomment
   cd [Path]
   ```
Run for data filtering:

  ```pyfunctiontypecomment
   python data_filtering.py
   ```

## Regression Analysis

1. To find correlation coefficients
2. To make a heatmap graph of correlation coefficients
3. To create OLS Model and fit
4. To find predicted values and compare with real values
5. To visualize the predicted values vs real values
6. Hypothesis testing 
7. To check Multicollinearity
8. To create Table 1 and Table 2 of the study

  ```pyfunctiontypecomment
   python regression.py
   ```


## Creating Graphs



1. To generate Figure 4 of the study:


  ```pyfunctiontypecomment
   python graph_high_school_exam_bubble.py
   ```

2. To generate Figure 5a of the study:

 ```pyfunctiontypecomment
   python graph_high_school_efficiency_factor_bubble.py
   ```
   
3. To generate Figure 5b of the study:

 ```pyfunctiontypecomment
   python graph_high_school_efficiency_factor_bar.py
   ```
   
4. To generate Figure 7a of the study:

 ```pyfunctiontypecomment
   python graph_province_efficiency_factor_bubble.py
   ```
5. To generate Figure 7b of the study:

 ```pyfunctiontypecomment
   python graph_province_efficieny_factor_map.py
   ```

