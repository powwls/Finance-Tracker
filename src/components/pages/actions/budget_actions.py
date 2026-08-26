# budget_actions.py
from tkinter import messagebox
from datetime import date

from server.db_connect import db, mycursor

def add_budget_to_db(user_id, category_dropdown, description_entry, amount_entry, date_entry, modal):
    category = category_dropdown.get()
    description = description_entry.get("1.0", "end").strip()
    amount = amount_entry.get().strip()
    end_date = date_entry.get_date()


    try:
        amount_val = round(float(amount), 2)
        if amount_val <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Amount", "Please enter a valid positive number for the amount.")
        return


    if end_date < date.today():
        messagebox.showerror("Invalid Date", "End date cannot be in the past.")
        return

    sql = "INSERT INTO tbl_budget (user_id, category, description, amount, budget_end_date) VALUES (%s, %s, %s, %s, %s)"
    val = (user_id, category, description, amount_val, end_date)


    try:
        mycursor.execute(sql, val)
        db.commit()

        messagebox.showinfo("Success", "Budget added successfully!")
        modal.destroy()
    except Exception as e:
        messagebox.showerror("Database Error", f"Something went wrong:\n{e}")
        
        
def fetch_budget_data(user_id):
    
    sql = """
        SELECT category, description, amount, amount_spent, budget_end_date, status 
        FROM tbl_budget 
        WHERE user_id = %s 
        ORDER BY created_at DESC
    """
    mycursor.execute(sql, (user_id,))
    return mycursor.fetchall()


def get_categories(user_id):
      
      
    sql = "SELECT category_name FROM tbl_categories WHERE user_id = %s"
    mycursor.execute(sql, (user_id,))
    categories = [row[0] for row in mycursor.fetchall()]
    if not categories:
        categories = ["No categories yet"]
    return categories
  