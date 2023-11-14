# IT496_Data_voyagers_Project3

# 🚀 Data Voyagers


## 1. 🎯 Introduction

In this project, we have done three tasks related to ICC Cricket World Cup 2023. 

## 2. ✨ Task1_1 Maximum runs scorer(Batsman)

- **Dataset Information:-**
  We have scraped the data of batsman's performance in each ODI match from the ESPN website. We merged 150 batsman html files and created the dataset Batsman_matches.csv
- **Features:-**
  The main features included avg_6,avg_4,avg_mins,avg_bf(balls faced),avg_sr(strike rate), player, ground, opposition for predicting runs.
- **Preprocessing:-**
  As player, ground and opposition were categorical and nominal features we used one hot encoding to preprocess them.
  For rest of the numerical columns, we used the standard scaling method.

- **Predictive Goals:-**
  For a given match we predicted the runs that a player is likely to score.<br>
  We predicted which player is most likely to be the highest run scorer.
- **Models**
  Xgboost Regressor-> R2-score- 74.16%
  Random Forest -> R2-score - 70.67%
  LightBgm -> R2-score - 52.08%
  DNN(Deep Neural Network) in Keras -> R2-score - 82.17%
  
  
## ✨ Task1_2

- **Dataset Information:-**
  We have scraped the data of batsman's performance in each match from the cricsheet website. And created ODI_matches.csv.
- **Features:-**
  The main features included batting_team,bowling_team,current_score,wickets_left, city, and last_5(Runs in last five overs) for predicting total runs at the end of the match.
- **Preprocessing:-**
  As batting_team,bowling_team, and city were categorical and nominal features we used one hot encoding to preprocess them.
  For rest of the numerical columns, we used the standard scaling method.

- **Predictive Goals:-**
  To predict first innings match score.

- **Models**
  Xgboost Regressor-> R2-score- 95.8%
  Random Forest -> R2-score - 70.8%

##  ✨ Task2

- **Dataset Information:-**
  We have scraped the data of each batsman and ballers performance in world cup 2023 from ESPN website. And created batsman_data.csv,ballers_data.csv,icc_rankings.csv,wc_stats.csv
  
- **Features:-**
  Batting_data-> Batting_average,runs_scored_before_cwc, number of sixes and fours,ground,player_name
  Bowling_data -> opposition,team,number_of_matches,maiden_overs,Total_overs,number of runs given,wickets taken
  ICC_rankings_data.csv -> current_rank,team, points.
  
- **Preprocessing:-**
  For the rest of the numerical columns, we used the standard scaling method.

- **Predictive Goals:-**
  Predicting points table of ICC CWC23 
  predicting the two finalists team and their 11 playing members
  
- **Models:-**
  Random Forest Classifier -> R2-score - 66.7%

  ## ✨ Task3

- **Dataset Information**
  Same dataset as of task2.
- **Features:-**
  same main features as that of task2.

- **Predictive Goals:-**
  Predicted the Winner of the World Cup.
  
- **Models**
  Random Forest Classifier -> R2-score - 66.7%

## External Dependencies or libraries


## Contributions
- **Natvar** Did'nt do anything
- **Vandan** - 
- **Shekhar** 
- **Shashank**
- **Dhairya** In Task1 predicted 




  
