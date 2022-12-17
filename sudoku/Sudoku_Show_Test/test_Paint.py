import unittest
import pygame
from Sudoku_Show.paint import Paint as pd

class TestAdd(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        lh.info("starting class: {} execution".format(cls.__name__))
        
    def setUp(self):
        self.selected_form = pygame.display.set_mode([260, 300], 0, 0) 
        self.move_x = 0
        self.move_y = 0
        self.form = pygame.display.set_mode([560, 700], 0, 0)
        
    def test_PaintSelected(self): # test routine
        self.assertEqual(pd.PaintSelected(self,self.selected_form, self.move_x, self.move_y), None)
        self.assertEqual(pd.PaintSelected(self,self.selected_form, 100, 50), None)
        self.assertEqual(pd.PaintSelected(self,self.selected_form, 260, 300), None)
        self.assertEqual(pd.PaintSelected(self,self.selected_form, -23, -678), None)
        
    def test_Paint_success(self): # test routine
        self.assertEqual(pd.Paint_success(self,self.form), True)
        #self.assertEqual(pd.Paint_success(self), None)
        
    @classmethod 
    def teardown_class(cls):
        lh.info("ending class: {} execution".format(cls.__name__))
        

if __name__ == "__main__":
    unittest.main()