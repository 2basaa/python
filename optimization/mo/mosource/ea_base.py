import random, sys
import copy

""" ------- Individual Class ------- """

class Individual(list):
    """Models an individual
    Inherits from list
        - Members of the list are the Variables of the individual
        - Other attributes of individual are
            - nvar:     number of variables
            - nobj:     number of objectives
            - fitness:  a tuple to keep fitness values
            - rank:     a list of length 2 to keep rankings 
    """
    def __init__(self, nobj, nvar, vlow, vhigh, initype):
        """Constructor
        
        Parameters
        ----------
        nobj: integer
            Number of objectives
        nvar: integer
            Number of variables
        vlow: integer (float)
            Lover bound for variables
        vhigh : integer (float)
            Upper bound for variables (if binary representation, 
            initial probability of ones)
        initype: string 
            Individual representation. So far: 'binary'
                
        """
        
        self.nvar = nvar
        self.nobj = nobj
        self.fitness = ()
        self.rank = [-1.0] * 2
        if initype == 'binary':
            for i in range(nvar):
                if random.random() < vhigh : # 0 < vhigh < 1
                    self.append(1)
                else:
                    self.append(0)
        else:
            sys.exit("Init Error: init " + str(initype))

    def printind(self):
        """Prints an individual
        The format is 
            v_1 v_2 ... v_nvar f_1 f_2 ... f_nobj r_0 r_1
        where 
         - v indicated a variable
         - f indicates fitness
         - r indicates rank
        """
        output = ' '.join(map(str,self)) + ' ' + ' '.join(map(str, self.fitness)) 
        output = output + ' ' + ' '.join(map(str,self.rank))
        #print(output)
        return output


""" ------- Population Class ------- """

class Population(list):
    """Models a population of individuals
    Inherits from list
        - Members of the list are Individuals
    """
    def __init__(self, size=0, nobj=0, nvar=0, vlow=0, vhigh=0, initype=0):
        """Constructor
        Creates a population by adding individuals. 
        If size is 0, creates an empty population
        
        Parameters
        ----------
        size: integer
            Population size
        nobj: integer
            Number of objectives
        nvar: integer
            Number of variables
        vlow: integer (float)
            Lover bound for variables
        vhigh : integer (float)
            Upper bound for variables (if binary representation, 
            initial probability of ones)
        initype: string 
            Individual representation. So far: 'binary'
                   
        """
        
        for i in range(size):
            self.append(Individual(nobj, nvar, vlow, vhigh, initype))
    
    def printpop(self):
        """Prints population
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        
        """
        for i in range(len(self)):
            print(i, self[i].printind())
        
    def fprintbest(self,f, i):
        """Writes to a file the i-th individual
        If propulation is ordered and i-th is 0, prints best inidividual
        
        Parameters
        ----------
        f: file pointer
            File pointer of file where to write
        i: integer
            Index of solution to be printed
        
        Returns
        -------
        None
        
        """
        f.write(self[i].printind()+'\n')
    
    def fprintpop(self,f):
        """Writes population to file
        
        Parameters
        ----------
        f: file pointer
            The pointer of a file obtained after opening that file
        """
        for i in range(len(self)):
            f.write(self[i].printind()+'\n')


""" ------- Parent Selection ------- """


def binary_tournament(pop, n):
    """Parent selection 
    Binary tournament based on fitness
    Performs a number of tournaments and adds winners to a pool of parents

    Parameters
    ----------
    pop: Population
        Population where to select parents from
    n: integer
        Number of tournaments (number of parents to be selected) 
        
    Returns
    -------
    Population
        Population of selected parents
           
    """
    parents = []
    #repeat n binary tournaments
    for k in range(0,n):  
        i = random.randint(0,len(pop)-1)
#        j = random.randint(0,len(pop)-1) # ERROR
        j = random.randint(1,len(pop)-1)      
        j = (i+j)%len(pop)
        if pop[i].fitness > pop[j].fitness:
#            parents.append(pop[i])  # ERROR
            parents.append(copy.deepcopy(pop[i]))
        else:
#            parents.append(pop[j])  # ERROR
            parents.append(copy.deepcopy(pop[j]))
    return parents




def binary_tournament_dom_cd(pop, n):
    """Parent selection 
    Binary tournament based on dominace rank and crowding distance
    Performs a given number of tournaments and adds winners to a pool of parents

    Parameters
    ----------
    pop: Population
        Population where to select parents from
    n: integer
        Number of tournaments (number of parents to be selected) 
        
    Returns
    -------
    Population
        Population of selected parents
           
    """

    parents = []
    #repeat n binaty tournaments
    for k in range(0,n):  
        i = random.randint(0,len(pop)-1)
        j = random.randint(1,len(pop)-1)
        j = (i+j)%len(pop)
        # decide by first rank, dominance
        # lower rank[0] better
        if pop[i].rank[0] != pop[j].rank[0]:
            #print("rank 1",  pop[i].rank[0], pop[j].rank[0])
            if pop[i].rank[0] < pop[j].rank[0]:
                parents.append(copy.deepcopy(pop[i]))
            else:
                parents.append(copy.deepcopy(pop[j]))
        else: #decide by secondary rank if same primary rank
            #print("rank 2", pop[i].rank[0], pop[j].rank[0])
            # larger rank[1] is better (crowding distance)
            if pop[i].rank[1] > pop[j].rank[1]:
                parents.append(copy.deepcopy(pop[i]))
            else:
                parents.append(copy.deepcopy(pop[j]))
            
    return parents



""" ------- Recombination Operators ------- """

def crossover_1p(ind1, ind2):
    """Recombination Operators 
    One point crossover  
    
    Parameters
    ----------
    ind1: Individual
        First parent for crossover 
    ind1: Individual
        Second parent for crossover 
        
    Returns
    -------
    Integer
        Number of variables where offspring differs from the parents
           
    """

    k = random.randint(0,len(ind1)-1)
    xind = copy.deepcopy(ind1)
    nvar_change = 0
    for i in range(k,len(ind1)):
        if ind1[i] != ind2[i]:
            nvar_change += 1
        ind1[i] = ind2[i]
        ind2[i] = xind[i]
    return nvar_change


""" ------- Mutation Operators ------- """

def bit_flip_mutation(ind, mutp):
    """Mutation Operators
   Bit flip mutation  
    
    Parameters
    ----------
    ind: Individual
        Individual to undergo mutation
    mutp: real
        Mutation probabbility per bit
        
    Returns
    -------
    Integer
        Number of variabels that change after mutation
           
    """

    nvar_change = 0
    for i in range(0,len(ind)):
        if random.random() < mutp:
            ind[i] = (ind[i]+1)%2
            nvar_change += 1
    return nvar_change


