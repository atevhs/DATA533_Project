from Sudoku_Show_Test.test_Generate import TestGenerate as tG
from Sudoku_Solve_Test.test_configs import TestConfigs as tC
from Sudoku_Show_Test.test_Paint import TestPaint as tP
from Sudoku_Solve_Test.test_Game_Sudoku import TestGame_Sudoku as tS
import unittest

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(tG))
    suite.addTest(unittest.makeSuite(tC))
    suite.addTest(unittest.makeSuite(tP))
    suite.addTest(unittest.makeSuite(tS))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    
my_suite()
