number = []
for i in range(5):
    word_1 = int(input())
    number.append(word_1)

hit = []
for i in range(5):
    word_2 = int(input())
    hit.append(word_2)

rate = []
rate_1 = int(hit[0]) / int(number[0])
rate.append(rate_1)
rate_2 = int(hit[1]) / int(number[1])
rate.append(rate_2)
rate_3 = int(hit[2]) / int(number[2])
rate.append(rate_3)
rate_4 = int(hit[3]) / int(number[3])
rate.append(rate_4)
rate_5 = int(hit[4]) / int(number[4])
rate.append(rate_5)

print(number)
print(hit)
print(rate)

ave = sum(rate) / len(rate)

print(ave)

if ave >= 0.3:
    print("好打者")
elif ave < 0.25:
    print("控え打者")
else:
    print("平均的な打者")



