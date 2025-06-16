import numpy as np
import argparse
import time

from edge_case import find_largest_product_edge

def read_file(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines if line.strip()]

    grid = np.array([list(map(int, line.split())) for line in lines])

    return grid


def find_largest_product(grid, k):
    n, m = grid.shape

    largest_product = 0
    path = []
    nums = []

    for row in range(n):
        
        for col in range(m):

            # Check horizontal product
            if col + k <= m:

                horizontal_product = np.prod(grid[row, col:col + k])

                if horizontal_product > largest_product:

                    largest_product = horizontal_product
                    path = [(row, c) for c in range(col, col + k)]
                    nums = [grid[row, c] for c in range(col, col + k)]
            

            # Check vertical product
            if row + k <= n:

                vertical_product = np.prod(grid[row:row + k, col])

                if vertical_product > largest_product:

                    largest_product = vertical_product
                    path = [(r, col) for r in range(row, row + k)]
                    nums = [grid[r, col] for r in range(row, row + k)]
            

            # Check diagonal down right product
            if col + k <= m and row + k <= n:

                diagonal_down_right_product = np.prod([grid[row + i, col + i] for i in range(k)])

                if diagonal_down_right_product > largest_product:

                    largest_product = diagonal_down_right_product
                    path = [(row + i, col + i) for i in range(k)]
                    nums = [grid[row + i, col + i] for i in range(k)]


            # Check diagonal down left product
            if col - k + 1 >= 0 and row + k <= n:

                diagonal_down_left_product = np.prod([grid[row + i, col - i] for i in range(k)])

                if diagonal_down_left_product > largest_product:

                    largest_product = diagonal_down_left_product
                    path = [(row + i, col - i) for i in range(k)]
                    nums = [grid[row + i, col - i] for i in range(k)]
    print(f"Numbers contributing to the largest product: {nums} \n")
    return largest_product, path


if __name__ == "__main__":


    parser = argparse.ArgumentParser(description="Find the largest product of k numbers in a grid.")
    parser.add_argument('--k', type=int, default=4, help='Number of consecutive numbers for the product')
    args = parser.parse_args()
    
    k = args.k

    grid = read_file('docs/grid2.txt')

    n, m = grid.shape
    print(f"\nFinding largest product of {k} numbers in a {n}x{m} grid: \n")

    start_time = time.perf_counter()
    if k <= 4:
        largest_product, path = find_largest_product(grid, k)
    else:
        largest_product, path = find_largest_product_edge(grid, k)
    end_time = time.perf_counter()
    
    print(f"Largest product: {largest_product} \n")
    print(f"Path: {path} \n")
    print(f"Execution time of search: {end_time - start_time:.4f} seconds")