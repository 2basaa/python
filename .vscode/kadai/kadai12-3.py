from jturtle import *

line_length = int(input())
line_size = int(input())
for i in range(line_size):
    forward(line_length)
    right(360 / line_size)

done() 