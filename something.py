
num = int(input("Enter a number >= 0: "))
while num < 0:
  print('invalid number')
  num = int(input("Error: Enter a number >= 0: "))
number_of_divisions = 0
while num > 0:
    num = num // 2
    number_of_divisions = number_of_divisions + 1
print(number_of_divisions)