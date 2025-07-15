def print_char(c):
    c = c.upper()
    grid = [[" " for _ in range(5)] for _ in range(7)]

    if c == 'A':
        for i in range(7):
            for j in range(5):
                if (i == 0 and j in [1, 2, 3]) or (i == 3) or (j == 0 and i != 0) or (j == 4 and i != 0):
                    grid[i][j] = "*"
    elif c == 'B':
        for i in range(7):
            for j in range(5):
                if j == 0 or (j == 4 and i not in [0, 3, 6]) or (i in [0, 3, 6] and j in [1, 2, 3]):
                    grid[i][j] = "*"
    elif c == 'C':
        for i in range(7):
            for j in range(5):
                if (i in [0, 6] and j in [1, 2, 3]) or (j == 0 and i not in [0, 6]):
                    grid[i][j] = "*"
    elif c == 'D':
        for i in range(7):
            for j in range(5):
                if j == 0 or (j == 4 and i not in [0, 6]) or (i in [0, 6] and j in [1, 2, 3]):
                    grid[i][j] = "*"
    elif c == 'E':
        for i in range(7):
            for j in range(5):
                if j == 0 or i in [0, 3, 6]:
                    grid[i][j] = "*"
    elif c == 'F':
        for i in range(7):
            for j in range(5):
                if j == 0 or i == 0 or i == 3:
                    grid[i][j] = "*"
    elif c == 'G':
        for i in range(7):
            for j in range(5):
                if (i in [0, 6] and j in [1, 2, 3]) or (j == 0 and i not in [0, 6]) or (i == 3 and j in [2, 3]) or (j == 4 and i in [4, 5]):
                    grid[i][j] = "*"
    elif c == 'H':
        for i in range(7):
            for j in range(5):
                if j == 0 or j == 4 or i == 3:
                    grid[i][j] = "*"
    elif c == 'I':
        for i in range(7):
            for j in range(5):
                if i == 0 or i == 6 or j == 2:
                    grid[i][j] = "*"
    elif c == 'J':
        for i in range(7):
            for j in range(5):
                if i == 0 or (j == 2 and i != 6) or (i == 6 and j in [1, 2]) or (i == 5 and j == 0):
                    grid[i][j] = "*"
    elif c == 'K':
        for i in range(7):
            for j in range(5):
                if j == 0 or (i + j == 4 and i < 4) or (i - j == 2 and i >= 4):
                    grid[i][j] = "*"
    elif c == 'L':
        for i in range(7):
            for j in range(5):
                if j == 0 or i == 6:
                    grid[i][j] = "*"
    elif c == 'M':
        for i in range(7):
            for j in range(5):
                if j == 0 or j == 4 or (i == j and j < 3) or (i + j == 4 and j > 1):
                    grid[i][j] = "*"
    elif c == 'N':
        for i in range(7):
            for j in range(5):
                if j == 0 or j == 4 or i == j:
                    grid[i][j] = "*"
    elif c == 'O':
        for i in range(7):
            for j in range(5):
                if (i in [0, 6] and j in [1, 2, 3]) or ((j == 0 or j == 4) and i not in [0, 6]):
                    grid[i][j] = "*"
    elif c == 'P':
        for i in range(7):
            for j in range(5):
                if j == 0 or (i in [0, 3] and j in [1, 2, 3]) or (j == 4 and i in [1, 2]):
                    grid[i][j] = "*"
    elif c == 'Q':
        for i in range(7):
            for j in range(5):
                if (i in [0, 6] and j in [1, 2, 3]) or ((j == 0 or j == 4) and i in [1, 2, 3, 4]) or (i == 5 and j == 3) or (i == 6 and j == 4):
                    grid[i][j] = "*"
    elif c == 'R':
        for i in range(7):
            for j in range(5):
                if j == 0 or (i in [0, 3] and j in [1, 2, 3]) or (j == 4 and i in [1, 2]) or (i - j == 2 and i >= 3):
                    grid[i][j] = "*"
    elif c == 'S':
        for i in range(7):
            for j in range(5):
                if (i in [0, 3, 6] and j in [1, 2, 3]) or (i in [1, 2] and j == 0) or (i in [4, 5] and j == 4):
                    grid[i][j] = "*"
    elif c == 'T':
        for i in range(7):
            for j in range(5):
                if i == 0 or j == 2:
                    grid[i][j] = "*"
    elif c == 'U':
        for i in range(7):
            for j in range(5):
                if (j == 0 or j == 4) and i != 6 or (i == 6 and j in [1, 2, 3]):
                    grid[i][j] = "*"
    elif c == 'V':
        for i in range(7):
            for j in range(5):
                if (i < 6 and (j == 0 and i < 4 or j == 4 and i < 4)) or (i - j == 2 and i > 3) or (i + j == 8 and i > 3):
                    grid[i][j] = "*"
    elif c == 'W':
        for i in range(7):
            for j in range(5):
                if j == 0 or j == 4 or (i == j and i > 2) or (i + j == 6 and i > 2):
                    grid[i][j] = "*"
    elif c == 'X':
        for i in range(7):
            for j in range(5):
                if i == j or i + j == 4:
                    grid[i][j] = "*"
    elif c == 'Y':
        for i in range(7):
            for j in range(5):
                if (i == j and i < 3) or (i + j == 4 and i < 3) or (j == 2 and i >= 3):
                    grid[i][j] = "*"
    elif c == 'Z':
        for i in range(7):
            for j in range(5):
                if i == 0 or i == 6 or i + j == 6:
                    grid[i][j] = "*"

    for row in grid:
        print("".join(row))


# Print A to Z
for ch in range(ord('A'), ord('Z') + 1):
    print(f"Pattern for {chr(ch)}:")
    print_char(chr(ch))
    print()
