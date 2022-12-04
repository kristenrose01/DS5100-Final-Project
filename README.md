# DS5100-Final-Project

Metadata
------
* Author: Kristen Rose
* Project Name: Monte Carlo Simulator

Synopsis
------

### Installing


### Importing


### Creating dice objects

```
die1 = Die(np.array([1,2,3,4,5,6]))
die2 = Die(np.array([1,2,3,4,5,6]))
fair_coin = Die(np.array(['H','T']))
```

### Playing games

```
die_list = [die1, die2]
game1 = Game(die_list)
game1.play_game(1000)
```

### Analyzing games

```
game1_analysis = Analyze(game1)
game1_analysis.facecount()
game1_analysis.jackpot()
```

API Description
------

### Classes

#### Die
     
A class to build, roll, and show a die.
    
##### Methods (with docstrings)

    change_weight(face_value, new_weight):
                
        """
        Changes the weight of a single face of a die.
        
        ----
        
        Parameters
            face_value (str, int, or float): String, integer, or float value from array of faces
            new_weight (int or float): Integer or float of new weight for face
            
        Returns
            None
        
        """
        
    roll_die(number_rolls):
       
        """
        Rolls the die one or more times.
        
        ----
        
        Parameters
            number_rolls (int): Number of times to roll die
            
        Returns
            List of outcomes
        
        """
        
    show_die():
        
        """
        Shows die's current set of faces and weights.
        
        ----
        
        Parameters
            None
            
        Returns
            dataframe of die's faces and weights
        
        """
        
#### Game

A class to conduct a game of rolling one or more dice of the same kind one or more times.
    
##### Methods (with docstrings)
    
    play_game(number_rolls):
        
        """
        Rolls one or more dice a specified number of times.
        
        ----
        
        Parameters
            number_rolls (int): Number of times to roll die
            
        Returns
            None
        
        """
        
    show_results(form='wide'):
        
        """
        Shows results of most recent game played.
        
        ----
        
        Parameters
            form (str): Form of dataframe to return ('wide' or 'narrow'). Default is wide. 
            
        Returns
            dataframe of results
        
        """
        
#### Analyzer

A class to analyze results and compute descriptive properties about a single game.
     
##### Attributes

    face_counts: dataframe
        number of times a given face appeared in each roll
    
    jackpot: dataframe
        times a roll resulted in all faces being the same
        
    combo: dataframe
        combination types of faces that were rolled and their counts
            
##### Methods (with docstrings)
    
    face_counts():
        
        """
        Computes how many times a given face is rolled in each roll.
        
        ----
        
        Parameters
            None
            
        Returns
            None
        
        """
        
    jackpot():
        
        """
        Computes how many times the game resulted in all faces being identical.
        
        ----
        
        Parameters
            None
            
        Returns
            Integer of number of times the game resulted in all faces being identical.
        
        """
        
    combo():
        
        """
        Computes the distinct combinations of faces rolled, along with their counts.
        
        ----
        
        Parameters
            None
            
        Returns
            None
        
        """


