import customtkinter as ctk 

from PIL import Image, ImageTk 


from src.components.layout.container import Main_Container 


class Side_Panel_Frame(ctk.CTkFrame):
      def __init__(self, master, user_id, width=220, height=900, *args, **kwargs):
            super().__init__(master, width=width, height=height, *args, **kwargs, fg_color="#FFFFFF", corner_radius=0)
            
            
            self.user_id = user_id
            
          
            self.width = width
            self.target_width = width
            self.is_animating = False  
            

            
            
        
        
        
      def side_panel_container(self):
            
            try:
                  self.pack(side="left", fill="y", padx=0, pady=0)
            
                  side_panel = Side_Panel_Frame(self, user_id=self.user_id)
                  side_panel.pack(side="left", fill="y", padx=0, pady=0)
                  side_panel.pack_propagate(False)
                  
                  client_logo = Image.open("./src/assets/icons/app_icon/snoopy_logo_wo_bg.png")
                  resized_image = client_logo.resize((120, 120))
                  client_logo = ImageTk.PhotoImage(resized_image)
                  
                  client_logo_label = ctk.CTkLabel(side_panel, image=client_logo, text="")
                  client_logo_label.image = client_logo
                  
                  client_logo_label.bind("<Button-1>", lambda event: side_panel.toggle_width())
                  
                  client_logo_label.pack(side="top", padx=0, pady=20)
                  
                  
                  " Pages @ Side Panel Frame "
                  
                  
                  
                  " CONTAINER FOR THE NAV PAGES "
                  
                  nav_pages = ctk.CTkFrame(side_panel, width=220, height=200, fg_color="#FFFFFF")
                  nav_pages.pack(side="left", fill="y", padx=20, pady=50)
                  nav_pages.pack_propagate(False)
                  
                 
                  
                  
                  
                  " DASHBOARD "
                  from src.components.layout.sp_actions.navigation import go_to_dashboard
                  
                  try:
                        dashboard_btn = ctk.CTkButton(nav_pages, text="Dashboard", 
                                                      text_color="#2F2F2F",
                                                      font=("Poppins", 20, "bold"),
                                                      fg_color="transparent",
                                                      anchor="w", 
                                                      hover_color="#7AACBF",
                                                      
                                                      
                                                      command=lambda: go_to_dashboard(self, self.user_id))
                        dashboard_btn.grid(row=0, column=0, padx=10, pady=10)
                  except Exception as e:
                        print("Error @ sidepanel.py | dashboard_btn: ", e)
                  
                  
                  " BUDGET " 
                  
                  
                  try: 
                        from src.components.layout.sp_actions.navigation import go_to_budget_page
                  
                        budget_btn = ctk.CTkButton(nav_pages, text="Budget",
                                                      text_color="#2F2F2F",
                                                      font=("Poppins", 20, "bold"),
                                                      fg_color="transparent", anchor="w",
                                                      command = lambda: go_to_budget_page(self, self.user_id),
                                                      hover_color="#7AACBF")
                                                     
                        budget_btn.grid(row=1, column=0, padx=10, pady=10)
                  
                  except Exception as e:
                        print("Error @ sidepanel.py | budget btn: ", e)
            
            
            
                  " EXPENSES "
                  
                  
                  try: 
                       
                        from src.components.layout.sp_actions.navigation import go_to_expenses_page
            
                        expenses_btn = ctk.CTkButton(nav_pages, text="Expenses",
                                                      text_color="#2F2F2F",
                                                      font=("Poppins", 20, "bold"),
                                                      fg_color="transparent", anchor="w",
                                                      hover_color="#7AACBF",
                                                      command = lambda : go_to_expenses_page(self, self.user_id)
                                                      )
                        expenses_btn.grid(row=2, column=0, padx=10, pady=10)
                  
                  except Exception as e:
                        print(f"Error @ side_panel_container | expenses: {e}")
                        
                        
                        pass
                  
                  
                  " GOALS TRACKER PAGE "
                  
                  try:
                        
                        
                        from src.components.layout.sp_actions.navigation import go_to_goals_page
                        
                        goals_tracker_btn = ctk.CTkButton(nav_pages, text="Goals Tracker",
                                                      text_color="#2F2F2F",
                                                      font=("Poppins", 20, "bold"),
                                                      fg_color="transparent", anchor="w",
                                                      hover_color="#A1BF97",
                                                      command = lambda : go_to_goals_page(self, self.user_id)
                                                      )
                        goals_tracker_btn.grid(row=3, column=0, padx=10, pady=10)
                  
                  
                  
                  except Exception as e:
                        print(f"Error @ side_panel_container | transactions: {e}")
                        pass
                  
             
                  
                  " USER PROFILE "
                  
                  try:
                       
               
                        
                              from src.components.layout.sp_actions.navigation import go_to_user_profile
                              
                              user_profile_btn = ctk.CTkButton(nav_pages, text="User Profile",
                                                      text_color="#2F2F2F",
                                                      font=("Poppins", 20, "bold"),
                                                      fg_color="transparent", anchor="w",
                                                       hover_color="#7AACBF",
                                                       command = lambda: go_to_user_profile(self, self.user_id)
                                                      )
                              user_profile_btn.grid(row=4, column=0, padx=10, pady=10)
                              print(f"\nSales can be viewed. This is admin. \nUser No.: {self.user_id}")

                       
                        
                  except Exception as e:
                        print(f"Error @ side_panel_container | user profile : {e}")
                        pass
                  
                  
                  
                 
                  
         
                  
                  
                  nav_pages.rowconfigure(7, weight=2) 
              
              
             
             
                  try:
                              from src.components.layout.sp_actions.navigation import go_to_log_out_handler
                              
                              logout_icon = Image.open("./src/assets/icons/app_icon/logout_icon.png")
                              resized_logout_icon = logout_icon.resize((30, 30))
                              logout_icon = ImageTk.PhotoImage(resized_logout_icon)
                              logout_btn = ctk.CTkButton(nav_pages, text="",
                                                            image=logout_icon,
                                                            text_color="#2F2F2F",
                                                            font=("Poppins", 20, "bold"),
                                                            fg_color="transparent",
                                                            command=lambda: go_to_log_out_handler(self),
                                                            hover_color="#7AACBF")
                              logout_btn.place(relx=0.5, rely=0.95, anchor="center")
                  except Exception as e:
                              print(f"Error @ side_panel_container | logout_btn: {e}")
                  # else:

                  
                  #       " SETTINGS "
                        
                  #       try:
                              
                  #             settings_icon = Image.open("./src/assets/icons/app_icon/setting_icon.png")
                  #             resized_settings_icon = settings_icon.resize((30, 30))
                  #             settings_icon = ImageTk.PhotoImage(resized_settings_icon)
                              
                  #             from src.components.layout.sp_actions.navigation import go_to_settings_page
                  #             settings_btn = ctk.CTkButton(nav_pages, 
                  #                                     image=settings_icon, 
                  #                                     text="", 
                  #                                     text_color="#2F2F2F", 
                  #                                     font=("Poppins", 20, "bold"), 
                  #                                     fg_color="transparent", 
                  #                                     command= lambda: go_to_settings_page(self, self.user_id),
                  #                                     hover_color="#999999")
                  #             settings_btn.place(relx=0.5, rely=0.95, anchor="center")
                              
                              
                  #       except Exception as e:
                  #             print(f"Error @ side_panel_container | settings_btn: {e}")
                        

                  
            
            except Exception as e:
                  print(f"Error @ side_panel_container | Side panel frame: {e}")
                  return self
            

      

      def toggle_width(self):
            if self.is_animating:
                  return

            self.target_width = 75 if self.width == 220 else 220
            self.is_animating = True
            self.animate_width()  

      def animate_width(self):
            step = 5 if self.target_width > self.width else -5

            if (step > 0 and self.width < self.target_width) or (step < 0 and self.width > self.target_width):
                  self.width += step
                  self.configure(width=self.width)  
                  self.after(8, self.animate_width)
            else:
                  self.width = self.target_width
                  self.configure(width=self.target_width)
                  self.is_animating = False