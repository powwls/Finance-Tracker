import customtkinter as ctk
from server.db_connect import db, mycursor

import tkinter as tk
from tkinter import messagebox
from src.components.layout.center_window_display import CenterWindowToDisplay
from datetime import date
from src.user_session import get_logged_in_user





def view_goal_modal(master, goal_id):
    user_id = get_logged_in_user()["user_id"]

    try:
        sql = """SELECT goal_id, goal_title, goal_amount, amount_saved, start_date, target_date, status
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
    modal.title("View Goal")
    modal.geometry(CenterWindowToDisplay(modal, 480, 520, modal._get_window_scaling))
    modal.resizable(False, False)
    modal.configure(fg_color="#1F2A38") 

 
    container = ctk.CTkFrame(modal, fg_color="#274156", corner_radius=15)
    container.pack(padx=25, pady=25, fill="both", expand=True)


    title_label = ctk.CTkLabel(
        container, text="🎯 Goal Details", text_color="#F0F0F0",
        font=("Poppins", 26, "bold"))
    title_label.pack(pady=(0, 10))


    underline = ctk.CTkFrame(container, height=3, width=120, fg_color="#4FD1C5", corner_radius=5)
    underline.pack(pady=(0, 25))

  
    target_amount = float(goal_data[2])
    amount_saved = float(goal_data[3])
    progress = min(1.0, amount_saved / target_amount) if target_amount > 0 else 0


    progress_container = ctk.CTkFrame(container, fg_color="transparent")
    progress_container.pack(fill="x", padx=20, pady=(0, 25))

    progress_bar = ctk.CTkProgressBar(progress_container, progress_color="#4FD1C5", height=20)
    progress_bar.set(progress)
    progress_bar.pack(fill="x")

    progress_label = ctk.CTkLabel(
        progress_container,
        text=f"Progress: {progress * 100:.1f}%",
        text_color="#D1D5DB",
        font=("Poppins", 14))
    progress_label.pack(anchor="e", pady=(5, 0))

    # Info labels grid
    info_frame = ctk.CTkFrame(container, fg_color="transparent")
    info_frame.pack(fill="both", expand=True, padx=15)

    labels = [
        ("Goal Title:", goal_data[1]),
        ("Target Amount:", f"₱{target_amount:,.2f}"),
        ("Amount Saved:", f"₱{amount_saved:,.2f}"),
        ("Start Date:", goal_data[4].strftime("%b %d, %Y") if hasattr(goal_data[4], 'strftime') else str(goal_data[4])),
        ("Target Date:", goal_data[5].strftime("%b %d, %Y") if hasattr(goal_data[5], 'strftime') else str(goal_data[5])),
        ("Status:", goal_data[6].capitalize())
    ]

    for i, (text, value) in enumerate(labels):
        text_label = ctk.CTkLabel(
            info_frame, text=text, text_color="#A0AEC0",
            font=("Poppins", 14, "bold"), anchor="w")
        text_label.grid(row=i, column=0, sticky="w", pady=6, padx=(0,10))

        value_label = ctk.CTkLabel(
            info_frame, text=value, text_color="#E2E8F0",
            font=("Poppins", 14), anchor="w")
        value_label.grid(row=i, column=1, sticky="w", pady=6)


    close_btn = ctk.CTkButton(
        container, text="Close", width=140, height=40,
        fg_color="#4FD1C5", hover_color="#38B2AC", text_color="#1A202C",
        font=("Poppins", 14, "bold"),
        command=modal.destroy)
    close_btn.pack(pady=25)

    modal.focus_set()
    modal.grab_set()