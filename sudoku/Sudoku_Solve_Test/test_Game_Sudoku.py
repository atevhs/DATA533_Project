import unittest
from Sudoku_Solve.Game_Sudoku import Game_Sudoku

import os
import sys
import time
import pygame
import numpy as np
from Sudoku_Show.paint import Paint
from Sudoku_Show.paint import Paintchild
from Sudoku_Show.Generate import Generate
from Sudoku_Solve import configs


class TestGame_Sudoku(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        lh.info("starting class: {} execution".format(cls.__name__))
        
    def setUp(self):
        self.screen_width = configs.parse_args1().screen_width
        self.screen_height = configs.parse_args1().screen_height
        self.selected_width = configs.parse_args2().selected_width
        self.selected_height = configs.parse_args2().selected_height
        self.block_gap = configs.parse_args3().block_gap
        self.block_size = configs.parse_args3().block_size
        self.level = configs.parse_args3().level
        self.game = Game_Sudoku(self.screen_width, self.screen_height, self.selected_width, self.selected_height,self.block_gap, self.block_size, self.level)
        
    def test_Form(self): # test routine
        self.assertIsNone(self.game.init())
        self.assertEqual(self.game.start, False)
        self.assertIsNone(self.game.IsSuccess())
        self.assertIsNone(self.game.IsRight(5))
        
    def test_IsSuccess(self): # test routine
        self.assertEqual(self.game.success_sign, False)
        self.assertEqual(self.game.blank, [])
        self.assertEqual(self.game.end_time, '')
        self.assertEqual(self.game.is_conflict, [])
     
    def tearDown(self):
        print("Execution ended for given Unit test") 
        
    @classmethod 
    def teardown_class(cls):
        lh.info("ending class: {} execution".format(cls.__name__))

if __name__ == "__main__":
    unittest.main()
