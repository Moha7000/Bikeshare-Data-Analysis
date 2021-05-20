import time
import pandas as pd
import numpy as np
import calendar as cal
from time import strptime



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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    city_loop_entered = False
    while city != 'chicago' and city != 'new york city' and city != 'washington' :
            if city_loop_entered == True:
                print('wrong input please try again')
            city = str(input('\nEnter the name of the city you want to analyze \n"chicago" , "new york city" , "washington": ' )).lower()
            city_loop_entered = True
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    month_loop_entered = False
    while month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june'and month != 'july' and month != 'all' :
            if month_loop_entered == True:
                print('wrong input please try again')
            month = input("\nenter the month's name to specify the analysis \nfor example type 'january', 'february','march', 'april', 'june', 'july', or type 'all' if you don't want to specify: ").lower()
            month_loop_entered = True


    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    day_loop_entered = False
    while day.lower() != 'sunday' and day != 'monday' and day != 'tuesday' and day != 'wednsday' and day != 'thursday' and day != 'friday'and day != 'saturday' and day != 'all' :
        if day_loop_entered == True:
                print('wrong input please try again')
        day = input("\nenter the day's name to specify the analysis \nfor example type 'sunday' , 'monday'...etc ,or type 'all' if you don't want to specify: ").lower()
        day_loop_entered = True

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month =  df.groupby(['month'])['month'].count().idxmax()
    print('The most common month is {}'.format(cal.month_name[popular_month]))    

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day
    popular_day =  df.groupby(['day'])['day'].count().idxmax()
    
    print('The most common day is {}'.format(popular_day))    
    

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour =  df.groupby(['hour'])['hour'].count().idxmax()
    
    print('The most common hour is at {}:00'.format(popular_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The Most Popular Start Stations is:\n        {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The Most Popular End Stations is:\n        {}'.format(popular_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df.groupby(['Start Station' , 'End Station'])['Start Station'].count().idxmax()
    print('The Most frequent combination of start station and end station trip:\n       {}'.format(popular_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    travel_time_total =  df['Travel Time'].sum()
    print('The Total Trips Duration:\n       {}'.format(travel_time_total))
    # extract hour from the Start Time column to create an hour column

    # TO DO: display mean travel time
    travel_time_mean =  df['Travel Time'].mean()
    print('The Average Trip Duration:\n       {}'.format(travel_time_mean))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby('User Type')['User Type'].count()
    print('The Type of Users And Their Count:\n        {}'.format(user_types.to_string()))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df.groupby('Gender')['Gender'].count()
        print('\nThe Genders of Users And Their Count:\n        {}'.format(gender_count.to_string()))
    else:
        print('\nNo Gender Specified In Washington File')

    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data.lower()=='yes':
        print(df.iloc[start_loc])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def data_analysis(df):
    time_analisis = 'no'
    time_analisis = input('Do You Want To Calculate The Most Frequent Times of Travel? Enter yes or no.\n')
    if time_analisis.lower() == 'yes' :
        time_stats(df)
        time_analisis = 'no'
    station_analisis = 'no'
    station_analisis = input('Do You Want To Display Statistics On The Most Popular Stations And Trip? Enter yes or no.\n')
    if station_analisis.lower() == 'yes' :
        station_stats(df)
        station_analisis = 'no'
    trip_duration_analisis = 'no'
    trip_duration_analisis = input('Do You Want Display statistics on the total and average trip duration? Enter yes or no.\n')
    if trip_duration_analisis.lower() == 'yes' :
        trip_duration_stats(df)
        trip_duration_analisis = 'no'
        trip_duration_analisis = 'no'
    user_analysis = 'no'
    user_analysis = input('Do You Want To Displays statistics on bikeshare users? Enter yes or no.\n')
    if user_analysis.lower() == 'yes' :
        user_stats(df)
        user_analysis = 'no'
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_data(df)
        data_analysis(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
