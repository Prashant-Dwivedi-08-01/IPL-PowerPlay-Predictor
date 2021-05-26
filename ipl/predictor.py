### Custom definitions and classes if any ###
import joblib
import numpy as np
import pandas as pd
import math


def predictRuns(testInput):

    venue = {'Buffalo Park': 1,
            'OUTsurance Oval': 2,
            'De Beers Diamond Oval': 3,
            'Shaheed Veer Narayan Singh International Stadium': 4,
            'Himachal Pradesh Cricket Association Stadium': 5,
            'JSCA International Stadium Complex': 6,
            'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium': 7,
            'Dr DY Patil Sports Academy': 8,
            'Kingsmead': 9,
            'New Wanderers Stadium': 10,
            'SuperSport Park': 11,
            'Sheikh Zayed Stadium': 12,
            'Newlands': 13,
            'Sawai Mansingh Stadium': 14,
            'Barabati Stadium': 15,
            'Maharashtra Cricket Association Stadium': 16,
            'Dubai International Cricket Stadium': 17,
            'M Chinnaswamy Stadium': 18,
            'Eden Gardens': 19,
            'Rajiv Gandhi International Stadium, Uppal': 20,
            "St George's Park": 21,
            'MA Chidambaram Stadium': 22,
            'Wankhede Stadium': 23,
            'Sharjah Cricket Stadium': 24,
            'Narendra Modi Stadium': 25,
            'Punjab Cricket Association Stadium, Mohali': 26,
            'Arun Jaitley Stadium': 27,
            'Subrata Roy Sahara Stadium': 28,
            'Punjab Cricket Association IS Bindra Stadium, Mohali': 29,
            'Rajiv Gandhi International Stadium': 30,
            'Holkar Cricket Stadium': 31,
            'Punjab Cricket Association IS Bindra Stadium': 32,
            'Brabourne Stadium': 33}

    batting_team = {'Chennai Super Kings': 1,
                    'Royal Challengers Bangalore': 2,
                    'Delhi Capitals': 3,
                    'Rajasthan Royals': 4,
                    'Mumbai Indians': 5,
                    'Punjab Kings': 6,
                    'Sunrisers Hyderabad': 7,
                    'Kolkata Knight Riders': 8}


    bowling_team = {'Mumbai Indians': 1,
                    'Sunrisers Hyderabad': 2,
                    'Chennai Super Kings': 3,
                    'Royal Challengers Bangalore': 4,
                    'Rajasthan Royals': 5,
                    'Kolkata Knight Riders': 6,
                    'Delhi Capitals': 7,
                    'Punjab Kings': 8}

     
    prediction = 0

    #model
    print("Hello I am here") 
    filename = "D:\\Jupiter_test\\NPTEL Project\\gui\\ipl\\ipl\\ordinal_enc_ridge_regressor_batsmen.pkl" 
    my_model = joblib.load(filename)

    df_ = pd.read_csv(testInput)

    inputData = np.zeros((1,5))
    #Order:  innings	no_of_batsmen	venue_enc	batting_team_enc	bowling_team_enc
    inputData[0,0] = df_.loc[0,'innings']
    inputData[0,1] = len(df_.loc[0,'batsmen'].split(","))
    inputData[0,2] = df_['venue'].map(venue)
    inputData[0,3] = df_['batting_team'].map(batting_team)
    inputData[0,4] = df_['bowling_team'].map(bowling_team)


    # prediction = int(round(my_model.predict(inputData)[0]))
    prediction = int(round(my_model.predict(inputData)[0]))
    return prediction

