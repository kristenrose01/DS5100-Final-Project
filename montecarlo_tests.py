import unittest
from montecarlo import Die
from montecarlo import Game
import pandas as pd
import numpy as np
import random

class DieTestCase(unittest.TestCase):
    
    def test_1_change_weight(self): 
        die1 = Die(np.array([1,2,3,4,5,6]))
        die1.change_weight(4, 2.0)
        
        self.assertTrue(2.0 in die1._die['weights'].values, "Weight not changed.")
        
    def test_2_roll_die(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        expected = die1.roll_die(4)
        
        self.assertEqual(4, len(expected), "Die rolled incorrectly.")
        
    def test_3_show_die(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        actual = die1.show_die()
        
        faces = np.array([1,2,3,4,5,6])
        weights = np.ones(6)
        expected = pd.DataFrame({'faces':faces,'weights':weights})
        
        self.assertTrue(actual.equals(expected), "Die is not shown.")
         
class GameTestCase(unittest.TestCase):
    
    def test_4_play_game(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array(['a','b','c','d','e','f']))
        
        Game1 = Game([die1, die2])
        Game1.play_game(4)
        actual = Game1._result.size
        
        self.assertEqual(actual, 8, "Game not played correctly.") 
        
        
if __name__ == '__main__':

    unittest.main()