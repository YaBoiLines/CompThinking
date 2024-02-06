'''
Jon Zheng

This is the alternate version of the code that uses if-else statements. The assignment goals say to use while statements, but the prompts say if
so I wrote this one as well. The test data is exactly the same.

This program is design to give the user the amount of time, in terms of years, it would take to get to their target goal depending on 
the inital principal, target, and expected interest rate. It outputs a table to give the user the year and the ending balance principal
at the end of the year.

read in the principal value as principal
set year = 0
if principal in less than or equal to zero
    display the message "principal has to be more than zero"
Otherwise read target goal value as target
if target is less than or equal to zero
    displays the message "Target had to be more than principal"
Otherwise read in interest rate as int_rate
if int_rate is less than or equal to zero 
    displays the message "Interest rate has to be more than zero"
otherwise set int_rate to int_rate / 100
print "Year , End of the year principal" as table header
while principal is less than target
    set principal equal to (principal * int_rate) + 1
    set year equal to year + 1
    print the year and the principal until principal hit target value
    
TEST DATA
I used the compounding interest calculator on the IRS.gov website. I typed in my input and verified by inputing the principal
and expected years and interest rate to verify the ending principal.
I       n       p       u       t              O    u    t    p    u    t
Principal   Target  Interest Rate               Expected number of years
   10         20         10                                 8
   1         100          5                                95
   999       1000        99                                 1
    '''
# Reads in intial input from user
principal = float(input('Enter principal: '))
year = 0

# Ends the program if invalid input is given
if principal <= 0:
    print('Principal has to be more than 0') # Gives error statement to user
    
else:
    # Reads in next input
    target = float(input("Enter minimum target: "))

    # Ends program if invalid input is given
    if target <= principal:
        print('Target has to be more than principal') #Error statement
        
    else:
        # Next input from user
        int_rate = float(input('Enter interest rate in percentage: '))

        # Continues loop to get value above zero
        if int_rate <=0:
            print('Interest rate has to be more than 0')
        
        else:

            # Converts interest rate to percentage
            int_rate /= 100

            # Creates table header
            print('Year, End of the year principal')

            while principal < target: # Continues the program until Target value is achieved
                principal *= int_rate + 1 # Principal is added to year after year
                year += 1 # Year increases by 1
                print(f'{year}: ${principal:.2f}') # Formatting for ease of reading