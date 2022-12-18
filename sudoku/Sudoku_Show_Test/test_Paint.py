import unittest
import pygame
from Sudoku_Show.paint import Paint as pd
from Sudoku_Solve.Game_Sudoku import Game_Sudoku
from Sudoku_Solve import configs
import time
import pygame
import datetime

class TestPaint(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        print("Testing Module Paint from Sudoku Show")
        #lh.info("starting class: {} execution".format(cls.__name__))
        
    def setUp(self):
        print("Setting up Unit Test")
        self.selected_form = pygame.display.set_mode([260, 300], 0, 0) 
        self.move_x = 0
        self.move_y = 0
        self.form = pygame.display.set_mode([560, 700], 0, 0)
        #self.form = Game_Sudoku.form
        self.time = 0
        self.start_time = 0
        self.end_time= 0
        self.screen_width = configs.parse_args1().screen_width
        self.screen_height = configs.parse_args1().screen_height
        self.selected_width = configs.parse_args2().selected_width
        self.selected_height = configs.parse_args2().selected_height
        self.block_gap = configs.parse_args3().block_gap
        self.block_size = configs.parse_args3().block_size
        self.level = configs.parse_args3().level
        self.game = Game_Sudoku(self.screen_width, self.screen_height, self.selected_width, self.selected_height,self.block_gap, self.block_size, self.level)
        
    def tearDown(self):
        print("Execution ended for given Unit test")
    
    def test_PaintSelected(self): # test routine
        self.assertIsNone(pd.PaintSelected(self,self.selected_form, self.move_x, self.move_y))
        self.assertIsNone(pd.PaintSelected(self,self.selected_form, 100, 50))
        self.assertNotEqual(pd.PaintSelected(self,self.selected_form, 260, 300), False)
        self.assertNotEqual(pd.PaintSelected(self,self.selected_form, -23, -678), False)
        
    def test_Paint_success(self): # test routine
        self.assertEqual(pd.Paint_success(self,pygame.display.set_mode([560, 700], 0, 0)), True)
        self.assertEqual(pd.Paint_success(self,pygame.display.set_mode([0,0], 0, 0)), True)
        self.assertNotEqual(pd.Paint_success(self,pygame.display.set_mode([100,20], 0, 0)), False)
        self.assertNotEqual(pd.Paint_success(self,pygame.display.set_mode([56, 70], 0, 0)), False)
        #self.assertEqual(pd.Paint_success(self), None)
        
    #def test_PaintForm(self): # test routine
    #    self.assertIsNone(pd.PaintForm(self, self.form, self.start_time, self.game.block_size, self.game.block_gap,
    #                  self.game.move_x, self.game.move_y, self.game.press_x, self.game.press_y, self.game.martix, 
    #                  self.game.blank, self.game.is_conflict, self.game.success_sign , self.game.start,self.end_time))
        
    @classmethod 
    def teardown_class(cls):
        print("Ending Testing for Module Paint from Sudoku Show")
        #lh.info("ending class: {} execution".format(cls.__name__))
        

if __name__ == "__main__":
    unittest.main()