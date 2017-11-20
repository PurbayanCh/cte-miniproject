import random
import numpy as np
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
        self.r_put()
        print(np.matrix(self.matrix))

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
        self.r_put()
        print(np.matrix(self.matrix))


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
        self.r_put()
        print(np.matrix(self.matrix))


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
        self.r_put()
        print(np.matrix(self.matrix))


    def play(self):
        self.r_put()
        self.r_put()
        print(np.matrix(self.matrix))
        while(1):
            a = input()
            if a=='w':
                self.up()
            if a=='a':
                self.left()
            if a=='s':
                self.down()
            if a=='d':
                self.right()
            if a=='q':
                break
            if self.check_end():
                print("You Lost!")
                break
    
    def check_end(self):
        a=1
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j]==0:
                    a=0
        return a

G = game()
G.play()