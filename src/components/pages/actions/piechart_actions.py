from server.db_connect import db, mycursor
from datetime import datetime, timedelta

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np



def close_figures():
    plt.close('all')


def category_piechart(card_metrics_frame, user_id):
    try:
            close_figures()

      
            labels, values = fetch_category_expense(user_id)

            if not values or sum(values) == 0:
                  return  

            fig, ax = plt.subplots(figsize=(6.0, 3.5), dpi=45)
            fig.patch.set_facecolor('#324360')
            ax.set_facecolor('#96CCD9')

      
            colors = ['#96CCD9', '#71BBB2', '#03393F', '#2BCCDE', '#CC33CC']

      
            explode = [0.1 if val == max(values) else 0 for val in values]

            wedges, texts, autotexts = ax.pie(
                  values,
                  labels=labels,
                  autopct='%1.1f%%',
                  startangle=140,
                  explode=explode,
                  colors=colors,
                  textprops={'color': '#FFFFFF', 'fontweight':800, 'fontsize': 20}
            )

            ax.set_title("Expenses by Category", fontsize=25, fontweight='bold', color='#F6F7FA')

      
            plt.ion()
            plt.pause(0.001)
            canvas = FigureCanvasTkAgg(fig, master=card_metrics_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

    except Exception as e:
        print(f"Error @ category_piechart: {e}")
        
        
def fetch_category_expense(user_id):
    try:
        sql = """
            SELECT category, SUM(amount) AS total
            FROM tbl_expenses
            WHERE user_id = %s
            GROUP BY category
        """
        mycursor.execute(sql, (user_id,))
        results = mycursor.fetchall()

        labels = [row[0] for row in results]
        values = [row[1] for row in results]

        return labels, values
    except Exception as e:
        print(f"Error @ fetch_category_expense: {e}")
        return [], []

