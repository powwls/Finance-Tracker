import customtkinter as ctk 



from src.components.layout.header import Header_Frame
from src.components.layout.container import Main_Container
from src.components.layout.sidepanel import Side_Panel_Frame
from src.components.layout.center_window_display import CenterWindowToDisplay



class Settings_Frame(Main_Container):
      def __init__(self, master, user_id, *args, **kwargs):
            super().__init__(master, *args, **kwargs)
            
            
            self.master = master 
            self.user_id = user_id
            
            # self.master.geometry("950x650")
            self.master.geometry(CenterWindowToDisplay(self.master, 1680, 900, self.master._get_window_scaling))
            
            self.settings_container()
            
            
      def settings_container(self):
            
            
           try:
                 
                 
                  side_panel = Side_Panel_Frame(self, user_id=self.user_id)
                  side_panel = side_panel.side_panel_container()
                  
                  header = Header_Frame(self, self.master.winfo_width(), 40)
                  header.pack(side="top", fill="x")
                  
                  ctk.CTkLabel(header, text="Settings", font=("Poppins", 24, "bold"), text_color="#2F2F2F").pack(side="left", padx=(20, 0), pady=(30, 10))
                  
                  main_container = Main_Container(self)
                  main_container.pack(side="left", fill="both", expand=True)
                  

                  container = ctk.CTkFrame(main_container, corner_radius=20, fg_color="#03393F")
                  container.pack(side="left", fill="both", expand=True, padx=20, pady=20)
              
                  
           
           
           
           except Exception as e:
                 print(f"Error @ settings.py: {e}")
            