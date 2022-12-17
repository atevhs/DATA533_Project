import unittest
import Generate as gd

class TestAdd(unittest.TestCase):

    def test_Las_sdk(self): # test routine
        self.assertEqual(gd.Las_sdk(30), True)
        self.assertEqual(gd.Las_sdk(40), True)
        self.assertEqual(gd.Las_sdk(50), True)
        self.assertEqual(gd.Las_sdk(100), False)
    
unittest.main()