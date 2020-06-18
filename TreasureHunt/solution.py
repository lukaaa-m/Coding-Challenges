import random as r
import math as m

arr_width = 10
arr_height = 10

arr = [['O'] * arr_width for i in range(arr_height)]

guess_arr = [['X'] * arr_width for i in range(arr_height)]

distance_zones = {0 : 'Hot!',
                  1 : 'Warm...',
                  2 : 'Cold :(',
                  3 : 'Freezing.'}

def chooseTreasureLoc():
    global treasure_x
    global treasure_y
    treasure_x = r.randint(0,arr_width-1)
    treasure_y = r.randint(0,arr_height-1)
    #print(f'Treasure X,Y: {treasure_x}, {treasure_y}')

    arr[treasure_y][treasure_x] = '1'

    #for row in arr:
    #    print(row)

def askUser():
    #THIS DOESN'T WORK AKSDLJFSDJF
    try:
        guess = input('Enter your coordinate guess (in format `x,y`)')
        guess = guess.split(',')
        x = int(guess[0]) - 1
        y = int(guess[1]) - 1
    except ValueError:
        askUser()
    return x,y

def getDistance(x,y):
    if x != treasure_x or y!= treasure_y:
        xdiff = x-treasure_x
        ydiff = y-treasure_y
        #print(f'Xdiff, Ydiff: {xdiff}, {ydiff}')

        d = m.sqrt(xdiff**2 + ydiff**2)

        zone = m.floor(d/4)
        #print(f'Distance: {d}')
        #print(f'Zone: {zone}')

        return distance_zones[zone]

    elif x == treasure_x and y == treasure_y:
        return 'You found the treasure! Congratulations'

chooseTreasureLoc()
def main():
    guessx, guessy = askUser()
    result = getDistance(guessx,guessy)

    guess_arr[guessy][guessx] = arr[guessx][guessy]
    for row in guess_arr:
        print(row)
    print(result)

    if result == 'You found the treasure! Congratulations':
        return 1
    else:
        return 0

while main() != 1:
    main()

    