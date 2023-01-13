import time
class bubble_sort:#バブルソート
    def __init__(self, data):#コンストラクタ
        self.data = data
        self.current_point = len(self.data) - 1
        self.max_index = len(self.data) - 1
        self.index = 0
        self.count = 0

    def reset_data(self):#データをリセットする
        self.current_point = len(self.data) - 1
        self.max_index = len(self.data) - 1
        self.index = 0
        self.count = 0

    def ascending(self):#昇順のソート
        while self.current_point != 0:#ポインタの場所が０でない場合
            for self.num in range(self.max_index, self.index, -1):#0~5まで行う。
                self.current_data = self.data[self.num]#現在のデータ
                if self.data[self.num-1] > self.data[self.num]:#swap
                    self.data[self.num] = self.data[self.num-1]
                    self.data[self.num-1] = self.current_data
                self.count += 1
            self.current_point -= 1#インデックスの場所を1つ前にずらす。
            self.index += 1 
        print(self.data)#昇順
        print(self.count)#回数
        self.reset_data()

    def descending(self):#降順のソート
        while self.current_point != 0:#ポインタの場所が０でない場合
            for self.num in range(self.max_index, self.index, -1):#0~5まで行う。
                self.current_data = self.data[self.num-1]#現在のデータ
                if self.data[self.num-1] < self.data[self.num]:#swap
                    self.data[self.num - 1] = self.data[self.num]
                    self.data[self.num] = self.current_data
                self.count += 1
            self.current_point -= 1#インデックスの場所を1つ前にずらす。
            self.index += 1 
        print(self.data)#降順
        print(self.count)#n(n-1)/2回
        self.reset_data()

start_time = time.time()
data = [2,3,4,1,5,7,3,8,5,3, 9,5,1,3,4,15,23,42]
bubble = bubble_sort(data)
bubble.ascending()
end_time = time.time()
#measurement_time = 測定時間
measurement_time = end_time - start_time 
print(measurement_time)
#bubble.descending()