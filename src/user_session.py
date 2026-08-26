
logged_in_user = {}



def set_logged_in_user(user_id, username, email, first_name, last_name):
    global logged_in_user

    logged_in_user = {
        "user_id": user_id,
        "username": username,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
    }

    print(f"✅ Logged in user: {logged_in_user}")

    
def clear_logged_in_user():
    global logged_in_user
    logged_in_user.clear()
    logged_in_user = {} 

    
print(f"Logged in user: {logged_in_user}")

def get_logged_in_user():
    

    return logged_in_user

