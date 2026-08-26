import customtkinter as ctk 
from PIL import Image, ImageTk 

from src.components.layout.container import Main_Container
from src.components.layout.center_window_display import CenterWindowToDisplay

from src.user_session import logged_in_user, set_logged_in_user

class Sign_In_Frame(Main_Container):
      def __init__(self, master, *args, **kwargs):
            super().__init__(master, width=950, height=650, *args, **kwargs)
            
            
            self.master = master 
            # self.master.geometry("950x650")
            self.master.geometry(CenterWindowToDisplay(self.master, 950, 650, self.master._get_window_scaling))
           
            self.sign_in_container()
            
            
            
      def sign_in_container(self):
            
            try:
                
                  
                  " Left Container @ Sign In Frame "
                  
                  
                  
                  left_container = ctk.CTkFrame(self, width=500, corner_radius=0, height=650, fg_color="#FFFFFF")
                  left_container.pack(side="left", fill="both", expand=False)
                  
                  
                  " Left Container Picture " 
                  left_image = Image.open('./src/assets/imgs/sign_in_pic1.png')
                  #left_image.putalpha(75)
                  resized_image = left_image.resize((500, 800))
                  left_image= ImageTk.PhotoImage(resized_image)
                  
                  
                  left_img_lbl = ctk.CTkLabel(left_container, image=left_image, text="")
      
                  " Display Logo "
                  left_img_lbl.image = left_image
                  left_img_lbl.place(x=0, y=0)
                  
                  
                  
                  
                  " Right Container @ Sign In Frame "
                  
                  right_container = ctk.CTkFrame(self, corner_radius=0, width=700, height=650, fg_color="#FFFFFF")
                  right_container.pack(side="right", fill="both", expand=False)
                  
                  
                  " Login Form @ Right Container "
                  
                  
                  form_title = ctk.CTkLabel (
                        
                        right_container, text="Sign in",
                        text_color="#283940",
                        font=("Poppins", 30, "bold")
                  )
                  form_title.pack(anchor="nw", padx=(40, 50), pady=(50, 0))
                  
                  
                  form_subheading = ctk.CTkLabel (
                        
                        right_container, 
                        text="Glad to see you! Please sign in to continue.",
                        text_color="#283940",
                        font=("Poppins", 16)
                  
                  )
                  
                  form_subheading.pack(padx=(5, 20), pady=(5, 0))
                  
                  
                  
                  " Form Container "
                  form_container = ctk.CTkFrame(right_container, width=550, height=490, fg_color="#FFFFFF")
                  form_container.pack(padx=(30, 30), pady=(10, 10), fill="x")
                
                  
                  
                  " Email Input "
                  email_label = ctk.CTkLabel(form_container, text="Email", text_color="#283940",
                                             font=("Poppins", 24, "bold"))
                  
                  email_label.pack(padx=(20, 20), pady=(20, 5), anchor="w")
                  
                  
                  email_entry = ctk.CTkEntry(form_container, placeholder_text="Enter your email address", 
                                               width=340,
                                             height=40,
                                               fg_color="#FFFFFF",
                                               text_color="#0D0D0D",
                                               border_color="#283940",
                                               border_width=3,
                                               font=("Poppins", 18))
                  
                  email_entry.pack(padx=(20, 20), pady=(5,20))
                  
                  
                  
                  " Password Input "
                  
                  password_label = ctk.CTkLabel(form_container, text="Password", text_color="#283940",
                                                font=("Poppins", 24, "bold"))
                  password_label.pack(padx=(20, 20), pady=(5, 5), anchor="w")
                  
                  
                  password_entry = ctk.CTkEntry(form_container, placeholder_text="Enter your password", 
                                                width=340,
                                                height=40,
                                                 fg_color="#FFFFFF",
                                               text_color="#0D0D0D",
                                                border_color="#283940",
                                                border_width=3,
                                                font=("Poppins", 18), show="•")
                  
                  password_entry.pack(padx=(20, 20), pady=(5,5))
                  
                  
                  " Show Password "
                  def show_password():
                        if password_entry.cget("show") == "•":
                              password_entry.configure(show="")
                        else:
                              password_entry.configure(show="•")
                  
                  show_password_button = ctk.CTkCheckBox(form_container, text="Show Password", 
                                                       text_color="#283940",
                                                       hover_color="#5697A6",
                                                       font=("Poppins", 16),
                                                       command=show_password)
                  
                  show_password_button.pack(anchor="w", padx=(20, 20), pady=(5,30))
                  
                  " Sign in Button "
                  sign_in_button = ctk.CTkButton(form_container, text="Sign in", width=340, height=50, 
                                                 fg_color="#283940",
                                                 hover_color="#5697A6",
                                                 text_color=self.ui_config.get("primary_btn_txt", "white"), 
                                                 border_width=0.2, 
                                                 cursor="hand2",
                                                 font=("Poppins", 18, "bold"),
                                                 command= lambda: self.verify_account(email_entry.get(), password_entry.get()))
                  
                  sign_in_button.pack(padx=(20, 20), pady=(5,20))

                  password_entry.focus()

                  # self.master.bind('<Return>',
                  #                  lambda event: self.verify_account(email_entry.get(), password_entry.get()))
                  
                  
                  " Create an account prompt "
                  
                  sign_up_frame = ctk.CTkFrame(right_container, width=550, height=100, fg_color="transparent")
                  sign_up_frame.pack(padx=(50, 30), pady=(0, 10), fill="x")
                  
                  sign_up_lbl = ctk.CTkLabel (
                        
                        sign_up_frame, 
                        text="Don't have an account?",
                        text_color="#283940",
                        font=("Poppins", 16)

                  )
                  
                  sign_up_lbl.grid(row=0, column=0, padx=(0, 5)) 
                  
                  
                  sign_up_btn = ctk.CTkButton (
                        
                        sign_up_frame, 
                        text="Create an account.",
                        text_color="#283940",
                        border_width=0.2, 
                        fg_color="transparent",
                        hover_color="#96CCD9",
                        cursor="hand2",
                        font=("Poppins", 16, "bold"),
                        command= lambda: self.redirect_to_sign_up()
                        
                        
                  )
                  
                  
                  sign_up_btn.grid(row=0, column=1, padx=(5, 50))  
                  
                  
                  
                  " Test Expand "
                  # self.after(5000, self.expand_frame) 
                  
                  
            except Exception as e:
                  print("Error @ Sign_in.py: ", e)
                  
      
            
      
      
      
      def redirect_to_sign_up(self):
            try:
                  for widget in self.master.winfo_children():
                        widget.destroy()
                        
                  from src.components.forms.sign_up import Sign_Up_Frame
                  Sign_Up_Frame(self.master)
                  
            except Exception as e:
                  print(f"Error @ redirect_to_sign_up | sign_in.py: {e}")
            
            
            
            
      def verify_account(self, email, password):
          try:
              from src.components.forms.actions.verify_user_account import verify_user_account
      
              success, message, user_id, username, first_name, last_name = verify_user_account(self, email, password)
      
              if success:
                  set_logged_in_user(user_id, username, email, first_name, last_name)
                  print(f"Logged in user: {logged_in_user}")
      
              return user_id
      
          except Exception as e:
              print(f"Error @ verify_account: {e}")
              return None