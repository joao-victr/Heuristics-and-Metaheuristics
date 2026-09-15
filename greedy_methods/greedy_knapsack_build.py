from read_knapsack import read_knapsack
from typing import Literal

def build(table: dict, capacity: int, policy: Literal['highest_ratio', 'lowest_weight'] = 'highest_ratio'):
    items = []
    num_items = len(table)
    for i in range(num_items):
        if policy == 'highest_ratio':
            ratio = table[i][0] / table[i][1]
            items.append((ratio, i, table[i][0]))
            items.sort(reverse=True)
        else:
            items.append((table[i][1], i, table[i][0]))
            items.sort()

    solution = 0
    current_weight = 0
    current_profit = 0

    for ratio, i, profit in items:
        _, weight = table[i]

        if current_weight + weight <= capacity:
            solution = solution | (1 << i)
            current_weight += weight
            current_profit += profit

    return solution, current_weight, current_profit