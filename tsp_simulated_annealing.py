from local_search import tsp_local_search
import random
import math

def generate_neighbour(solution: list):
    rand1 = random.randint(0, len(solution) - 1)
    rand2 = random.randint(0, len(solution) - 1)
    new_solution = tsp_local_search.swap(solution, rand1, rand2)
    return new_solution


def solve(initial_solution: list, matrix, temperature: float, coef: float, SAmax: int = 100):
    solution = initial_solution
    solution_value = tsp_local_search.evaluate(solution, matrix)
    best_solution = initial_solution
    best_solution_value = solution_value

    j = 0
    while temperature > 1e-10:
        for i in range(SAmax):
            neighbour = generate_neighbour(solution)
            neighbour_value = tsp_local_search.evaluate(neighbour, matrix)

            if neighbour_value < solution_value:
                solution = neighbour
                solution_value = solution_value
                if neighbour_value < best_solution_value:
                    best_solution = neighbour
                    best_solution_value = neighbour_value

            elif random.random() < math.e**(-(neighbour_value - solution_value)/ temperature):
                solution = neighbour
                solution_value = solution_value
        temperature = coef * temperature
        if j % 100 == 0:
            print(f'Temperature: {temperature}')
        j+=1
    return best_solution, best_solution_value