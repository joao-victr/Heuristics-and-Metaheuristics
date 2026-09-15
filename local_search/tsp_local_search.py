import numpy as np

def swap(solution: list, i:int, j: int):
    temp_solution = solution.copy()
    temp = temp_solution[i]
    temp_solution[i] = temp_solution[j]
    temp_solution[j] = temp
    return temp_solution

def evaluate(solution: list, distance_matrix: np.array):
    distance = 0
    for i in range(len(solution) - 1):
        distance += distance_matrix[solution[i] - 1][solution[i + 1] - 1]
    distance += distance_matrix[solution[-1] - 1][solution[0] - 1]
    return distance

def run(initial_solution: list, matrix, max_iter = 100):
    current_solution = initial_solution
    current_distance = evaluate(initial_solution, matrix)
    num_cities = len(matrix)

    for _ in range(max_iter):
        for i in range(num_cities - 1):
            for j in range(i + 1, num_cities):
                new_solution = swap(current_solution, i, j)
                new_distance = evaluate(new_solution, matrix)
                if new_distance < current_distance:
                    current_solution = new_solution
                    current_distance = new_distance
                    
    return current_solution, current_distance
