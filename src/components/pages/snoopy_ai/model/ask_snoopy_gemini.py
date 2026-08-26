#database connection
from server.db_connect import db, mycursor
from datetime import datetime, timedelta

import google.generativeai as genai
from src.components.pages.snoopy_ai.config_folder.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def process_preset_query(query, user_id):
    lowered = query.lower()
    known_categories = fetch_known_categories(user_id)

    if query == "What's my biggest expense?":
        return biggest_expense_prompt(user_id)
    elif query == "Any budgeting tips?":
        return budgeting_tips_prompt(user_id)
    elif query == "Summarize my spending":
        return spending_summary_prompt(user_id)

  
    for time_key in ["yesterday", "today", "last week", "last month", "last year"]:
        if time_key in lowered:
            start_date, end_date = get_date_range_from_keyword(time_key)
            if start_date and end_date:
              
                return expense_by_date_prompt(user_id, start_date, end_date)

    # Check for category expenses
    if "expense" in lowered or "expenses" or "spend" or "spending" or "spent" in lowered:
        for cat in known_categories:
            if cat in lowered:
                return category_expense_prompt(user_id, cat)

        return spending_summary_prompt(user_id)
    
    
    if "budget" in lowered or "budgets" in lowered:
        known_budget_categories =fetch_budget_categories(user_id)  # you'll need to create this
        for cat in known_budget_categories:
            if cat in lowered:
                return category_budget_prompt(user_id, cat)

        return fetch_budget_summary(user_id)

 
    return query

def expense_by_date_prompt(user_id, start_date, end_date):
    conn = db
    cursor = conn.cursor()
    query = """
        SELECT SUM(amount) FROM tbl_expenses
        WHERE user_id = %s AND expenses_date BETWEEN %s AND %s
    """
    cursor.execute(query, (user_id, start_date, end_date))
    result = cursor.fetchone()
    cursor.close()

    if result and result[0]:
        amount = result[0]
        return f"Your total expenses from {start_date} to {end_date} are ₱{amount:.2f}."
    else:
        return f"No expenses found from {start_date} to {end_date}."


def get_date_range_from_keyword(keyword):
    today = datetime.now().date()
    if keyword == "yesterday":
        start_date = today - timedelta(days=1)
        end_date = start_date
    elif keyword == "today":
        start_date = today
        end_date = today
    
    elif keyword == "last week":
        start_date = today - timedelta(days=7)
        end_date = today
    
    elif keyword == "last month":
        start_date = today - timedelta(days=30)
        end_date = today
    
    elif keyword == "last year":
        start_date = today - timedelta(days=365)
        end_date = today
  
    else:
        return None, None
    return start_date, end_date


def fetch_known_categories(user_id):
    conn = db
    cursor = conn.cursor()
    query = "SELECT DISTINCT category FROM tbl_expenses WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    categories = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return categories

def category_expense_prompt(user_id, category):
    conn = db
    cursor = conn.cursor()
    query = """
        SELECT SUM(amount) FROM tbl_expenses
        WHERE user_id = %s AND category = %s
    """
    cursor.execute(query, (user_id, category))
    result = cursor.fetchone()
    cursor.close()

    if result and result[0]:
        amount = result[0]
        return (
            f"You have spent ₱{amount:.2f} on {category} recently. "
            "Let me know if you'd like tips on reducing expenses in this category!"
        )
    else:
        return f"No recorded expenses found for category '{category}'."


def biggest_expense_prompt(user_id):
    
    conn = db
    print("Database connection established.")
    cursor = conn.cursor()
    
    query = """
        SELECT category, SUM(amount) as total
        FROM tbl_expenses
        WHERE user_id = %s
        GROUP BY category
        ORDER BY total DESC
        LIMIT 1
    """
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    cursor.close() 

    if result:
        category, amount = result
        return (
            f"The user's biggest expense category is '{category}' with a total of ₱{amount:.2f}. "
            "Give a short analysis and suggest how they might reduce it in a friendly tone."
        )
    else:
        return "No expenses found for this user."

