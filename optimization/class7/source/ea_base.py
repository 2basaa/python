import random, sys
import copy
import numpy as np

class Individual(list):
    def __init__(self, nobj, nvar, vlow, vhigh, initype):
        self.nvar = nvar
        self.nobj = nobj
        self.fitness = ()
        self.rank = [-1.0] * 2
        self.xmin= vlow
        self.xmax= vhigh
        if initype == 'binary':#2進数
            for i in range(nvar):
                if random.random() < vhigh : # 0 < vhigh < 1
                    self.append(1)
                else:
                    self.append(0)
        elif initype == 'int':#整数
            for i in range(nvar):
                self.append(random.randint(vlow,vhigh))
        elif initype == 'real':
            for i in range(nvar):
                r = vlow + (vhigh - vlow)*random.random()
                self.append(r)
        elif initype == 'permutation':#順列
            x = np.random.permutation(vhigh)
            lx = x.tolist()
            for i in range(nvar):
                self.append(lx[i])
        else:
            sys.exit("Init Error: init " + str(initype))

    def printind(self):
        output = ' '.join(map(str,self)) + ' '
        output += ' '.join(map(str, self.fitness))
        output += ' ' + ' '.join(map(str,self.rank))
        #print(output)
        return output

class Population(list):
    def __init__(self, size=0, nobj=0, nvar=0, vlow=0, vhigh=0, initype=0):
        for i in range(size):
            self.append(Individual(nobj, nvar, vlow, vhigh, initype))

    def printpop(self):
        for i in range(len(self)):
            self[i].printind()

    def fprintbest(self,f, i):
        f.write(self[i].printind()+'\n')

    def fprintpop(self,f):
        for i in range(len(self)):
            f.write(self[i].printind()+'\n')

def binary_tournament(pop, n):
    parents = []
    #repeat n binary tournaments
    for k in range(0,n):
        i = random.randint(0,len(pop)-1)
        j = random.randint(0,len(pop)-1)
        j = (i+j)%len(pop)
        if pop[i].fitness > pop[j].fitness:
            parents.append(pop[i])
        else:
            parents.append(pop[j])
    return parents

def crossover_1p(ind1, ind2):
    k = random.randint(0,len(ind1)-1)
    #print(k)
    xind = copy.deepcopy(ind1)
    nvar_change = 0
    for i in range(k,len(ind1)-1):
        if ind1[i] != ind2[i]:
            nvar_change += 1
        ind1[i] = ind2[i]
        ind2[i] = xind[i]
    return nvar_change

def bit_flip_mutation(ind, mutp):
    nvar_change = 0
    for i in range(0,len(ind)):
        if random.random() < mutp:
            ind[i] = (ind[i]+1)%2
            nvar_change += 1
    return nvar_change
    
###########real_problem_operators##############
def crossover_blend(ind1, ind2, pcv = 0.5):
    nvar_change = 0
    for i in range(len(ind1)):
        if (random.random() < pcv): # crossover this variable
            x1 = ind1[i]
            x2 = ind2[i]
            if x2 > x1:
                xlow = x1 - 0.5 * abs(x2 -x1)
                xhigh = x2 + 0.5 * abs(x2 -x1)
            else:
                xlow = x2 - 0.5 * abs(x2 -x1)
                xhigh = x1 + 0.5 * abs(x2 -x1)

            ind1[i] = xlow + random.random()*(xhigh - xlow)
            ind2[i] = xlow + random.random()*(xhigh - xlow)
            if ind1[i] < ind1.xmin:
                ind1[i] = ind1.xmin
            if ind1[i] > ind1.xmax:
                ind1[i] = ind1.xmax
            if ind2[i] < ind2.xmin:
                ind2[i] = ind2.xmin
            if ind2[i] > ind2.xmax:
                ind2[i] = ind2.xmax
            nvar_change += 1
    return nvar_change

def gaussian_mutation(ind, mutp):
    step = 0.5
    nvar_change = 0
    for i in range(0,len(ind)):
        if random.random() < mutp:
            ind[i] = ind[i]+ step*random.gauss(0, 1)
        if ind[i] < ind.xmin:
            ind[i] = ind.xmin
        if ind[i] > ind.xmax:
            ind[i] = ind.xmax
        nvar_change += 1
    return nvar_change