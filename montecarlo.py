import numpy as np
import pandas as pd
import random

class Die:
   
    def __init__(self, faces):

        if (faces.dtype != '<U1') and (faces.dtype != 'int64'):
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
            
        index = self._die[self._die['faces']==face_value].index.values
        self._die.loc[index, 'weights'] = new_weight

    def roll_die(self, number_rolls=1):
       
        return random.choices(self._die["faces"], self._die['weights'], k=number_rolls)
        
    def show_die(self):
        
        return self._die
    
class Game:
    
    def __init__(self, die_list):
        self.die_list = die_list
    
    def play_game(self, number_rolls):

        self._result = pd.DataFrame()
        self._result.index.names = ['Roll']
        
        for i in range(0, len(self.die_list)):
            die = self.die_list[i]
            self._result[i] = die.roll_die(number_rolls)

    def show_results(self, form):
        pass
    

class Analyzer:
    def __init__(self,game):
        pass
    
    def face_counts():
        pass
    
    def jackpot():
        pass
    
    def combo():
        pass