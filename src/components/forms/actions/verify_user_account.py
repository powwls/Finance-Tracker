from server.db_connect import db
import bcrypt
import time

from tkinter import messagebox
from src.user_session import set_logged_in_user
MAX_LOGIN_ATTEMPTS = 4
LOCKOUT_TIME = 5  
# in seconds





failed_attempts_cache = {}

def verify_user_account(self, email, password):
    try:
        mycursor = db.cursor()
        sql = "SELECT user_id, username, email_address, first_name, last_name, password FROM tbl_users WHERE email_address = %s"
        mycursor.execute(sql, (email,))
        result = mycursor.fetchone()

        if result:
            user_id, username, email, first_name, last_name, hashed_password  = result

            
            if email in failed_attempts_cache:
                failed_data = failed_attempts_cache[email]
                if failed_data["attempts"] >= MAX_LOGIN_ATTEMPTS:
                    current_time = time.time()
                    if current_time - failed_data["last_failed_attempt"] < LOCKOUT_TIME:
                        remaining_lockout_time = LOCKOUT_TIME - (current_time - failed_data["last_failed_attempt"])
                        messagebox.showerror("Account Locked", f"Account locked due to too many failed login attempts. Please try again in {int(remaining_lockout_time)} seconds.")
                        return False, "Account locked", None, None, None

          
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
              
                failed_attempts_cache.pop(email, None)
                
                set_logged_in_user(user_id, username, email, first_name, last_name)

                try:
                    print(f"User account verified for user: {email}")
                    go_to_dashboard(self, user_id)
                    return True, "success", user_id, username, first_name, last_name
                except Exception as e:
                    print(f"Error @ redirect_to_dashboard | verify_user_account: {e}")

                return True, "success", user_id, username
            else:
                
                current_time = time.time()
                if email not in failed_attempts_cache:
                    failed_attempts_cache[email] = {"attempts": 0, "last_failed_attempt": current_time}
                failed_attempts_cache[email]["attempts"] += 1
                failed_attempts_cache[email]["last_failed_attempt"] = current_time

                messagebox.showerror("Oops! An error occurred.", "Invalid credentials. Please try again.")
                return False, "Invalid credentials", None, None, None
        else:
            messagebox.showerror("Oops! An error occurred.", "Invalid credentials. Please try again.")
            return False, "Invalid credentials", None, None, None

    except Exception as e:
        print(f"Error @ verify_user_account: {e}")
        return False, "Error during verification", None, None, None


def go_to_dashboard(self, user_id):
    try:
      
      
            
        from src.components.layout.sp_actions.redirects import redirect_to_dashboard
        redirect_to_dashboard(self, user_id)

    except Exception as e:
        print(f"Error @ redirect_to_dashboard: {e}")
        
        
def is_user_admin(user_id):
    try:
        mycursor = db.cursor()
        sql = "SELECT account_type FROM tbl_users WHERE user_id = %s"
        mycursor.execute(sql, (user_id,))
        result = mycursor.fetchone()

        if result and result[0] == "Admin":
            return True
        else:
            return False
    except Exception as e:
        print(f"Error @ is_user_admin: {e}")
        return False