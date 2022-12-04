import numpy as np
import pandas as pd
import random

class Die:
    
    """
    A class to build, roll, and show a die.
    
    ---- 
    
    Methods
    
    change_weight(face_value, new_weight):
        Used to change the weight of a single face of a die.
        
    roll_die(number_rolls):
        Used to roll the die one or more times.
        
    show_die():
        Used to show die's current set of faces and weights.

    """   

    def __init__(self, faces):
        
        """
        Initializes die object.
        
        ----
        
        Parameters
            faces (array): A numpy array of strings or numbers
            
        Returns
            None
        
        """

        if (faces.dtype != '<U1') and (faces.dtype != 'int64') and (faces.dtype != 'float64'):
            raise TypeError("Array must contain strings or numbers.")
 
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Faces must be unique; no duplicates.")
            
        weights = []
        
        for i in faces:
            weights.append(1.0)
        
        self._die = pd.DataFrame({"faces":faces, "weights":weights})

    def change_weight(self, face_value, new_weight):
        
        """
        Changes the weight of a single face of a die.
        
        ----
        
        Parameters
            face_value (str, int, or float): String, integer, or float value from array of faces
            new_weight (int or float): Integer or float of new weight for face
            
        Returns
            None
        
        """
        
        if face_value not in list(self._die["faces"]):
            raise ValueError("Face is not valid.")
            
        if type(new_weight) == int:
            float(new_weight)
        elif (type(new_weight) != float):
            raise TypeError("New weight is not valid.")
            
        index = self._die[self._die['faces']==face_value].index.values
        self._die.loc[index, 'weights'] = new_weight

    def roll_die(self, number_rolls=1):
       
        """
        Rolls the die one or more times.
        
        ----
        
        Parameters
            number_rolls (int): Number of times to roll die
            
        Returns
            List of outcomes
        
        """
        
        return random.choices(self._die["faces"], self._die['weights'], k=number_rolls)
        
    def show_die(self):
        
        """
        Shows die's current set of faces and weights.
        
        ----
        
        Parameters
            None
            
        Returns
            dataframe of die's faces and weights
        
        """
        
        return self._die
    
class Game:
    
    """
    A class to conduct a game of rolling one or more dice of the same kind one or more times.
    
    ---- 
    
    Methods
    
    play_game(number_rolls):
        Used to roll one or more dice a specified number of times.
        
    show_results(form='wide'):
        Used to show results of the most recent game played.
        
    """    
    
    def __init__(self, die_list):
        
        """
        Initializes game object.
        
        ----
        
        Parameters
            die_list (list): List of die objects
            
        Returns
            None
        
        """
            
        self.die_list = die_list   
                    
        for i in range(0, len(self.die_list)):
            if sorted(self.die_list[i]._die['faces'].tolist()) != sorted(self.die_list[0]._die['faces'].tolist()):
                raise ValueError("Die objects do not have same number of sides and set of faces.")
            
            
    def play_game(self, number_rolls):

        """
        Rolls one or more dice a specified number of times.
        
        ----
        
        Parameters
            number_rolls (int): Number of times to roll die
            
        Returns
            None
        
        """
        
        self._result = pd.DataFrame()
        self._result.index.names = ['Roll']
        
        for i in range(0, len(self.die_list)):
            die = self.die_list[i]
            self._result[i] = die.roll_die(number_rolls)
            
        for j in range(0, len(self._result)):
            label = "{number}".format(number = (j+1))
            self._result = self._result.rename(index = {j: label})
        

    def show_results(self, form='wide'):
        
        """
        Shows results of most recent game played.
        
        ----
        
        Parameters
            form (str): Form of dataframe to return ('wide' or 'narrow'). Default is wide. 
            
        Returns
            dataframe of results
        
        """
            
        if form=='wide': 
            return self._result
        elif form=='narrow':
            return self._result.stack()
        else:
            raise ValueError("Form is not valid.")

class Analyzer:
    
    """
    A class to analyze results and compute descriptive properties about a single game.
    
    ---- 
    
    Attributes

    face_counts: dataframe
        number of times a given face appeared in each roll
    
    jackpot: dataframe
        times a roll resulted in all faces being the same
        
    combo: dataframe
        combination types of faces that were rolled and their counts
        
    permutations: int
        number of sequence types rolled
            
    ---- 
    
    Methods
    
    face_counts():
        Used to compute how many times a given face is rolled in each roll.
        
    jackpot():
        Used to compute how many times the game resulted in all faces being identical.
        
    combo():
        Used to compute the distinct combinations of faces rolled, along with their counts.
        
    """    
    
    def __init__(self,game):
        
        """
        Initializes analyzer object.
        
        ----
        
        Parameters
            game (Class object): Object from Game class to analyze.
            
        Returns
            None
        
        """
        
        self._game = game
        
        self.permutation = len(self._game._result.apply(lambda x: pd.Series(x).sort_values(), axis=1).value_counts().to_frame('n').sort_index())
    
    def face_counts(self):
        
        """
        Computes how many times a given face is rolled in each roll.
        
        ----
        
        Parameters
            None
            
        Returns
            None
        
        """
        
        Analyzer.face_counts = self._game._result.apply(pd.Series.value_counts, axis=1).fillna(0).astype(int).rename_axis(columns = 'Face')
    
    def jackpot(self):
                
        """
        Computes how many times the game resulted in all faces being identical.
        
        ----
        
        Parameters
            None
            
        Returns
            Integer of number of times the game resulted in all faces being identical.
        
        """
        
        self.jackpot = self._game._result[self._game._result.nunique(axis=1) == 1]
        jackpot_num = len(self.jackpot)
     
        return jackpot_num
    
    def combo(self):
        
        """
        Computes the distinct combinations of faces rolled, along with their counts.
        
        ----
        
        Parameters
            None
            
        Returns
            None
        
        """
        
        self.combo = self._game._result.apply(lambda x: pd.Series(x).sort_values(), axis=1).value_counts().to_frame('n').sort_index()
    

    