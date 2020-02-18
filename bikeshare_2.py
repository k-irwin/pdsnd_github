
# Bikeshare Data Project

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# Get User Name ************************************************************************************************

def get_name():
    """This sub gets the user's name"""

    name = input("\nHello, What is your name?\n")
    return name


# Get User answer to search ************************************************************************************************

def search_question(name):
    """This procedure checks if the user wants to search the data"""
    greating = ['\nWelcome {}, Would you like to explore some data: (1)Yes, (2)No\n', '\nPlease choose yes or no {}.\n']
    index = 0
    while True:
      response = str(input(greating[index].format(name)).lower())
      if response not in ('yes', 'no', '1', '2'):
        print('Sorry, that option is not available.')
        index = 1
        continue
      elif response == 'yes':
        return True
      elif response == '1':
        return True
      elif response == 'no':
        return False
      elif response == '2':
        return False
      else:
        break


# Get User Input ************************************************************************************************

def get_filters(name):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nGreat choice {}! Let\'s explore some US bikeshare data!'.format(name))

    # Start of TO DUE Section 1

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:

      while True:
        cities = str(input("\nWhich city's data are you interested in: (1)New York City, (2)Chicago or (3)Washington?\n").lower())
        if cities not in ('new york city', 'chicago', 'washington', '1', '2', '3'):
          print("Sorry, that city's data is not available. Please try again.")
          continue
        elif cities == '1':
          city = 'new york city'
          break
        elif cities == '2':
          city = 'chicago'
          break
        elif cities == '3':
          city = 'washington'
          break
        else:
          city = cities
          break


      # get user input for month (all, january, february, ... , june)

      while True:
        months = str(input("\nWhich month\'s data are you interested in? (1)January, (2)February, (3)March, (4)April, (5)May, (6)June or (7)all?\n").lower())
        if months not in ('january', 'february', 'march', 'april', 'may', 'june', 'all', '1', '2', '3', '4', '5', '6', '7'):
          print("Sorry, that months's data is not available. Please try again.")
          continue
        elif months == '1':
          month = 'january'
          break
        elif months == '2':
          month = 'february'
          break
        elif months == '3':
          month = 'march'
          break
        elif months == '4':
          month = 'april'
          break
        elif months == '5':
          month = 'may'
          break
        elif months == '6':
          month = 'june'
          break
        elif months == '7':
          month = 'all'
          break
        else:
          month = months
          break

      # get user input for day of week (all, monday, tuesday, ... sunday)

      while True:
        days = str(input("\nWhich day\'s data are you interested in: (1)Sunday, (2)Monday, (3)Tuesday, (4)Wednesday, (5)Thursday, (6)Friday, (7)Saturday or (8)all.\n").lower())
        if days not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all','1', '2', '3', '4', '5', '6', '7', '8'):
          print("Sorry, that day's data is not available. Please try again.")
          continue
        elif days == '1':
          day = 'sunday'
          break
        elif days == '2':
          day = 'monday'
          break
        elif days == '3':
          day = 'tuesday'
          break
        elif days == '4':
          day = 'wednesday'
          break
        elif days == '5':
          day = 'thursday'
          break
        elif days == '6':
          day = 'friday'
          break
        elif days == '7':
          day = 'saturday'
          break
        elif days == '8':
          day = 'all'
          break
        else:
          day = days
          break

      # Verify user input selection

      choices = [city.title(), month.title(), day.title()]

      response = str(input('\nYou choose {}, {}, and {}, is that the correct data {}? (1)Yes, (2)No\n'.format(*choices, name)).lower())
      if response not in ('yes', 'no', '1', '2'):
        while True:
          valid_answer = str(input('\nPlease choose yes or no. {}.\n'.format(name)).lower())
          if valid_answer not in ('yes', 'no', '1', '2'):
            continue
          elif valid_answer == '1':
            response = 'yes'
            break
          else:
            response = valid_answer
            break
      elif response == '1':
        response = 'yes'
      elif response == 'yes':
        response = 'yes'
      else:
        response = 'no'

      if response.lower() != 'yes':
        print('\nPlease make another data selection {}.'.format(name))
        continue
      else:
        break

    print("\nOkay {}, retrieving Data for {}, {}, and {}............\n".format(name, *choices))

    # End of TO DUE Section 1

    print('-'*40)
    return city, month, day


