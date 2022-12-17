import unittest
from Sudoku_Show.Generate import Generate as gd
import random
import numpy as np

class TestAdd(unittest.TestCase):
    def __init__(self, n):
        self.martix = np.zeros((9, 9), dtype='i1')
        self.Nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.n = n  
        self.uniqueMartix = []
        
    def test_Las_sdk(self): # test routine
        self.assertEqual(gd.Las_sdk(self,counts=30), True)
        self.assertEqual(gd.Las_sdk(self,counts=40), True)
        self.assertEqual(gd.Las_sdk(self,counts=50), True)
        self.assertEqual(gd.Las_sdk(self,counts=100), False)
    
unittest.main()