import customtkinter as ctk 

from src.components.layout.header import Header_Frame
from src.components.layout.container import Main_Container
from src.components.layout.sidepanel import Side_Panel_Frame
from src.components.layout.center_window_display import CenterWindowToDisplay

from PIL import Image, ImageTk
import io 

from src.user_session import get_logged_in_user
from src.components.pages.actions.user_profile_actions import fetch_user_profile, upload_profile_picture, change_profile


class User_Profile_Frame(Main_Container):
    def __init__(self, master, user_id, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master 
        self.user_id = user_id

        self.master.geometry(CenterWindowToDisplay(self.master, 1680, 900, self.master._get_window_scaling))
        self.user_profile_container()
        
    def img_upload(self, image_label):
                    from tkinter import filedialog
                    
                    global image_path
                    
                    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
                    if image_path:
                        img = Image.open(image_path)
                        img = img.resize((300, 300))
                        img = ImageTk.PhotoImage(img)
                        image_label.configure(image=img)
                        image_label.image = img
                        
                        print("Image uploaded successfully")
                        
                        upload_profile_picture(image_path, user_id=self.user_id)
                        
                        
                    else:
                        image_label.configure(image="", text="No Image Selected")

    def user_profile_container(self):
        try:
            user_data = get_logged_in_user()
            first_name = user_data.get("first_name", "First")
            last_name = user_data.get("last_name", "Last")
            username = user_data.get("username", "Username")
            email = user_data.get("email", "Email")


            side_panel = Side_Panel_Frame(self, user_id=self.user_id)
            side_panel = side_panel.side_panel_container()
            
     
            header = Header_Frame(self, self.master.winfo_width(), 40)
            header.pack(side="top", fill="x")
            ctk.CTkLabel(header, text="User Profile", font=("Poppins", 24, "bold"), text_color="#2F2F2F").pack(side="left", padx=(20, 0), pady=(30, 10))

     
            main_container = Main_Container(self)
            main_container.pack(side="left", fill="both", expand=True)

            container = ctk.CTkFrame(main_container, corner_radius=20, fg_color="#324360")
            container.pack(side="left", fill="both", expand=True, padx=20, pady=20)

         
            left_container = ctk.CTkFrame(container, corner_radius=20, fg_color="#324360")
            left_container.pack(side="left", fill="both", expand=True, padx=20, pady=20)

            ctk.CTkLabel(left_container, text="Personal Information", font=("Poppins", 32, "bold"), text_color="#FFFFFF").pack(anchor="w", padx=(20, 0), pady=(10, 10))

     
            name_frame = ctk.CTkFrame(left_container, corner_radius=20, fg_color="#324360")
            name_frame.pack(side="top", fill="x", padx=20, pady=5)

            ctk.CTkLabel(name_frame, text="Name: ", font=("Poppins", 24, "bold"), text_color="#FFFFFF").pack(side="left", padx=(20, 0), pady=(10, 10))
            ctk.CTkLabel(name_frame, text=f"{first_name} {last_name}", font=("Poppins", 24), text_color="#FFFFFF").pack(side="left", padx=(10, 0), pady=(10, 10))

   
            username_fr = ctk.CTkFrame(left_container, corner_radius=20, fg_color="#324360")
            username_fr.pack(side="top", fill="x", padx=20, pady=5)

            ctk.CTkLabel(username_fr, text="Username: ", font=("Poppins", 24, "bold"), text_color="#FFFFFF").pack(side="left", padx=(20, 0), pady=(10, 10))
            ctk.CTkLabel(username_fr, text=username, font=("Poppins", 24), text_color="#FFFFFF").pack(side="left", padx=(10, 0), pady=(10, 10))


            address_fr = ctk.CTkFrame(left_container, corner_radius=20, fg_color="#324360")
            address_fr.pack(side="top", fill="x", padx=20, pady=5)

            ctk.CTkLabel(address_fr, text="Address: ", font=("Poppins", 24, "bold"), text_color="#FFFFFF").pack(side="left", padx=(20, 0), pady=(10, 10))
            ctk.CTkLabel(address_fr, text="Manila City Jail", font=("Poppins", 24), text_color="#FFFFFF").pack(side="left", padx=(10, 0), pady=(10, 10))

       
            email_fr = ctk.CTkFrame(left_container, corner_radius=20, fg_color="#324360")
            email_fr.pack(side="top", fill="x", padx=20, pady=5)

            ctk.CTkLabel(email_fr, text="Email: ", font=("Poppins", 24, "bold"), text_color="#FFFFFF").pack(side="left", padx=(20, 0), pady=(10, 10))
            ctk.CTkLabel(email_fr, text=email, font=("Poppins", 24), text_color="#FFFFFF").pack(side="left", padx=(10, 0), pady=(10, 10))

       
            phone_fr = ctk.CTkFrame(left_container, corner_radius=20, fg_color="#324360")
            phone_fr.pack(side="top", fill="x", padx=20, pady=5)

            ctk.CTkLabel(phone_fr, text="Contact No: ", font=("Poppins", 24, "bold"), text_color="#FFFFFF").pack(side="left", padx=(20, 0), pady=(10, 10))
            ctk.CTkLabel(phone_fr, text="0912345679", font=("Poppins", 24), text_color="#FFFFFF").pack(side="left", padx=(10, 0), pady=(10, 10))

         
            btn_fr = ctk.CTkFrame(left_container, corner_radius=20, fg_color="#324360")
            btn_fr.pack(side="top", fill="x", padx=20, pady=5)

            try:
                from src.components.layout.sp_actions.navigation import go_to_edit_user_profile
                edit_btn = ctk.CTkButton(btn_fr, text="Edit Profile", font=("Poppins", 21, "bold"),
                                        text_color="#FFFFFF", fg_color="#507DBC", hover_color="#789ADA",
                                        width=160, height=40, cursor="hand2",
                                        command= lambda: go_to_edit_user_profile(self, self.user_id))
                edit_btn.pack(side="left", padx=(10, 30), pady=(10, 10))

            except Exception as e:
                print(f"Error @ edit_btn: {e}")

            right_container = ctk.CTkFrame(container, corner_radius=20, fg_color="#324360")
            right_container.pack(side="left", fill="both", expand=True, padx=20, pady=20)

            upload_image_frame = ctk.CTkFrame(right_container, width=200, height=200, corner_radius=10, fg_color="#FFFFFF")
            upload_image_frame.pack(side="top", padx=20, pady=5, ipadx=20, ipady=20)

            preview_image_frame = ctk.CTkFrame(upload_image_frame, fg_color="#FFFFFF")
            preview_image_frame.pack(anchor="w", padx=5, fill="x", expand=True)

            
            upload_btn_fr = ctk.CTkFrame(right_container, corner_radius=20, fg_color="#324360")
            upload_btn_fr.pack(side="top", padx=20, pady=5)
            
            profile_picture_image = None 
            
            try:
                
                profile_picture = fetch_user_profile(user_id=self.user_id)
                
                image_blob = profile_picture[0]
                
                resized_image = Image.open(io.BytesIO(image_blob)).resize((200, 200))
                
                profile_picture_image = ImageTk.PhotoImage(resized_image)
                
                
                
                
            except Exception as e:
                print("Error @ user_profile.py | fetch_user_profile: ", e)
            
            self.image_label = ctk.CTkLabel(preview_image_frame, image=profile_picture_image, text="", width=200, height=200)
            self.image_label.pack(anchor="center", padx=20, pady=20)
            
        
            
            upload_img_btn = ctk.CTkButton(upload_btn_fr, text="Upload Image",
                                            font=("Poppins", 21, "bold"),
                                             text_color="#FFFFFF", fg_color="#507DBC", hover_color="#789ADA",
                                             width=160, height=40, cursor="hand2", command=lambda: self.img_upload(self.image_label))
            
            if profile_picture is not None:
                change_profile_btn = ctk.CTkButton(upload_btn_fr, text="Change Profile",
                                            font=("Poppins", 21, "bold"),
                                             text_color="#2F2F2F", fg_color="#71BBB2", hover_color="#FDFDFD",
                                             width=160, height=40, cursor="hand2", command=lambda:  change_profile(self.image_label, self.user_id))
                change_profile_btn.pack(side="bottom", pady=15, padx=20, fill="x")
                upload_img_btn.pack_forget()  
            else:
                upload_img_btn.pack(side="bottom", pady=15, padx=20, fill="x")
                
            


        except Exception as e:
            print(f"Error @ user_profile.py: {e}")
            
        
            
   
    
    
                
                
                        
                

