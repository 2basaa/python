import ea_base as ea
import sea
import stat_sea
import real_problem as problem
import os
def main(obj, var, psize, gen, pc, vm, clones, problem_fn):
 
    """ Create the name of the output folder"""
    par = "_obj" + str(obj) + "_var" + str(var) + "_psize" + str(psize)
    par += "_gen" + str(gen) + "_pc"+ str(pc)
    par += "_vm" + str(vm) + "_clones" + str(clones)
    out_folder = problem_fn + par
    """ Create the problem """
    cwd=os.getcwd()
    rf = problem.RealProblem(problem_fn)
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
        pop = sea.sea_mu_plus_lambda(evaluate = rf.fitness,
            select = ea.binary_tournament, recombine = ea.crossover_blend,
            mutate = ea.gaussian_mutation, initype='real', seed=i,
            psize=psize, nvar = var, vlow=-3, vhigh=3,
            ngen=gen, pcx=pc, pmut=vm/var, keepclones = clones)
        os.chdir("..")
    """
    Output some statistics in the designated output folder
    """
    nbp= 10 # number of boxplots in addition to gen=0
    gen_list = [int(x*gen/nbp) for x in range(0,nbp+1)]
    #gen_list = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    far, lastg = stat_sea.stat_simple_ea(".", runs, gen_list, var)

    os.chdir(cwd)
    return pop

if __name__ == "__main__":
    main(obj=1, var=30, psize=50, gen=200, pc=1.0, vm=1, 
        clones=False, problem_fn="Ackley")