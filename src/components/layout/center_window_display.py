import customtkinter as CTk
      
      
def CenterWindowToDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):
    
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    
  
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    
    return f"{width}x{height}+{x}+{y}"