class selection:
    def __init__(self, data):
        self.data = data
        self.start_index = 1#インデックスの開始位置
        self.min_point = 0#最小要素のインデックス
        self.max_point = 0#最大要素のインデックス
        self.min_value = 0#最小要素の値
        self.max_value = 0#最大要素の値
        self.point = 0#開始位置
        self.count = 0#試行回数

    def ascending(self):#昇順ソート
        while self.start_index <= len(self.data)-1:#開始位置がリストの末尾まで
            self.min_value = self.data[self.point]#最小値
            #最小値を探す
            for self.num in range(self.start_index, len(self.data)):
                if self.min_value > self.data[self.num]:
                    self.min_value = self.data[self.num]
                    self.min_point = self.num
                self.count += 1
            self.data[self.min_point] = self.data[self.point]#swap
            self.data[self.point] = self.min_value#swap
            self.start_index += 1#開始位置を変更
            self.point += 1#最小値を探すためのポイント
            self.min_point = self.point#最小値のポイント
        print(self.data)
        print(self.count)#n(n-1)/2回
        #以下では初期化を行う
        self.start_index = 1
        self.min_point = 0
        self.point = 0
        self.count = 0

    def descending(self):#降順ソート
        while self.start_index <= len(self.data)-1:#開始位置がリストの末尾まで
            self.max_value = self.data[self.point]#最大値
            #最大値を探す
            for self.num in range(self.start_index, len(self.data)):
                if self.max_value < self.data[self.num]:
                    self.max_value = self.data[self.num]
                    self.max_point = self.num
                self.count += 1
            self.data[self.max_point] = self.data[self.point]#swap
            self.data[self.point] = self.max_value#swap
            self.start_index += 1#開始位置を変更
            self.point += 1#最大値を探すためのポイント
            self.max_point = self.point#最大値のポイント
        print(self.data)
        print(self.count)#n(n-1)/2回
        #初期化
        self.start_index = 1
        self.max_point = 0
        self.point = 0
        self.count = 0
    
data = [7, 3, 1, 5, 6, 4, 9]
selection = selection(data)
selection.ascending()
selection.descending()