import numpy as np

def read_file(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines if line.strip()]

    grid = np.array([list(map(int, line.split())) for line in lines])

    return grid


if __name__ == "__main__":
    k = 4

    grid = read_file('docs/grid2.txt')

    n, m = grid.shape
    print(f"Finding largest product of {k} numbers in a {n}x{m} grid")

