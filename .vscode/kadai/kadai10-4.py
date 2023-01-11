end_day = 29 
start_wday = 2
target_week = start_wday
print('   ' * start_wday, end = '')
for day in range(1, end_day + 1):
    print(' %2d' % day, end ='')
    target_week += 1
    if target_week == 7:
        print()
        target_week = 0