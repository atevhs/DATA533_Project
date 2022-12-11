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
 
    # create sudoku
    def build_martix(self):
        # self.LasVegas(11)  # sudoku generate
        while not self.LasVegas(11):
            pass
        self.Generate(self.n)
        return self.martix
 
    # Lasvegas algorithm to generate sudoku
    def LasVegas(self, counts):
        """
        :param counts: the number of numbers
        :return:
        """
        while counts:
            # [x, y] is grid position, which means the position of grid is generated randomly
            row = random.randint(0, 8)
            col = random.randint(0, 8)
 
            # blank in matrix
            if self.martix[row, col] == 0:
                # get number randomly
                value = random.sample(self.Get_possible(row, col), 1)[0]
                self.martix[row, col] = value
                counts -= 1
 
        # use DFS to solve the sudoku
        if self.Solve():
            return True
        else:
            return False
 
    # solve sudoku
    def Solve(self):
        for row in range(9):
            for col in range(9):
                if self.martix[row, col] == 0:
                    possible = self.Get_possible(row, col)  # all possible numbers
                    for value in possible:
                        self.martix[row, col] = value
                        if self.Solve():
                            return True
                        self.martix[row, col] = 0
                        self.row, self.col = row, col
                    return False
        return True
 
    # number[1, 9] Randomly arranged
    def Get_possible(self, row, col):
        """
        :param row: x-coordinate
        :param col: y-coordinate
        :return: return possible number set
        """
        # [x, y] is the position of large grid(3 by 3 little square)
        x, y = row // 3, col // 3
        """
        self.martix[row, :]: [row, col]the row of grid
        self.martix[:, col]: [row, col]the column of grid
        """
        rowSet = set(self.martix[row, :])  # [row, col] the row number set
        colSet = set(self.martix[:, col])  # [row, col] the column number set
        blockSet = set(self.martix[x * 3: x * 3 + 3, y * 3: y * 3 + 3].reshape(9))  # [row, col] the large gird number set
 
        return self.Nums - rowSet - colSet - blockSet
 
    # Generate Sudoku puzzles from Sudoku disks
    def Generate(self, n):
        # level represent the number of blank number,usually 50-60
        # we can make at most 63-64 blank square which can have unique result,but will take a long time
        self.uniqueMartix = self.martix.copy()
 
        counts = 0
        while counts < n:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            # it havs been digged
            if self.uniqueMartix[row, col] == 0:
                continue
 
            # Digging out the grid generates a unique nine-box grid. If there is, keep digging, if there is no unique solution, do not dig this grid
            if self.IsUnique(row, col):
                # save after digging
                self.uniqueMartix[row, col] = 0
 
                # Keep digging after the hole until the specified number of grids are dug
                self.martix = self.uniqueMartix.copy()
 
                counts += 1
 
    # determine whether we have unique solution
    def IsUnique(self, row, col):
        for value in range(1, 10):
            if self.martix[row][col] != value:
                # if we dig this number
                self.martix[row][col] = 0
                if value in self.Get_possible(row, col):
                    # replace a number to see whether there is another solution
                    self.martix[row][col] = value
                    if self.Solve():
                        return False
 
                # The DFS above has changed the value of self.martix, restoring the state before replacing this number
                self.martix = self.uniqueMartix.copy()
 
        # have tried all other numbers, only one solution
        return True