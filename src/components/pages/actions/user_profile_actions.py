from server.db_connect import db, mycursor
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import io

def fetch_user_profile(user_id):
      
      try:
            sql = "SELECT profile_picture FROM tbl_users_profiles WHERE user_id = %s"
            mycursor.execute(sql, (user_id,))
            return mycursor.fetchone()
      
      except Exception as e:
            print(f"Error @ fetch_user_profile: {e}")
            return None

def upload_profile_picture(file_path, user_id):
    try:
        with open(file_path, "rb") as file:
            data = file.read()
            sql = "INSERT INTO tbl_users_profiles (profile_picture, user_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE profile_picture = VALUES(profile_picture)"
            mycursor.execute(sql, (data, user_id))
            db.commit()
            return True
    except Exception as e:
        print(f"Error @ upload_profile_picture: {e}")
        return False

def change_profile(image_label, user_id):
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if image_path:
        img = Image.open(image_path)
        img = img.resize((200, 200))  
        img = ImageTk.PhotoImage(img)
        image_label.configure(image=img)
        image_label.image = img
        
       
        upload_profile_picture(image_path, user_id)
        
        print("Profile picture updated successfully")
    else:
        print("No image selected")
        
        

def save_profile_changes(username, first_name, last_name, email, phone, address, user_id):
    try:
       
        field_order = [
            ("username", username),
            ("first_name", first_name),
            ("last_name", last_name),
            ("contact", phone),
            ("email_address", email),
            ("address", address)
        ]

      
        fields = [f"{key} = %s" for key, val in field_order if val]
        values = [val for key, val in field_order if val]

        if not fields:
            return False  

        sql = "UPDATE tbl_users SET " + ", ".join(fields) + " WHERE user_id = %s"
        values.append(user_id)

        print(f"SQL Query: {sql}")
        print(f"Values: {values}")

        mycursor.execute(sql, values)
        db.commit()

        messagebox.showinfo("Success", "Profile saved successfully")
    
        return True

    except Exception as e:
        print(f"Error @ save_profile_changes: {e}")
        return False
