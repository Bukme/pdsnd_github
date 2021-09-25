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

        User inputs are made case insensitive to be able to handle both upper and lower cases. 
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities_list = ['chicago','new york city','washington']
    city = input('Enter the name of a city;Chicago,New York City or Washington:').lower()

    while city not in cities_list:
        print('That\'s an invalid entry! Please, try again')
        city = input('Enter the name of a city;Chicago, New York city or Washington:').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months_list = ['january','february','march','april','may','june','all']
    month = input('Please enter the name of a month from January to June or All:').lower()

    while month not in months_list:
        print('That\'s an invalid entry! Please, try again')
        month=input('Please enter the name of a month from January to June or All:').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_list=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    day = input('Please, input a day of the week from Monday to Sunday or All:').lower()

    while day not in days_list:
        print('That\'s an invalid entry! Please, try again')
        day = input('Please, input a day of the week from Monday to Sunday or all:').lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('The most frequent month is:',popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('The most frequent day of the week is:',popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is:',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:',popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most frequently used End Station is:',popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print ('The most frequent combination of start and end station is:', popular_start_station + " and " + popular_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is:',total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time is:',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('There are {} numbers of user types'.format(user_types))

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Total number of gender is:',gender)
    else:
        print('Gender stats cannot be calculated, it does not exist in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        popular_birth_year = df['Birth Year'].mode()[0]

        print('Earliest year of birth is:',earliest_birth_year)
        print('Most recent year of birth is:',recent_birth_year)
        print('Most common year of birth is:',popular_birth_year)

    else:
        print('Birth Year stats cannot be calculated, it does not exist in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        view_data = input('would you like to view first five rows of individual trip data? Yes or No: ').lower()
        start_loc = 0
        while view_data == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input('\nWould you like to continue? yes or no: ').lower()
            if view_display != 'yes':
                break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
