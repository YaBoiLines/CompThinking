'''
Jon Zheng
This program is designed to display the date based on the user input regarding month, day, year and format of how the date is arrange.
The program will also calculate whether the date is considered a "magic date" if the product of the month and day equals the last two
digits of the year.

Pseudocode:
Read in the month in a value between 1-12 as month
Read in the day in a value between 1-31 as day
Read in the year in the form of a 4 digit number as year
Read in the format choice for the date as format_choice

If the user chooses 'ddmmyy', program will set variable, printed_date, to specified format in relation to date, month and year.
Otherwise, program will set variable, printed_date, to format in relation to 'mmddyy' 

Program will print the date based on the chosen format

if the products of the month and day equal the reminder of the years divided by 100, program will display "It is a magic date".

TEST DATA
Input                                               Output
Month:   Day:     Year:     Format:                  Date:         Magic Date Message?:
  1       1       1901       mmddyy                 1/1/1901                Yes
  10     31       1993       mmddyy                10/31/1993                No
  5       5       1994       ddmmyy                 5/5/1994                Yes

'''
# Inputs for the days, months, and the years as integers
month = int(input('Enter month (1-12): '))
day = int(input('Enter day (1-31): '))
year = int(input('Enter year: '))


# Input for the choice of format
format_choice = input('Choose which format to use: ddmmyy or mmddyy: ')

# Chooses the format based user input
if format_choice == 'ddmmyy':
    printed_date = f'{day}/{month}/{year}'
elif format_choice == 'mmddyy':
    printed_date = f'{month}/{day}/{year}'
else:
    print('That is not a valid format')

# Program will print the day based on the chosen format
print (printed_date)

# Determines the magic day
if (month * day) == year % 100:
    print ('It is a magic date')
    