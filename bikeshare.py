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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("What city would you like to analyze, Chicago, New York City, or Washington?\n").lower()
    
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("That is not a valid entry. Please enter a valid city name: Chicago, New York City, or Washington.\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('What month would you like to analyze? Enter January, February, March, April, May, June, or "all".\n').lower()
    
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('That is not a valid entry. Please enter a valid month: January, February, March, April, May, June, or "all".\n').lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('What day of the week would you like to analyze? Enter a day of the week or "all" to view all days.\n').lower()
    
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input('That is not a valid entry. Please enter a valid day of the week or "all" to view all days.\n').lower()

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
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
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

    df['month'] = df['Start Time'].dt.strftime("%B")

    common_month = df['month'].mode()[0]
   
    print('Most Common Start Month:', common_month)

    # TO DO: display the most common day of week
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['day'] = df['Start Time'].dt.strftime("%A")

    common_day = df['day'].mode()[0]
    
    print('Most Common Start Day:', common_day)

    # TO DO: display the most common start hour
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['hour'] = df['Start Time'].dt.strftime("%I %p")

    common_hour = df['hour'].mode()[0]
    
    print('Most Common Start Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    
    print('Most Common Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    
    common_end_station = df['End Station'].mode()[0]
    
    print('Most Common End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    common_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    
    print('Most Common Combination of Start and End Station:', common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    
    print("Total Travel Time: ", total_travel_time)

    # TO DO: display average travel time
    
    average_travel_time = df['Trip Duration'].mean()
    
    print("Average Travel Time: ", average_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print('There are {} Subscribers and {} Customers.'.format(user_types[0], user_types[1]))

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('There are {} Males and {} Females.'.format(gender_types[0], gender_types[1]))
    except:
        print("There is no gender data available for Washington.")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        print("The earliest birth year is {}.".format(earliest_birth_year))
    
        most_recent_birth_year = int(df['Birth Year'].max())
        print("The most recent birth year is {}.".format(most_recent_birth_year))
    
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("The most common birth year is {}.".format(most_common_birth_year))

    except:
        print("There is no birth year data available for Washington.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_raw_data(df):    
    user_input = input('\nWould you like to see 5 lines of raw data? Enter "yes" or "no".\n').lower()
    counter = 0
    while True :
        if user_input != 'no':
            print(df.iloc[counter : counter + 5])
            counter += 5
            user_input = input('\nWould you like to see another 5 lines of raw data? Enter "yes" or "no".\n').lower()
        else:
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
