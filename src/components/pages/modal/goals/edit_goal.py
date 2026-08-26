import customtkinter as ctk
from server.db_connect import db, mycursor

from tkinter import messagebox
from src.components.layout.center_window_display import CenterWindowToDisplay
from src.user_session import get_logged_in_user

def edit_goal_modal(master, goal_id):
    user_id = get_logged_in_user()["user_id"]

    try:
        sql = """SELECT goal_title, goal_amount, amount_saved, start_date, target_date, status
                 FROM tbl_goals WHERE user_id = %s AND goal_id = %s"""
        mycursor.execute(sql, (user_id, goal_id))
        goal_data = mycursor.fetchone()

        if not goal_data:
            messagebox.showerror("Error", "Goal not found.")
            return

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch goal details: {e}")
        return


    modal = ctk.CTkToplevel(master)
    modal.title("Edit Goal")
    modal.geometry(CenterWindowToDisplay(modal, 480, 400, modal._get_window_scaling))
    modal.resizable(False, False)
    modal.configure(fg_color="#03393F")

    container = ctk.CTkFrame(modal, fg_color="#03393F", corner_radius=12)
    container.pack(padx=20, pady=20, fill="both", expand=True)

    ctk.CTkLabel(container, text="Editing Goal", font=("Poppins", 24, "bold"),
                 text_color="#EAEAEA").pack(pady=(0, 20))

    ctk.CTkLabel(container, text="Goal Title:", font=("Poppins", 14, "bold"),
                 text_color="#EAEAEA", anchor="w").pack(fill="x", pady=(0, 5))
    ctk.CTkLabel(container, text=goal_data[0], font=("Poppins", 14),
                 text_color="#FFFFFF", anchor="w").pack(fill="x", pady=(0, 15))


    ctk.CTkLabel(container, text="Target Amount:", font=("Poppins", 14, "bold"),
                 text_color="#EAEAEA", anchor="w").pack(fill="x", pady=(0, 5))
    ctk.CTkLabel(container, text=f"₱{float(goal_data[1]):,.2f}", font=("Poppins", 14),
                 text_color="#FFFFFF", anchor="w").pack(fill="x", pady=(0, 15))


    ctk.CTkLabel(container, text="Amount Saved:", font=("Poppins", 14, "bold"),
                 text_color="#EAEAEA", anchor="w").pack(fill="x", pady=(0, 5))
    amount_saved_var = ctk.StringVar(value=f"{float(goal_data[2]):.2f}")
    amount_saved_entry = ctk.CTkEntry(container, textvariable=amount_saved_var, font=("Poppins", 14))
    amount_saved_entry.pack(fill="x", pady=(0, 20))

    def save_changes():
      try:
            new_amount_saved = float(amount_saved_var.get())
            target_amount = float(goal_data[1])

            if new_amount_saved < 0:
                  messagebox.showwarning("Invalid input", "Amount saved cannot be negative.")
                  return
            if new_amount_saved > target_amount:
                  messagebox.showwarning("Invalid input", "Amount saved cannot exceed target amount.")
                  return

            # Automatic status update based on amount saved
            if new_amount_saved == 0:
                  new_status = "Not Started"
            elif new_amount_saved < target_amount:
                  new_status = "In Progress"
            else:  
                  new_status = "Achieved"

            update_sql = """UPDATE tbl_goals SET amount_saved = %s, status = %s WHERE user_id = %s AND goal_id = %s"""
            mycursor.execute(update_sql, (new_amount_saved, new_status, user_id, goal_id))
            db.commit()

            messagebox.showinfo("Success", "Goal updated successfully.")
            modal.destroy()

      except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid number for amount saved.")
      except Exception as e:
            messagebox.showerror("Error", f"Failed to update goal: {e}")



    btn_frame = ctk.CTkFrame(container, fg_color="transparent")
    btn_frame.pack(fill="x", pady=(10, 0))

    save_btn = ctk.CTkButton(btn_frame, text="Save", command=save_changes)
    save_btn.pack(side="right", padx=(5, 0))

    cancel_btn = ctk.CTkButton(btn_frame, text="Cancel", fg_color="#555555",
                               hover_color="#777777", command=modal.destroy)
    cancel_btn.pack(side="right", padx=(0, 5))

    modal.focus_set()
    modal.grab_set()
