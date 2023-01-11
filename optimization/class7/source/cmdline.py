import ea_base as ea 
import sea
import stat_sea
import problem
import os

def main(obj, var, psize, gen, ipone, pc, vm, clones, problem_fn):
    """ Main function to call sea_mu_plus_lambda to solve single objective
    0/1 knapasack problems

    Parameters
    ----------
    obj: integer
    number of objectives
    var: integer
    number of variables
    psize: integer
    population size
    gen: integer
    number of generations
    ipone: real number in [0,1]
    initial probability of ones
    pc: real number in [0,1]
    probability of crossover
    vm: integer in [0, var]
    expected number of variables that undergo mutation
    clones: boolean (True, False)
    allow clones
    problem: string
    file name where the problem is described

    Returns
    -------
    Population
    The evolved population

    Comment
    -------
    Some problems and their optimum
    knapPI_1_100_1000_1 9147
    1
    knapPI_1_500_1000_1 28857
    knapPI_1_1000_1000_1 54503
    knapPI_1_10000_1000_1 563647
    """

    """ Create the name of the output folder"""
    #knapPI_1_100_1000_1_obj1_var100_psize100_gen200_ipone0.05
    #_pc1.0_vm1_clonesFalse
    par = "_obj" + str(obj) + "_var" + str(var) + "_psize" + str(psize)
    par += "_gen" + str(gen) + "_ipone"+ str(ipone) + "_pc"+ str(pc)
    par += "_vm" + str(vm) + "_clones" + str(clones)
    out_folder = problem_fn + par
    """ Create the problem """
    cwd=os.getcwd()
    problem_path = '../problems/instances_01_KP/large_scale/'
    knapsack = problem.Knapsack(problem_path + problem_fn )
    """ Set the output folder and move there"""
    results="../output/Sea/" + out_folder
    os.mkdir(results)
    os.chdir(results)

    """ Run the algorithm a given number of runs """
    runs=30
    for i in range(1,runs+1):
        print("*** Run ", i, " ***")
        run = "run"+str(i)
        os.mkdir(run)
        os.chdir(run)
        pop = sea.sea_mu_plus_lambda(evaluate = knapsack.fitness,
            select = ea.binary_tournament, recombine = ea.crossover_1p,
            mutate = ea.bit_flip_mutation, initype='binary', seed=i,
            psize=psize, nvar = knapsack.nitems, vlow=0, vhigh=ipone,
            ngen=gen, pcx=pc, pmut=vm/knapsack.nitems, keepclones = clones)
        os.chdir("..")
        """
        Output some statistics in the designated output folder
        """
    nbp= 10 # number of boxplots in addition to gen=0
    gen_list = [int(x*gen/nbp) for x in range(0,nbp+1)]
    #gen_list = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    far, lastg = stat_sea.stat_simple_ea(".", runs, gen_list, knapsack.nitems)

    os.chdir(cwd)
    return pop

if __name__ == "__main__":
    main(obj=1, var=100, psize=50, gen=30, ipone=0.05, pc=1.0, vm=1,
        clones=True, problem_fn="knapPI_1_100_1000_1.txt")