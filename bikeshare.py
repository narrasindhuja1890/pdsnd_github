<<<<<<< HEAD
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()
    while city not in ('chicago','new york','washington'):
          city =input('\nPlease enter Chicago or New York or Washington.\n').lower()
          continue
          city = CITY_DATA[city]
          break
    user_input=input('\nWould you like to filter the data by month, day, or not at all?\n')
             # TO DO: get user input for month (all, january, february, ... , june)
    if user_input=="month":
      month = input('\nWhich month - January, February, March, April, May, or June?\n').lower()
      while month not in ('january','february','march','april','may','june'):
            month = input('\nPlease enter January, February, March, April, May, or June\n').lower()
            continue
            break
      day='all'
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)  
    elif user_input=="day":
      day = input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
      month='all'  
    else:
        month ='all'
        day='all'
       
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
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1      
        df = df[df['month'] == month]

    if day != 'all':
       
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on travel times"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', popular_day)


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Start Station:{}'.format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print('End Station:{}'.format(df['End Station'].mode()[0]))  


    # TO DO: display most frequent combination of start station and end station trip
    combination = df['Start Station'] +" "+ df['End Station']
    print('Combination of Start and End Station:{}'.format(combination.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:{}'.format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('Total mean travel time:{}'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('Gender stats unavailable')
    else:
        print(df.groupby('Gender').count())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Birth Year stats unavailable')
    else:
        print('Earliest year of birth:{}'.format(df['Birth Year'].min()))
        print('Most recent year of birth:{}'.format(df['Birth Year'].max()))
        print('Most common year of birth:{}'.format(df['Birth Year'].count()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    choice = input('\nWould you like to see raw data? Please enter Yes or No\n').lower()  
    while choice == 'yes':
            for i in range(10):
                print(df.iloc[i])
            choice = input('\nWould you like to see more? Please enter Yes or No\n').lower()
            if choice =='yes':
               continue
            else:
               break              
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
||||||| 34561df
=======
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by:
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()
    while city not in ('chicago','new york','washington'):
          city =input('\nPlease enter Chicago or New York or Washington.\n').lower()
          continue
          city = CITY_DATA[city]
          break
    user_input=input('\nWould you like to filter the data by month, day, or not at all?\n')
             # TO DO: get user input for month (all, january, february, ... , june)
    if user_input=="month":
      month = input('\nWhich month - January, February, March, April, May, or June?\n').lower()
      while month not in ('january','february','march','april','may','june'):
            month = input('\nPlease enter January, February, March, April, May, or June\n').lower()
            continue
            break
      day='all'
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)  
    elif user_input=="day":
      day = input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
      month='all'  
    else:
        month ='all'
        day='all'
       
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
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1      
        df = df[df['month'] == month]

    if day != 'all':
       
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent travel times."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', popular_day)


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Start Station:{}'.format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print('End Station:{}'.format(df['End Station'].mode()[0]))  


    # TO DO: display most frequent combination of start station and end station trip
    combination = df['Start Station'] +" "+ df['End Station']
    print('Combination of Start and End Station:{}'.format(combination.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:{}'.format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('Total mean travel time:{}'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """bikeshare users stats."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('Gender stats unavailable')
    else:
        print(df.groupby('Gender').count())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Birth Year stats unavailable')
    else:
        print('Earliest year of birth:{}'.format(df['Birth Year'].min()))
        print('Most recent year of birth:{}'.format(df['Birth Year'].max()))
        print('Most common year of birth:{}'.format(df['Birth Year'].count()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    choice = input('\nWould you like to see raw data? Please enter Yes or No\n').lower()  
    while choice == 'yes':
            for i in range(10):
                print(df.iloc[i])
            choice = input('\nWould you like to see more? Please enter Yes or No\n').lower()
            if choice =='yes':
               continue
            else:
               break              
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
>>>>>>> refactoring
