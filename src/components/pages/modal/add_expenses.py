import customtkinter as ctk
from server.db_connect import db, mycursor

import tkinter as tk 
from tkcalendar import DateEntry
from tkinter import messagebox 
from src.components.layout.center_window_display import CenterWindowToDisplay
from datetime import date


from src.components.pages.actions.expenses_actions import get_categories

def add_expenses_modal(master, user_id):
      modal = ctk.CTkToplevel(master)
      modal.title("Add Expense")
      
      modal.geometry(CenterWindowToDisplay(modal, 450, 500, modal._get_window_scaling))
      modal.resizable(False, False)
      modal.configure(fg_color="#324360")

      container = ctk.CTkFrame(modal, fg_color="#324360")
      container.pack(padx=15, pady=15, fill="both", expand=True)

      
      ctk.CTkLabel(container, text="Add Expense", text_color="#FFFFFF",
                  font=("Poppins", 26, "bold")).pack(pady=(5, 10), anchor="w", padx=10)

      # Category lbl 
      category_lbl = ctk.CTkLabel(container, text="Category", text_color="#FFFFFF", font=("Poppins", 21, "bold"))
      category_lbl.pack(anchor="w", padx=10)

      # Category dropdown, fetches from the db 
      category_dropdown = ctk.CTkOptionMenu(container, values=get_categories(), width=300, height=40,
                                                font=("Poppins", 16, "bold"), text_color="#2F2F2F", fg_color="#FFFFFF")
      category_dropdown.pack(anchor="w", padx=10, pady=(5, 0))

      # Description
      description_lbl = ctk.CTkLabel(container, text="Description", text_color="#FFFFFF", font=("Poppins", 21, "bold"))
      description_lbl.pack(anchor="w", padx=10, pady=(10, 0))

      # entry ng description
      description_entry = ctk.CTkTextbox(container, font=("Poppins", 18), text_color="#2F2F2F",
                                          width=380, height=100, fg_color="#FFFFFF")
      description_entry.pack(anchor="w", padx=10, pady=(5, 0))

      
      amount_lbl = ctk.CTkLabel(container, text="Amount", text_color="#FFFFFF", font=("Poppins", 21, "bold"))
      date_lbl = ctk.CTkLabel(container, text="Date", text_color="#FFFFFF", font=("Poppins", 21, "bold"))
      
      amount_lbl.place(x=10, y=285)
      date_lbl.place(x=230, y=285)
      
      # --- VALIDATION FOR AMOUNT ENTRY ---
      def validate_amount_input(char):
            if char == "":
                  return True
            try:
                  float(char)
                  return True
            except ValueError:
                  return False


      vcmd = container.register(validate_amount_input)



      amount_entry = ctk.CTkEntry( container, font=("Poppins", 18),  text_color="#2F2F2F", width=150, height=30, fg_color="#FFFFFF",  validate="key",
      validatecommand=(vcmd, "%P")
      )
      amount_entry.place(x=10, y=320)

      date_container = tk.Frame(container, bg="#03393F")
      date_container.place(x=230, y=320)

      date_entry = DateEntry(date_container, width=15, height=40, background='#507DBC', font=("Poppins", 13),
                              foreground='white', borderwidth=2, date_pattern='mm-dd-yy', state="readonly", mindate=date.today())
      date_entry.pack()
      selected_date = date_entry.get_date()
      if selected_date < date.today():
            messagebox.showerror("Invalid Date", "You cannot select a future date.")
            return


      try:
            from src.components.pages.actions.expenses_actions import add_expenses_to_db

            add_expenses_btn = ctk.CTkButton(container, text="Add Expense", width=200, height=40, font=("Poppins", 18, "bold"),
                                          text_color="#FFFFFF", fg_color="#507DBC", hover_color="#789ADA", command=lambda: add_expenses_to_db(user_id, category_dropdown, description_entry, amount_entry, date_entry, modal))
            add_expenses_btn.pack(anchor="center", pady=(120, 0))

      except Exception as e:
            print(f"Error at add_expenses_btn: ", {e})


      modal.focus_set()
      modal.grab_set()



