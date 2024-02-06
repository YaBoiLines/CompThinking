#Calculating the area and perimeter of the rectangle

#Get the length of the rectangle
rec_len = int(input('What is the length of the rectangle?: '))

#Get the width of the rectangle
rec_wid = int(input('What is the width of the rectangle?: '))

#Calculate the area of the rectangle
rec_area = rec_len * rec_wid

#Calculate the perimeter of the rectangle
rec_peri = (2 * rec_len) + (2 * rec_wid)

#Display all the data for the consumer
print ('length:', rec_len , 'width:', rec_wid , 'area:', rec_area , 'perimeter:', rec_peri)