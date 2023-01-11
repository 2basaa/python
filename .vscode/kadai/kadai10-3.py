end_day = 29
for day in range(1, end_day +1):
    print(' %2d' % day, end ='')
    if day % 7 == 0:
        print()