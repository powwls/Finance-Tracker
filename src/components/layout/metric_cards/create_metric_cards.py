# Database connection
from server.db_connect import db, mycursor

# GUI
import customtkinter as ctk
import tkinter as tk

# For notif
from tkinter import messagebox

# For debugging.
import traceback


" pa horizontal "
def create_metric_card(frame, title, value, subhead, col):
    try:
        cards_width = 320
        cards_height = 150

        card = ctk.CTkFrame(frame, width=cards_width, height=cards_height, corner_radius=10, fg_color="#324360")
        card.grid(row=0, column=col, padx=10, pady=10)
        # card.pack_propagate(False)

        card_title_frame = ctk.CTkFrame(card, width=cards_width, height=70, corner_radius=10, fg_color="#324360")
        card_title_frame.pack(fill="both", expand=False, padx=10, pady=5)

        card_title = ctk.CTkLabel(card_title_frame, text=title, text_color="#F6F7FA", font=("Poppins", 23, "bold"),
                                  width=300, height=50)
        card_title.place(relx=0.75, rely=0.5, anchor="e")

        card_value_frame = ctk.CTkFrame(card, width=cards_width, height=50, corner_radius=10, fg_color="#324360")
        card_value_frame.pack(fill="both", expand=False, padx=10, pady=5)

        card_value = ctk.CTkLabel(card_value_frame, text=value, text_color="#F6F7FA", font=("Poppins", 32, "bold"),
                                  bg_color="#324360", fg_color="#324360",
                                  height=100)
        card_value.place(relx=0.5, rely=0.5, anchor="e")

        card_subheading_fr = ctk.CTkFrame(card, width=cards_width, height=50, corner_radius=10, fg_color="#324360")
        card_subheading_fr.pack(fill="both", expand=False, padx=10, pady=5)

        card_subheading_txt = ctk.CTkLabel(card_subheading_fr, text=subhead, text_color="#F6F7FA",
                                           font=("Poppins", 16, "bold"), fg_color="#324360",
                                           height=50)
        card_subheading_txt.place(relx=0.65, rely=0.45, anchor="e")

        return card_value



    except Exception as e:
        print(f"Error @ create_metric_card: {e}")
        traceback.print_exc()
        
" pa vertical "

def create_metric_cards_ver(frame, title, value, subhead, row):
    try:
        cards_width = 400
        cards_height = 200

        card = ctk.CTkFrame(frame, width=cards_width, height=cards_height, corner_radius=10, fg_color="#324360")
        card.grid(row=row, column=0, padx=10, pady=10)
        card.pack_propagate(False)

        # Title section
        card_title_frame = ctk.CTkFrame(card, width=cards_width, height=40, corner_radius=10, fg_color="#324360")
        card_title_frame.pack(fill="both", expand=False, padx=10, pady=(30, 0))
        card_title_frame.pack_propagate(False)

        card_title = ctk.CTkLabel(card_title_frame, width=cards_width, text=title, text_color="#F6F7FA", font=("Poppins", 23, "bold"))
        card_title.pack(anchor="w", padx=10)

        # Value section
        card_value_frame = ctk.CTkFrame(card, width=cards_width, height=50, corner_radius=10, fg_color="#324360")
        card_value_frame.pack(fill="both", expand=False, padx=10, pady=(5, 0))
        card_value_frame.pack_propagate(False)

        card_value = ctk.CTkLabel(card_value_frame, text=value, text_color="#F6F7FA",
                                  font=("Poppins", 34, "bold"))
        card_value.pack(anchor="center")

        # Subheading section
        card_subheading_fr = ctk.CTkFrame(card, width=cards_width, height=40, corner_radius=10, fg_color="#324360")
        card_subheading_fr.pack(fill="both", expand=False, padx=10, pady=(5, 10))
        card_subheading_fr.pack_propagate(False)

        card_subheading_txt = ctk.CTkLabel(card_subheading_fr, text=subhead, text_color="#F6F7FA",
                                           font=("Poppins", 16, "bold"))
        card_subheading_txt.pack(anchor="center")

        return card_value

    except Exception as e:
        print(f"Error @ create_metric_cards_ver: {e}")
        traceback.print_exc()
