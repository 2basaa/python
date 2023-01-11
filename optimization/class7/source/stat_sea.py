import pandas as pd
import matplotlib.pyplot as plt

def get_fitness_all_runs(foutput, nruns, nvar):
    f_all_runs = pd.DataFrame()
    for i in range(1,nruns+1):
        fname = foutput + "/run" + str(i) + "/best.txt"
        data = pd.read_csv(fname, sep=" ", header=None)#
        f_all_runs = pd.concat([f_all_runs, data[nvar]], axis = 1)

    return f_all_runs

def hist_local_optima(foutput, f_all_runs):
    myFig = plt.figure()
    lastgen = f_all_runs[f_all_runs.shape[0]-1:].copy()
    plt.xlabel("Runs")
    plt.ylabel("Local optima")
    plt.hist(lastgen, bins=30, orientation = 'horizontal')
    myFig.savefig(foutput+"/histFinalSol.png",format="png",bbox_inches='tight')
    
    lgs = lastgen.T.sort_values(f_all_runs.shape[0]-1,ascending=False)
    f = open(foutput+"/local_optima.txt", "w")
    for i in range(lgs.shape[0]):
        f.write(str(lgs.iat[i,0]) + "\n")
    f.close()
    return lastgen

def boxplot_fitness_transition(foutput, f_all_runs, genlist):
    farT = f_all_runs.T
    myFig = plt.figure()
    plt.xlabel("Generarions")
    plt.ylabel("Fitness")
    plt.tight_layout()
    farT[genlist].boxplot()
    myFig.savefig("./"+foutput+"/evol.png", format="png", bbox_inches='tight')
    return farT
    
def stat_simple_ea(foutput, nruns, genlist, nvar):
    print("Statistics sea")

    f_all_runs = get_fitness_all_runs(foutput, nruns, nvar)
    lastgen = hist_local_optima(foutput, f_all_runs)
    farT = boxplot_fitness_transition(foutput,f_all_runs, genlist)

    return farT, lastgen