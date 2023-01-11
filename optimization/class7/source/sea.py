import random, operator, copy
import ea_base as ea

def sea_mu_plus_lambda(evaluate=None, select=None, recombine=None, mutate=None,
        seed=None, psize=None, nvar=None, vlow=None, vhigh=None,
        initype=None, ngen=None, pcx=None, pmut=None, keepclones = False):
    #Set random genetator
    random.seed(seed)
    #Initial population
    pop = ea.Population(size=psize, nobj=1, nvar=nvar, vlow=vlow,
                        vhigh=vhigh, initype=initype)

    #Evaluate the initial population
    for ind in pop:
        ind.fitness = evaluate(ind)

    #Output the population
    f = open("best.txt", "w")
    print(' --Generation 0')
    pop.sort(key= operator.attrgetter('fitness'), reverse=True)
    #pop.printpop()
    pop.fprintbest(f, 0)
    for g in range(1, ngen+1):
        #select parents
        parents = select(pop, len(pop))
        offspring = copy.deepcopy(parents)
        #Apply crossover and mutation on the offspring
        #list[start:stop:step]
        for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < pcx:
                recombine(ind1, ind2)
            mutate(ind1, pmut)
            mutate(ind2, pmut)

        #Evaluate offspring population
        for ind in offspring:
            ind.fitness = evaluate(ind)

        #Truncate the population (extinctive selection)
        #The new population is the best among pop and offspring
        join_pop = pop + offspring
        #Delete clones
        if keepclones == False:
            join_pop = []
            for ind in (pop+offspring):
                if ind not in join_pop:
                    join_pop.append(ind)
        join_pop.sort(key = operator.attrgetter('fitness'), reverse= True)
        pop[:] = join_pop[0:psize]
        #Output the population and or best
        if g%(ngen/4) == 0:
            print(' --Generation', g)
        #pop.printpop()
        pop.fprintbest(f, 0)
    f.close()
    print('Ends')
    return pop 