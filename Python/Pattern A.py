def print_A(height):
    width = (2 * height) - 1
    n = width // 2
    for i in range(height):
        for j in range(width + 1):
            if j == n or j == (width - n) or (i == height // 2 and j > n and j < (width - n)):
                print("*", end="")
            else:
                print(" ", end="")
        print()
        n -= 1

# Example usage
print_A(5)
