num=[1,10,9,3,5,6,2,7,8,15,14,19,178,217,333]
num1 = list(filter(lambda i: i % 7 == 0, num))
print(num1)