

def read_knapsack(input_path):
    with open(input_path, 'r', encoding="utf-8") as input_file:
        content = input_file.read().splitlines()

    instances = [line.split(' ') for line in content]

    table = {i-1: (int(instances[i][0]), int(instances[i][1])) for i in range(1, len(instances))}
    num_items = int(instances[0][0])
    max_capacity = int(instances[0][1])
    return table, max_capacity