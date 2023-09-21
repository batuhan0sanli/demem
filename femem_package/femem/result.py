class FEMEMResult:
    def __init__(self, **kwargs):
        self.runtime = kwargs.get('runtime')
        self.total_potential = kwargs.get('fun')
        self.total_weight = kwargs.get('total_weight')
        self.best_solution = kwargs.get('u')

        self.total_iterations = kwargs.get('nit')
        self.total_evaluations = kwargs.get('nfev')

        self.restraints = kwargs.get('r')
        self.displacements = kwargs.get('u')
        self.elongation_rate = kwargs.get('n')
        self.stress = kwargs.get('s')
        # self.strain: list = []

    def __repr__(self):
        return """
        FEMEM Results:
        
        Runtime           : {runtime:.4f} seconds
        Total Potential   : {total_potential}
        Total Weight      : {total_weight}
        Best Solution     : {best_solution}
        Total Iterations  : {total_iterations}
        Total Evaluations : {total_evaluations}
        Restraints        : {restraints}
        Displacements     : {displacements}
        Elongation Rate   : {elongation_rate}
        Stress            : {stress}
        """.format(**self.__dict__)
