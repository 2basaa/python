number = []
n = int(input())
for i in range(n):
    word = int(input())
    number.append(word)
print(number)
answer = sum(number)
print(answer)
if answer > 100:
    print("100より大きいです。")
else:
    print("100以下です。")