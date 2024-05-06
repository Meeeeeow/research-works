# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 00:15:28 2021

@author: User
"""

import pandas as pd;
import numpy as np;
import datetime;
import time;
import random;
from collections import Counter;

timestamps_dataset=[];
full_date_list=[];
year =2021;
data =[];
segment = 0;
day_number = 0;
is_weekday = 0;
is_holiday = 0;
all_activities = ['Walking','Driving','Inactive','Active'];
for i in list(range(1,32)):
    month = 1;
    for l in range(len(all_activities)):
        date = i;
        for j in range(0,24):
            hour = j;
            dates = datetime.datetime(year,month,date,hour,0,0);
            x =  dates.strftime("%m/%d/%Y %I:%M:%S %p");
            full_date_list.append(x);
            date_str = datetime.datetime.strptime(x, "%m/%d/%Y %I:%M:%S %p")
    
            timestamp = int(datetime.datetime.timestamp(date_str))
            
            timestamps_dataset.append(timestamp);
            
            if j >= 0 and j < 6:  #midnight
                    segment = 0;
            elif  j >= 6 and j < 12: #morning
                    segment  = 1;
            elif  j >= 12 and j < 18: #noon
                    segment = 2;
            elif  j >= 18 and j < 24: #night
                    segment = 3; 
                    
            day_name = datetime.datetime.fromtimestamp(timestamp).strftime("%A");
            if day_name == 'Friday':
                day_number = 0;
                is_weekday = 0;
                is_holiday = 1;
            elif day_name == 'Saturday':
                day_number = 1;
                is_weekday = 1;
                is_holiday = 1;
            elif day_name == 'Sunday':
                day_number = 2;
                is_weekday = 1;
                is_holiday = 0;
            elif day_name == 'Monday':
                day_number = 3;
                is_weekday = 1;
                is_holiday = 0;
            elif day_name == 'Tuesday':
                day_number = 4;
                is_weekday = 1;
                is_holiday = 0;
            elif day_name == 'Wednesday':
                day_number = 5;
                is_weekday = 1;
                is_holiday = 0;
            elif day_name == 'Thursday':
                day_number = 6;
                is_weekday = 1;
                is_holiday = 0;
            print(day_name , day_number , x);
            if l == 0 and is_weekday == 1 and is_holiday == 1:  #saturdays and other holidays except friday
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = random.randrange(58,106,3);
                elif j == 11:
                    activity_count = random.randrange(260,310,5);
                elif j == 12:
                    activity_count = random.randrange(240,260,2);
                elif j == 13:
                    activity_count = 0;
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = random.randrange(360,380,2);
                elif j == 18:
                    activity_count = random.randrange(370,400,2);
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
            elif l == 0 and is_weekday == 1 and is_holiday == 0:  #workdays
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = random.randrange(58,106,3);
                elif j == 9:
                    activity_count = random.randrange(300,360,3);
                elif j == 10:
                    activity_count = 0;
                elif j == 11:
                    activity_count = 0;
                elif j == 12:
                    activity_count = 0;
                elif j == 13:
                    activity_count = 0;
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = random.randrange(360,380,2);
                elif j == 18:
                    activity_count = random.randrange(370,400,2);
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
            elif l == 0 and is_weekday == 0 and is_holiday == 1:  #fridays
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = random.randrange(58,106,3);
                elif j == 11:
                    activity_count = random.randrange(58,106,3);
                elif j == 12:
                    activity_count = random.randrange(100,145,3);
                elif j == 13:
                    activity_count = random.randrange(180,300,6);
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = random.randrange(360,380,2);
                elif j == 18:
                    activity_count = random.randrange(370,400,2);
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
            
            if l == 1 and is_weekday == 1 and is_holiday == 1:   
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = 0;
                elif j == 11:
                    activity_count = 0;
                elif j == 12:
                    activity_count = 0;
                elif j == 13:
                    activity_count = 0;
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = 0;
                elif j == 18:
                    activity_count = 0;
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
            elif l == 1 and is_weekday == 1 and is_holiday == 0:
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = 0;
                elif j == 11:
                    activity_count = 0;
                elif j == 12:
                    activity_count = 0;
                elif j == 13:
                    activity_count = 0;
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = 0;
                elif j == 18:
                    activity_count = 0;
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
                    
            elif l == 1 and is_weekday == 0 and is_holiday == 1:
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = 0;
                elif j == 11:
                    activity_count = 0;
                elif j == 12:
                    activity_count = 0;
                elif j == 13:
                    activity_count = 0;
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = 0;
                elif j == 18:
                    activity_count = 0;
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
                
            if l == 2 and is_weekday == 1 and is_holiday == 1:
                if j == 0:
                    activity_count = random.randrange(540,600,3);
                elif j == 1:
                    activity_count =random.randrange(540,600,3);
                elif j == 2:
                    activity_count = random.randrange(700,710,2);
                elif j == 3:
                    activity_count = random.randrange(700,710,2);
                elif j == 4:
                    activity_count = random.randrange(700,710,2);
                elif j == 5:
                    activity_count = random.randrange(700,710,2);
                elif j == 6:
                    activity_count = random.randrange(700,710,2);
                elif j == 7:
                    activity_count = random.randrange(700,710,2);
                elif j == 8:
                    activity_count = random.randrange(700,710,2);
                elif j == 9:
                    activity_count = random.randrange(700,710,2);
                elif j == 10:
                    activity_count = random.randrange(560,590,5);
                elif j == 11:
                    activity_count = random.randrange(280,300,2);
                elif j == 12:
                    activity_count = random.randrange(280,300,2);
                elif j == 13:
                    activity_count = random.randrange(535,540,1);
                elif j == 14:
                    activity_count = random.randrange(535,540,1);
                elif j == 15:
                    activity_count = random.randrange(535,540,1);
                elif j == 16:
                    activity_count = random.randrange(535,540,1);
                elif j == 17:
                    activity_count = random.randrange(160,175,3);
                elif j == 18:
                    activity_count = random.randrange(160,175,3);
                elif j == 19:
                    activity_count = random.randrange(540,600,3);
                elif j == 20:
                    activity_count =random.randrange(540,600,3);
                elif j == 21:
                    activity_count = random.randrange(540,600,3);
                elif j == 22:
                    activity_count = random.randrange(540,600,3);
                elif j == 23:
                    activity_count =random.randrange(540,600,3);
                    
            elif l == 2 and is_weekday == 1 and is_holiday == 0:
                if j == 0:
                    activity_count = random.randrange(540,600,3);
                elif j == 1:
                    activity_count = random.randrange(540,600,3);
                elif j == 2:
                    activity_count =  random.randrange(700,710,2);
                elif j == 3:
                    activity_count =  random.randrange(700,710,2);
                elif j == 4:
                    activity_count =  random.randrange(700,710,2);
                elif j == 5:
                    activity_count =  random.randrange(700,710,2);
                elif j == 6:
                    activity_count =  random.randrange(700,710,2);
                elif j == 7:
                    activity_count =  random.randrange(700,710,2);
                elif j == 8:
                    activity_count = random.randrange(560,590,5);
                elif j == 9:
                    activity_count = random.randrange(170,180,1);
                elif j == 10:
                    activity_count = random.randrange(230,240,2);
                elif j == 11:
                    activity_count = random.randrange(230,240,2);
                elif j == 12:
                    activity_count = random.randrange(230,240,2);
                elif j == 13:
                    activity_count = random.randrange(535,540,1);
                elif j == 14:
                    activity_count = random.randrange(535,540,1);
                elif j == 15:
                    activity_count = random.randrange(535,540,1);
                elif j == 16:
                    activity_count = random.randrange(535,540,1);
                elif j == 17:
                    activity_count = random.randrange(160,175,3);
                elif j == 18:
                    activity_count = random.randrange(160,175,3);
                elif j == 19:
                    activity_count =random.randrange(540,600,3);
                elif j == 20:
                    activity_count = random.randrange(540,600,3);
                elif j == 21:
                    activity_count = random.randrange(540,600,3);
                elif j == 22:
                    activity_count =random.randrange(540,600,3);
                elif j == 23:
                    activity_count = random.randrange(540,600,3);
                    
            elif l == 2 and is_weekday == 0 and is_holiday == 1: # friday
                if j == 0:
                    activity_count = random.randrange(540,600,3);
                elif j == 1:
                    activity_count = random.randrange(540,600,3);
                elif j == 2:
                    activity_count = random.randrange(700,710,2);
                elif j == 3:
                    activity_count = random.randrange(700,710,2);
                elif j == 4:
                    activity_count = random.randrange(700,710,2);
                elif j == 5:
                    activity_count = random.randrange(700,710,2);
                elif j == 6:
                    activity_count = random.randrange(700,710,2);
                elif j == 7:
                    activity_count = random.randrange(700,710,2);
                elif j == 8:
                    activity_count = random.randrange(700,710,2);
                elif j == 9:
                    activity_count = random.randrange(700,710,2);
                elif j == 10:
                    activity_count = random.randrange(560,590,5);
                elif j == 11:
                    activity_count = random.randrange(280,300,2);
                elif j == 12:
                    activity_count = random.randrange(460,470,1);
                elif j == 13:
                    activity_count = random.randrange(240,250,1);
                elif j == 14:
                    activity_count = random.randrange(535,540,1);
                elif j == 15:
                    activity_count = random.randrange(535,540,1);
                elif j == 16:
                    activity_count = random.randrange(535,540,1);
                elif j == 17:
                    activity_count = random.randrange(160,175,3);
                elif j == 18:
                    activity_count = random.randrange(160,175,3);
                elif j == 19:
                    activity_count = random.randrange(540,600,3);
                elif j == 20:
                    activity_count = random.randrange(540,600,3);
                elif j == 21:
                    activity_count =random.randrange(540,600,3);
                elif j == 22:
                    activity_count = random.randrange(540,600,3);
                elif j == 23:
                    activity_count = random.randrange(540,600,3);
                
            if l == 3 and is_weekday == 1 and is_holiday == 1:
                if j == 0:
                    activity_count = random.randrange(15,108,3);
                elif j == 1:
                    activity_count = random.randrange(15,108,3);
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count =  0;
                elif j == 11:
                    activity_count =  random.randrange(80,90,1);
                elif j == 12:
                    activity_count =  random.randrange(170,180,1);
                elif j == 13:
                    activity_count = random.randrange(84,144,3);
                elif j == 14:
                    activity_count = random.randrange(84,144,3);
                elif j == 15:
                    activity_count = random.randrange(84,144,3);
                elif j == 16:
                    activity_count = random.randrange(84,144,3);
                elif j == 17:
                    activity_count = random.randrange(78,84,1);
                elif j == 18:
                    activity_count = random.randrange(72,78,1);
                elif j == 19:
                    activity_count = random.randrange(15,108,3);
                elif j == 20:
                    activity_count = random.randrange(15,108,3);
                elif j == 21:
                    activity_count = random.randrange(15,108,3);
                elif j == 22:
                    activity_count = random.randrange(15,108,3);
                elif j == 23:
                    activity_count = random.randrange(15,108,3);
                    
            elif l == 3 and is_weekday == 1 and is_holiday == 0:
                if j == 0:
                    activity_count = random.randrange(15,108,3);
                elif j == 1:
                    activity_count = random.randrange(15,108,3);
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = random.randrange(84,144,2);
                elif j == 10:
                    activity_count = random.randrange(400,444,2);
                elif j == 11:
                    activity_count = random.randrange(400,444,2);
                elif j == 12:
                    activity_count = random.randrange(400,444,2);
                elif j == 13:
                    activity_count = random.randrange(84,144,3);
                elif j == 14:
                    activity_count = random.randrange(84,144,3);
                elif j == 15:
                    activity_count = random.randrange(84,144,3);
                elif j == 16:
                    activity_count = random.randrange(84,144,3);
                elif j == 17:
                    activity_count = random.randrange(78,84,1);
                elif j == 18:
                    activity_count = random.randrange(72,78,1);
                elif j == 19:
                    activity_count = random.randrange(15,108,3);
                elif j == 20:
                    activity_count = random.randrange(15,108,3);
                elif j == 21:
                    activity_count = random.randrange(15,108,3);
                elif j == 22:
                    activity_count = random.randrange(15,108,3);
                elif j == 23:
                    activity_count = random.randrange(15,108,3);
                    
            elif l == 3 and is_weekday == 0 and is_holiday == 1:
                if j == 0:
                    activity_count = random.randrange(15,108,3);
                elif j == 1:
                    activity_count = random.randrange(15,108,3);
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = 0;
                elif j == 11:
                    activity_count = random.randrange(150,276,3);
                elif j == 12:
                    activity_count = random.randrange(0,84,3);
                elif j == 13:
                    activity_count = random.randrange(90,118,2);
                elif j == 14:
                    activity_count = random.randrange(84,144,3);
                elif j == 15:
                    activity_count = random.randrange(84,144,3);
                elif j == 16:
                    activity_count = random.randrange(84,144,3);
                elif j == 17:
                    activity_count = random.randrange(78,84,1);
                elif j == 18:
                    activity_count = random.randrange(72,78,1);
                elif j == 19:
                    activity_count = random.randrange(15,108,3);
                elif j == 20:
                    activity_count = random.randrange(15,108,3);
                elif j == 21:
                    activity_count = random.randrange(15,108,3);
                elif j == 22:
                    activity_count = random.randrange(15,108,3);
                elif j == 23:
                    activity_count = random.randrange(15,108,3);
                    
            data.append([timestamp,x,j,segment,day_number,i,1,is_weekday,is_holiday,l,activity_count])
    
for i in list(range(1,29)):
    month = 2;
    for l in range(len(all_activities)):
        date = i;
        for j in range(0,24):
            hour = j;
            dates = datetime.datetime(year,month,date,hour,0,0);
            x =  dates.strftime("%m/%d/%Y %I:%M:%S %p");
            full_date_list.append(x);
            date_str = datetime.datetime.strptime(x, "%m/%d/%Y %I:%M:%S %p")
    
            timestamp = int(datetime.datetime.timestamp(date_str))
            
            timestamps_dataset.append(timestamp);
            
            if j >= 0 and j < 6:  #midnight
                    segment = 0;
            elif  j >= 6 and j < 12: #morning
                    segment  = 1;
            elif  j >= 12 and j < 18: #noon
                    segment = 2;
            elif  j >= 18 and j < 24: #night
                    segment = 3; 
                    
            day_name = datetime.datetime.fromtimestamp(timestamp).strftime("%A");
            if day_name == 'Friday':
                day_number = 0;
                is_weekday = 0;
                is_holiday = 1;
            elif day_name == 'Saturday':
                day_number = 1;
                is_weekday = 1;
                is_holiday = 1;
            elif day_name == 'Sunday':
                day_number = 2;
                is_weekday = 1;
                is_holiday = 0;
            elif day_name == 'Monday':
                day_number = 3;
                is_weekday = 1;
                is_holiday = 0;
            elif day_name == 'Tuesday':
                day_number = 4;
                is_weekday = 1;
                is_holiday = 0;
            elif day_name == 'Wednesday':
                day_number = 5;
                is_weekday = 1;
                is_holiday = 0;
            elif day_name == 'Thursday':
                day_number = 6;
                is_weekday = 1;
                is_holiday = 0;
            print(day_name , day_number , x);   
            
            if i == 21:
                is_holiday = 1;
            if l == 0 and is_weekday == 1 and is_holiday == 1:  #saturdays and other holidays except friday
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = random.randrange(58,106,3);
                elif j == 11:
                    activity_count = random.randrange(260,310,5);
                elif j == 12:
                    activity_count = random.randrange(240,260,2);
                elif j == 13:
                    activity_count = 0;
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = random.randrange(360,380,2);
                elif j == 18:
                    activity_count = random.randrange(370,400,2);
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
            elif l == 0 and is_weekday == 1 and is_holiday == 0:  #workdays
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = random.randrange(58,106,3);
                elif j == 9:
                    activity_count = random.randrange(300,360,3);
                elif j == 10:
                    activity_count = 0;
                elif j == 11:
                    activity_count = 0;
                elif j == 12:
                    activity_count = 0;
                elif j == 13:
                    activity_count = 0;
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = random.randrange(360,380,2);
                elif j == 18:
                    activity_count = random.randrange(370,400,2);
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
            elif l == 0 and is_weekday == 0 and is_holiday == 1:  #fridays
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = random.randrange(58,106,3);
                elif j == 11:
                    activity_count = random.randrange(58,106,3);
                elif j == 12:
                    activity_count = random.randrange(100,145,3);
                elif j == 13:
                    activity_count = random.randrange(180,300,6);
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = random.randrange(360,380,2);
                elif j == 18:
                    activity_count = random.randrange(370,400,2);
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
            
            if l == 1 and is_weekday == 1 and is_holiday == 1:   
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = 0;
                elif j == 11:
                    activity_count = 0;
                elif j == 12:
                    activity_count = 0;
                elif j == 13:
                    activity_count = 0;
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = 0;
                elif j == 18:
                    activity_count = 0;
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
            elif l == 1 and is_weekday == 1 and is_holiday == 0:
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = 0;
                elif j == 11:
                    activity_count = 0;
                elif j == 12:
                    activity_count = 0;
                elif j == 13:
                    activity_count = 0;
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = 0;
                elif j == 18:
                    activity_count = 0;
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
                    
            elif l == 1 and is_weekday == 0 and is_holiday == 1:
                if j == 0:
                    activity_count = 0;
                elif j == 1:
                    activity_count = 0;
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = 0;
                elif j == 11:
                    activity_count = 0;
                elif j == 12:
                    activity_count = 0;
                elif j == 13:
                    activity_count = 0;
                elif j == 14:
                    activity_count = 0;
                elif j == 15:
                    activity_count = 0;
                elif j == 16:
                    activity_count = 0;
                elif j == 17:
                    activity_count = 0;
                elif j == 18:
                    activity_count = 0;
                elif j == 19:
                    activity_count = 0;
                elif j == 20:
                    activity_count = 0;
                elif j == 21:
                    activity_count = 0;
                elif j == 22:
                    activity_count = 0;
                elif j == 23:
                    activity_count = 0;
                
            if l == 2 and is_weekday == 1 and is_holiday == 1:
                if j == 0:
                    activity_count = random.randrange(540,600,3);
                elif j == 1:
                    activity_count =random.randrange(540,600,3);
                elif j == 2:
                    activity_count = random.randrange(700,710,2);
                elif j == 3:
                    activity_count = random.randrange(700,710,2);
                elif j == 4:
                    activity_count = random.randrange(700,710,2);
                elif j == 5:
                    activity_count = random.randrange(700,710,2);
                elif j == 6:
                    activity_count = random.randrange(700,710,2);
                elif j == 7:
                    activity_count = random.randrange(700,710,2);
                elif j == 8:
                    activity_count = random.randrange(700,710,2);
                elif j == 9:
                    activity_count = random.randrange(700,710,2);
                elif j == 10:
                    activity_count = random.randrange(560,590,5);
                elif j == 11:
                    activity_count = random.randrange(280,300,2);
                elif j == 12:
                    activity_count = random.randrange(280,300,2);
                elif j == 13:
                    activity_count = random.randrange(535,540,1);
                elif j == 14:
                    activity_count = random.randrange(535,540,1);
                elif j == 15:
                    activity_count = random.randrange(535,540,1);
                elif j == 16:
                    activity_count = random.randrange(535,540,1);
                elif j == 17:
                    activity_count = random.randrange(160,175,3);
                elif j == 18:
                    activity_count = random.randrange(160,175,3);
                elif j == 19:
                    activity_count = random.randrange(540,600,3);
                elif j == 20:
                    activity_count =random.randrange(540,600,3);
                elif j == 21:
                    activity_count = random.randrange(540,600,3);
                elif j == 22:
                    activity_count = random.randrange(540,600,3);
                elif j == 23:
                    activity_count =random.randrange(540,600,3);
                    
            elif l == 2 and is_weekday == 1 and is_holiday == 0:
                if j == 0:
                    activity_count = random.randrange(540,600,3);
                elif j == 1:
                    activity_count = random.randrange(540,600,3);
                elif j == 2:
                    activity_count =  random.randrange(700,710,2);
                elif j == 3:
                    activity_count =  random.randrange(700,710,2);
                elif j == 4:
                    activity_count =  random.randrange(700,710,2);
                elif j == 5:
                    activity_count =  random.randrange(700,710,2);
                elif j == 6:
                    activity_count =  random.randrange(700,710,2);
                elif j == 7:
                    activity_count =  random.randrange(700,710,2);
                elif j == 8:
                    activity_count = random.randrange(560,590,5);
                elif j == 9:
                    activity_count = random.randrange(170,180,1);
                elif j == 10:
                    activity_count = random.randrange(230,240,2);
                elif j == 11:
                    activity_count = random.randrange(230,240,2);
                elif j == 12:
                    activity_count = random.randrange(230,240,2);
                elif j == 13:
                    activity_count = random.randrange(535,540,1);
                elif j == 14:
                    activity_count = random.randrange(535,540,1);
                elif j == 15:
                    activity_count = random.randrange(535,540,1);
                elif j == 16:
                    activity_count = random.randrange(535,540,1);
                elif j == 17:
                    activity_count = random.randrange(160,175,3);
                elif j == 18:
                    activity_count = random.randrange(160,175,3);
                elif j == 19:
                    activity_count =random.randrange(540,600,3);
                elif j == 20:
                    activity_count = random.randrange(540,600,3);
                elif j == 21:
                    activity_count = random.randrange(540,600,3);
                elif j == 22:
                    activity_count =random.randrange(540,600,3);
                elif j == 23:
                    activity_count = random.randrange(540,600,3);
                    
            elif l == 2 and is_weekday == 0 and is_holiday == 1: # friday
                if j == 0:
                    activity_count = random.randrange(540,600,3);
                elif j == 1:
                    activity_count = random.randrange(540,600,3);
                elif j == 2:
                    activity_count = random.randrange(700,710,2);
                elif j == 3:
                    activity_count = random.randrange(700,710,2);
                elif j == 4:
                    activity_count = random.randrange(700,710,2);
                elif j == 5:
                    activity_count = random.randrange(700,710,2);
                elif j == 6:
                    activity_count = random.randrange(700,710,2);
                elif j == 7:
                    activity_count = random.randrange(700,710,2);
                elif j == 8:
                    activity_count = random.randrange(700,710,2);
                elif j == 9:
                    activity_count = random.randrange(700,710,2);
                elif j == 10:
                    activity_count = random.randrange(560,590,5);
                elif j == 11:
                    activity_count = random.randrange(280,300,2);
                elif j == 12:
                    activity_count = random.randrange(460,470,1);
                elif j == 13:
                    activity_count = random.randrange(240,250,1);
                elif j == 14:
                    activity_count = random.randrange(535,540,1);
                elif j == 15:
                    activity_count = random.randrange(535,540,1);
                elif j == 16:
                    activity_count = random.randrange(535,540,1);
                elif j == 17:
                    activity_count = random.randrange(160,175,3);
                elif j == 18:
                    activity_count = random.randrange(160,175,3);
                elif j == 19:
                    activity_count = random.randrange(540,600,3);
                elif j == 20:
                    activity_count = random.randrange(540,600,3);
                elif j == 21:
                    activity_count =random.randrange(540,600,3);
                elif j == 22:
                    activity_count = random.randrange(540,600,3);
                elif j == 23:
                    activity_count = random.randrange(540,600,3);
                
            if l == 3 and is_weekday == 1 and is_holiday == 1:
                if j == 0:
                    activity_count = random.randrange(15,108,3);
                elif j == 1:
                    activity_count = random.randrange(15,108,3);
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count =  0;
                elif j == 11:
                    activity_count =  random.randrange(80,90,1);
                elif j == 12:
                    activity_count =  random.randrange(170,180,1);
                elif j == 13:
                    activity_count = random.randrange(84,144,3);
                elif j == 14:
                    activity_count = random.randrange(84,144,3);
                elif j == 15:
                    activity_count = random.randrange(84,144,3);
                elif j == 16:
                    activity_count = random.randrange(84,144,3);
                elif j == 17:
                    activity_count = random.randrange(78,84,1);
                elif j == 18:
                    activity_count = random.randrange(72,78,1);
                elif j == 19:
                    activity_count = random.randrange(15,108,3);
                elif j == 20:
                    activity_count = random.randrange(15,108,3);
                elif j == 21:
                    activity_count = random.randrange(15,108,3);
                elif j == 22:
                    activity_count = random.randrange(15,108,3);
                elif j == 23:
                    activity_count = random.randrange(15,108,3);
                    
            elif l == 3 and is_weekday == 1 and is_holiday == 0:
                if j == 0:
                    activity_count = random.randrange(15,108,3);
                elif j == 1:
                    activity_count = random.randrange(15,108,3);
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = random.randrange(84,144,2);
                elif j == 10:
                    activity_count = random.randrange(400,444,2);
                elif j == 11:
                    activity_count = random.randrange(400,444,2);
                elif j == 12:
                    activity_count = random.randrange(400,444,2);
                elif j == 13:
                    activity_count = random.randrange(84,144,3);
                elif j == 14:
                    activity_count = random.randrange(84,144,3);
                elif j == 15:
                    activity_count = random.randrange(84,144,3);
                elif j == 16:
                    activity_count = random.randrange(84,144,3);
                elif j == 17:
                    activity_count = random.randrange(78,84,1);
                elif j == 18:
                    activity_count = random.randrange(72,78,1);
                elif j == 19:
                    activity_count = random.randrange(15,108,3);
                elif j == 20:
                    activity_count = random.randrange(15,108,3);
                elif j == 21:
                    activity_count = random.randrange(15,108,3);
                elif j == 22:
                    activity_count = random.randrange(15,108,3);
                elif j == 23:
                    activity_count = random.randrange(15,108,3);
                    
            elif l == 3 and is_weekday == 0 and is_holiday == 1:
                if j == 0:
                    activity_count = random.randrange(15,108,3);
                elif j == 1:
                    activity_count = random.randrange(15,108,3);
                elif j == 2:
                    activity_count = 0;
                elif j == 3:
                    activity_count = 0;
                elif j == 4:
                    activity_count = 0;
                elif j == 5:
                    activity_count = 0;
                elif j == 6:
                    activity_count = 0;
                elif j == 7:
                    activity_count = 0;
                elif j == 8:
                    activity_count = 0;
                elif j == 9:
                    activity_count = 0;
                elif j == 10:
                    activity_count = 0;
                elif j == 11:
                    activity_count = random.randrange(150,276,3);
                elif j == 12:
                    activity_count = random.randrange(0,84,3);
                elif j == 13:
                    activity_count = random.randrange(90,118,2);
                elif j == 14:
                    activity_count = random.randrange(84,144,3);
                elif j == 15:
                    activity_count = random.randrange(84,144,3);
                elif j == 16:
                    activity_count = random.randrange(84,144,3);
                elif j == 17:
                    activity_count = random.randrange(78,84,1);
                elif j == 18:
                    activity_count = random.randrange(72,78,1);
                elif j == 19:
                    activity_count = random.randrange(15,108,3);
                elif j == 20:
                    activity_count = random.randrange(15,108,3);
                elif j == 21:
                    activity_count = random.randrange(15,108,3);
                elif j == 22:
                    activity_count = random.randrange(15,108,3);
                elif j == 23:
                    activity_count = random.randrange(15,108,3);
            
            data.append([timestamp,x,j,segment,day_number,i,2,is_weekday,is_holiday,l,activity_count])
new_df = pd.DataFrame(data, columns=['timestamp', 'date','hour','segemnt','day_of_week','day_of_month','month','is_weekday','is_holiday','activity','activity_count']);

print(new_df);
new_df.to_csv('test1.csv' , index = False);

# print(len(timestamps_dataset));
# print(len(full_date_list));


