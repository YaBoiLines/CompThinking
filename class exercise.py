'''
# Create variables for the user inputs 
start_pop = int(input('Starting number of organisms: '))
rate_increase = float(input('Average daily increase: '))
days_multply = int(input('Number of days to multiply: '))
# Initialize accumulator
pop = 0
# Create the table heading
print('Days Aproximates\tPopulation')
print('----------------------------')

for days in range(1,days_multply + 1):
    
    pop += start_pop *rate_increase 
    
    print(f'{days+1}\t\t\t{pop}')

    

# 5.29
import circle 
import rectangle

area_circle_choice = 1
circumfrence_choice = 2 
area_rectangle_choice = 3
perimeter_rectangle_choice = 4
quit_choice = 5

def main():
    choice = 0
    choice = int(input('Enter your choice: '))
    if choice == area_circle_choice:
        radius = float(input("Enter the circle's radius: "))
        print('The area is', circle.area(radius))
    elif choice == circumfrence_choice:
        radius = float(input("Enter the circle's radius"))
        print('The circumfrence is', circle.circumfrence(radius))
    elif choice == area_rectangle_choice:
        width = float(input("Enter the rectangle width: "))
        
7.1
numbers = [1, 2, 3, 4, 5]
numbers[2] = 99
print(numbers)

7.2
numbers = list(range(3))
print(numbers)

7.3
numbers = [10] * 5
print(numbers)

7.4
numbers = list(range(1,10,2))
for n in numbers:
    print(n)
    
7.5  
numbers=[1,2,3,4,5]
print(numbers[-2])

7.7
numbers1= [1,2,3]
numbers2=[10,20,30]
numbers3=numbers1+numbers2
print(numbers1)
print(numbers2)
print(numbers3)

7.8
numbers1=[1,2,3]
numbers2=[10,20,30]
numbers2+=numbers1
print(numbers1)
print(numbers2)


def main():
    # Get the test scores form the user
    scores = get_scores()
    # Get the total of the test scores
    total = get_total(scores)
    # Get the lowest test score
    lowest = min(scores)
    # Subtract the lowest test score
    total -= lowest
    #Calucate average, minus 1 because we drop lowest score
    average = total / (len(scores)-1)
    #Display average
    print(f'Average with the lowest grade dropped:{average}')

def get_scores():
    #Empty list
    test_scores = []
    #variable to control loop
    again = 'y'
    #Get scores form users and add them to list
    while again == 'y':
        #Get a score and add to the list
        value = float(input('Enter a test score: '))
        test_scores.append(value)
        
        #If user wants to do it again
        print('Do you want to add another score?')
        again = input('y = yes, anything else = no: ')
        print()
    #Return the list
    return test_scores

def get_total(value_list):
    #Create a variable as accumulator
    total = 0.0
    #Calculate the total of the list elements
    for num in value_list:
        total+= num
        return total
    
if __name__ == '__main__':
    main()
    '''
import matplotlib.pyplot as plt


def main():
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    bar_width = 5
    plt.bar(left_edges, heights, bar_width)
    plt.show()
#if __name__=='__main__':
main()
    
    