import customtkinter as ctk
from src.config.config_loader import load_config

class Main_Container(ctk.CTkFrame):
    def __init__(self, master, width=1680, height=900, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        
     
        self.config = load_config()
        self.ui_config = self.config.get("ui", {}) 
        
        self.master = master 
        self.geometry = self.master.geometry
        
        

        
        self.configure(fg_color="#F2F2F2")
        
     
   
        
        
        self.pack(side="left", fill="both", expand=True)