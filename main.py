from read_tsp import read_tsp
from read_knapsack import read_knapsack
from local_search import tsp_local_search, knapsack_local_search
from greedy_methods import greedy_tsp_build, greedy_knapsack_build
import tsp_simulated_annealing

graph = read_tsp('data/tsp_51')

initial_tsp_solution, distance = greedy_tsp_build.build(graph, random_start=True, policy='min')

print(f'Solução Inicial:\n{initial_tsp_solution}')
print(f'Valor:\n{distance}')


k = 10
alpha = 0.95

new_solution, new_value = tsp_simulated_annealing.solve(
    initial_solution=initial_tsp_solution,
    matrix=graph,
    temperature=10000,
    coef=alpha,
    SAmax=k * len(graph)
)
print(f'Solução Inicial:\n{initial_tsp_solution}')
print(f'Valor:\n{distance}')


print("\n\n")
print(f'Solução Final:\n{new_solution}')
print(f'Valor:\n{new_value}')

