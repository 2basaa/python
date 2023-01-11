import problem as problem
import ea_base as ea
import sea as sea
import random

problem_path = "../problems/instances_01_KP/large_scale/"
problem_fn = "knapPI_1_100_1000_1.txt"

fname = problem_path + problem_fn
knap = problem.Knapsack(fname)

###############Knapsack####################
x=[0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0]
knap.fitness(x)
print(knap.fitness(x))
x=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
knap.fitness(x)
x=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
knap.fitness(x)

##############Individual###################
#nobj= 1; nvar=20; vlow=0; vhigh=0.1; initype='binary'
nobj= 1; nvar=20; vlow=0; vhigh=5; initype='int'

#indv1の生成
indv1 = ea.Individual(nobj, nvar, vlow, vhigh, initype)
indv1.fitness
knap.fitness(indv1)

###indv1の評価と代入###
indv1.fitness = knap.fitness(indv1)

##indv1の評価値をアクセス####
indv1.fitness[0]

##評価値更新できない###
#indv1.fitness[0] = -100
indv1.printind()

##############Population###################
size = 10
pop = ea.Population(size, nobj, nvar, vlow, vhigh, initype)
'''
pop
pop[0]
knap.fitness(pop[0])
pop[0].fitness = knap.fitness(pop[0])

for i in range(0, len(pop)):
    pop[i].fitness = knap.fitness(pop[i])

for i in range(0, len(pop)):
    print(pop[i].fitness)

pop.printpop()

f = open("pop_test.txt", "w")
pop.fprintpop(f)
f.close()

f = open("pop_test_best.txt", "w")
pop.fprintbest(f, 3)
f.close()
'''

ind1 = pop[0]
ind2 = pop[1]
y=ea.crossover_1p(ind1, ind2)
type(ind1)
ind1.printind()
ind2.printind()
print(ind1)

####Mutation###
ind1 = pop[0]
y=ea.bit_flip_mutation(ind1, 0.1)
print(y)
ind1.printind()

random.randint(0, len(pop)-1)
random.randint(0, 2)

A = [1, 2, 3, 4, 5]
B = A
A[0] = -100

parents = ea.binary_tournament(pop, 6)
ea.crossover_1p(parents[0], parents[1])

problem_path = '../problems/instances_01_KP/low-dimensional/'
problem_fn = "f2_l-d_kp_20_878.txt"
knap = problem.Knapsack(problem_path + problem_fn)

sea.sea_mu_plus_lambda(evaluate=knap.fitness, select=ea.binary_tournament,
 recombin=ea.crossover_1p, mutate=ea.bit_flip_mutation,seed=33, psize=50, 
 nvar=knap.nitems, vlow=0, vhigh=0.5,inittype='binary', ngen=100, pcx=1.0, pmut=2.0, keepclones = False)
