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

df = pd.read_csv('dataset_primo_user_cleaned_data/Activity Class User35.csv');
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
timestamps_dataset1 = [];
ac =[];
for time in df['timestamp']:
    date_list.append(datetime.datetime.fromtimestamp(time).strftime("%m/%d/%Y"));
    full_date_list.append(datetime.datetime.fromtimestamp(time).strftime("%m/%d/%Y %I:%M:00 %p"));
    activities.append(modified_df.iloc[j]['Activity Class'])
    j += 1;
full_date_set = sorted(set(date_list));  

all_activities = ['Walking', 'Driving' ,'Inactive' , 'Active']; # 0 1 2 3

print(full_date_list)
print(full_date_set);
for dates in full_date_list:
      date = datetime.datetime.strptime(dates, "%m/%d/%Y %I:%M:00 %p")

      timestamp = int(datetime.datetime.timestamp(date))

      timestamps_dataset.append(timestamp);
print(len(timestamps_dataset));

num_cols = len(modified_df.axes[1]);

modified_df.insert(num_cols  , "modified timestamps", timestamps_dataset);

for date in full_date_set:
    date_time_obj = datetime.datetime.strptime(date, '%m/%d/%Y');
    timestamps  =datetime.datetime.timestamp(date_time_obj);
    timestamps_dataset.append(timestamps);
    day_name = datetime.datetime.fromtimestamp(timestamps).strftime("%A");
    day_number = int(datetime.datetime.fromtimestamp(timestamps).strftime("%w"));
    print(day_name , day_number , date);
    if day_number == 0:
        weekends = 0;
    else:
        weekends = 1;
    for l in range(len(all_activities)):    
        for h in hours:
            for m in minutes:
                year = int(date_time_obj.strftime("%Y"));
                month = int(date_time_obj.strftime("%m"));
                day_which = int(date_time_obj.strftime("%d"));
                if h >= 0 and h < 6:  #midnight
                    segment = 0;
                elif  h >= 6 and h < 12: #morning
                    segment  = 1;
                elif  h >= 12 and h < 18: #noon
                    segment = 2;
                elif  h >= 18 and h < 24: #night
                    segment = 3;
                    
                date_obj = datetime.datetime(year,month,day_which,h,m,00);
                timestamps_now  = datetime.datetime.timestamp(date_obj);
                
                if date_obj.strftime("%m/%d/%Y %I:%M:00 %p") in full_date_list:
                    date = datetime.datetime.strptime(date_obj.strftime("%m/%d/%Y %I:%M:00 %p"), "%m/%d/%Y %I:%M:00 %p")

                    timestamp = int(datetime.datetime.timestamp(date))
                    
                    mod2 = modified_df.loc[(modified_df['modified timestamps'] == timestamp) & (modified_df['Activity Class'] == all_activities[l])];
                    #print(f' i am {mod2}');
                    if mod2.empty:
                        activity_count = 0;
                    else:
                        activity = mod2.iloc[0]['Activity Class'] 
                        ac.append(activity);
                        activity_count = 1;
                else:
                    activity_count = 0;
                    
                data.append([timestamps_now , date_obj , day_number , weekends , segment , l,activity_count , h , m]);
            
            
                
          
new_df = pd.DataFrame(data, columns=['timestamp', 'date','day number','weekends','segemnt','activity number','activity count','hours','minutes']);

new_df.to_csv('test user35.csv');
print(len(new_df));
print(ac);
print(all_activities[0]);
print(i);
print(len(timestamps_dataset1));
print(timestamps_dataset == timestamps_dataset1);

total = new_df['activity count'].sum();
print(total);
print(len(ac));
print(len(full_date_list));