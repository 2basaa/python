number = int(input())
word = 1

if number == 0 or number == 1 or number == 2:
    print("0~2を入力しました。")
    print(number)
elif number == 3 or number == 4 or number == 5 or number == 6:
    print("3~6を入力しました。")
    print(number)
else:
    for i in range(5):
#word += 2でwordが2たされた状態になる。
        word += 2
    print("7~9を入力しました。")
    print(word)