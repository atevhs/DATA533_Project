import unittest
from Sudoku_Show.Generate import Generate
from Sudoku_Solve.Game_Sudoku import Game_Sudoku
import random
import numpy as np

class TestGenerate(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        print("Testing Module Paint from Sudoku Show")
        
    def setUp(self):
        self.martix = np.zeros((9, 9), dtype='i1')
        self.Nums = {1, 2, 3, 4, 5, 6, 7, 8, 9} 
        self.uniqueMartix = []
        #self.possible_num = 30
        self.game = Generate(30)
        
    def test_Las_sdk(self): # test routine
        self.assertNotEqual(self.game.Las_sdk(30), True)
        self.assertFalse(self.game.Solve())
        self.assertNotEqual(self.game.Solve(), True)
        self.assertFalse(self.game.Las_sdk(0))
        #self.assertNotEqual(self.game.build_martix(), False)
        
    def test_possible_num(self):
        self.assertNotEqual(self.game.possible_num(5,2), 0)
        self.assertEqual(self.game.possible_num(5,2), {1, 2, 3, 4, 5, 6, 7, 8, 9})
        self.assertIsNone(self.game.__init__(2))
        self.assertNotEqual(self.game.__init__(2),False)
        
    def tearDown(self):
        print("Execution ended for given Unit test")   
         
    @classmethod 
    def teardown_class(cls):
        print("Ending Testing for Module Paint from Sudoku Show")
        #lh.info("ending class: {} execution".format(cls.__name__))

if __name__ == "__main__":
    unittest.main()