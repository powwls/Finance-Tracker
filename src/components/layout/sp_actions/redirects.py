from customtkinter import CTk, CTkFrame 
import customtkinter as ctk
import tkinter as tk
from src.components.layout.center_window_display import CenterWindowToDisplay

def redirect_to_dashboard(self, user_id):
      try:
        
            for widget in self.master.winfo_children():
                  widget.destroy()

            from src.components.pages.dashboard import Dashboard_Frame
            
            dashboard_frame = Dashboard_Frame(self.master, user_id=user_id)
            dashboard_frame.pack(fill="both", expand=True)

      except Exception as e:
            print(f"Error @ redirect_to_dashboard | redirects.py : {e}")
            

def redirect_to_budget_page(self, user_id):
      try:
        
            for widget in self.master.winfo_children():
                  widget.destroy()

            from src.components.pages.budget import Budget_Frame
            
            budget_frame = Budget_Frame(self.master, user_id=user_id)
            budget_frame.pack(fill="both", expand=True)

      except Exception as e:
            print(f"Error @ redirect to budget | redirects.py : {e}")



def redirect_to_expenses_page(self, user_id):
      try:
        
            for widget in self.master.winfo_children():
                  widget.destroy()

            from src.components.pages.expenses import Expenses_Frame
            
            expenses_frame = Expenses_Frame(self.master, user_id=user_id)
            expenses_frame.pack(fill="both", expand=True)
            
      except Exception as e:
            print(f"Error @ redirect to expenses  | redirects.py : {e}")
            




def redirect_to_user_profile(self, user_id):
      try:
        
            for widget in self.master.winfo_children():
                  widget.destroy()

            from src.components.pages.user_profile import User_Profile_Frame
            
            user_profile_frame = User_Profile_Frame(self.master, user_id=user_id)
            user_profile_frame.pack(fill="both", expand=True)
            
           
      except Exception as e:
            print(f"Error @ redirect to user  | redirects.py : {e}")

def redirect_to_edit_user_profile(self, user_id):
      try:
        
            for widget in self.master.winfo_children():
                  widget.destroy()

            from src.components.pages.actions.edit_profile import Edit_Profile_Frame
            
            edit_user_profile_frame = Edit_Profile_Frame(self.master, user_id=user_id)
            edit_user_profile_frame.pack(fill="both", expand=True)
            
      except Exception as e:
            print(f"Error @ redirect_to_edit_user_profile | redirects.py : {e}")

def redirect_to_goals_page(self, user_id):
      try:
        
            for widget in self.master.winfo_children():
                  widget.destroy()

            from src.components.pages.goal_tracker import GoalTracker_Frame
            
            goals_fr = GoalTracker_Frame(self.master, user_id=user_id)
            goals_fr.pack(fill="both", expand=True)
            
      except Exception as e:
            print(f"Error @ redirect_to_settings | redirects.py : {e}")



def log_out_handler(self):
    try:
        from src.components.forms.sign_in import Sign_In_Frame
        from src.user_session import clear_logged_in_user, logged_in_user
       
      
        print(f"Before logout: {logged_in_user}") 
        clear_logged_in_user()
        print(f"After logout: {logged_in_user}")
        for widget in self.master.winfo_children():
            widget.destroy()

       
        sign_in_frame = Sign_In_Frame(self.master)
        sign_in_frame.pack()

    except Exception as e:
        print(f"Error in log_out: {e}")