# Get Data from File ************************************************************************************************

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

    # Start of TO DUE Section 2

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

    # End of TO DUE Section 2

    return df


# Get Travel Times ************************************************************************************************

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Start of TO DUE Section 3

    # display the most common month

    most_month = df['month'].mode()[0]
    month_lst = ['January', 'February', 'March', 'April', 'May', 'June']
    month_name = month_lst[most_month - 1]
    print('Most Common Month: {}'.format(month_name))

    # display the most common day of week

    most_day = df['day_of_week'].mode()[0]
    print('Most Common day: {}'.format(most_day))

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['hour'].mode()[0]
    if most_hour == 24:
      start_hour = 12
      print('Most Common Start Hour: {}:00 AM'.format(start_hour))
    elif most_hour > 12:
      start_hour = most_hour - 12
      print('Most Common Start Hour: {}:00 PM'.format(start_hour))
    elif most_hour == 12:
      print('Most Common Start Hour: {}:00 PM'.format(most_hour))
    else:
      print('Most Common Start Hour: {}:00 AM'.format(most_hour))
    #print('Most Common Start Hour: {}'.format(most_hour))

    # End of TO DUE Section 3

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Get Station Information ************************************************************************************************

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # Start of TO DUE Section 4

    # display most commonly used start station

    start_station = df['Start Station'].mode().values[0]
    print('Most Commonly used start station: {}'.format(start_station))

    # display most commonly used end station

    end_station = df['End Station'].mode().values[0]
    print('Most Commonly used end station: {}'.format(end_station))

    # display most frequent combination of start station and end station trip

    df['travel_route'] = df['Start Station']+ ", " + df['End Station']
    trip_combination = df['travel_route'].mode().values[0].split(',')
    print('Most frequent trip combination of start station and end station: {}(start) and{}(end)'.format(*trip_combination))

    # End of TO DUE Section 4


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Get Travel Times ************************************************************************************************

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Start of TO DUE Section 5

    # Load variables

    minutes = 60
    hours = 60 * minutes
    days = 24 * hours

    # display total travel time

    total_travel_time = round(sum(df['Trip Duration'])/days, 2)
    print('Total travel time: {} Days'.format(total_travel_time))

    # display mean travel time

    mean_travel_time = round(df['Trip Duration'].mean()/minutes, 2)
    print('Mean travel time: {} Minutes'.format(mean_travel_time))

    # End of TO DUE Section 5

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Get User Stats ************************************************************************************************

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n\nCalculating User Stats...\n')
    start_time = time.time()

    # Start of TO DUE Section 6

    # Display counts of user types

    print("User Types")

    try:
      is_subscriber = df[df['User Type'] == 'Subscriber']
      subscriber_count = is_subscriber['User Type'].value_counts()
      print("Subscriber: {}".format(subscriber_count[0]))
    except:
      print("Subscriber: No data available for this selection.")

    try:
      is_customer = df[df['User Type'] == 'Customer']
      customer_count = is_customer['User Type'].value_counts()
      print("Customer: {}".format(customer_count[0]))
    except:
      print("Customer: No data available for this selection.")


    # Display counts of gender

    print("\nGender Types")

    try:
      is_male = df[df.Gender == 'Male']
      male_count = is_male['Gender'].value_counts()
      print("Male: {}".format(male_count[0]))
    except:
      print("Male: No data available for this selection.")

    try:
      is_female = df[df.Gender == 'Female']
      female_count = is_female['Gender'].value_counts()
      print("Female: {}".format(female_count[0]))
    except:
      print("Female: No data available for this selection.")


    # Display earliest, most recent, and most common year of birth

    print("\nYear of Birth")

    try:
      earliest_year = int(df['Birth Year'].min())
      print('Earliest Year: {}'.format(earliest_year))
    except KeyError:
      print("Earliest Year: No data available for this selection.")

    try:
      most_recent_year = int(df['Birth Year'].max())
      print('Most Recent Year: {}'.format(most_recent_year))
    except KeyError:
      print("Most Recent Year: No data available for this selection.")

    try:
      most_common_year = int(df['Birth Year'].value_counts().idxmax())
      print('Most Common Year: {}'.format(most_common_year))
    except KeyError:
      print("Most Common Year: No data available for this selection.")

    # End of TO DUE Section 6

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Display raw data ************************************************************************************************

