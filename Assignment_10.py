'''
Jon Zheng

This program was designed to determine whether or not the matrix given in the program is considered a LoShu Magic Square
or not. It calculates the sum of the rows, columns, and the diagonals. The program will display a message telling
the user if the results.

'''
def magic_square(square):
    #Verifies all rows, columns, and diagonals have the same sum
    goal = sum(square[0])
    
    #Check rows
    for row in square:
        if sum(row) != goal:
            return False
    
    #Check columns
    for col in range(3):
        if sum(square[row][col] for row in range(3)) != goal:
            return False
    
    #check first diagonal
    if sum(square[i][i] for i in range(3)) != goal:
        return False
    
    #Check second Diagnonal
    if sum(square[i][2-i] for i in range (3)) != goal:
        return False
    
    return True
def main():
    
    Lo_Shu_Grid = [
        [3, 4, 5],
        [8, 9, 1],
        [3, 4, 6]
    ]
    if magic_square(Lo_Shu_Grid):
        print('The square is a Lo Shu Magic Square')
    else:
        print('The square is not a Lo Shu Magic Square')
        
main()