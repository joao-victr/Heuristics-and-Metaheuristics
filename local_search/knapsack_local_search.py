import sys
import random

def generate_initial_solution(table: dict, capacity: int, num_items: int):
    items = []
    for i in range(num_items):
        ratio = table[i][0] / table[i][1]
        items.append((ratio, i))

    items.sort(reverse=True)
    solution = 0
    current_weight = 0

    for ratio, i in items:
        _, weight = table[i]

        if current_weight + weight <= capacity:
            solution = solution | (1 << i)
            current_weight += weight

    return solution

def evaluate(solution: int, num_items: int, table: dict, capacity: int):
    value = 0
    weight = 0
    for i in range(num_items):
        if 1<<i & solution:
            value += table[i][0]
            weight += table[i][1]

    if weight > capacity:
        return -1, weight

    return value, weight

def flip(solution: int, index: int):
    return solution ^ (1 << index)

def run(solution: int, table: dict, max_capacity: int, max_iter: int = 100):
    num_items = len(table)
    current_solution = solution
    current_solution_value, current_weight = evaluate(solution=current_solution, num_items=num_items, table=table, capacity=max_capacity)

    for _ in range(max_iter):
        for i in range(num_items):
            new_solution = flip(solution=current_solution, index=i)
            new_value, new_weight = evaluate(solution=new_solution, num_items=num_items, table=table, capacity=max_capacity)
            if new_value > current_solution_value:
                current_solution = new_solution
                current_solution_value = new_value
                current_weight = new_weight

    return current_solution, current_weight, current_solution_value