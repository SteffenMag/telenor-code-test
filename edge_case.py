from decimal import Decimal, getcontext

# To support finding the product of 5 or more numbers with high precision

def find_largest_product_edge(grid, k):
    getcontext().prec = 50
    n, m = grid.shape
    largest_product = Decimal(0)
    path = []

    for row in range(n):

        for col in range(m):

            if col + k <= m:

                horizontal_product = Decimal(1)

                for c in range(col, col + k):

                    horizontal_product *= Decimal(int(grid[row, c]))

                if horizontal_product > largest_product:

                    largest_product = horizontal_product
                    path = [(row, c) for c in range(col, col + k)]

            
            if row + k <= n:

                vertical_product = Decimal(1)
                
                for r in range(row, row + k):
                
                    vertical_product *= Decimal(int(grid[r, col]))
                
                if vertical_product > largest_product:
                
                    largest_product = vertical_product
                    path = [(r, col) for r in range(row, row + k)]

            
            if col + k <= m and row + k <= n:

                diagonal_down_right_product = Decimal(1)

                for i in range(k):

                    diagonal_down_right_product *= Decimal(int(grid[row + i, col + i]))

                if diagonal_down_right_product > largest_product:

                    largest_product = diagonal_down_right_product
                    path = [(row + i, col + i) for i in range(k)]


            if col - k + 1 >= 0 and row + k <= n:

                diagonal_down_left_product = Decimal(1)

                for i in range(k):

                    diagonal_down_left_product *= Decimal(int(grid[row + i, col - i]))

                if diagonal_down_left_product > largest_product:

                    largest_product = diagonal_down_left_product
                    path = [(row + i, col - i) for i in range(k)]

    return largest_product, path