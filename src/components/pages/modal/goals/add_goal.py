import customtkinter as ctk
from server.db_connect import db, mycursor

import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
from src.components.layout.center_window_display import CenterWindowToDisplay
from datetime import date
from src.user_session import get_logged_in_user

from src.components.pages.actions.goal_actions import add_goal_to_db_action


def add_goal_modal(master):
    user_id = get_logged_in_user()["user_id"]

    modal = ctk.CTkToplevel(master)
    modal.title("Set a Savings Goal")
    modal.geometry(CenterWindowToDisplay(modal, 500, 500, modal._get_window_scaling))
    modal.resizable(False, False)
    modal.configure(fg_color="#03393F")

    container = ctk.CTkFrame(modal, fg_color="#03393F", corner_radius=10)
    container.pack(padx=20, pady=20, fill="both", expand=True)

    # Header
    ctk.CTkLabel(container, text="💰 Add New Savings Goal", text_color="#EAEAEA",
                 font=("Poppins", 26, "bold")).pack(pady=(5, 15), anchor="center")

    goal_name_var = tk.StringVar()
    target_amount_var = tk.StringVar()
    initial_saved_var = tk.StringVar()


    frame_goal_name = ctk.CTkFrame(container, fg_color="transparent")
    frame_goal_name.pack(fill="x", padx=10, pady=5)
    
    ctk.CTkLabel(frame_goal_name, text="🏷 What's your goal?", text_color="#EAEAEA", font=("Poppins", 16, "bold")).pack(anchor="w")
    
    goal_name_entry = ctk.CTkEntry(frame_goal_name, textvariable=goal_name_var,  font=("Poppins", 16), placeholder_text="e.g. Vacation Fund")
    goal_name_entry.pack(fill="x", pady=(5, 0))


    amount_frame = ctk.CTkFrame(container, fg_color="transparent")
    amount_frame.pack(fill="x", padx=10, pady=5)

    # Target Amount Frame
    target_frame = ctk.CTkFrame(amount_frame, fg_color="transparent")
    target_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))
    ctk.CTkLabel(target_frame, text="🎯 Target Amount (₱)", text_color="#EAEAEA", font=("Poppins", 16, "bold")).pack(anchor="w")
    
    
    target_amount_entry = ctk.CTkEntry(target_frame, textvariable=target_amount_var,  font=("Poppins", 16), placeholder_text="e.g. 5000")
    target_amount_entry.pack(fill="x", pady=(5, 0))

    # Initial Saved Frame
    initial_frame = ctk.CTkFrame(amount_frame, fg_color="transparent")
    initial_frame.pack(side="left", fill="both", expand=True, padx=(5, 0))
    ctk.CTkLabel(initial_frame, text="💵 Initial Saved Amount (₱)", text_color="#EAEAEA", font=("Poppins", 16, "bold")).pack(anchor="w")
    
    
    initial_saved_entry = ctk.CTkEntry(initial_frame, textvariable=initial_saved_var, font=("Poppins", 16),  placeholder_text="e.g. 1000")
    initial_saved_entry.pack(fill="x", pady=(5, 0))

    # Date pickers side-by-side
    date_frame = ctk.CTkFrame(container, fg_color="transparent")
    date_frame.pack(fill="x", padx=10, pady=5)

    # Start Date Frame
    start_frame = ctk.CTkFrame(date_frame, fg_color="transparent")
    start_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))
    ctk.CTkLabel(start_frame, text="📅 Start Date", text_color="#EAEAEA", font=("Poppins", 16, "bold")).pack(anchor="w")
    
    start_date_entry = DateEntry(start_frame, width=18, background="#2C5364", foreground="white",  mindate=date.today(),date_pattern="yyyy-mm-dd",  font=("Poppins", 16) )
    start_date_entry.set_date(date.today())
    start_date_entry.pack(fill="x", pady=(5, 0))

    # Target Date Frame
    target_date_frame = ctk.CTkFrame(date_frame, fg_color="transparent")
    target_date_frame.pack(side="left", fill="both", expand=True, padx=(5, 0))
    ctk.CTkLabel(target_date_frame, text="📆 Target Date", text_color="#EAEAEA", font=("Poppins", 16, "bold")).pack(anchor="w")
    
    
    target_date_entry = DateEntry(target_date_frame, width=18, background="#2C5364", foreground="white",  font=("Poppins", 16), date_pattern="yyyy-mm-dd",  mindate=date.today())
    target_date_entry.pack(fill="x", pady=(5, 0))

    # Status Dropdown
    frame_status = ctk.CTkFrame(container, fg_color="transparent")
    frame_status.pack(fill="x", padx=10, pady=5)

    ctk.CTkLabel(frame_status, text="📌 Status", text_color="#EAEAEA", font=("Poppins", 16, "bold")).pack(anchor="w")
    
#     status_var = tk.StringVar(value="In Progress")
    
    status_values = ["Not Started", "In Progress", "Achieved"]
    
    status_dropdown = ctk.CTkOptionMenu(frame_status,  values=status_values, font=("Poppins", 16, "bold"))

    
    status_dropdown.pack(fill="x", pady=(5, 0))

    def add_goal_to_db():
        goal_name = goal_name_var.get().strip()
        target_amount = target_amount_var.get().strip()
        initial_saved = initial_saved_var.get().strip()
        start_date = start_date_entry.get_date()
        target_date = target_date_entry.get_date()
        status = status_dropdown.get()

        try:
            add_goal_to_db_action(user_id, goal_name, target_amount, initial_saved, start_date, target_date, status)
            messagebox.showinfo("Success", "🎉 Goal added successfully!")
            modal.destroy()
        except ValueError as ve:
            messagebox.showerror("Invalid Input", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add goal: {e}")

   
    btn_frame = ctk.CTkFrame(container, fg_color="transparent")
    btn_frame.pack(pady=20)

    ctk.CTkButton(btn_frame, text="Cancel", command=modal.destroy,
                  fg_color="#555", hover_color="#777", corner_radius=8, width=100).pack(side="left", padx=10)
    
    ctk.CTkButton(btn_frame, text="➕ Add Goal", command=add_goal_to_db,
                  fg_color="#00A86B", hover_color="#007F5F", corner_radius=8, width=120).pack(side="left", padx=10)

    modal.focus_set()
    modal.grab_set()

