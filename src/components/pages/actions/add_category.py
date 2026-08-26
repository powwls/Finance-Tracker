import customtkinter as ctk 
from server.db_connect import db, mycursor

from tkinter import messagebox 
from src.components.layout.center_window_display import CenterWindowToDisplay

from src.user_session import get_logged_in_user



def add_category(master):
    
      user_id = get_logged_in_user()["user_id"]
      
      modal = ctk.CTkToplevel(master)
      modal.title("Add Category")
      
      modal.geometry(CenterWindowToDisplay(modal, 300, 150, modal._get_window_scaling))
      
      modal.resizable(False, False)
      modal.configure(fg_color="#324360")
      
      
      
      container = ctk.CTkFrame(modal, fg_color="#324360")
      container.grid(row=0, column=0, padx=(15, 15), pady=(15, 15), sticky="nsew")
      container.grid_columnconfigure(0, weight=0)
      
      
      category_frame = ctk.CTkFrame(
          container,
          fg_color="#324360",
          corner_radius=5,
          width=300,
          height=40
      )
      category_frame.grid(row=1, column=0, padx=(30, 30), pady=(10, 5), sticky="ew")
      category_frame.grid_columnconfigure(0, weight=1)
      category_frame.grid_columnconfigure(1, weight=0)  
      
      category_lbl = ctk.CTkLabel(category_frame, text="Category:", text_color="#FFFFFF",
                     font=("Poppins", 23,"bold"))
      category_lbl.grid(row=0, column=0, padx=(10, 10), pady=(5, 0), sticky="w")
      
      category_entry = ctk.CTkEntry(category_frame, placeholder_text="Enter Category", fg_color="#FDFDFD", text_color="#2F2F2F", width=150,
                                     font=("Poppins", 18))
      category_entry.grid(row=1, column=0, padx=(10, 10), pady=(5, 0), sticky="w")
      
      add_btn = ctk.CTkButton(category_frame, text="Add", width=20, font=("Poppins", 16, "bold"), text_color="#FFFFFF", fg_color="#507DBC",
                            command=lambda: add_category_db(user_id, category_entry.get(), modal) if validate_category(category_entry.get()) else None
                            )
      add_btn.grid(row=1, column=1, padx=(10, 10), pady=(5, 0), sticky="e")
      
      
      
      
      modal.focus_set()
      modal.grab_set()
      
      
def validate_category(category_name):
    if not category_name:
        messagebox.showerror("Error", "Category name is required")
        return False
    if len(category_name) > 50:
        messagebox.showerror("Error", "Category name cannot be longer than 50 characters")
        return False
    if not category_name.replace(" ", "").isalnum():
        messagebox.showerror("Error", "Category name can only contain letters, numbers, and spaces")
        return False
    return True
      
      
def add_category_db(user_id, category_name, modal):
    try:
        default_type = "Expense"  
        sql = "INSERT INTO tbl_categories (user_id, category_name, category_type) VALUES (%s, %s, %s)"
        val = (user_id, category_name, default_type)
        mycursor.execute(sql, val)
        
        db.commit()  

        if mycursor.rowcount > 0:
            messagebox.showinfo("Success", "Category added successfully")
            modal.destroy()
        else:
            messagebox.showerror("Error", "Failed to add category")
            
    except Exception as e:
        print(f"Error @ add_category_db: {e}")
        messagebox.showerror("Database Error", f"Something went wrong:\n{e}")

