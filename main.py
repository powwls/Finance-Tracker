from customtkinter import CTk, CTkFrame 
import tkinter as tk 
import sys, os 

import customtkinter as ctk 

from src.components.forms.sign_in import Sign_In_Frame
from src.components.layout.center_window_display import CenterWindowToDisplay


def app_window():
      
      try:
            root = CTk()
            
            root.title("Personal Finance Tracker")
            root.geometry(CenterWindowToDisplay(root, 950, 800, root._get_window_scaling()))
            root.resizable(True, True)
            
            icon = os.path.join(sys.path[0], "./src/assets/icons/app_icon/snoopy_logo.ico")
            
            Sign_In_Frame(root)
      
            
            
            root.iconbitmap(icon)
            
            root.mainloop()
            
      except Exception as e:
            print("Error @ main.py | app_window: ", e)
      
      


if __name__ == "__main__":
    app_window()