# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        results_fact = (1,1,2,6,24,120,720,5040,40320,362880)
        for i in range(10):
            self.assertEqual(utils.fact(i) , results_fact[i])

        with self.assertRaises(ValueError):
            utils.fact(-1)

        with self.assertRaises(TypeError):
            utils.fact("2")
    
    def test_roots(self):
        self.assertEqual(utils.roots(4,0,-4), (1,-1))
        self.assertEqual(utils.roots(0,4,0), (0))
        self.assertEqual(utils.roots(0,0,4), ())
        self.assertEqual(utils.roots(1,2,5), ())

    
    def test_integrate(self):
        self.assertEqual(utils.integrate("x", 0, 1), 1/2 )
        self.assertEqual(utils.integrate("x**2", 0, 3), 9)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())