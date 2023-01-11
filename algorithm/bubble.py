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

data = [2,3,4,1,5,7, 3]
bubble = bubble_sort(data)
bubble.ascending()
bubble.descending()