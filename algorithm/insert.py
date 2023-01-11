#挿入ソート
class insert:
    def __init__(self, data):
        self.data = data#
        self.data_number = len(self.data)#
        self.start_index = 1#開始インデックス
        self.insert_index = 0#挿入インデックス
        self.point = 0#変わったかどうかのためのポイント
        self.count = 0#試行回数

    def ascending(self):#昇順
        #0からlen(data)-1回まで
        while self.start_index < len(self.data):
            self.standard = self.data[self.start_index]#基準値
            for self.num in range(0, self.start_index):#０からstart_index-1まで
                if self.data[self.num] < self.standard:#挿入位置を探す
                    self.point += 1
                    self.insert_index = self.num
                self.count += 1
            del self.data[self.start_index]#データの開始インデックスを削除する
            if self.insert_index == 0 and self.point == 0:#for文の中のifが行われていない場合
                self.data.insert(self.insert_index, self.standard)
            #for文の中のifが発生した場合
            elif self.insert_index != 0 or self.insert_index == 0 and self.point != 0:
                self.data.insert(self.insert_index+1, self.standard)
            #挿入ソートの場所を探す
            self.point = 0
            self.start_index += 1
            self.insert_index = 0
        print(self.data)
        print(self.count)
        #初期化
        self.start_index = 1
        self.insert_index = 0
        self.point = 0
        self.count = 0

    def descending(self):#昇順
        #0からlen(data)-1回まで
        while self.start_index < len(self.data):
            self.standard = self.data[self.start_index]#基準値
            for self.num in range(0, self.start_index):#０からstart_index-1まで
                if self.data[self.num] > self.standard:#挿入位置を探す
                    self.point += 1
                    self.insert_index = self.num
                self.count += 1
            del self.data[self.start_index]#データの開始インデックスを削除する
            if self.insert_index == 0 and self.point == 0:#for文の中のifが行われていない場合
                self.data.insert(self.insert_index, self.standard)
            #for文の中のifが発生した場合
            elif self.insert_index != 0 or self.insert_index == 0 and self.point != 0:
                self.data.insert(self.insert_index+1, self.standard)
            #挿入ソートの場所を探す
            self.point = 0
            self.start_index += 1
            self.insert_index = 0
        print(self.data)
        print(self.count)
        #初期化
        self.start_index = 1
        self.insert_index = 0
        self.point = 0
        self.count = 0

data = [ 9, 7, 6, 8, 3, 5, 4]
insert = insert(data)
insert.ascending()
insert.descending()