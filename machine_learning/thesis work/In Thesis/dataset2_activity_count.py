# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:37:53 2021

@author: User
"""

import pandas as pd;
import numpy as np;
import datetime;
import time;
from collections import Counter;

df = pd.read_csv('dataset_secondo/user12.csv');
counter = 0;
activity_count = 0;
day_count = 0;


cols = list(df.columns);
modified_df = df[cols[0:3] +[cols[-1]]]; #csv to fill out day state of  a date


print(modified_df);
date_list = [];
full_date_list=[];
full_activity_list=modified_df['activity'];

activity_list=[];
activity_list1=[];
activity_list2=[];
activity_list3=[];activity_list4=[];activity_list5=[];activity_list6=[];activity_list7=[];activity_list8=[];
activity_list9=[];activity_list10=[];activity_list11=[];activity_list12=[];activity_list13=[];activity_list14=[];
activity_list15=[];activity_list16=[];activity_list17=[];activity_list18=[];activity_list19=[];activity_list20=[];
activity_list21=[];activity_list22=[];activity_list23=[];
previous_date='';
final_list=dict();
day_state =['Midnight','Morning','Noon','Night'];

def allocate_day_state(hour,activity,date):
        global previous_date,counter,day_count,activity_list,activity_list1,activity_list2,activity_list3,activity_list4,activity_list5, activity_list6,activity_list7,activity_list8,activity_list9,activity_list10,activity_list11,activity_list12,activity_list13,activity_list14,activity_list15,activity_list16,activity_list17,activity_list18,activity_list19,activity_list20,activity_list21,activity_list22,activity_list23;
        
        # one day has passed
        if previous_date != date and previous_date != '':
            #date as key and activities as  values 
            final_list[previous_date] = Counter(activity_list3),Counter(activity_list4),Counter(activity_list5),Counter(activity_list6),Counter(activity_list7),Counter(activity_list8),Counter(activity_list2),Counter(activity_list9),Counter(activity_list10),Counter(activity_list11),Counter(activity_list12),Counter(activity_list13),Counter(activity_list1),Counter(activity_list14),Counter(activity_list15),Counter(activity_list16),Counter(activity_list17),Counter(activity_list18),Counter(activity_list),Counter(activity_list19),Counter(activity_list20),Counter(activity_list21),Counter(activity_list22),Counter(activity_list23);
            previous_date = date; #mm/dd/yy
            activity_list=[];
            activity_list1=[];
            activity_list2=[];
            activity_list3=[];activity_list4=[];activity_list5=[];activity_list6=[];activity_list7=[];
            activity_list8=[];activity_list9=[];activity_list10=[];activity_list11=[];activity_list12=[];
            activity_list13=[];activity_list14=[];activity_list15=[];activity_list16=[];activity_list17=[];
            activity_list18=[];activity_list19=[];activity_list20=[];
            activity_list21=[];activity_list22=[];activity_list23=[];
         
            
            
        
        if int(hour) == 0 and date_list[counter] == date:  #midnight(3 - 8)

            activity_list3.append(activity);
            previous_date = date;
            counter+=1;   
            return 0;
        elif int(hour) == 1 and date_list[counter] == date:  #midnight

            activity_list4.append(activity);
            previous_date = date;
            counter+=1;   
            return 0;
        elif int(hour) == 2 and date_list[counter] == date:  #midnight

            activity_list5.append(activity);
            previous_date = date;
            counter+=1;   
            return 0;
        elif int(hour) == 3 and date_list[counter] == date:  #midnight

            activity_list6.append(activity);
            previous_date = date;
            counter+=1;   
            return 0;
        elif int(hour) == 4 and date_list[counter] == date:  #midnight

            activity_list7.append(activity);
            previous_date = date;
            counter+=1;   
            return 0;
        elif int(hour) == 5 and date_list[counter] == date:  #midnight

            activity_list8.append(activity);
            previous_date = date;
            counter+=1;   
            return 0;
        
        elif int(hour) == 6 and date_list[counter] == date: #morning(2,9-13)
            activity_list2.append(activity);      
            previous_date = date;
            counter+=1;
            return 1;
        elif int(hour) == 7 and date_list[counter] == date: #morning
            activity_list9.append(activity);      
            previous_date = date;
            counter+=1;
            return 1;
        elif int(hour) == 8 and date_list[counter] == date: #morning
            activity_list10.append(activity);      
            previous_date = date;
            counter+=1;
            return 1;
        elif int(hour) == 9 and date_list[counter] == date: #morning
            activity_list11.append(activity);      
            previous_date = date;
            counter+=1;
            return 1;
        elif int(hour) == 10 and date_list[counter] == date: #morning
            activity_list12.append(activity);      
            previous_date = date;
            counter+=1;
            return 1;
        elif int(hour) == 11 and date_list[counter] == date: #morning
            activity_list13.append(activity);      
            previous_date = date;
            counter+=1;
            return 1;
        elif int(hour) == 12 and date_list[counter] == date:  #noon(1,14 -18)
            activity_list1.append(activity); 
            previous_date = date;
            counter+=1;
            return 2;
        elif int(hour) == 13 and date_list[counter] == date:  #noon
            activity_list14.append(activity); 
            previous_date = date;
            counter+=1;
            return 2;
        elif int(hour) == 14 and date_list[counter] == date:  #noon
            activity_list15.append(activity); 
            previous_date = date;
            counter+=1;
            return 2;
        elif int(hour) == 15 and date_list[counter] == date:  #noon
            activity_list16.append(activity); 
            previous_date = date;
            counter+=1;
            return 2;
        elif int(hour) == 16 and date_list[counter] == date:  #noon
            activity_list17.append(activity); 
            previous_date = date;
            counter+=1;
            return 2;
        elif int(hour) == 17 and date_list[counter] == date:  #noon
            activity_list18.append(activity); 
            previous_date = date;
            counter+=1;
            return 2;
        elif int(hour) == 18 and date_list[counter] == date:  #night(0,19-23)
            activity_list.append(activity);
            previous_date = date;
            counter+=1;
            return 3;
        elif int(hour) == 19 and date_list[counter] == date:  #night
            activity_list19.append(activity);
            previous_date = date;
            counter+=1;
            return 3;
        elif int(hour) == 20 and date_list[counter] == date:  #night
            activity_list20.append(activity);
            previous_date = date;
            counter+=1;
            return 3;
        elif int(hour) == 21 and date_list[counter] == date:  #night
            activity_list21.append(activity);
            previous_date = date;
            counter+=1;
            return 3;
        elif int(hour) == 22 and date_list[counter] == date:  #night
            activity_list22.append(activity);
            previous_date = date;
            counter+=1;
            return 3;
        elif int(hour) == 23 and date_list[counter] == date:  #night
            activity_list23.append(activity);
            previous_date = date;
            counter+=1;
            return 3;
       
## midnight morning noon night
for time in df['timestamp']:
    date_list.append(datetime.datetime.fromtimestamp(time).strftime("%D"));
    full_date_list.append(datetime.datetime.fromtimestamp(time).strftime("%D %I:00:00 %p"));
full_date_set = sorted(set(full_date_list));    
print(full_date_set)
unique_dates = set(date_list);
#to print out the day state modified csv necessary complonents

for time in df['timestamp']:
    hour = datetime.datetime.fromtimestamp(time).strftime("%H");
    date = datetime.datetime.fromtimestamp(time).strftime("%D");
    activity = df.iloc[activity_count]['activity'];
    time_state = allocate_day_state(hour,activity,date);
    
    activity_count += 1;
    # print(activity_count);
final_list[previous_date] = Counter(activity_list3),Counter(activity_list4),Counter(activity_list5),Counter(activity_list6),Counter(activity_list7),Counter(activity_list8),Counter(activity_list2),Counter(activity_list9),Counter(activity_list10),Counter(activity_list11),Counter(activity_list12),Counter(activity_list13),Counter(activity_list1),Counter(activity_list14),Counter(activity_list15),Counter(activity_list16),Counter(activity_list17),Counter(activity_list18),Counter(activity_list),Counter(activity_list19),Counter(activity_list20),Counter(activity_list21),Counter(activity_list22),Counter(activity_list23);      
# # to print out final user csv

final_list = list(final_list.items());

data=[];
segment = ['6pm - 12am','12pm - 6pm','6am - 12pm','12am - 6am']

# # list of all activity counts counter  in  each day 
for i in range(len(final_list)):
    activity=[];
    date = datetime.datetime.strptime(final_list[i][0],"%m/%d/%y");
    timestamp_unique_date = datetime.datetime.timestamp(date);
    print(timestamp_unique_date);

    day = int(datetime.datetime.fromtimestamp(timestamp_unique_date).strftime("%w"));
    print(day);
    day_name = datetime.datetime.fromtimestamp(timestamp_unique_date).strftime("%A");
    print(day_name)
    #distinct activities in the dataset
    full_activity_list = ['Driving','Walking','Inactive','Active'];

    # to get the counters in a list 
    for item in final_list[i][1]:
            activity.append(item); 
    print(f'i am {activity}')
    #distribute activity count  over a day in 4  segments        
    walking=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    driving=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    inactive=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    active=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    
   
    # get activity count  matrix  for all activities
    for j in range(24):
        for k,v in activity[j].items():  
            print(k,v);
            print(f'i am {j}');
            if k == 'Walking':
                walking[j] = v;
            if k == 'Driving':
                driving[j]= v;
            if k == 'Inactive':
                inactive[j] = v;
            if k == 'Active':
                active[j] = v;
    
    print(f'he is {walking}');
    print(driving);
    print(active);
    print(inactive);
    
    # just assign remain
    ##  i =0->midnight ,1->morning , 2 -> noon ,3->night
    ##  walking -> 0, driving -> 1, inactive -> 2, active -> 3;
    ## sunday -> 0,monday -> 1 ,tuesday -> 2,wedneday->3,thutsday->4,friday->5,saturday->6;
    
    #append  the data fro csv
    year = int(date.strftime("%Y"));
    month = int(date.strftime("%m"));
    day_which = int(date.strftime("%d"));
    print(year,month,day);
    for activity in full_activity_list:
          
          if activity == 'Walking':
            
            for j in range(24):
                date_obj = datetime.datetime(year,month,day_which,j,00,00)
                timestamp  =datetime.datetime.timestamp(date_obj);
                if j >= 0 and j < 6:  #midnight
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,0,0,walking[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,0,0,walking[j]]);
                if j >= 6 and j < 12:  #morning
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,0,1,walking[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,0,1,walking[j]]);
                if j >= 12 and j < 18: #noon
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,0,2,walking[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,0,2,walking[j]]);
                if j >= 18 and j < 24: #night
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,0,3,walking[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,0,3,walking[j]]);

          if activity == 'Driving':
              for j in range(24):
                date_obj = datetime.datetime(year,month,day_which,j,00,00)
                timestamp  =datetime.datetime.timestamp(date_obj);

                if j >= 0 and j < 6:  #midnight
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,1,0,driving[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,1,0,driving[j]]);
                if j >= 6 and j < 12:  #morning
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,1,1,driving[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,1,1,driving[j]]);
                if j >= 12 and j < 18: #noon
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,1,2,driving[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,1,2,driving[j]]);
                if j >= 18 and j < 24: #night
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,1,3,driving[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,1,3,driving[j]]);
                    
          if activity == 'Inactive':
              for j in range(24):
                date_obj = datetime.datetime(year,month,day_which,j,00,00)
                timestamp  =datetime.datetime.timestamp(date_obj);

                
                if j >= 0 and j < 6:  #midnight
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,2,0,inactive[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,2,0,inactive[j]]);
                if j >= 6 and j < 12:  #morning
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,2,1,inactive[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,2,1,inactive[j]]);
                if j >= 12 and j < 18: #noon
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,2,2,inactive[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,2,2,inactive[j]]);
                if j >= 18 and j < 24: #night
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,2,3,inactive[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,2,3,inactive[j]]);
                    
          if activity == 'Active':
              for j in range(24):
                date_obj = datetime.datetime(year,month,day_which,j,00,00)
                timestamp  =datetime.datetime.timestamp(date_obj);

                
                if j >= 0 and j < 6:  #midnight
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,3,0,active[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,3,0,active[j]]);
                if j >= 6 and j < 12:  #morning
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,3,1,active[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,3,1,active[j]]);
                if j >= 12 and j < 18: #noon
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,3,2,active[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,3,2,active[j]]);
                if j >= 18 and j < 24: #night
                    if day == 0:
                        data.append([int(timestamp),date_obj,day,0,3,3,active[j]]);
                    else:
                        data.append([int(timestamp),date_obj,day,1,3,3,active[j]]);
        
    
    new_df = pd.DataFrame(data, columns=['timestamp', 'date', 'day number','weekends','activity number','segment','activity count'])
    print(len(new_df));        
print(unique_dates)        
#to csv
new_df.to_csv('dataset_secondo_user_activity_count/user4 activity count.csv');                  
    

        
        