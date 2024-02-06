'''
Jon Zheng
This program is designed to be a calculator that takes in certains commands to perform addtion, subtraction, multiplication, division, and
squaring. It will ask for two number in the form of integers and calulate the result then display it. It will only ask for one integer for
the square.

Pseudocode
Print the message to explain the program and all command prompts.
Read in the command by the user as command
if the command is equal to a, it will read in the first number as first_num and the second number as sec_num
    set result to first_num + sec_num
    print the sum of the two integers
if the command is s, it will read in the first number as first_num and the second number as sec_num
    set result to first_num - sec_num
    print the difference of the two integers
if the command is d, it will read in the first number as first_num and the second number as sec_num
    if the sec_num is equal to 0, print the message "the divisor can't be 0"
    otherwise, set result to first_num / sec_num
    print the quotient of the two integers
if the command is q, it will read in the number as num_square
    set result equal to num_square ** 2
    print the suare value
otherwise, any other input is given the program will give an error message

TEST DATA
Operation       Operand1        Operand2        Expected Output
a                   0               1                 1
s                   0               1                -1
m                   0               1                 0
d                   7               2                 3.5
d                   4               0             Divisor can't be 0
q                   0               N/A               0
q                   9               N/A               81
'''

# Initial Introduction to Program
print("""This is a simple calculator that supports
addition, subtraction, multiplication, division, and square

Enter:

a to add
s to subtract
m to multiply
d to divide
q to square""")

# Ask for user input
command = input('Enter command: ')

# First command for addition
if command == 'a':
    first_num = int(input('Enter the first number: '))
    sec_num = int(input('Enter the second number: '))
    result = first_num + sec_num
    print(f'The sum is {result}')
  
# Second command for subtraction  
elif command == 's':
    first_num = int(input('Enter the first number: '))
    sec_num = int(input('Enter the second number: '))
    result = first_num - sec_num
    print(f'The difference is {result}')
    
# Third command for multiplication
elif command == 'm':
    first_num = int(input('Enter the first number: '))
    sec_num = int(input('Enter the second number: '))
    result = first_num * sec_num
    print(f'The product is {result}')
    
# Fourth command for division
elif command == 'd':
    first_num = int(input('Enter the first number: '))
    sec_num = int(input('Enter the second number: '))
    
    # Verifies the divisor is not 0
    if sec_num == 0: 
        print("Divisor can't be 0")
    else:
        result = first_num / sec_num
        print(f'The quotient is {result}')

# Fifth command for squares
elif command == 'q':
    num_square = int(input('Enter number to be squared: '))
    result = num_square ** 2
    print(f'The square is {result}')
   
# Tells users of invalid command 
else:
    print('Invalid command')