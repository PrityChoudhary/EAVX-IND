def print_small_char(c):
    grid = [[" " for _ in range(10)] for _ in range(14)]

    if c == 'a':
        for i in range(7):
            for j in range(5):
                if i == 2 and j in [1, 2, 3] or \
                   i in [3, 4, 5] and (j == 1 or j == 4) or \
                   i == 6 and j in [1, 2, 3]:
                    grid[i][j] = "*"
    elif c == 'b':
        for i in range(7):
            for j in range(5):
                if j == 0 or \
                   (i in [0, 3, 6] and j in [1, 2, 3]) or \
                   j == 4 and i in [1, 2, 4, 5]:
                    grid[i][j] = "*"
    elif c == 'c':
        for i in range(7):
            for j in range(5):
                if i in [2, 6] and j in [1, 2, 3] or \
                   j == 0 and i in [3, 4, 5]:
                    grid[i][j] = "*"
    elif c == 'd':
        for i in range(7):
            for j in range(5):
                if j == 4 or \
                   (i in [2, 6] and j in [1, 2, 3]) or \
                   j == 0 and i in [3, 4, 5]:
                    grid[i][j] = "*"
    elif c == 'e':
        for i in range(7):
            for j in range(5):
                if i in [2, 4, 6] and j in [1, 2, 3] or \
                   j == 0 and i in [3, 4, 5] or \
                   j == 4 and i == 4:
                    grid[i][j] = "*"
    elif c == 'f':
        for i in range(7):
            for j in range(5):
                if i == 2 and j in [1, 2, 3] or \
                   j == 0 and i in [3, 4, 5, 6] or \
                   j == 2 and i in [0, 1]:
                    grid[i][j] = "*"
    elif c == 'g':
        for i in range(7):
            for j in range(5):
                if i == 2 and j in [1, 2, 3] or \
                   i == 6 and j in [1, 2, 3] or \
                   j == 0 and i in [3, 4, 5] or \
                   j == 4 and i in [3, 4, 5] or \
                   i == 4 and j == 2:
                    grid[i][j] = "*"
    elif c == 'h':
        for i in range(7):
            for j in range(5):
                if j == 0 or \
                   i == 3 and j in [1, 2, 3] or \
                   j == 4 and i in [4, 5, 6]:
                    grid[i][j] = "*"
    elif c == 'i':
        for i in range(7):
            for j in range(5):
                if i == 2 and j == 2 or \
                   j == 2 and i in [3, 4, 5, 6]:
                    grid[i][j] = "*"
    elif c == 'j':
        for i in range(7):
            for j in range(5):
                if i == 2 and j == 2 or \
                   j == 2 and i in [3, 4, 5] or \
                   i == 6 and j in [1, 2]:
                    grid[i][j] = "*"
    elif c == 'k':
        for i in range(7):
            for j in range(5):
                if j == 0 or \
                   i + j == 5 and i < 4 or \
                   i - j == 2 and i > 3:
                    grid[i][j] = "*"
    elif c == 'l':
        for i in range(7):
            for j in range(5):
                if j == 0 and i in [2, 3, 4, 5, 6] or \
                   i == 6 and j in [1, 2, 3]:
                    grid[i][j] = "*"
    elif c == 'm':
        for i in range(7):
            for j in range(5):
                if i in [3, 4, 5, 6] and (j == 0 or j == 2 or j == 4):
                    grid[i][j] = "*"
    elif c == 'n':
        for i in range(7):
            for j in range(5):
                if j == 0 or \
                   j == 4 and i >= 3 or \
                   i == 3 and j in [1, 2, 3]:
                    grid[i][j] = "*"
    elif c == 'o':
        for i in range(7):
            for j in range(5):
                if i in [2, 6] and j in [1, 2, 3] or \
                   j == 0 and i in [3, 4, 5] or \
                   j == 4 and i in [3, 4, 5]:
                    grid[i][j] = "*"
    elif c == 'p':
        for i in range(7):
            for j in range(5):
                if j == 0 or \
                   i == 3 and j in [1, 2, 3] or \
                   i == 2 and j in [1, 2, 3] or \
                   j == 4 and i == 4:
                    grid[i][j] = "*"
    elif c == 'q':
        for i in range(7):
            for j in range(5):
                if i == 2 and j in [1, 2, 3] or \
                   i == 6 and j in [1, 2, 3] or \
                   j == 0 and i in [3, 4, 5] or \
                   j == 4 and i in [3, 4, 5] or \
                   i == 5 and j == 2:
                    grid[i][j] = "*"
    elif c == 'r':
        for i in range(7):
            for j in range(5):
                if j == 0 or \
                   i == 3 and j in [1, 2, 3] or \
                   j == 4 and i == 4:
                    grid[i][j] = "*"
    elif c == 's':
        for i in range(7):
            for j in range(5):
                if i in [2, 4, 6] and j in [1, 2, 3] or \
                   i == 3 and j == 0 or \
                   i == 5 and j == 4:
                    grid[i][j] = "*"
    elif c == 't':
        for i in range(7):
            for j in range(5):
                if i == 2 and j in [0, 1, 2, 3, 4] or \
                   j == 2 and i in [3, 4, 5, 6]:
                    grid[i][j] = "*"
    elif c == 'u':
        for i in range(7):
            for j in range(5):
                if (j == 0 or j == 4) and i in [3, 4, 5] or \
                   i == 6 and j in [1, 2, 3]:
                    grid[i][j] = "*"
    elif c == 'v':
        for i in range(7):
            for j in range(5):
                if (i - j == 3 and i > 2) or (i + j == 7 and i > 2):
                    grid[i][j] = "*"
    elif c == 'w':
        for i in range(7):
            for j in range(5):
                if i in [3, 4, 5, 6] and (j == 0 or j == 2 or j == 4):
                    grid[i][j] = "*"
    elif c == 'x':
        for i in range(7):
            for j in range(5):
                if i + j == 6 or i == j:
                    grid[i][j] = "*"
    elif c == 'y':
        for i in range(7):
            for j in range(5):
                if (i - j == 0 and i < 5) or \
                   (i + j == 4 and i < 5) or \
                   j == 2 and i in [5, 6]:
                    grid[i][j] = "*"
    elif c == 'z':
        for i in range(7):
            for j in range(5):
                if i == 2 or i == 6 or i + j == 6:
                    grid[i][j] = "*"

    for row in grid:
        print("".join(row))


# Print a to z
for ch in range(ord('a'), ord('z') + 1):
    print(f"Pattern for {chr(ch)}:")
    print_small_char(chr(ch))
    print()
