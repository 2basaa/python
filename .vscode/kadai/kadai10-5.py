start_wday = 2 
end_days = [31, 28, 31, 31, 31, 30, 31, 31, 30, 31, 30, 31]
for end_day in end_days :
    print('   ' * start_wday, end ='')
    target_week = start_wday
    for day in range(1, end_day + 1):
        print(' %2d' % day, end ='')
        target_week += 1
        if target_week == 7:
            print()
            target_week = 0
    start_wday = target_week
    print("\n")