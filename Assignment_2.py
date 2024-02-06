'''
Jon Zheng
This program will ask how many rooms they are, area of a single room, and the number of room carpeted. 
It will then output the total area tiled

Pseudocode:
Read in the total number of rooms into num_room
Read in the area of a single room into area_singleRoom
Read in the number of carpeted rooms into num_carpetRoom
set area_tiled = (num_room * area_singleRoom) - (area_singleRoom * num_carpetRoom)
Print the the number of rooms, area of a single room, number of rooms carpeted, and the area tiled

Sample Set one:
I           n           p                   u               t                   Output
Number of Rooms       Area of a room        Number of carpeted rooms        Area tiled
        4                   10                          2                       20
        
Sample Set two:
I           n           p                   u               t                   Output
Number of Rooms       Area of a room        Number of carpeted rooms        Area tiled
        0                   10                          0                        0
'''

num_room = int(input('Enter number of rooms: '))

area_singleRoom = float(input('Enter area of a single room: '))

num_carpetRoom = int(input('Enter number of rooms carpeted: '))

area_tiled = (num_room * area_singleRoom) - (area_singleRoom * num_carpetRoom)

print(f'Number of rooms: {num_room}, Area of a single room: {area_singleRoom}, Number of rooms carpeted: {num_carpetRoom}, Area tiled: {area_tiled}')