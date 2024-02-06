
# First function for addition
def add():
    first_num = int(input('Enter a number: '))
    sec_num = int(input('Enter a number: '))
    result = first_num + sec_num
    print(f'{first_num} + {sec_num} is {result}')
  
# Second function for subtraction  
def subtract():
    first_num = int(input('Enter a number: '))
    sec_num = int(input('Enter a number: '))
    result = first_num - sec_num
    print(f'{first_num} - {sec_num} is {result}')
    
# Third function for multiplication
def multiply():
    first_num = int(input('Enter a number: '))
    sec_num = int(input('Enter a number: '))
    result = first_num * sec_num
    print(f'{first_num} * {sec_num} is {result}')
    
# Fourth function for division
def divide():
    first_num = int(input('Enter a number: '))
    sec_num = int(input('Enter a number: '))
    
    # Verifies the divisor is not 0
    while sec_num == 0: # Creates the loop to get a valid denominator
        print("Divisor can't be 0")
        sec_num = int(input('Enter a valid number: ')) # Input message for new value
    
    result = first_num // sec_num
    print(f'{first_num} / {sec_num} is {result}')
  
# Creates function to call other arithmetric functions 
def calculate():
    command = input('Enter operation a (add), s (subtract), m (multiply), d (divide), and e (exit): ') # Input for user
        
    if command == "a":
        add()
            
    elif command == "s":
        subtract()
            
    elif command == "m":
        multiply()
            
    elif command == "d":
        divide()
    
    elif command != "a" and command != "s" and command != "m" and command != "d" and command != "e":
        print('Enter valid input')
    
    calculate() #reloops calculation function
      
calculate()#Start the program