
# Set accumulators
even_total = 0
odd_total = 0

# Begins program?
num = 0
# Actual Program
while num >= 0:
    num = int(input('Enter an integer: '))
     
    # Determines if number is even or odd and stop if negative
    if num % 2 == 0 and num > 0:
        even_total += num
        # Stops program if negative   
    elif num > 0 :   
        odd_total += num
    
# Prints final values 
print(f"Sum of even integers {even_total}")
print(f'Sum of odd integers {odd_total}')
