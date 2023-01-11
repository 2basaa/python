number = list(range(1, 101))

for i in number:
    if i == 2:
        print(i)
    elif i == 3:
        print(i)
    elif i == 5:
        print(i)
    elif i == 7:
        print(i)
    elif i % 2 == 1:
        if not i % 3 == 0:
            if not i % 5 == 0:
                if not i % 7 == 0:
                    if i > 1:
                        print(i)