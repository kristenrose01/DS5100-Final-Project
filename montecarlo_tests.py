import unittest
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
import pandas as pd
import numpy as np
import random

class DieTestCase(unittest.TestCase):
    
    def test_1_init_die_pass(self):
        
        die1 = Die(np.array([1,2,3,4,5,6]))
        actual = die1._die
        
        expected = pd.DataFrame({'faces':np.array([1,2,3,4,5,6]), 'weights':np.ones(6)})
        
        self.assertTrue(actual.equals(expected), "Die is initialized correctly.")
        
    def test_2_init_die_fail(self):
        with self.assertRaises(ValueError):  
            die1 = Die(np.array([1,1,2,3,4,5]))
    
    def test_3_change_weight(self): 
        die1 = Die(np.array([1,2,3,4,5,6]))
        die1.change_weight(4, 2.0)
        
        self.assertTrue(2.0 in die1._die['weights'].values, "Weight not changed.")
        
    def test_4_roll_die(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        expected = die1.roll_die(4)
        
        self.assertEqual(4, len(expected), "Die rolled incorrectly.")
        
    def test_5_show_die(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        actual = die1.show_die()
        
        faces = np.array([1,2,3,4,5,6])
        weights = np.ones(6)
        expected = pd.DataFrame({'faces':faces,'weights':weights})
        
        self.assertTrue(actual.equals(expected), "Die is not shown.")
         
class GameTestCase(unittest.TestCase):
    
    def test_6_init_pass(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        
        game1 = Game([die1, die2])
        
        self.assertTrue(game1.die_list == [die1, die2])
        
    def test_7_init_fails(self):
        with self.assertRaises(ValueError):
            die1 = Die(np.array([1,2,3,4,5,6]))
            die2 = Die(np.array(['a','b','c','d','e','f']))
        
            game1 = Game([die1, die2])
    
    def test_8_play_game(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        
        game1 = Game([die1, die2])
        game1.play_game(4)
        actual = game1._result.size
        
        self.assertEqual(actual, 8, "Game not played correctly.") 
        
    def test_9_show_results_wide(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        
        game1 = Game([die1, die2])
        game1.play_game(4)
        actual = game1.show_results().shape
        expected = (4, 2)
        
        self.assertEqual(actual, expected, "Results not shown accurately.")
        
    def test_10_show_results_narrow(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        
        game1 = Game([die1, die2])
        game1.play_game(4)
        actual = game1.show_results(form='narrow').shape
        expected = (8,)
    
        self.assertEqual(actual, expected, "Results not shown accurately.")
        
class AnalyzerTestCase(unittest.TestCase):
    
    def test_11_init_pass(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        
        game1 = Game([die1, die2])
        analyzer1 = Analyzer(game1)
        
        self.assertTrue(len(analyzer1._game.die_list) == 2, "Analyzer not initialized correctly.")
        
    def test_12_face_counts(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        
        game1 = Game([die1, die2])
        game1.play_game(4)
        analyzer1 = Analyzer(game1)
        analyzer1.face_counts()
        actual = analyzer1.face_counts.values.sum()
        expected = 8
        
        self.assertEqual(actual, expected, "Face counts are not displayed accurately.")
        
    def test_13_jackpot(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        
        game1 = Game([die1, die2])
        game1.play_game(4)
        analyzer1 = Analyzer(game1)
        
        actual = analyzer1.jackpot()
        expected = len(analyzer1.face_counts[(analyzer1.face_counts == 2).any(axis=1)])
        
        self.assertEqual(actual, expected, "Jackpot number is not accurate.")
        
    def test_14_combo(self):
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        
        game1 = Game([die1, die2])
        game1.play_game(4)
        analyzer1 = Analyzer(game1)
        analyzer1.combo()
        
        actual = analyzer1.combo.values.sum()
        expected = 4
        
        self.assertEqual(actual, expected, "Total number of rolls is not accurate.")
        
if __name__ == '__main__':

    unittest.main()