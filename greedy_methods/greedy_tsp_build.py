from read_tsp import read_tsp
from typing import Literal
import random

def build(matrix, start:int = 1, random_start=False, policy: Literal['min', 'max'] = 'min'):

    start = start if not random_start else random.randint(1, len(matrix))
    current_solution = [start]
    current_distance = 0
    for i in range(len(matrix) - 1):
        row = list(enumerate(matrix[current_solution[-1] - 1].copy()))
        row = [item for item in row if item[1] != 0 and item[0] + 1 not in current_solution]

        next = min(row, key=lambda x: x[1]) if policy == 'min' else max(row, key=lambda x: x[1]) 
        current_solution.append(next[0] + 1)
        current_distance += next[1]

    current_distance += matrix[current_solution[-1]][0]

    return current_solution, current_distance