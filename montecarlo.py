import numpy as np
import pandas as pd
import random

class Die:
   
    def __init__(self, faces):

        if (faces.dtype != '<U1') and (faces.dtype != 'int64') and (faces.dtype != 'float64'):
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
                    
        for i in range(0, len(self.die_list)):
            if sorted(self.die_list[i]._die['faces'].tolist()) != sorted(self.die_list[0]._die['faces'].tolist()):
                raise ValueError("Die objects do not have same number of sides and set of faces.")
            
            
    def play_game(self, number_rolls):

        self._result = pd.DataFrame()
        self._result.index.names = ['Roll']
        
        for i in range(0, len(self.die_list)):
            die = self.die_list[i]
            self._result[i] = die.roll_die(number_rolls)
            
        for j in range(0, len(self._result)):
            label = "{number}".format(number = (j+1))
            self._result = self._result.rename(index = {j: label})

    def show_results(self, form='wide'):
        
        if form=='wide': 
            return self._result
        elif form=='narrow':
            return self._result.stack()
        else:
            raise ValueError("Form is not valid.")

class Analyzer:

    face_counts = pd.DataFrame()
    jackpot = pd.DataFrame()
    
    def __init__(self,game):
        
        self._game = game
        
        #for i in range (0, len(game.die_list)):
            #print(f"The data type of the faces of die {i} is", game.die_list[i]._die['faces'].dtype)
    
    def face_counts(self):
        
        Analyzer.face_counts = self._game._result.apply(pd.Series.value_counts, axis=1).fillna(0).astype(int).rename_axis(columns = 'Face')

        return Analyzer.face_counts
    
    def jackpot(self):
        
        jpcol = pd.Series(dtype=int)
        
        jackpot_num = len(self.face_counts[(self.face_counts == len(self._game.die_list)).any(axis=1)])
        
        jpcol=pd.Series(np.where((self.face_counts == len(self._game.die_list)).any(axis=1), 1, 0))
        jpdf = pd.DataFrame(jpcol)

        for j in range(0, len(jpcol)):
            label = "{number}".format(number = (j+1))
            jpdf = jpdf.rename(index = {j: label})
            
        jpdf = jpdf.rename(columns = {0: 'Jackpot'})
        
        self.jackpot = self.face_counts.join(jpdf)
            
        return jackpot_num
    
    def combo():
        pass