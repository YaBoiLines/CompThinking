'''
#1
product = 0
while product < 100:
    num = int(input('Enter an integer: '))
    result = num * 10
    product += result
    
#2
sum = 0
keep_going = 'y'
while keep_going == 'y':
    a = int(input('Enter first integer: '))
    b = int(input('Enter second integer: '))
    sum += (a + b)
    print(sum)
    keep_going = input("Do you want to keep going? y or n: ")

#3
for num in range (0, 1001, 10):
    print(num)

#4
sum = 0
for num in range (10):
    number = int(input('Enter a number: '))
    sum += number
    print(sum)

#5  
denominator = 30
total = 0
for numerator in range(1, 31):
    value = numerator/ denominator
    total = total + value
    denominator -= 1
    print(total)
'''
