import numpy as np
import pandas as pd
import random

class Die:
   
    def __init__(self, faces):
        
        if (faces.dtype() != '<U1') and (faces.dtype() != 'int64'):
            raise TypeError("Array must contain strings or numbers.")
 
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Faces must be unique; no duplicates.")
            
        weights = []
        
        for i in faces:
            weights.append(1.0)
        
        self._die = pd.DataFrame({"faces":faces, "weights":weights})

    def change_weight(self, face_value, new_weight):
        
        if face_value not in self._die["faces"]:
            raise ValueError("Face is not valid.")
            
        if type(new_weight) == int:
            float(new_weight)
        elif (type(new_weight) != float):
            raise TypeError("New weight is not valid.")

    def roll_die(self, number_times=1):
       
        self.outcomes = random.choices(self._die["faces"], weights, k=number_times)
        return self.outcomes
        
    def show_die(self):
        
        return self._die
    

class Game:
    def __init__(die_list):
        pass
    
    def play_game(number_rolls):
        pass

    def show_results(form):
        pass
    

class Analyzer:
    def __init__(game):
        pass
    
    def face_counts():
        pass
    
    def jackpot():
        pass
    
    def combo():
        pass