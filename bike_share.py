# script was written in VS editor by Harish 

import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    global city
    while True:
        city_names = ['chicago','new york city','washington']
        city_names = [x.lower() for x in city_names ]
        month_names = ["all","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug", "Sep", "Oct", "Nov", "Dec","January","February","March","April","May","June","July","August","September","October","November","December"]
        month_names = [x.lower() for x in month_names]
        day_names = ['all','Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat',"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        day_names =[x.lower() for x in day_names]

        c=input('Enter city name: ') or 'chicago'
        m=input('Enter month name: ') or 'all'
        d=input('Enter day name: ') or 'all'
        c,m,d= c.lower(),m.lower(),d.lower()
        
        if c in city_names and m in month_names and d in day_names:
            print('Data format is correct')
            break
        else:
            print('Data in wrong format')
    city =c
    month =m
    day =d
    print('Hello! Let\'s explore some US bikeshare data!')
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    p_c= CITY_DATA[city]
    df_1 = pd.read_csv(p_c)
    
    df_1['Start Time']= pd.to_datetime(df_1['Start Time'])
    df_1['End Time']= pd.to_datetime(df_1['End Time'])
    df_1['month']=df_1['Start Time'].dt.month_name()
    df_1['day']=df_1['Start Time'].dt.day_name()
    df_1['hour']= df_1['Start Time'].dt.hour
    
    return df_1



def time_stats(df_1):
    """Displays statistics on the most frequent times of travel."""
    print('Hello welcome')
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('{} month is most popular month'.format(df_1['month'].mode()[0]))

    print('{} is most popular day'.format(df_1['day'].mode()[0]))

    print('The {}.00 hour is most popular'.format(df_1['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df_1):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    ss = df_1['Start Station'].value_counts().idxmax()
    es = df_1['End Station'].value_counts().idxmax()
    print('The most popular Start Station {}'.format(ss))
    print('The most popular End Station {}'.format(es))
    
    print('Most famous start station is {} & end staion is {}'.format(ss,es))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df_1):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('Total travel duration {} minutes'.format(sum(df_1['Trip Duration'])/60))
    print('Average travel duration {} minutes'.format(df_1['Trip Duration'].mean()/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df_1):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    if city =='washington':
        try:
            print('Washington city has no gender & birth year data')
        except:
            print('Some error has occured')
    else:
        x=df_1['User Type'].value_counts()
        print('Number of user types\n {}'.format(x))
        y=df_1['Gender'].value_counts()

        print('Number of gender types\n {}'.format(y))
        ear= df_1['Birth Year'].min()
        more =df_1['Birth Year'].max()
        mc= df_1['Birth Year'].value_counts().idxmax()
        print('The earliest birth date {} , most recent birth date {} and common birth year {}'.format(ear,more,mc))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def dis(df_1):
    """ Displays raw data of bikeshare"""
    
    ip=input('Do you want to see 5 lines of raw data? Enter yes or no: ')
    i=0
    while True:
        try:
            if ip.lower() =='yes':
                print(df_1[i:i+5])
                i+=5
            else:
                #print('ok')
                break
            ip1 = input('Do you want to see another 5 lines? Enter yes or no: ')
            if ip1.lower()=='yes':
                continue
            else:
                break
        except:
            print('invalid response')
    #print('Thanks for review')

def main():
    while True:
        city, month, day = get_filters()
        df_1 = load_data(city, month, day)
        time_stats(df_1)
        station_stats(df_1)
        trip_duration_stats(df_1)
        user_stats(df_1)
        dis(df_1)
        print('hello')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()