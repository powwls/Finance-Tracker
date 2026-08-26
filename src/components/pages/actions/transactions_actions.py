from server.db_connect import db, mycursor

def fetch_recent_transactions(user_id, limit=10):
    try:
        query = """
            SELECT created_at AS date, 'Expense' AS type, description, amount
            FROM tbl_expenses
            WHERE user_id = %s

            UNION ALL

            SELECT created_at AS date, 'Budget' AS type, description, amount
            FROM tbl_budget
            WHERE user_id = %s
            ORDER BY date DESC
            LIMIT %s
        """
        mycursor.execute(query, (user_id, user_id, limit))
        results = mycursor.fetchall()

        transactions = [
            {
                "date": row[0].strftime("%b %d, %Y"),
                "type": row[1],
                "description": row[2] if row[2] else "—",
                "amount": f"₱{row[3]:,.2f}"
            }
            for row in results
        ]

        return transactions

    except Exception as e:
        print("Error @fetch_recent_transactions:", e)
        return []

" FOR TRANSACTIONS PAGE "

def fetch_transactions(user_id):
    
    try:
        
        pass 
        
        
    
    except Exception as e:
        print("Error @fetch_transactions:", e)
        return []