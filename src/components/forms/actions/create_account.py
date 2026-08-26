import bcrypt
from server.db_connect import db
import customtkinter as ctk
from tkinter import messagebox

def create_account_handler(self, firstname, lastname, username, email, password):
    try:    
        
        
            if check_email_exists(email):
                  messagebox.showerror("Email already exists.", "The email address you entered is already in use.")
                  return
        
            if check_username_exists(username):
                  messagebox.showerror("Username already exists.", "The username you entered is already taken.")
                  return
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            
            success = save_user_account(firstname, lastname, username, email, hashed_password)
            
            if success:
                  
                  from src.components.forms.sign_in import Sign_In_Frame
                  
                  messagebox.showinfo("Success", "Account created successfully")
                  
            
                  print(f"\nAccount created for user: {username}\nFirst name: {firstname}\nLast name: {lastname}\nUsername: {username}\nEmail: {email}\nPassword: {password}")
                  
                  try: 
                        print(f"\nRedirecting to: Sign_in_Frame | sign_in.py\n")
                        
                        
                              
                        redirect_to_sign_in(self)
                  except Exception as e:
                        print(f"Error redirecting to Sign_in_Frame: {e}")
                  
                  
            else:
                  
                  return
        
    except Exception as e:
        print(f"Error @ create_account_handler: {e}")
        print("An unexpected error occurred. Please try again.")


def redirect_to_sign_in(self):
    try:
          
        for widget in self.master.winfo_children():
            widget.destroy()
            
        from src.components.forms.sign_in import Sign_In_Frame
        Sign_In_Frame(self.master)
        
    except Exception as e:
        print(f"Error @ redirect_to_sign_in: {e}")



def save_user_account(firstname, lastname, username, email, password):
    try:
        mycursor = db.cursor()
        
       
        sql = "INSERT INTO tbl_users (first_name, last_name, username, email_address, password) VALUES (%s, %s, %s, %s, %s)" 
        val = (firstname, lastname, username, email, password)
        
        
        mycursor.execute(sql, val)
        db.commit()
        
        if mycursor.rowcount > 0:  
            return True  
        else:
            return False  
        
    except Exception as e:
        print(f"Error @ save_user_account: {e}")
        return False  
  
  
  
def check_email_exists(email):
    try:
        mycursor = db.cursor()
        sql = "SELECT * FROM tbl_users WHERE email_address = %s"
        mycursor.execute(sql, (email,))
        
        if mycursor.fetchone():  
            return True
        else:
            return False
    except Exception as e:
        print(f"Error @ check_email_exists: {e}")
        return False
  



def check_username_exists(username):
    try:
        mycursor = db.cursor()
        sql = "SELECT * FROM tbl_users WHERE username = %s"
        mycursor.execute(sql, (username,))
        
        if mycursor.fetchone():  
            return True
        else:
            return False
    except Exception as e:
        print(f"Error @ check_username_exists: {e}")
        return False
  
  