def budgeting_tips_prompt(user_id):
    return "Give the user 3 short, practical budgeting tips tailored to people managing personal finances in the Philippines."

def spending_summary_prompt(user_id):
    conn = db
    print("Database connection established.")
    cursor = conn.cursor()
    query = """
        SELECT category, SUM(amount) FROM tbl_expenses
        WHERE user_id = %s
        GROUP BY category
    """
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()
    cursor.close() 

    if rows:
        summary = "\n".join([f"- {cat}: ₱{amt:.2f}" for cat, amt in rows])
        return (
            f"Here is the user's recent spending summary by category:\n{summary}\n"
            "Please explain the data simply, and suggest one area they could cut back on."
        )
    else:
        return "No spending data found for this user."
    
def category_expense_prompt(user_id, category_keyword):
    conn = db
    cursor = conn.cursor()
    query = """
        SELECT SUM(amount) FROM tbl_expenses
        WHERE user_id = %s AND category LIKE %s
    """
    like_pattern = f"%{category_keyword}%"
    cursor.execute(query, (user_id, like_pattern))
    result = cursor.fetchone()
    cursor.close()

    if result and result[0]:
        amount = result[0]
        return (
            f"The total expenses for '{category_keyword}' is ₱{amount:.2f}. "
            "If you'd like, I can suggest ways to save on this category!"
        )
    else:
        return f"No expenses found for category '{category_keyword}'."


# ? FOR BUDGET

def fetch_budget_summary(user_id):
    conn = db
    cursor = conn.cursor()
    query = """
        SELECT category, SUM(amount) FROM tbl_budget
        WHERE user_id = %s
        GROUP BY category
    """
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()
    cursor.close()

    if rows:
        summary = "\n".join([f"- {cat}: ₱{amt:.2f}" for cat, amt in rows])
        return (
            f"Here is your budget summary by category:\n{summary}\n"
            "Feel free to adjust your budgets as needed."
        )
    else:
        return "No budget data found for this user."

def fetch_budget_categories(user_id):
    conn = db
    cursor = conn.cursor()
    query = "SELECT DISTINCT category FROM tbl_budget WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    categories = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return categories



def biggest_budget_item(user_id):
    conn = db
    cursor = conn.cursor()
    query = """
        SELECT category, SUM(amount) as total
        FROM tbl_budget
        WHERE user_id = %s
        GROUP BY category
        ORDER BY total DESC
        LIMIT 1
    """
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        category, amount = result
        return (
            f"Your biggest budget allocation is '{category}' with ₱{amount:.2f}. "
            "Consider reviewing this category to optimize your spending."
        )
    else:
        return "No budget data found for this user."


def category_budget_prompt(user_id, category_keyword):
    conn = db
    cursor = conn.cursor()
    query = """
        SELECT SUM(amount) FROM tbl_budget
        WHERE user_id = %s AND category LIKE %s
    """
    like_pattern = f"%{category_keyword}%"
    cursor.execute(query, (user_id, like_pattern))
    result = cursor.fetchone()
    cursor.close()

    if result and result[0]:
        amount = result[0]
        return (
            f"Your budget for '{category_keyword}' is ₱{amount:.2f}. "
            "Let me know if you want tips on how to adjust this budget!"
        )
    else:
        return f"No budget found for category '{category_keyword}'."



def ask_snoopy_gemini(prompt, user_id=None):
    try:
        enriched_prompt = process_preset_query(prompt, user_id) if user_id else prompt
        model = genai.GenerativeModel(
            "gemini-2.0-flash",
            system_instruction = (
                    "You're Snoopy, a friendly and helpful personal finance assistant. "
                    "You're working with spending data from a user in the Philippines. "
                    "Be concise, helpful, and use Filipino currency (₱). "
                    "If data is missing, provide general financial tips."
                )

        )
        response = model.generate_content(enriched_prompt)
        if not response.text or not response.text.strip():
            return "The assistant couldn’t generate a proper response. Try rephrasing your question."

        return response.text.strip()
    except Exception as e:
        print(f"Error with Gemini API: {e}")
        return "Sorry, I couldn't get an answer. Please try again."
