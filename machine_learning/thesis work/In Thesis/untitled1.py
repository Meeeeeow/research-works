# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 00:15:28 2021

@author: User
"""

import pandas as pd;
import numpy as np;
import datetime;
import time;
from collections import Counter;

df = pd.read_csv('dataset_primo_user_cleaned_data/Activity Class User24.csv');
cols = list(df.columns);

modified_df = df[cols[0:3] +[cols[-1]]]; #csv to fill out day state of  a date


print(modified_df);
cols = list(modified_df.columns);

date_list = [];
full_date_list = [];
j = 0;
i = 0;
activities = [];
data=[];
weekends = 0;
segment = 0;
activity_number = 0;
activity_count = 0;
hours =list(range(0,24));
minutes = list(range(0,60));
timestamps_dataset = [];
ac =[];
for time in df['timestamp']:
    date_list.append(datetime.datetime.fromtimestamp(time).strftime("%m/%d/%Y"));
    full_date_list.append(datetime.datetime.fromtimestamp(time).strftime("%m/%d/%Y %I:%M:00 %p"));
    activities.append(modified_df.iloc[j]['Activity Class'])
    j += 1;
full_date_set = sorted(set(date_list));  


print(full_date_list)
# for date in full_date_list:
#      date_time = datetime.datetime.strptime(date, '%m/%d/%Y %I:%M:%S %p');
#      print(date_time)
for date in full_date_set:
    date_time_obj = datetime.datetime.strptime(date, '%m/%d/%Y');
    timestamps  =datetime.datetime.timestamp(date_time_obj);
    day_name = datetime.datetime.fromtimestamp(timestamps).strftime("%A");
    day_number = int(datetime.datetime.fromtimestamp(timestamps).strftime("%w"));
    print(day_name , day_number , date);
    if day_number == 0:
        weekends = 0;
    else:
        weekends = 1;
        
    for h in hours:
        for m in minutes:
            year = int(date_time_obj.strftime("%Y"));
            month = int(date_time_obj.strftime("%m"));
            day_which = int(date_time_obj.strftime("%d"));
            if h >= 0 and h < 6:
                segment = 0;
            elif  h >= 6 and h < 12:
                segment  = 1;
            elif  h >= 12 and h < 18:
                segemnt = 2;
            elif  h >= 18 and h < 24:
                segment = 3;
                
            date_obj = datetime.datetime(year,month,day_which,h,m,00);
            timestamps_now  = datetime.datetime.timestamp(date_obj);
            
            if date_obj.strftime("%m/%d/%Y %I:%M:00 %p") in full_date_list:
                timestamps_dataset.append(date_obj.strftime("%m/%d/%Y %I:%M:00 %p"));
                activity = activities[i];
                ac.append(activities[i]);
                activity_count = 1;
                if activity == 'Walking':
                    activity_number = 0;
                elif activity == 'Driving':
                    activity_number = 1;
                elif activity == 'Inactive':
                    activity_number = 2;
                elif activity == 'Active':
                    activity_number = 3;
                    
                i+=1;
            else:
                activity_count = 0;
                
            data.append([timestamps_now , date_obj , day_number , weekends , segment , activity_number,activity_count , h , m]);
            
            
                
          
new_df = pd.DataFrame(data, columns=['timestamp', 'date','day number','weekends','segemnt','activity_number','activtiy_count','hours','minutes']);

new_df.to_csv('test.csv');
print(ac == activities);
