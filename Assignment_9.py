'''
Jon Zheng

This program is designed to read in the users input on how many rows the K shape will have. It verifies the input is greater than 5 and an 
odd number.

I add or subtracted the amount of loops from the second set of asteriks from the first loop based on if it hit the middle section of the row. 
I used the equation (rows + or - 2) / 2 to get my middle point. The "+ or - 2" is due to the loop already starting at 1.  
'''
#get user input for number of rows to draw k
rows = int(input("Enter number of rows (odd value >= 5): "))

#validate input 
while rows < 5 or rows % 2==0:
   
     print("Bad resonse;", end =" ")
     
     #get user input for number of rows to draw k
     rows = int(input("Enter an odd number 5 or more: "))
     
for i in range(rows):#loop through number of rows
   
     print('*', end ="")#print asterik on every line at position 0
     
     #loop through number of cols but leave first column and continue 
     for j in range(1,int( ( rows + 3 ) / 2 ) ):
        
        if( i + j == int( ( rows + 2 ) / 2) or i-j == int( ( rows - 2 ) / 2 ) ):
           
           print('*', end =" ")#print asterik symbol 
        else:
           
           print(' ', end =" ")#print space
           
     print()#print new line