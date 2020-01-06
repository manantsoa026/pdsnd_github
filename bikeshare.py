#
# This is final Udacity project that explore bike share date with Python
#
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']

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
   
    city = input('\nPlease choose a  City (chicago, new york city, washington) :').lower()
    while city not in CITY_DATA:
        city = input('\nPlease choose a  City (chicago, new york city, washington) :').lower()
    

    
    # TO DO: get user input for month (all, january, february, ... , june)
   
    month = input('\nPlease choose a  Month ( january, february, ..., june, or all): ').lower()
    while month not in MONTHS:
        month = input('\nPlease choose a  Month ( january, february, ..., june, or all): ').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    week_days = ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    day = input('\nPlease choose a Day (all, monday, tuesday, ..., sunday): ').lower()
    while day not in week_days:
        day = input('\nPlease choose a Day (all, monday, tuesday, ..., sunday): ').lower()
    

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
        imonth = MONTHS.index(month)+1
        df= df[df['month']==imonth]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
   

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mcm = df['Start Time'].dt.month.mode()[0]

    print("\nThe most common month is : %s" % MONTHS[mcm - 1])

    # TO DO: display the most common day of week
    mc_day_of_week = df['Start Time'].dt.weekday_name.mode()[0]

    print("\nThe most common day of week is : %s" % mc_day_of_week)

    # TO DO: display the most common start hour
    mc_start_hour = df['Start Time'].dt.hour.mode()[0]
    print("\nThe most common start hour is : %s h" % mc_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mc_used_start_station = df['Start Station'].mode()[0]
    print("\nThe most common start station is : %s "% mc_used_start_station) 

    # TO DO: display most commonly used end station
    mc_used_end_station = df['End Station'].mode()[0]
    print("\nThe most common end station is : %s "% mc_used_end_station) 
    

    # TO DO: display most frequent combination of start station and end station trip
    mc_used_combined_start_end_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print("\nThe most common combination of start and end station is :") 
    print(mc_used_combined_start_end_station) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\nThe total travel time is : %s s "%total_travel_time) 

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nThe mean travel time is : %s s "%mean_travel_time) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\n Counts of user types:\n %s " %df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print("\n Counts of gender :\n %s " %df['Gender'].value_counts())
    except:
        print("\n Counts of gender : Sorry there are no User gender in your city choice\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_ybirth = df['Birth Year'].min()
        most_recent_ybirth = df['Birth Year'].max()
        most_common_ybirth = df['Birth Year'].mode()
        print("\nthe most earliest year of birth : %s" %int(earliest_ybirth))
        print("\nthe most recent year of birth : %s" %int(most_recent_ybirth))
        print("\nthe most common year of birth : %s" %int(most_common_ybirth))
    
    except:
        print("\n earliest, most recent, and most common year of birth : ")
        print("Sorry there is no User Birth Year in your City choice\n")
  
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    begin = 0
    end = 5
    df_raw_size = df.size
    
    
    try:
        while  end < df_raw_size:
            prompt = input("\nwould you like to show the row data ? Enter yes or no (yes for more data): ") 
            if prompt.lower() == 'yes':
                print(df.iloc[begin:end])
                begin += 5
                end += 5
            
            elif prompt.lower() == 'no':
                break
            else:
                print("\nPlease specify 'yes' or 'no'\n")
        
     
    except: 
        print("sorry  there is an error ")
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        # Ask the user if they want to restart their request 
        restart = input('\nWould you like to restart? Enter yes or no : \n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