def display_data(df, name):
    """Display raw data from CSV file if requested by user."""

    # Get user input to see raw data

    get_data = input("Do you want to see the raw data {}? (1)Yes, (2)No\n".format(name)).lower()
    if get_data not in ('yes', 'no', '1', '2'):
        while True:
          valid_answer_1 = str(input('\nPlease choose yes or no {}.\n'.format(name)).lower())
          if valid_answer_1 not in ('yes', 'no', '1', '2'):
            continue
          elif valid_answer_1 == '1':
            get_data = 'yes'
            break
          else:
            get_data = valid_answer_1
            break
    elif get_data == '1':
      get_data = 'yes'
    elif get_data == 'yes':
      get_data = 'yes'
    else:
      get_data = 'no'


    # Get the number of rows to be viewed

    if get_data == 'yes':
      while True:
        get_rows = input("\nHow many rows would you like to view?\n")
        if (get_rows.isdigit()):
          start_index = 0
          end_index = int(get_rows)
          row_count = int(get_rows)
          break
        elif not (get_rows.isdigit()):
          print("Please enter a number\n")
          continue
        else:
          start_index = 0
          end_index = 5
          row_count = 5
          break


    # Desplay raw data if requested

    if get_data == 'yes':
        while end_index <= df.shape[0] - 1:

            data_set = df.iloc[start_index:end_index,:]
            print(data_set)
            start_index = end_index
            end_index += row_count

            #Get user input ot continue
            more_data = input("Do you wish to continue?  (1)Yes, (2)No\n").lower()
            if more_data not in ('yes', 'no', '1', '2'):
              while True:
                valid_answer_2 = str(input('\nPlease choose yes or no {}.\n'.format(name)).lower())
                if valid_answer_2 not in ('yes', 'no', '1', '2'):
                  continue
                elif valid_answer_2 == '2':
                  more_data = 'no'
                  break
                else:
                  more_data = valid_answer_2
                  break
            elif more_data == '2':
              more_data = 'no'
            elif more_data == 'no':
              more_data = 'no'
            else:
              more_data = 'yes'

            if more_data == 'no':
                break


# Main Function ************************************************************************************************

def main():
    user_name = get_name()
    search = search_question(user_name)
    if search == True:
      while True:
        city, month, day = get_filters(user_name)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df, user_name)

        restart = input('\nWould you like do another search {}?  Please enter (1)Yes or (2)No.\n'.format(user_name)).lower()
        if restart not in ('yes', 'no', '1', '2'):
          while True:
            valid_answer = str(input('\nPlease choose yes or no {}.\n'.format(name)).lower())
            if valid_answer not in ('yes', 'no', '1', '2'):
              continue
            elif valid_answer == '1':
              restart = 'yes'
              break
            else:
              restart = valid_answer
              break
        elif restart == '1':
          restart = 'yes'
        elif restart == 'yes':
          restart = 'yes'
        else:
          restart = 'no'

        if restart != 'yes':
            print('\nThank you for exploring data {}, come back again when your ready for another search.'.format(user_name))
            break
    else:
      print('\nSorry to hear that {}, maybe another time.'.format(user_name))



if __name__ == "__main__":
	main()
