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