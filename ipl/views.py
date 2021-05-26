from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
import numpy as np
from .predictor import  predictRuns

# def result(request):
def home(request):
    if request.method == 'POST':
        venue = request.POST["venue"]
        batting_team = request.POST["batting_team"]
        bowling_team = request.POST["bowling_team"]
        innings = int(request.POST["innings"])

        batsmen = []
        i = 1
        no_of_bt = int(request.POST.get('no-of-bt'))
        print(no_of_bt)
        while(no_of_bt > 0):
            bt = request.POST.get(f'bt-{i}')
            if(bt != None):
                print(bt)
                batsmen.append(bt)
            i = i+1
            no_of_bt =  no_of_bt-1
        print(batsmen)

        bowlers = []
        i = 1
        no_of_bl = int(request.POST.get('no-of-bl'))
        print(no_of_bl)
        while( no_of_bl > 0):
            bl = request.POST.get(f'bl-{i}')
            if(bl != None):
                print(bl)
                bowlers.append(bl)
            i = i+1
            no_of_bl =  no_of_bl-1
        print(bowlers)

        

        #Creating CSV file
        # Venue,Innings,batting,bowling,batsmen,bowlers
        bt_str = ""
        for bt in batsmen:
            bt_str+=bt+","
        bt_str = bt_str[:-1]

        bl_str = ""
        for bl in bowlers:
            bl_str+=bl+","
        bl_str =  bl_str[:-1]
        print(bl_str)


        data = np.array([[venue, innings, batting_team, bowling_team, bt_str, bl_str]])
        df = pd.DataFrame(data = data, columns=['venue', 'innings', 'batting_team', 'bowling_team','batsmen','bowlers'])
        # df.reset_index(drop=True, inplace=True)
        df.to_csv("inputFile.csv", index=False)
     

        runs = predictRuns('D:\\Jupiter_test\\NPTEL Project\\gui\\ipl\\inputFile.csv')
        print(runs)

        params = {
            'response':True,
            'venue':  venue,
            'bowling_team':  bowling_team,
            'batting_team': batting_team,
            'innings':  innings,
            'batsmen': batsmen,
            'bowlers': bowlers,
            'runs': runs
        }
        return render(request, "home.html", params)
    else:
        params = {
            'response':False
        }
        return render(request, "home.html")