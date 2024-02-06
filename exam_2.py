'''
num = -1 
loop = 0

while num < 0:
    num = int(input('Enter Number: '))
    print('Invalid number')
    while num > 0:
        if num == 0:
            print("0")
            break
        else:
            num = num // 2 
            loop += 1
            
print(loop)
'''
num = -1
loop = 0
while num < 0:
    num = int(input('Enter Number: '))
    if num < 0:
        print('Invalid number')
    else:
        while num > 0:
            if num == 0:
                print("0")
                num = -1
                break
            else:
                num = num // 2 
                loop += 1
            
print(loop)