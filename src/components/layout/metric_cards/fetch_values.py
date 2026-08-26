# src/components/forms/actions/dashboard_actions.py
from server.db_connect import db, mycursor

def fetch_dashboard_metrics(user_id):
    try:
        # Total Expenses
        mycursor.execute("SELECT COALESCE(SUM(amount), 0) FROM tbl_expenses WHERE user_id = %s", (user_id,))
        total_expenses = mycursor.fetchone()[0]

        # Total Budget
        mycursor.execute("SELECT COALESCE(SUM(amount), 0) FROM tbl_budget WHERE user_id = %s", (user_id,))
        total_budget = mycursor.fetchone()[0]

        # Remaining
        remaining = total_budget - total_expenses

        # Top Expense Category
        mycursor.execute("""
            SELECT category, SUM(amount) AS total
            FROM tbl_expenses
            WHERE user_id = %s
            GROUP BY category
            ORDER BY total DESC
            LIMIT 1
        """, (user_id,))
        top_category_data = mycursor.fetchone()

        if top_category_data:
            top_category = top_category_data[0]
            top_category_amount = top_category_data[1]
        else:
            top_category = "No Data"
            top_category_amount = 0

        return {
            "expenses": total_expenses,
            "budget": total_budget,
            "remaining": remaining,
            "top_category": top_category,
            "top_category_amount": top_category_amount
        }

    except Exception as e:
        print(f"Error fetching dashboard metrics: {e}")
        return {
            "expenses": 0,
            "budget": 0,
            "remaining": 0,
            "top_category": "Error",
            "top_category_amount": 0
        }
        
        


    
    
