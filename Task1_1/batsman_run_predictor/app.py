import streamlit as st
import pickle
import pandas as pd
import numpy as np
from tensorflow import keras

pipe = pickle.load(open('model.pkl','rb'))
player=['Hashmatullah Shahidi', 'Rashid Khan', 'Abdul Rahman', 'Fazalhaq Farooqi',
'Mujeeb Ur Rahman', 'Naveen-ul-Haq', 'Noor Ahmad', 'Ibrahim Zadran',
'Ikram Alikhil', 'Najibullah Zadran', 'Rahmanullah Gurbaz', 'Riaz Hassan',
'Azmatullah Omarzai', 'Mohammad Nabi', 'Rahmat Shah', 'AT Carey',
'GJ Maxwell', 'MP Stoinis', 'PJ Cummins', 'JR Hazlewood', 'MA Starc',
'A Zampa', 'TM Head', 'JP Inglis', 'M Labuschagne', 'SPD Smith', 'DA Warner',
'SA Abbott', 'C Green', 'MR Marsh', 'Najmul Hossain Shanto', 'Hasan Mahmud',
'Mustafizur Rahman', 'Nasum Ahmed', 'Shoriful Islam', 'Tanzim Hasan Sakib',
'Taskin Ahmed', 'Anamul Haque', 'Litton Das', 'Mushfiqur Rahim',
'Tanzid Hasan', 'Towhid Hridoy', 'Mahedi Hasan', 'Mahmudullah',
'Mehidy Hasan Miraz', 'BFW de Leede', 'CN Ackermann', 'JC Buttler',
'DJ Willey', 'CR Woakes', 'AAP Atkinson', 'AU Rashid', 'MA Wood', 'SM Curran',
'JM Bairstow', 'HC Brook', 'DJ Malan', 'JE Root', 'MM Ali', 'BA Carse',
'LS Livingstone', 'BA Stokes', 'Ishan Kishan', 'JJ Bumrah', 'KL Rahul',
'Kuldeep Yadav', 'LV van Beek', "MP O'Dowd", 'Mohammed Shami',
'Mohammed Siraj', 'PA van Meekeren', 'A Dutt', 'RE van der Merwe',
'NRJ Croes', 'Saqib Zulfiqar', 'Shariz Ahmad', 'Vikramjit Singh',
'KS Williamson', 'MJ Santner', 'TA Boult', 'LH Ferguson', 'KA Jamieson',
'IS Sodhi', 'TG Southee', 'TWM Latham', 'DP Conway', 'GD Phillips', 'WA Young',
'MS Chapman', 'DJ Mitchell', 'JDS Neesham', 'R Ravindra', 'Babar Azam',
'Mohammad Nawaz (3)', 'Shadab Khan', 'Haris Rauf', 'Hasan Ali',
'Shaheen Shah Afridi', 'Usama Mir', 'Fakhar Zaman', 'Imam-ul-Haq',
'Saud Shakeel', 'Abdullah Shafique', 'Iftikhar Ahmed', 'Mohammad Rizwan',
'Agha Salman', 'Mohammad Wasim (1)', 'M Prasidh Krishna', 'RA Jadeja',
'RG Sharma', 'R Ashwin', 'T Bavuma', 'G Coetzee', 'L Ngidi', 'T Shamsi',
'K Rabada', 'KA Maharaj', 'RR Hendricks', 'AK Markram', 'HE van der Dussen',
'DA Miller', 'H Klaasen', 'Q de Kock', 'M Jansen', 'AL Phehlukwayo',
'SA Edwards', 'SN Thakur', 'SS Iyer', 'Shubman Gill', 'BKG Mendis',
'AD Mathews', 'PVD Chameera', 'D Madushanka', 'CAK Rajitha', 'M Theekshana',
'DN Wellalage', 'FDM Karunaratne', 'P Nissanka', 'MDKJ Perera',
'S Samarawickrama', 'KIC Asalanka', 'DM de Silva', 'MADI Hemantha',
'C Karunaratne', 'SA Yadav', 'SA Engelbrecht', 'AT Nidamanuru', 'V Kohli',
'W Barresi']
opposition = ['Bangladesh', 'Sri Lanka', 'Pakistan', 'India', 'Australia', 'New Zealand',
 'South Africa', 'England', 'Netherlands', 'Afghanistan']

ground = ['Dharamsala', 'Delhi', 'Chennai', 'Pune', 'Lucknow', 'Wankhede', 'Ahmedabad',
 'Bengaluru', 'Eden Gardens', 'Hyderabad']

st.title('Cricket Match Score Predictor')

Player = st.selectbox('Select Player',sorted(player))
col1, col2 = st.columns(2)
with col1:
    Opposition = st.selectbox('Select Opposition', sorted(opposition))
with col2:
    Ground = st.selectbox('Select Ground', sorted(ground))


