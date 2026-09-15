from read_tsp import read_tsp
from read_knapsack import read_knapsack
from local_search import tsp_local_search, knapsack_local_search
from greedy_methods import greedy_tsp_build, greedy_knapsack_build

graph = read_tsp('data/tsp_51')

initial_tsp_solution, distance = greedy_tsp_build.build(graph, random_start=True, policy='min')

new_solution, new_distance = tsp_local_search.run(initial_tsp_solution, graph, max_iter=100)

print("PROBLEMA DO CAIXEIRO VIAJANTE\n")
print(f"Solução Gulosa:\n{initial_tsp_solution}\nDistancia: {distance}")
print(f'\n\nSolução melhorada:\n{new_solution}\nDistancia: {new_distance}')


knapsack, capacity = read_knapsack('data/mochila_100_1000_1')

initial_knapsack_solution, initial_weight, initial_profit = greedy_knapsack_build.build(knapsack, capacity, policy='lowest_weight')

new_knapsack_solution, new_weight, new_profit = knapsack_local_search.run(
    initial_knapsack_solution,
    knapsack,
    capacity,
    max_iter=1000
)

print("\n")
print("PROBLEMA DA MOCHILA\n")
print(f"Solução Gulosa:\n{bin(initial_knapsack_solution)}\nPeso: {initial_weight}\nBeneficio: {initial_profit}")
print(f'\n\nSolução melhorada:\n{bin(new_knapsack_solution)}\nPeso: {new_weight}\nBeneficio: {new_profit}')
