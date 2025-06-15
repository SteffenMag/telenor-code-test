import numpy as np
import argparse

def read_file(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines if line.strip()]

    grid = np.array([list(map(int, line.split())) for line in lines])

    return grid


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Find the largest product of k numbers in a grid.")
    parser.add_argument('--k', type=int, default=4, help='Number of consecutive numbers for the product')
    args = parser.parse_args()
    
    k = args.k

    grid = read_file('docs/grid2.txt')

    n, m = grid.shape
    print(f"Finding largest product of {k} numbers in a {n}x{m} grid")

