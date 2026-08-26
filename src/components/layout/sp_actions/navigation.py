" FOR SIDE_PANEL NAVIGATION "


def go_to_dashboard(self, user_id):
      try:
        
            from src.components.layout.sp_actions.redirects import redirect_to_dashboard
            redirect_to_dashboard(self, user_id)

      except Exception as e:
            print(f"Error @ redirect_to_dashboard: {e}")
            


def go_to_budget_page(self, user_id):
      try:
        
            from src.components.layout.sp_actions.redirects import redirect_to_budget_page
            redirect_to_budget_page(self, user_id)

      except Exception as e:
            print(f"Error @ redirect_to_orders_history | navigation.py : {e}")
      



def go_to_expenses_page(self, user_id):
      try:
        
            from src.components.layout.sp_actions.redirects import redirect_to_expenses_page
            redirect_to_expenses_page(self, user_id)

      except Exception as e:
            print(f"Error @ go_to_expenses | navigation.py : {e}")


def go_to_user_profile(self, user_id):
      try:
        
            from src.components.layout.sp_actions.redirects import redirect_to_user_profile
            redirect_to_user_profile(self, user_id)

      except Exception as e:
            print(f"Error @ go_to_user_profile | navigation.py : {e}")
            
def go_to_edit_user_profile(self, user_id):
      try:
        
            from src.components.layout.sp_actions.redirects import redirect_to_edit_user_profile
            redirect_to_edit_user_profile(self, user_id)

      except Exception as e:
            print(f"Error @ go_to_edit_user_profile | navigation.py : {e}")

def go_to_goals_page(self, user_id):
      try:
        
            from src.components.layout.sp_actions.redirects import redirect_to_goals_page
            redirect_to_goals_page(self, user_id)

      except Exception as e:
            print(f"Error @ go_to_goals | navigation.py : {e}")

def go_to_log_out_handler(self):
      try:
            from src.components.layout.sp_actions.redirects import log_out_handler
            log_out_handler(self)
      except Exception as e:
            print(f"Error @ log_out: {e}")




def exit_app (self):
      try:
            from src.user_session import clear_logged_in_user
            clear_logged_in_user()
            self.master.destroy()
      except Exception as e:
            print(f"Error @ exit_app: {e}")