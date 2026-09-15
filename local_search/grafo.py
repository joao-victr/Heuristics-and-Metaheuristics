import sys
import numpy


def create_graph(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().splitlines()

    instances = [line.split(' ') for line in content]

    adj_list = {i: [] for i in range(int(instances[0][0]) + 1)}
        
    matrix_dim = int(instances[0][0]) + 1

    adj_matrix = numpy.zeros((matrix_dim, matrix_dim))

    for i in range(1, len(instances)):
        node_u = int(instances[i][0])
        node_v = int(instances[i][1])
        weight = int(instances[i][2])

        adj_matrix[node_u][node_v] = weight
        adj_matrix[node_v][node_u] = weight

        adj_list[node_u].append((node_v, weight))
        adj_list[node_v].append((node_u, weight))

    del adj_list[0]
    return adj_list, adj_matrix


# adj_list, adj_matrix = create_graph('tsp_5')

# print('MATRIZ DE ADJACENCIA:')

# for row, col in enumerate(adj_matrix):
#     print(row, col)


# print('\n\nLISTA DE ADJACENCIA:')

# for node, neighbour in adj_list.items():
#     print(f'Node {node} - Neighbours { neighbour}')