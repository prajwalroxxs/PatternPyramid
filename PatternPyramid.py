rows = int(input("Enter the number of rows: "))

print("\nLower Triangular Pattern:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\nUpper Triangular Pattern:")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("\nPyramid Pattern:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
