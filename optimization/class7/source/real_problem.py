import functions_mv as func
import numpy as np
class RealProblem:
    def __init__(self, fname):
        """Constructor
        Parameters
        ----------
        fname: string
        name of the real function
        """
        # For minimization functions
        self.sign = -1.0
        self.fname = fname
        if fname == 'Squared':
            self.func = func.squared_f
        elif fname == 'Rastrigin':
            self.func = func.rastrigin
        elif fname == 'Rosenbrock':
            self.func = func.rosenbrock
        elif fname == 'Styblinski':
            self.func = func.styblinski
        elif fname == 'Ackley':
            self.func = func.ackley
        else:
            print("Error: RealProblem: ", fname)
            exit()


    def fitness(self, x):
        y = self.func(np.array(x))
        return self.sign*y,