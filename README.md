# Obesity Data Analysis
Final project Python for Data Analysis

## Dataset

Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico

https://archive.ics.uci.edu/ml/datasets/Estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition+

The dataset contains the following information :

Feature | Type | Meaning
:------: | :------: | :------:
Gender   | {"Female","Male"}  |
Age| int |
Height | meters |
Weight | kg |
Family history w/ overweight | {"yes","no"} |
Frequent consumption of high caloric food (FAVC) |{"yes","no"} |
Frequency of consumption of vegetables (FCVC)| 1, 2, 3| 1:Never; 2:Sometimes; 3:Always
Number of main meals (NCP)| int |
Consumption of food between meals (CAEC)| {"No","Sometimes","Frequently","Always"} |
Smoke | {"yes","no"} |
Consumption of water daily (CH2O)| 1, 2, 3 |1:Less than a liter;  2:Between 1 and 2L;  3:More than 2L
Calories consumption monitoring (SCC)| {"yes","no"} |
Physical activity frequency (FAF) | 0, 1, 2, 3 | 0:None; 1:1 or 2 days; 2:2 or 4 days; 3:4 or 5 days
Time using technology devices (TUE) | 0, 1, 2 | 0:0-2 hours; 1:3-5 hours; 2:More than 5 hours
Consumption of alcohol (CALC)| {"No","Sometimes","Frequently","Always"}
Transportation used (MTRANS) | {"Automobile","Bike","Motorbike","Public_Transportation","Walking"} |
NObesity | {"Insufficient Weight", "Normal Weight", "Overweight Level I", "Overweight Level II", "Obesity Type I", "Obesity Type II", "Obesity Type III"}|
      
      
      
23% of the data was collected directly from users through a web platform with a survey and the other 77% was generated synthetically using the Weka tool and the SMOTE filter.

## Goal
With this dataset I find interesting to try to predict "NObesity" according to the eating habits and physical condition of an individual without knowing its weight.  

Thus, this will be the goal of this work.
