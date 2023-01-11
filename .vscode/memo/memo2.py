print("メモ帳")
name = input("氏名：")
date = input("日付：")
memo = input("メモ：")

with open ('memo.csv', 'a') as f:
    f.write(name + ",")
    f.write(date + ",")
    f.write(memo + "\n")