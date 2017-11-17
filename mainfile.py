import random

# puts 2 at a random unoccupied space
def r_put(matrix):
    while(1):
        a = random.randint(0,3)
        b = random.randint(0,3)
        if(matrix[a][b]==0):
            matrix[a][b] = 2
            break

def up(matrix):
    for k in range(0,4):
        for i in range(1,4):
            for j in range(4):
                if matrix[i][j]==matrix[i-1][j]:
                    matrix[i-1][j]+=matrix[i][j]
                    matrix[i][j]=0
                if matrix[i-1][j]==0:
                    matrix[i-1][j]=matrix[i][j]
                    matrix[i][j]=0
    r_put(matrix)
    print(matrix)
matrix = [[0 for i in range(4)] for i in range(4)]
