from kata import VariablesCount
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(VariablesCount("a || b && !c || !b && d"), 4)

    def test2(self):
        self.assertEqual(VariablesCount("a || b && !c"), 3)
    
    def test3(self):
        self.assertEqual(VariablesCount("a || b && !c || !b"), 4)

    def test4(self):
        self.assertEqual(VariablesCount("a || b && !c"), 2)

unittest.main()