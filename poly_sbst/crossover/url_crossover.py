import numpy as np
from poly_sbst.crossover.abstract_crossover import AbstractCrossover



class UrlCrossover(AbstractCrossover):
    def __init__(self, cross_rate: float = 0.9):
        super().__init__(cross_rate)


    def _do_crossover(self, problem, a, b) -> tuple:
        mid = min(len(a),len(b))//2
        
        a_new = np.concatenate((a[:mid], b[mid:]))
        b_new = np.concatenate((b[:mid], a[mid:]))
        return a_new, b_new