#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe

#それぞれの月の末尾を決定させる
def detect_month(number):
    #month_date = 0
    #date is 31
    if number == 1 or number == 3 or number == 5 or \
        number == 8 or number == 10 or number == 12:
        month_date = 31
    #date is 28
    elif number == 2:
        month_date = 28
    #date is 30
    else:
        month_date = 30
    return month_date

#改行を作る
#カレンダーとしての見やすさを作成
def suit_day(now_date, day_of_week_number, last_day):
    #見やすくするために10以下と10以上で分けて出力させる
    if now_date < 10:
        #土曜日なら改行
        if day_of_week_number == 6:
            #1桁の時
            print(" " + str(now_date))
            day_of_week_number = -1
        else:
            print(" " + str(now_date), end="  ")
    else:
        #土曜日なら改行
        if day_of_week_number == 6:
            print(now_date)
            day_of_week_number = -1
        else:
            print(now_date, end="  ")
    #月の最終日なら改行
    if now_date == last_day:
        print("\n")  
    day_of_week_number += 1           
    return day_of_week_number  
    
#月の初めの曜日を合わせる
def fit_first_day(day_of_week_number):
    print("")
    for block_num in range(day_of_week_number):
        print(end="    ")#endを使うことで改行無し

#2023年のカレンダーを作成
def main():
    #day_of_weekは曜日
    day_of_week = ["日","月","火","水","木","金","土"]
    week_name = ["January", "February", "March", "April", "May", "Jun", "July", 
                 "August", "September", "October", "November", "December"]
    #現在の曜日の番号
    day_of_week_number = 0
    print("----------2023-----------")
    #1月から12月まで
    for now_month in range(1, 13):
        print(str(now_month) + "月"+ "            " + week_name[now_month-1])
        print("-------------------------")
        #曜日を出力
        for day in day_of_week:
            print(day, end="  ")
        fit_first_day(day_of_week_number)
        last_day = detect_month(now_month)
        #日にちを出力
        for now_date in range(1, last_day + 1):
            day_of_week_number = suit_day(now_date, day_of_week_number, last_day)
                  
if __name__ == "__main__":
    main()