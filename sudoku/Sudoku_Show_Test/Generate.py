import random
import numpy as np

class Generate(object):
    # initiate grid
    def __init__(self, n):
        self.martix = np.zeros((9, 9), dtype='i1')
        self.Nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.n = n  # blank number
        # when blanking ,save the grid step by step
        self.uniqueMartix = []

    # generate sudoku
    def Las_sdk(self, counts):
        """
        :param counts: the number of numbers
        """
        while counts:
            # [x, y] is grid position, which means the position of grid is generated randomly
            r = random.randint(0, 8)
            c = random.randint(0, 8)
 
            # blank in matrix
            if self.martix[r, c] == 0:
                # get number randomly
                v = random.sample(self.possible_num(r, c), 1)[0]
                self.martix[r, c] = v
                counts -= 1
 
        # solve the sudoku
        if self.Solve():
            return True
        else:
            return False
 
    # solve sudoku
    def Solve(self):
        for r in range(9):
            for c in range(9):
                if self.martix[r, c] == 0:
                    possible = self.possible_num(r, c)  # all possible numbers
                    for v in possible:
                        self.martix[r, c] = v
                        if self.Solve():
                            return True
                        self.martix[r, c] = 0
                        self.r, self.c = r, c
                    return False
        return True

    # create sudoku
    def build_martix(self):
        while not self.Las_sdk(11):
            pass
        self.Generate(self.n)
        return self.martix
 
 
    # number[1, 9] Randomly arranged
    def possible_num(self, r, c):
        """
        :param r: x-coordinate
        :param c: y-coordinate
        :return: return possible number set
        """
        # [x, y] is the position of large grid(3 by 3 little square)
        x, y = r // 3, c // 3
        """
        self.martix[r, :]: [r, c]the r of grid
        self.martix[:, c]: [r, c]the cumn of grid
        """
        rSet = set(self.martix[r, :])  # [r, c] the r number set
        cSet = set(self.martix[:, c])  # [r, c] the cumn number set
        blockSet = set(self.martix[x * 3: x * 3 + 3, y * 3: y * 3 + 3].reshape(9))  # [r, c] the large gird number set
 
        return self.Nums - rSet - cSet - blockSet
 
    # Generate Sudoku puzzles from Sudoku disks
    def Generate(self, n):
        # level represent the number of blank number,usually 30-50
        # we can make at most 63-64 blank square which can have unique result,but will take a long time
        self.uniqueMartix = self.martix.copy()
 
        counts = 0
        while counts < n:
            r = random.randint(0, 8)
            c = random.randint(0, 8)
            # it havs been digged
            if self.uniqueMartix[r, c] == 0:
                continue
 
            # Digging out the grid generates a unique nine-box grid. If there is, keep digging, if there is no unique solution, do not dig this grid
            if self.IsOnly(r, c):
                # save after digging
                self.uniqueMartix[r, c] = 0
 
                # Keep digging after the hole until the specified number of grids are dug
                self.martix = self.uniqueMartix.copy()
 
                counts += 1
 
    # determine whether we have unique solution
    def IsOnly(self, r, c):
        for v in range(1, 10):
            if self.martix[r][c] != v:
                # if we dig this number
                self.martix[r][c] = 0
                if v in self.possible_num(r, c):
                    # replace a number to see whether there is another solution
                    self.martix[r][c] = v
                    if self.Solve():
                        return False
 
                # The above has changed the v of self.martix, restoring the state before replacing this number
                self.martix = self.uniqueMartix.copy()
 
        # have tried all other numbers, only one solution
        return True