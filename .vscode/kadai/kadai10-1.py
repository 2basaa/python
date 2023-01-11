from turtle import *

EXPANSION = 10
def move_point(code):
    if code == 0 or code == 1:
        forward(code * EXPANSION)
    elif code == 2 or code == 3:
        right(90)
        forward(code * EXPANSION)
        left(90)
    elif code == 4 or code == 5:
        right(180)
        forward(code * EXPANSION)
        left(180)
    elif code == 6 or code == 7:
        left(90)
        forward(code * EXPANSION)
        right(90)
    elif code == 8 or code == 9:
        right(90)
        circle(code * EXPANSION)
        left(90)
    return 

number = input()
left(90)
move_point(int(number[0]))
move_point(int(number[1]))
move_point(int(number[2]))
move_point(int(number[3]))

done()