import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

pipe = pickle.load(open('model.pkl','rb'))

teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka',
 'Netherlands']

cities = ['Colombo',
 'London',
 'Mirpur',
 'Sydney',
 'Centurion',
 'Melbourne',
 'Abu Dhabi',
 'Rangiri',
 'Johannesburg',
 'Adelaide',
 'Birmingham',
 'Perth',
 'Auckland',
 'Brisbane',
 'Dubai',
 'Karachi',
 'Wellington',
 'Cape Town',
 'Southampton',
 'Lahore',
 'Manchester',
 'Hamilton',
 'Cardiff',
 'Durban',
 'Nottingham',
 'Pallekele',
 'Sharjah',
 'Christchurch',
 'Mumbai',
 'Port Elizabeth',
 'Chandigarh',
 'Hambantota',
 'Dhaka',
 'Leeds',
 'Delhi',
 'Antigua',
 'Chennai',
 'Ahmedabad',
 'Guyana',
 'Napier',
 'Chester-le-Street',
 'Trinidad',
 'St Kitts',
 'St Lucia',
 'Jamaica',
 'Pune',
 'Hobart',
 'Barbados',
 'Chattogram',
 'Hyderabad',
 'Harare',
 'Bloemfontein',
 'Kolkata',
 'Bridgetown',
 'Mount Maunganui',
 'Nagpur',
 'Visakhapatnam',
 'Grenada',
 'Chittagong',
 'Rawalpindi',
 'Dunedin',
 'Jaipur',
 'Lucknow',
 'Bristol',
 'Paarl',
 'Rajkot',
 'Multan',
 'Fatullah',
 'Dambulla',
 'Kandy',
 'Nelson',
 'Amstelveen',
 'Indore',
 'Cuttack',
 'Dharamsala',
 'Canberra',
 'Kanpur',
 'Potchefstroom',
 'Ranchi',
 'Kuala Lumpur',
 'East London',
 'Bengaluru',
 'Kimberley',
 'Guwahati',
 'Vadodara',
 'Queenstown',
 'Port of Spain',
 'St Vincent',
 'Cairns',
 'Dublin',
 'Bangalore',
 'Faisalabad',
 'Gqeberha',
 'Kochi',
 'Dominica',
 'Darwin',
 "St George's",
 'Doha',
 'Gwalior',
 'North Sound',
 'Benoni',
 'Bulawayo',
 'Rotterdam',
 'Taunton',
 'Providence',
 'Belfast',
 'Kingstown',
 'Peshawar',
 'Margao']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score',min_value=0,step=1)
with col4:
    overs = st.number_input('Current Overs',min_value=0.0,max_value=50.0)
with col5:
    wickets = st.number_input('Current Wickets',min_value=0,max_value=10,step=1)

last_n = st.number_input('Runs scored in last 5 overs',min_value=0,max_value=current_score,step=1)

if st.button('Predict Score'):
    balls_left = 300 - (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'city':city, 'current_score': [current_score],'balls_left': [balls_left], 'wicketsleft': [wickets], 'crr': [crr], 'last_n': [last_n]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))


