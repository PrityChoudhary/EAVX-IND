def print_digit(digit):
    for i in range(5):
        for j in range(5):
            if digit == 1:
                if j == 2:
                    print("*", end="")
                else:
                    print(" ", end="")
            elif digit == 2:
                if i == 0 or i == 2 or i == 4:
                    print("*", end="")
                elif i == 1 and j == 4:
                    print("*", end="")
                elif i == 3 and j == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
            elif digit == 3:
                if i == 0 or i == 2 or i == 4:
                    print("*", end="")
                elif (i == 1 or i == 3) and j == 4:
                    print("*", end="")
                else:
                    print(" ", end="")
            elif digit == 4:
                if i < 3 and j == 0:
                    print("*", end="")
                elif i == 2:
                    print("*", end="")
                elif j == 4:
                    print("*", end="")
                else:
                    print(" ", end="")
            elif digit == 5:
                if i == 0 or i == 2 or i == 4:
                    print("*", end="")
                elif i == 1 and j == 0:
                    print("*", end="")
                elif i == 3 and j == 4:
                    print("*", end="")
                else:
                    print(" ", end="")
            elif digit == 6:
                if i == 0 or i == 2 or i == 4:
                    print("*", end="")
                elif i == 1 and j == 0:
                    print("*", end="")
                elif i == 3 and (j == 0 or j == 4):
                    print("*", end="")
                else:
                    print(" ", end="")
            elif digit == 7:
                if i == 0:
                    print("*", end="")
                elif i == 1 and j == 4:
                    print("*", end="")
                elif i == 2 and j == 3:
                    print("*", end="")
                elif i == 3 and j == 2:
                    print("*", end="")
                elif i == 4 and j == 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            elif digit == 8:
                if i == 0 or i == 2 or i == 4:
                    print("*", end="")
                elif j == 0 or j == 4:
                    print("*", end="")
                else:
                    print(" ", end="")
            elif digit == 9:
                if i == 0 or i == 2:
                    print("*", end="")
                elif i == 1 and (j == 0 or j == 4):
                    print("*", end="")
                elif i == 3 and j == 4:
                    print("*", end="")
                elif i == 4 and j == 4:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()


# Print all digits from 1 to 9
for d in range(1, 10):
    print(f"Pattern for {d}:\n")
    print_digit(d)
    print()
