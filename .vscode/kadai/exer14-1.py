make = {
    "大分県" : {"マヨ" : 1.82, "ケチャ":0.89, "みそ" : 2.71},
    "岐阜県" : {"マヨ" : 2.43, "ケチャ":0.84, "みそ" : 1.20},
    "佐賀県" : {"マヨ" : 2.50, "ケチャ":1.37, "みそ" : 2.30},
    "滋賀県" : {"マヨ" : 2.04, "ケチャ":1.06, "みそ" : 1.33},
    "千葉県" : {"マヨ" : 1.86, "ケチャ":0.89, "みそ" : 1.61},
    "長野県" : {"マヨ" : 1.85, "ケチャ":1.14, "みそ" : 3.22},
    "奈良県" : {"マヨ" : 1.87, "ケチャ":0.96, "みそ" : 1.61},
    "新潟県" : {"マヨ" : 1.79, "ケチャ":0.80, "みそ" : 2.15},
    "福島県" : {"マヨ" : 2.15, "ケチャ":0.94, "みそ" : 2.44},
    "三重県" : {"マヨ" : 2.09, "ケチャ":1.08, "みそ" : 1.39}
} 

sum_mayo = sum([i["マヨ"] for i in make.values()])
sum_ketch = sum([i["ケチャ"] for i in make.values()])
sum_miso = sum([i["みそ"] for i in make.values()])
ave_mayo = sum_mayo / len([i["マヨ"] for i in make.values()])
ave_ketch = sum_ketch / len([i["ケチャ"] for i in make.values()])
ave_miso = sum_miso / len([i["みそ"] for i in make.values()])

print("マヨ" , '   ' , '{:.2f}'.format(round(sum_mayo, 3), 2).format(2), round(ave_mayo, 3))
print("ケチャ" , '  ', round(sum_ketch, 3), '{:.2f}'.format(round(ave_ketch, 2),2))
print("みそ" , '   ' , round(sum_miso, 3), '{:.2f}'.format(round(ave_miso, 2),2)) 