col3,col4 = st.columns(2)

with col3:
    avg_4s = st.number_input('Average_4s',min_value=0.000,step=0.001)
with col4:
    avg_6s = st.number_input('Average_6s',min_value=0.0)

col5,col6,col7 = st.columns(3)

with col5:
    avg_bf = st.number_input('Average_ball_faced',min_value=0.000,step=0.001)
with col6:
    avg_sr = st.number_input('Average_strike_rate',min_value=0.000,step=0.001)
with col7:
    avg_mins = st.number_input('Average_minutes',min_value=0.000,step=0.001)


if st.button('Predict Score'):
    columns_list = ['avg_6s', 'avg_4', 'avg_bf', 'avg_sr', 'avg_mins', 'player_A Dutt', 'player_A Zampa', 'player_AAP Atkinson', 'player_AD Mathews', 'player_AK Markram', 'player_AL Phehlukwayo', 'player_AT Carey', 'player_AT Nidamanuru', 'player_AU Rashid', 'player_Abdul Rahman', 'player_Abdullah Shafique', 'player_Agha Salman', 'player_Anamul Haque', 'player_Azmatullah Omarzai', 'player_BA Carse', 'player_BA Stokes', 'player_BFW de Leede', 'player_BKG Mendis', 'player_Babar Azam', 'player_C Green', 'player_C Karunaratne', 'player_CAK Rajitha', 'player_CN Ackermann', 'player_CR Woakes', 'player_D Madushanka', 'player_DA Miller', 'player_DA Warner', 'player_DJ Malan', 'player_DJ Mitchell', 'player_DJ Willey', 'player_DM de Silva', 'player_DN Wellalage', 'player_DP Conway', 'player_FDM Karunaratne', 'player_Fakhar Zaman', 'player_Fazalhaq Farooqi', 'player_G Coetzee', 'player_GD Phillips', 'player_GJ Maxwell', 'player_H Klaasen', 'player_HC Brook', 'player_HE van der Dussen', 'player_Haris Rauf', 'player_Hasan Ali', 'player_Hasan Mahmud', 'player_Hashmatullah Shahidi', 'player_IS Sodhi', 'player_Ibrahim Zadran', 'player_Iftikhar Ahmed', 'player_Ikram Alikhil', 'player_Imam-ul-Haq', 'player_Ishan Kishan', 'player_JC Buttler', 'player_JDS Neesham', 'player_JE Root', 'player_JJ Bumrah', 'player_JM Bairstow', 'player_JP Inglis', 'player_JR Hazlewood', 'player_K Rabada', 'player_KA Jamieson', 'player_KA Maharaj', 'player_KIC Asalanka', 'player_KL Rahul', 'player_KS Williamson', 'player_Kuldeep Yadav', 'player_L Ngidi', 'player_LH Ferguson', 'player_LS Livingstone', 'player_LV van Beek', 'player_Litton Das', 'player_M Jansen', 'player_M Labuschagne', 'player_M Prasidh Krishna', 'player_M Theekshana', 'player_MA Starc', 'player_MA Wood', 'player_MADI Hemantha', 'player_MDKJ Perera', 'player_MJ Santner', 'player_MM Ali', 'player_MP O'Dowd', 'player_MP Stoinis', 'player_MR Marsh', 'player_MS Chapman', 'player_Mahedi Hasan', 'player_Mahmudullah', 'player_Mehidy Hasan Miraz', 'player_Mohammad Nabi', 'player_Mohammad Nawaz (3)', 'player_Mohammad Rizwan', 'player_Mohammad Wasim (1)', 'player_Mohammed Shami', 'player_Mohammed Siraj', 'player_Mujeeb Ur Rahman', 'player_Mushfiqur Rahim', 'player_Mustafizur Rahman', 'player_NRJ Croes', 'player_Najibullah Zadran', 'player_Najmul Hossain Shanto', 'player_Nasum Ahmed', 'player_Naveen-ul-Haq', 'player_Noor Ahmad', 'player_P Nissanka', 'player_PA van Meekeren', 'player_PJ Cummins', 'player_PVD Chameera', 'player_Q de Kock', 'player_R Ashwin', 'player_R Ravindra', 'player_RA Jadeja', 'player_RE van der Merwe', 'player_RG Sharma', 'player_RR Hendricks', 'player_Rahmanullah Gurbaz', 'player_Rahmat Shah', 'player_Rashid Khan', 'player_Riaz Hassan', 'player_S Samarawickrama', 'player_SA Abbott', 'player_SA Edwards', 'player_SA Engelbrecht', 'player_SA Yadav', 'player_SM Curran', 'player_SN Thakur', 'player_SPD Smith', 'player_SS Iyer', 'player_Saqib Zulfiqar', 'player_Saud Shakeel', 'player_Shadab Khan', 'player_Shaheen Shah Afridi', 'player_Shariz Ahmad', 'player_Shoriful Islam', 'player_Shubman Gill', 'player_T Bavuma', 'player_T Shamsi', 'player_TA Boult', 'player_TG Southee', 'player_TM Head', 'player_TWM Latham', 'player_Tanzid Hasan', 'player_Tanzim Hasan Sakib', 'player_Taskin Ahmed', 'player_Towhid Hridoy', 'player_Usama Mir', 'player_V Kohli', 'player_Vikramjit Singh', 'player_W Barresi', 'player_WA Young', 'ground_Abu Dhabi', 'ground_Adelaide', 'ground_Ahmedabad', 'ground_Amstelveen', 'ground_Auckland', 'ground_Basseterre', 'ground_Belfast', 'ground_Bengaluru', 'ground_Benoni', 'ground_Birmingham', 'ground_Bloemfontein', 'ground_Bridgetown', 'ground_Brisbane', 'ground_Bristol', 'ground_Bulawayo', 'ground_Cairns', 'ground_Canberra', 'ground_Cape Town', 'ground_Cardiff', 'ground_Centurion', 'ground_Chattogram', 'ground_Chennai', 'ground_Chester-le-Street', 'ground_Christchurch', 'ground_Colombo (PSS)', 'ground_Colombo (RPS)', 'ground_Colombo (SSC)', 'ground_Cuttack', 'ground_Dambulla', 'ground_Darwin', 'ground_Delhi', 'ground_Dharamsala', 'ground_Doha', 'ground_Dubai (DSC)', 'ground_Dublin', 'ground_Dunedin', 'ground_Durban', 'ground_East London', 'ground_Eden Gardens', 'ground_Faisalabad', 'ground_Fatullah', 'ground_Glasgow', 'ground_Gqeberha', 'ground_Guwahati', 'ground_Gwalior', 'ground_Hambantota', 'ground_Hamilton', 'ground_Harare', 'ground_Hobart', 'ground_Hyderabad', 'ground_Indore', 'ground_Jaipur', 'ground_Johannesburg', 'ground_Kanpur', 'ground_Karachi', 'ground_Kimberley', 'ground_Kingston', 'ground_Kochi', 'ground_Lahore', 'ground_Leeds', 'ground_Lord\'s', 'ground_Lucknow', 'ground_Manchester', 'ground_Melbourne', 'ground_Mirpur', 'ground_Mohali', 'ground_Mount Maunganui', 'ground_Multan', 'ground_Nagpur', 'ground_Napier', 'ground_Nelson', 'ground_North Sound', 'ground_Nottingham', 'ground_Paarl', 'ground_Pallekele', 'ground_Perth', 'ground_Port of Spain', 'ground_Potchefstroom', 'ground_Providence', 'ground_Pune', 'ground_Queenstown', 'ground_Raipur', 'ground_Rajkot', 'ground_Ranchi', 'ground_Rawalpindi', 'ground_Rotterdam', 'ground_Sharjah', 'ground_Southampton', 'ground_Sydney', 'ground_Taunton', 'ground_The Hague', 'ground_The Oval', 'ground_Thiruvananthapuram', 'ground_Vadodara', 'ground_Visakhapatnam', 'ground_Wankhede', 'ground_Wellington', 'opposition_Afghanistan', 'opposition_Australia', 'opposition_Bangladesh', 'opposition_England', 'opposition_India', 'opposition_Netherlands', 'opposition_New Zealand','opposition_Pakistan','opposition_South Africa','opposition_Sri Lanka']
    data = np.zeros((1, len(columns_list)))
    df = pd.DataFrame(data, columns=columns_list)
    str1='player_'+player
    df[str1]=1
    str1='opposition_'+opposition
    df[str1]=1
    str1='ground_'+ground
    df[str1]=1
    df['avg_4s']=avg_4s
    df['avg_6s']=avg_6s
    df['avg_bf']=avg_bf
    df['avg_sr']=avg_sr
    df['avg_mins']=avg_mins
    # df = pd.DataFrame(
    #  {'player': [player], 'opposition': [opposition],'ground':[ground],'avg_4s': [avg_4s],'avg_6s':[avg_6s],'avg_bf':[avg_bf],'avg_sr':[avg_sr],'avg_mins':[avg_mins]})
    # print(df)
    # df_encoded = pd.get_dummies(df['player'], columns=player, prefix='player')
    # df = pd.concat([df, df_encoded], axis=1)
    # df_encoded = pd.get_dummies(df['opposition'], columns=opposition, prefix='opposition')
    # df = pd.concat([df, df_encoded], axis=1)
    # df_encoded = pd.get_dummies(df['ground'], columns=ground, prefix='ground')
    # df = pd.concat([df, df_encoded], axis=1)
    # df=df.drop(['player','opposition','ground'])
    result = pipe.predict(df)
    st.header("Predicted Runs - " + str(int(result[0])))


