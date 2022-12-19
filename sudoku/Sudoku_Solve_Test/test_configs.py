import argparse
from Sudoku_Solve import configs as cf
import unittest

class TestConfigs(unittest.TestCase):
    def setup_class(cls):
        lh.info("starting class: {} execution".format(cls.__name__))
        
    def setUp(self):
        self.a1 = cf.parse_args1()
        self.a2 = cf.parse_args2()
        self.a3 = cf.parse_args3()

    def test_parse_args1(self):
        self.assertEqual(self.a1.screen_height, 700)
        self.assertEqual(self.a1.screen_width, 560)
        self.assertNotEqual(self.a1.screen_height, 600)
        self.assertNotEqual(self.a1.screen_width, 500)

    def test_parse_args2(self):
        self.assertEqual(self.a2.selected_height, 300)
        self.assertEqual(self.a2.selected_width, 260)
        self.assertNotEqual(self.a2.selected_height, 30)
        self.assertNotEqual(self.a2.selected_width, 26)

    def test_parse_args3(self):
        self.assertEqual(self.a3.level, 0)
        self.assertEqual(self.a3.block_gap, 1)
        self.assertEqual(self.a3.block_size, 60)
        self.assertNotEqual(self.a3.level, 1)
     
    def tearDown(self):
        print("Execution ended for given Unit test") 

    def teardown_class(cls):
        lh.info("ending class: {} execution".format(cls.__name__))
        

if __name__ == "__main__":
    unittest.main()
