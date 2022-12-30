import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAY_DATA = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Select a city to get its data: Chicago, New York City or Washington \n>").lower()
    while city not in CITY_DATA.keys():
        print('You must choose a city from the cities in the list')
        city = input("Select a city to get its data: Chicago, New York City or Washington\n>").lower()
       
    # Get user input for month (all, january, february, ... , june)
    while True:
          month = input("Select a month (all, january, february, ... , june)\n>").lower()
          if month in MONTH_DATA:
              break
          else:
              print('You must choose a month from the months in the list')

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
          day = input("Select a day (all, monday, tuesday, ... sunday)\n>").lower()
          if day in DAY_DATA:
              break
          else:
              print('You must choose a day from the months in the list')


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
 
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month = MONTH_DATA.index(month) 
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is :", most_common_month)

    

    # Display the most common day of week

    most_common_day = df['day_of_week'].mode()[0]
    print("Most common day of week :", most_common_day)
    
    # Display the most common start hour
    most_start = df['month'].mode()[0]
    print("Most common start hour :", most_start)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


     # Display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", most_commonly_used_start_station)

     # Display most commonly used end station
    most_commonly_uesd_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :", most_commonly_uesd_end_station)

    # Display most frequent combination of start station and end station trip
    frequent_combination = df[['Start Station', 'End Station']].mode().loc[0]
    print("Most frequent combination of start station and end station trip : {}, {}"\
            .format(frequent_combination[0], frequent_combination[1]))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type:')
    print(df['User Type'].value_counts())
    if city == 'chicago' or city == 'new york city':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year:')
        common_year = df['Birth Year'].mode()[0]
        print('Most Recent Year:',common_year)
        recent_year = df['Birth Year'].max()
        print('Most Common Year:',recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:',earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df):

    print(df.head())
    index = 0
    while True:
        raw_data = input('\nDo you want to see the next five rows? yes or no.\n')
        if raw_data.lower() != 'yes':
            return
        index = index + 5
        print(df.iloc[index:index+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
