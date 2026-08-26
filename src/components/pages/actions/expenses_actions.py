# expenses_actions.py
from tkinter import messagebox
from datetime import date

from server.db_connect import db, mycursor

def add_expenses_to_db(user_id, category_dropdown, description_entry, amount_entry, date_entry, modal):
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
        messagebox.showerror("Invalid Date", "Date cannot be in the past.")
        return

    sql = "INSERT INTO tbl_expenses (user_id, category, description, amount, expenses_date) VALUES (%s, %s, %s, %s, %s)"
    val = (user_id, category, description, amount_val, end_date)

    try:
        mycursor.execute(sql, val)
        db.commit()

    # HERE THE LOGIC
        select_budget_sql = """
            SELECT budget_id FROM tbl_budget 
            WHERE user_id = %s AND category = %s AND budget_end_date >= CURDATE()
            ORDER BY budget_end_date ASC
            LIMIT 1
        """

        mycursor.execute(select_budget_sql, (user_id, category))
        budget_row = mycursor.fetchone()

        if budget_row:
            budget_id = budget_row[0]
            update_sql = """
                        UPDATE tbl_budget 
                        SET amount_spent = amount_spent + %s 
                        WHERE budget_id = %s
                    """
            mycursor.execute(update_sql, (amount_val, budget_id))
            db.commit()
        else:
            messagebox.showwarning("No Active Budget", f"There is no active budget for the '{category}' category.")

        messagebox.showinfo("Success", "Expenses added successfully!")
        modal.destroy()
    except Exception as e:
        messagebox.showerror("Database Error", f"Something went wrong:\n{e}")


def fetch_expenses_data(user_id):
    sql = """
        SELECT category, description, amount, expenses_date 
        FROM tbl_expenses 
        WHERE user_id = %s
        ORDER BY created_at DESC
    """
    mycursor.execute(sql, (user_id,))
    return mycursor.fetchall()



def get_categories():

    sql = "SELECT category_name FROM tbl_categories"
    mycursor.execute(sql)
    return [row[0] for row in mycursor.fetchall()]