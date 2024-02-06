'''
Jon Zheng

# Input from user
width = int(input("Enter width (between 1 and 99, not divisible by 10): "))

# Verifies input fits condition of assignment
while width < 1 or width > 99 or width % 10 ==0:
    # Asks for correct input
    width = int(input('Width has to be between 1 and 99, not divisible by 10: reenter: '))
        
# Gets the last digit for the loop statement
last_digit = width % 10

# Creates the loop based on the last digit variable
for n in range(last_digit):
    
    #Creates the loop to print as many times as the last digit is
    for n in range(last_digit):
        
        #Prints the * symbol as many as last digit is
        print(last_digit * "*")
     
    #Creates loop for print numbers up to last digit   
    for n in range(last_digit):
        
        #prints the last digit
        print(n + 1)
#Last loop for trailing "*"s    
for n in range(last_digit):  
          
    print(last_digit * '*')
    
    '''
    
# Jon Zheng
# Introduces functions

# Input from user
width = int(input("Enter width (between 1 and 99, not divisible by 10): "))

# Verifies input fits condition of assignment
while width < 1 or width > 99 or width % 10 ==0:
    # Asks for correct input
    width = int(input('Width has to be between 1 and 99, not divisible by 10: reenter: '))
        
# Gets the last digit for the loop statement
last_digit = width % 10

# Creates function for the for loop
def loop_func():
    
    for n in range(last_digit):
        print(last_digit * '*')

# Creates the loop based on the last digit variable
for n in range(last_digit):
    
    loop_func()
     
    #Creates loop for print numbers up to last digit   
    for n in range(last_digit):
        
        #prints the last digit
        print(n + 1)
        
#Last loop for trailing "*"s    
loop_func()