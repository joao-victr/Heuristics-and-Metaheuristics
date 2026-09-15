import math
import numpy as np

def read_tsp(input_path):
    with open(input_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read().splitlines()

    content = [line.split(" ") for line in content]

    for i in range(len(content)):
        content[i] = [int(element) for element in content[i]]

    num_cities = len(content)
    matrix = np.zeros((num_cities, num_cities))

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            x1, y1 = content[i][1], content[i][2]
            x2, y2 = content[j][1], content[j][2]
            dij = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
            matrix[i][j] = dij
            matrix[j][i] = dij
    return matrix