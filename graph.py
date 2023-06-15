
"""
The hanging man graphical art is taken form :
https://ascii.co.uk/art/hangman
"""
def hangman(step):
    show = (
    """
    """,
    """
                   
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
                                    __/ |                               
                                    |___/                               
      """
      
menu_text = """
    ***********MENUE**********
    (1) RULES
    (2) PLAY
    (3) EXIT

    """
play_cat = """

****************** Categories ******************

      (1) Contries
      (2) Animals
      (3) Foods
      (4) Things

"""
