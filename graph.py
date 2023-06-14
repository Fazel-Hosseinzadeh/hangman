"""
The hanging man graphical art is taken form :
https://ascii.co.uk/art/hangman
"""
def hangman(step):
    show=[
    """
    """,
    """
          _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
     |___
    """,
    """
          _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
     |___
    """,
    """
          _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
     |___
    """,
    """
          _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
     |___
    """,
    """
          _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
     |___
    """,
    """
          _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
     |___
    """,
    """
          _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
     |___
    """,
    ]
    print(show[step])
    

"""
The logo art is taken form :
https://ascii.co.uk/art/hangman
"""

logo="""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
    """