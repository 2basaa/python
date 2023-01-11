class Knapsack:
    def __init__(self, fname) :
        self.fname = fname
        fproblem = open(self.fname)
        line = (fproblem.readline()).split()
        self.nitems = int(line[0])
        self.capacity = int(line[1])
        self.profit=[]
        self.weigth=[]
        for i in range(self.nitems):
            line = (fproblem.readline()).split()
            self.profit.append(int(line[0]))
            self.weigth.append(int(line[1]))
        fproblem.close()

    def fitness(self, x):
        f = 0
        for i in range(len(x)):
            f = f + self.profit[i]*x[i]
        g = 0
        for i in range(len(x)):
            g = g + self.weigth[i]*x[i]

        # penalization term if
        if g > self.capacity:
            f = -(g-self.capacity)
        return f,