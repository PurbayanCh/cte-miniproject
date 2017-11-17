import random

class game:
    
    def __init__(self):
        self.matrix = [[0 for i in range(4)] for i in range(4)]
    
    # puts 2 at a random unoccupied space
    def r_put(self):
        while(1):
            a = random.randint(0,3)
            b = random.randint(0,3)
            if(self.matrix[a][b]==0):
                self.matrix[a][b] = 2
                break


def up(self):
    for k in range(4):
        for i in range(1,4):
            for j in range(4):
                if self.matrix[i][j]==self.matrix[i-1][j]:
                    self.matrix[i-1][j]+=self.matrix[i][j]
                        self.matrix[i][j]=0
                    if self.matrix[i-1][j]==0:
                        self.matrix[i-1][j]=self.matrix[i][j]
                        self.matrix[i][j]=0
    r_put()
        print(self.matrix)


def down(self):
    for k in range(4):
        for i in range(2,-1,-1):
            for j in range(4):
                if self.matrix[i][j]==self.matrix[i+1][j]:
                    self.matrix[i+1][j]+=self.matrix[i][j]
                        self.matrix[i][j]=0
                    if self.matrix[i+1][j]==0:
                        self.matrix[i+1][j]=self.matrix[i][j]
                        self.matrix[i][j]=0
    r_put()
        print(self.matrix)


def left(self):
    for k in range(4):
        for j in range(1,4):
            for i in range(4):
                if self.matrix[i][j]==self.matrix[i][j-1]:
                    self.matrix[i][j-1]+=self.matrix[i][j]
                        self.matrix[i][j]=0
                    if self.matrix[i][j-1]==0:
                        self.matrix[i][j-1]=self.matrix[i][j]
                        self.matrix[i][j]=0
    r_put()
        print(self.matrix)


def right(self):
    for k in range(4):
        for j in range(2,-1,-1):
            for i in range(4):
                if self.matrix[i][j]==self.matrix[i][j+1]:
                    self.matrix[i][j+1]+=self.matrix[i][j]
                        self.matrix[i][j]=0
                    if self.matrix[i][j+1]==0:
                        self.matrix[i][j+1]=self.matrix[i][j]
                        self.matrix[i][j]=0
    r_put(self.matrix)
        print(self.matrix)


def play(self):
    r_put(self.matrix)
        r_put(self.matrix)
        print(self.matrix)
        while(1):
            a = input()
            if a=='w':
                up(self.matrix)
            if a=='a':
                left(self.matrix)
            if a=='s':
                down(self.matrix)
            if a=='d':
                right(self.matrix)
            if a=='q':
                break

G = game()
G.play()
