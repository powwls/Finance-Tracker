# goals_actions.py

from server.db_connect import db, mycursor
def add_goal_to_db_action(user_id, goal_name, target_amount, initial_saved, start_date, target_date, status):
    
    if not goal_name or not target_amount:
        raise ValueError("Please fill out required fields (Goal Name and Target Amount).")
  
  

    try:
        float_target = float(target_amount)
        float_saved = float(initial_saved) if initial_saved else 0.0
        if float_target <= 0:
            raise ValueError("Target amount must be greater than 0.")
        if float_saved < 0:
            raise ValueError("Initial saved amount cannot be negative.")
        if target_date <= start_date:
            raise ValueError("Target Date must be after Start Date.")

        sql = """
            INSERT INTO tbl_goals 
                (user_id, goal_title, goal_amount, amount_saved, start_date, target_date, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (user_id, goal_name, float_target, float_saved, start_date, target_date, status)
        mycursor.execute(sql, values)
        db.commit()

    except Exception as e:
       
        raise e

" FOR GOALS METRIC "

def get_goal_metrics(user_id):
    try:
        sql = """
        SELECT 
            COALESCE(SUM(amount_saved), 0) AS total_saved,
            SUM(CASE WHEN status = 'In Progress' THEN 1 ELSE 0 END) AS in_progress_count,
            SUM(CASE WHEN status = 'Achieved' THEN 1 ELSE 0 END) AS achieved_count
        FROM tbl_goals
        WHERE user_id = %s
        """
        mycursor.execute(sql, (user_id,))
        result = mycursor.fetchone()
        return result 
  # (total_saved, in_progress_count, achieved_count)

    except Exception as e:
        print("Error @get_goal_metrics:", e)
        return (0, 0, 0)


" FOR GOALS LIST "

def fetch_goals_list(user_id):
      try:
            
            sql = "SELECT goal_id, goal_title, goal_amount, amount_saved, start_date, target_date, status FROM tbl_goals WHERE user_id = %s"
            mycursor.execute(sql, (user_id,))
            result = mycursor.fetchall()
            return result
      
      except Exception as e:
            print("Error @fetch_goals_list:", e)
            return []


def delete_goal_by_id(goal_id):
    try:
        query = "DELETE FROM tbl_goals WHERE goal_id = %s"
        mycursor.execute(query, (goal_id,))
        db.commit()

        print(f"✅ Goal with ID {goal_id} deleted successfully.")

    except Exception as e:
        print(f"Error deleting goal with ID {goal_id}: {e}")
