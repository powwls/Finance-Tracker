import customtkinter as ctk 
from PIL import Image, ImageTk 

from tkinter import messagebox
import re


from src.components.layout.container import Main_Container
from src.components.layout.center_window_display import CenterWindowToDisplay





class Sign_Up_Frame(Main_Container):
      def __init__(self, master, *args, **kwargs):
            super().__init__(master, *args, **kwargs)
            
            
            self.master = master 
            # self.master.geometry("950x650")
            self.master.geometry(CenterWindowToDisplay(self.master, 1020, 750, self.master._get_window_scaling))
            self.sign_up_container()
            
            
            
      def sign_up_container(self):
            
            try:
                
                  
                  
                  " Left Container @ Sign Up Frame "
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
                  
                  right_container = ctk.CTkFrame(self, width=500, height=650, fg_color="#FFFFFF")
                  right_container.pack(side="right", fill="both", expand=False)
                  
                  
                  " Create account Form @ Right Container "
                  
                  
                  form_title = ctk.CTkLabel (
                        
                        right_container, text="Sign up",
                        text_color="#283940",
                        font=("Poppins", 30, "bold")
                  )
                  form_title.pack(anchor="nw", padx=(43, 50), pady=(50, 0))
                  
                  
                  form_subheading = ctk.CTkLabel (
                        
                        right_container, 
                        text="Hey there! Let's get you signed up.",
                        text_color="#283940",
                        font=("Poppins", 16)
                  
                  )
                  
                  form_subheading.pack(anchor="w", padx=(50, 0), pady=(5, 0))
                  
                  
                  " Form Container "
                  form_container = ctk.CTkFrame(right_container, width=550, height=490, fg_color="#FFFFFF")
                  form_container.pack(padx=(30, 30), pady=(5, 5), fill="x")

               
                  form_container.grid_columnconfigure(0, weight=1)
                  form_container.grid_columnconfigure(1, weight=1)

                

                  " First Name Label "
                  first_name_label = ctk.CTkLabel(
                  form_container, text="First name",
                  text_color="#283940",
                  font=("Poppins", 22, "bold")
                  )
                  first_name_label.grid(row=0, column=0, pady=(25, 10), padx=(28, 10), sticky="w")

                  
                  " First Name Entry " 
                  self.first_name_entry = ctk.CTkEntry(
                  form_container, placeholder_text="John",
                  width=200, height=40, fg_color="#FFFFFF", border_color="#283940",
                  text_color="#0D0D0D",
                  border_width=3,
                  font=("Poppins", 18)
                  )
                  self.first_name_entry.grid(row=1, column=0, pady=(0, 10), padx=(28, 10), sticky="ew")

                  " Last Name Label " 
                  last_name_label = ctk.CTkLabel(
                  form_container, text="Last name",
                  text_color="#283940",
                  font=("Poppins", 22, "bold")
                  )
                  last_name_label.grid(row=0, column=1, pady=(25, 10), padx=(10, 28), sticky="w")

                  " Last Name Entry " 
                  self.last_name_entry = ctk.CTkEntry(
                  form_container, placeholder_text="Doe",
                  width=200, height=40, fg_color="#FFFFFF", border_color="#283940",
                  text_color="#0D0D0D",
                  border_width=3,
                  font=("Poppins", 18)
                  )
                  self.last_name_entry.grid(row=1, column=1, pady=(0, 10), padx=(10, 28), sticky="ew")
                  
                                    
                  " Email Input "
                  email_label = ctk.CTkLabel(form_container, text="Email", text_color="#283940",
                                             font=("Poppins", 22, "bold"))
                  
                  email_label.grid(row=2, column=0, pady=(0, 10), padx=(28, 10), sticky="w", columnspan=2)  
                  
                  
                  self.email_entry = ctk.CTkEntry(form_container, placeholder_text="example@domain.com", 
                                               width=340, height=40, fg_color="#FFFFFF", border_color="#283940",
                                               text_color="#0D0D0D",
                                               border_width=3,
                                               font=("Poppins", 18))
                  
                  self.email_entry.grid(row=3, column=0, pady=(0, 15), padx=(25, 25), sticky="ew", columnspan=2) 
                  
                  
                  " Username Input "
                  username_lbl = ctk.CTkLabel(form_container, text="Username", text_color="#283940",
                                             font=("Poppins", 22, "bold"))
                  
                  username_lbl.grid(row=4, column=0, pady=(0, 10), padx=(28, 10), sticky="w", columnspan=2)
                  
                  
                  self.username_entry = ctk.CTkEntry(form_container, placeholder_text="Enter your username", 
                                               width=340, height=40, fg_color="#FFFFFF", border_color="#283940",
                                              text_color="#0D0D0D",
                                               border_width=3,
                                               font=("Poppins", 18))
                  
                  self.username_entry.grid(row=5, column=0, pady=(0, 15), padx=(25, 25), sticky="ew", columnspan=2)
                  
                  
                  
                  " Password Input "
                  
                  password_label = ctk.CTkLabel(form_container, text="Password", text_color="#283940",
                                                font=("Poppins", 22, "bold"))
                  password_label.grid(row=6, column=0, pady=(0, 10), padx=(28, 10), sticky="w", columnspan=2)
                  
                  
                  self.password_entry = ctk.CTkEntry(form_container, placeholder_text="Create a password", 
                                                width=340, height=40, fg_color="#FFFFFF", border_color="#283940",
                                                text_color="#0D0D0D",
                                                border_width=3,
                                                font=("Poppins", 18), show="•")
                  
                  self.password_entry.grid(row=7, column=0, pady=(0, 15), padx=(25, 25), sticky="ew", columnspan=2)
                  
                  
                  " Show Password "
                  def show_password():
                        if self.password_entry.cget("show") == "•":
                              self.password_entry.configure(show="")
                        else:
                              self.password_entry.configure(show="•")
                  
                  show_password_button = ctk.CTkCheckBox(form_container, text="Show Password", 
                                                       text_color="#283940",
                                                       hover_color="#5697A6",
                                                       font=("Poppins", 16),
                                                       command=show_password)
                  
                  show_password_button.grid(row=8, column=0, pady=(0, 15), padx=(25, 25), sticky="ew", columnspan=2)
                  
                  " Sign up Button "
                  sign_up_button = ctk.CTkButton(form_container, text="Sign up", width=340, height=50, 
                                fg_color="#283940",
                               hover_color="#5697A6",
                                text_color="#FFFFFF", 
                                border_width=0.2, 
                                cursor="hand2",
                                font=("Poppins", 18, "bold"),
                                command=lambda: self.user_entries_validation(self.first_name_entry.get(), 
                                                                          self.last_name_entry.get(), 
                                                                          self.username_entry.get(), 
                                                                          self.email_entry.get(), 
                                                                          self.password_entry.get()))

                  
                  sign_up_button.grid(row=9, column=0, pady=(0, 15), padx=(25, 25), sticky="ew", columnspan=2)
                  
                  
                  " Already have an account kineso "
                  
                  sign_in_frame = ctk.CTkFrame(right_container, width=550, height=100, fg_color="transparent")
                  sign_in_frame.pack(padx=(90, 30), pady=(0, 10), fill="x")
                  
                  sign_in_lbl = ctk.CTkLabel (
                        
                        sign_in_frame, 
                        text="Already have an account?",
                        text_color="#283940",
                        font=("Poppins", 16)

                  )
                  
                  sign_in_lbl.grid(row=0, column=0, padx=(0, 5)) 
                  
                  
                  sign_in_btn = ctk.CTkButton (
                        
                        sign_in_frame, 
                        text="Sign in here.",
                        text_color="#283940",
                        border_width=0.2, 
                        fg_color="transparent",
                        hover_color="#96CCD9",
                        cursor="hand2",
                        font=("Poppins", 16, "bold"),
                        command= lambda: self.redirect_to_sign_in()
                        
                        
                  )
                  
                  
                  sign_in_btn.grid(row=0, column=1, padx=(5, 0))  
                  
                  
                  
                  
                  
                  
            except Exception as e:
                  print("Error @ Sign_in.py: ", e)
                  
      
            
            
            
            
      def redirect_to_sign_in(self):
            try:
                  
                  for widget in self.master.winfo_children():
                        widget.destroy()
                        
                  from src.components.forms.sign_in import Sign_In_Frame
                  Sign_In_Frame(self.master)
                  
            except Exception as e:
                  print(f"Error @ redirect_to_sign_in: {e}")
      
      
      def user_entries_validation(self, firstname: str, lastname: str, username: str, email: str, password: str):
            try:
                  
                  
                  
                  
                  firstname = firstname.strip()
                  lastname = lastname.strip()
                  username = username.strip()
                  email = email.strip()
                  password = password.strip()
                  
                  
                  
                  
                  
                  
                  
                  if firstname == "" or lastname == "" or username == "" or email == "" or password == "":
                        messagebox.showerror("Oops! An error occured.", "All fields are required.")
                        return
                  
                  if len(password) < 8:
                        messagebox.showerror("Oops! An error occured.", "Password must be at least 8 characters long")
                        return
                  
                  if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
                        messagebox.showerror("Oops! An error occured.", "Invalid email address.")
                        return
                  
                  
                  
                  try:
                        from src.components.forms.actions.create_account import create_account_handler
                        result = create_account_handler(self=self, firstname=firstname, lastname=lastname, username=username, email=email, password=password)
                        
                        
                        " DO NOT remove this COMMENT "
                        # self.first_name_entry.delete(0, ctk.END)
                        # self.last_name_entry.delete(0, ctk.END)
                        # self.username_entry.delete(0, ctk.END)
                        # self.email_entry.delete(0, ctk.END)
                        # self.password_entry.delete(0, ctk.END)
                        
                        
                        # ? This doesn't do anything lol 
                        if result:
                              print("Angas: Account created successfully")
                              return
                        
                        
                        
                  
                  except Exception as e:
                       
                        print("Error @ user_entries_validation:", f"An error occurred: {str(e)}")
                        
                        
                        
                  # ? For Debugging / Printing out the user entries
                  # print("\n\nFirst name: ", firstname, "\nLast name: ", lastname, "\nUsername: ", username, "\nEmail: ", email, "\nPassword: ", password)
                  
                  
            except Exception as e:
                  print("Error @ handle_user_account: ", e)