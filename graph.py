
"""
The hanging man graphical art is taken form :
https://ascii.co.uk/art/hangman
"""
def hangman(step):
    show = (
"""
        STAGE = 0  
      _____________
     |/            
     |             
     |             
     |             
     |             
     |             
     |___          
                   
""",
"""
        STAGE = 1  
      _____________
     |/      |     
     |      (_)    
     |             
     |             
     |             
     |             
     |___          
                   
""",
"""
        STAGE = 2     
      _____________
     |/      |     
     |      (_)    
     |       |     
     |             
     |             
     |             
     |___          
                   
""",
"""
        STAGE = 3     
      _____________
     |/      |     
     |      (_)    
     |      \|     
     |             
     |             
     |             
     |___          
                   
""",
"""
        STAGE = 4     
      _____________
     |/      |     
     |      (_)    
     |      \|/    
     |             
     |             
     |             
     |___          
                   
""",
"""
        STAGE = 5     
      _____________
     |/      |     
     |      (_)    
     |      \|/    
     |       |     
     |             
     |             
     |___          
                   
""",
"""
        STAGE = 6     
      _____________
     |/      |     
     |      (_)    
     |      \|/    
     |       |     
     |      /      
     |             
     |___          
                   
""",
"""
        STAGE = 7     
      _____________
     |/      |     
     |      (_)    
     |      \|/    
     |       |     
     |      / \\   
     |             
     |___          
                    
""",
    )
    return show[step]
    

"""
The logo art is taken form :
https://ascii.co.uk/art/hangman
"""

logo = """
       _                                                    
      | |                                                   
      | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __         
      | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \        
      | | | | (_| | | | | (_| | | | | | | (_| | | | |       
      |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|       
                         __/  |                             
                        |___ /                              
"""
      
menu_text = """
    *********** MENU **********
    (1) RULES
    (2) PLAY
    (3) EXIT

    """
play_cat = """

****************** Categories ******************

      (1) Countries
      (2) Animals
      (3) Foods
      (4) Objects

"""
