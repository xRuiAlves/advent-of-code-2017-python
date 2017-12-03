input_val = 347991

# Create the matrix
matrix = [[0 for i in range (0,200)] for j in range(0,200)]

# Set the starting  point (Level 1)
level = 1
x = 100
y = 100
matrix[x][y] = 1
print(matrix[x][y])

while True:
    # Go to the next level (by summing one to X)
    level += 1
    x += 1

    # Compute that point
    matrix[x][y] = matrix[x-1][y] + matrix[x-1][y-1] + matrix[x][y-1] + matrix[x+1][y-1] + matrix[x+1][y] + matrix[x+1][y+1] + matrix[x][y+1] + matrix[x-1][y+1]
    print(matrix[x][y])

    if(matrix[x][y] > input_val):
        break

    # Compute the remaining points in this level
    for i in range(0,(level-1)*2 - 1):
        y -= 1
        matrix[x][y] = matrix[x-1][y] + matrix[x-1][y-1] + matrix[x][y-1] + matrix[x+1][y-1] + matrix[x+1][y] + matrix[x+1][y+1] + matrix[x][y+1] + matrix[x-1][y+1]
        print(matrix[x][y])
        if(matrix[x][y] > input_val):
            exit()

    for i in range(0,(level-1)*2):
        x -= 1
        matrix[x][y] = matrix[x-1][y] + matrix[x-1][y-1] + matrix[x][y-1] + matrix[x+1][y-1] + matrix[x+1][y] + matrix[x+1][y+1] + matrix[x][y+1] + matrix[x-1][y+1]
        print(matrix[x][y])
        if(matrix[x][y] > input_val):
            exit()

    for i in range(0,(level-1)*2):
        y += 1
        matrix[x][y] = matrix[x-1][y] + matrix[x-1][y-1] + matrix[x][y-1] + matrix[x+1][y-1] + matrix[x+1][y] + matrix[x+1][y+1] + matrix[x][y+1] + matrix[x-1][y+1]
        print(matrix[x][y])
        if(matrix[x][y] > input_val):
            exit()

    for i in range(0,(level-1)*2):
        x += 1
        matrix[x][y] = matrix[x-1][y] + matrix[x-1][y-1] + matrix[x][y-1] + matrix[x+1][y-1] + matrix[x+1][y] + matrix[x+1][y+1] + matrix[x][y+1] + matrix[x-1][y+1]
        print(matrix[x][y])
        if(matrix[x][y] > input_val):
            exit()
