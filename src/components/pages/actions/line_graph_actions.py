# src/components/pages/actions/line_graph_actions.py
from server.db_connect import db, mycursor
from datetime import datetime, timedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


def close_figures():
    plt.close('all')


def expense_budget_linegraph(line_graph_frame, user_id):
    try:
        close_figures()

      
        labels, expenses, budgets = fetch_daily_expense_and_budget(user_id)

        x = np.arange(len(labels))
        expenses = np.array([float(e) for e in expenses])
        budgets = np.array([float(b) for b in budgets])

        # Plotting
        fig, ax = plt.subplots(figsize=(6.5, 3.8), dpi=100)
        fig.patch.set_facecolor('#FFFFFF')
        fig.canvas.manager.set_window_title("Daily Expenses vs Budget")

        ax.plot(x, expenses, label="Expenses", color="#FF6B6B", linewidth=2.5, marker='o')
        ax.fill_between(x, expenses, color="#FF6B6B", alpha=0.1)

        ax.plot(x, budgets, label="Budget", color="#4CAF50", linewidth=2.5, linestyle='--')
        ax.fill_between(x, budgets, color="#4CAF50", alpha=0.1)

        ax.set_title("Daily Expenses vs Budget", fontsize=14, weight='bold', color="#2F2F2F")
        ax.set_ylabel("Amount (₱)", fontsize=11)
        ax.set_xlabel("Date", fontsize=11)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=9)
        ax.tick_params(axis='y', labelsize=9, colors='gray')
        ax.tick_params(axis='x', labelsize=9, colors='gray')

        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)
        ax.spines['left'].set_alpha(0.2)
        ax.spines['bottom'].set_alpha(0.2)
        ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.2)
        ax.legend(fontsize=10, loc='upper right', frameon=False)

        canvas = FigureCanvasTkAgg(fig, master=line_graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        plt.show()

    except Exception as e:
        print(f"Error @ expense_budget_linegraph: {e}")


def fetch_daily_expense_and_budget(user_id):
    try:
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=6)

        date_range = [start_date + timedelta(days=i) for i in range(7)]
        date_labels = [d.strftime("%b %d") for d in date_range]
        date_keys = [d.strftime("%Y-%m-%d") for d in date_range]

 
        mycursor.execute("""
            SELECT expenses_date AS date, SUM(amount)
            FROM tbl_expenses
            WHERE user_id = %s AND expenses_date BETWEEN %s AND %s
            GROUP BY expenses_date
        """, (user_id, start_date, end_date))
        expense_data = {
            row[0].strftime("%Y-%m-%d"): float(row[1])
            for row in mycursor.fetchall()
        }

        mycursor.execute("""
            SELECT budget_end_date AS date, SUM(amount)
            FROM tbl_budget
            WHERE user_id = %s AND budget_end_date BETWEEN %s AND %s
            GROUP BY budget_end_date
        """, (user_id, start_date, end_date))
        budget_data = {
            row[0].strftime("%Y-%m-%d"): float(row[1])
            for row in mycursor.fetchall()
        }

        expenses = [expense_data.get(date_key, 0.0) for date_key in date_keys]
        budgets = [budget_data.get(date_key, 0.0) for date_key in date_keys]

        return date_labels, expenses, budgets

    except Exception as e:
        print(f"Error @ fetch_daily_expense_and_budget: {e}")
        return [], [], []
