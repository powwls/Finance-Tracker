import customtkinter as ctk
import time
from src.user_session import logged_in_user,  get_logged_in_user
from PIL import Image, ImageTk

from src.components.pages.snoopy_ai.ai_modal import snoopy_ai_modal
class Header_Frame(ctk.CTkFrame):
    def __init__(self, master, width, height, *args, **kwargs):
        super().__init__(master, *args, **kwargs, width=width, height=height, fg_color="transparent", corner_radius=0)
        
        self.pack(side="top", fill="x")


        self.greeting_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.greeting_frame.pack(side="right", padx=(20, 50), pady=(30, 10))

            
        
        
        self.greeting_label = ctk.CTkLabel(self.greeting_frame, text="Greetings,  ", font=("Poppins", 16), text_color="#2F2F2F")
        self.greeting_label.grid(row=0, column=0)

        self.username_label = ctk.CTkLabel(self.greeting_frame, text="", font=("Poppins", 16, "bold"), text_color="#2F2F2F")
        self.username_label.grid(row=0, column=1)

        
        
        
        self.time_label = ctk.CTkLabel(self, text="", font=("Poppins", 20, "bold"), text_color="#2F2F2F")
        self.time_label.pack(side="right", padx=(20, 20), pady=(30, 10))

        ai_icon = Image.open("./src/assets/icons/app_icon/ai_icon.png")
        resized_image = ai_icon.resize((20, 20))
        ai_icon = ImageTk.PhotoImage(resized_image)
        
        
        
        self.snoopy_ai = ctk.CTkButton(
            self.greeting_frame,
            image=ai_icon,
            text="Snoopy Ai",
            fg_color="#324360",
            text_color="#FFFFFF",
            font=("Poppins", 12, "bold"),
            width=20,
            height=20,
            corner_radius=200,
            hover_color="#5697A6",
            command=lambda: self.open_snoopy_modal()
        )
        self.snoopy_ai.grid(row=0, column=2, padx=(20, 0), pady=(30, 30))
        
        

        print(f"Logged in user: {logged_in_user}")
        self.update_labels()
        self.update_time()
        
    def open_snoopy_modal(self):
        snoopy_ai_modal(self.master, logged_in_user.get('user_id'))

    def update_time(self):
        current_time = time.strftime("%I:%M:%S %p")
        self.time_label.configure(text=current_time)
        self.after(1000, self.update_time)

    def update_labels(self):
        logged_in_user = get_logged_in_user()
        self.username_label.configure(text=logged_in_user.get('username', 'None'))
        self.after(1000, self.update_labels)