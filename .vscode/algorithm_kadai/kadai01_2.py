number_list = [] 
for number in range(0, 11):
  if number == 0:
    print(number)
    number_list.append(number)

  elif number == 1:
    print(number)
    number_list.append(number)

  else:
    fib = number_list[number - 1] + number_list[number - 2]
    print(fib)
    number_list.append(fib)
