prefectures = {'大分県': 1.82, 
'岐阜県': 2.43, 
'佐賀県': 2.5, 
'滋賀県': 2.04,
'千葉県': 1.86,
'長野県': 1.85,
'奈良県': 1.87,
'新潟県': 1.79,
'福島県': 2.15,
'三重県': 2.09}
print('合計:', str('{:.2f}'.format(round(sum(prefectures.values()), 2))).ljust(5) + ',', end = '')
average = sum(prefectures.values()) / len(prefectures)
print(' ', '平均:', str(round(average, 2)))
print('県名 ', '本数  ', '差')
print('-----------------')

for prefecture, number in prefectures.items():
    difference = '{:.2f}'.format(round((number - average), 2))
    print(prefecture, '{:.2f}'.format(number), difference.rjust(5))
