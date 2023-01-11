from jturtle import *
line_height = float(input())
line_width = round(10 / line_height, 6)
rectangle = [line_height, line_width, line_height, line_width]

if line_height < 0:
    print(rectangle)
    exit(0)

for line in rectangle:
    forward(line)
    right(90)

done()