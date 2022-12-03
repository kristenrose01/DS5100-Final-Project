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
        
        if face_value not in list(self._die["faces"]):
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
    
    def jackpot(self):
        
        self.jackpot = self._game._result[self._game._result.nunique(axis=1) == 1]
        jackpot_num = len(self.jackpot)
     
        return jackpot_num
    
    #def combo(self):
        
        #df = self._game._result.apply(sorted, axis=1).value_counts().to_frame('n').sort_index()
        #df = df.reset_index()
        
        #lst = []
        #for i in df['index'][1]:
            #lst.append({i}, )
        #lst = np.asarray(lst)    
            
        #self.combo = pd.DataFrame(df['index'].to_list(), columns=[1,2])
        #counts = df.n.values
        #self.combo['n'] = counts
        #self.combo = self.combo.set_index([])
        
        self.combo = self._game._result.loc[:, [0, 1]].drop_duplicates().values 
        
        #num_combos = len(self.combo)
        #message = f"There were {num_combos} distinct combinations of faces rolled."
        
        #return message
    
    def combo(self):
        
        self.combo = self._game._result.apply(lambda x: pd.Series(x).sort_values(), axis=1).value_counts().to_frame('n').sort_index()
        num_combos = len(self.combo)
        message = f"There were {num_combos} combinations of faces rolled."
        
        return message
        