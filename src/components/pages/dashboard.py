import customtkinter as ctk 


#user session
from src.user_session import get_logged_in_user



from src.components.layout.header import Header_Frame
from src.components.layout.container import Main_Container
from src.components.layout.sidepanel import Side_Panel_Frame
from src.components.layout.center_window_display import CenterWindowToDisplay

# metric cards
from src.components.layout.metric_cards.create_metric_cards import create_metric_card
from src.components.layout.metric_cards.fetch_values import fetch_dashboard_metrics


from src.components.pages.actions.line_graph_actions import expense_budget_linegraph, fetch_daily_expense_and_budget

#recent transactions
from src.components.pages.actions.transactions_actions import fetch_recent_transactions

class Dashboard_Frame(Main_Container):
      def __init__(self, master, user_id, *args, **kwargs):
            super().__init__(master, *args, **kwargs)
            
            
            self.master = master 
            self.user_id = user_id

            
            
            # self.master.geometry("950x650")
            self.master.geometry(CenterWindowToDisplay(self.master, 1680, 900, self.master._get_window_scaling))
            
            self.dashboard_container()
            
            
      def dashboard_container(self):
            
            
           try:

                 
                  side_panel = Side_Panel_Frame(self, user_id=self.user_id)
                  side_panel = side_panel.side_panel_container()
                  
                  header = Header_Frame(self, self.master.winfo_width(), 40)
                  header.pack(side="top", fill="x")
                  
                  ctk.CTkLabel(header, text="Dashboard", font=("Poppins", 24, "bold"), text_color="#2F2F2F").pack(side="left", padx=(20, 0), pady=(30, 10))
                  
                  main_container = Main_Container(self)
                  main_container.pack(side="left", fill="both", expand=True)
                  

                  container = ctk.CTkFrame(main_container, corner_radius=20, fg_color="#F2F2F2")
                  container.pack(side="left", fill="both", expand=True, padx=20, pady=20)
              
                  
                  card_metrics_frame = ctk.CTkFrame(container, width=200, height = 250, corner_radius=5, fg_color="#F2F2F2")
                  card_metrics_frame.pack(fill="x", pady = 20, padx = 20)
           
                  
                  
                  # ? metric cards 
                  try:
                      # TODO: fetch the actual values from the database
                      metrics = fetch_dashboard_metrics(user_id=self.user_id)

                      for widget in card_metrics_frame.winfo_children():
                          widget.destroy()

                      create_metric_card(card_metrics_frame, "Expenses", f"₱ {metrics['expenses']:,.2f}",
                                         "amount of expenses", 1)
                      create_metric_card(card_metrics_frame, "Budget", f"₱ {metrics['remaining']:,.2f}",
                                         "remaining budget", 2)
                      
                      
                      
                      create_metric_card(card_metrics_frame, f"{metrics['top_category']}", f"₱ {metrics['top_category_amount']:,.2f}",
                                    "most spent on category", 3)
                      
                      def open_piechart(card_metrics_frame, user_id):
                          from src.components.pages.actions.piechart_actions import category_piechart
                          
                          category_piechart(card_metrics_frame, user_id)
                    
                      open_piechart(card_metrics_frame, self.user_id)
                      
                      
                    

                  except Exception as e:
                      print(f"Error @ dashboard_container | metric cards value : {e}")

                        
                  try:
                        
             
                       
                        
                        # ?: LEFT CONTAINER - Recent Transactions

                        left_container = ctk.CTkFrame(container, width=700, height=700, corner_radius=10, fg_color="#324360")
                        left_container.pack(side="left", padx=10, pady=10)
                        left_container.propagate(False)


                        ctk.CTkLabel(left_container, text="Recent Transactions", font=("Poppins", 24, "bold"), text_color="#FFFFFF").pack(anchor="w", padx=(4, 0), pady=(10, 10))
                    
                        tbl_header_fr = ctk.CTkFrame(left_container, fg_color="#7AB3BF", corner_radius=0)
                        tbl_header_fr.pack(fill="x")

                        tbl_headers = ["Date", "Type", "Description", "Amount"]
                        column_header_w = [150, 150, 180, 150]

                        for idx, header in enumerate(tbl_headers):
                              header_label = ctk.CTkLabel(tbl_header_fr, text=header, text_color="#324360", font=("Poppins", 18, "bold"))
                              header_label.grid(row=0, column=idx, padx=10, pady=10, sticky="w")
                              
                              header_label.configure(width=column_header_w[idx])

                             
                              if idx < len(tbl_headers) - 1:
                                    separator = ctk.CTkFrame(tbl_header_fr, width=1, height=30, fg_color="#C5D9C7")
                                    separator.grid(row=0, column=idx + 1, sticky="ns", padx=(5, 0))

                        transactions_history_fr = ctk.CTkScrollableFrame(left_container, width=200, height=700, fg_color="#FFFFFF")
                        transactions_history_fr.pack(fill="x", pady=(0.3, 2))

                        transactions = fetch_recent_transactions(user_id=self.user_id, limit=10)

                        for row_idx, txn in enumerate(transactions):
                            values = [txn["date"], txn["type"], txn["description"], txn["amount"]]

                            for col_idx, value in enumerate(values):
                                lbl = ctk.CTkLabel(transactions_history_fr, text=value, font=("Poppins", 14),
                                                   text_color="#2F2F2F", anchor="w", width=column_header_w[col_idx])
                                lbl.grid(row=row_idx, column=col_idx, padx=(35 if col_idx == 0 else 10), pady=6,
                                         sticky="w")

                            # def view_details_callback(txn=txn):
                            #     print(f"Viewing details for: {txn}")

                            # action_btn = ctk.CTkButton(transactions_history_fr, text="View", font=("Poppins", 12),
                            #                            fg_color="#468189", hover_color="#35656A", text_color="#FFFFFF",
                            #                            corner_radius=6, width=column_header_w[4], height=30,
                            #                            command=view_details_callback)
                            # action_btn.grid(row=row_idx, column=5, padx=5, pady=6, sticky="w")










                        # ?: RIGHT CONTAINER - Line Graph/Pie Charts
                        
                        right_container = ctk.CTkFrame(container, width=800, height=800, corner_radius=10, fg_color="#324360")
                        right_container.pack(side="right", padx=40, pady=70, ipadx=20, ipady=20)
                        right_container.pack_propagate(False)
                        
                        
                        top_spending_cat_pie_fr = ctk.CTkFrame(right_container, width=600, height=450, corner_radius=0, fg_color="#324360")
                        top_spending_cat_pie_fr.pack(side="top", padx=20, pady=5, ipadx=5, ipady=20)
                        
                        
                        line_graph_chart_fr = ctk.CTkFrame(top_spending_cat_pie_fr, width=500, height=400, corner_radius=1, fg_color="#FFFFFF")
                        line_graph_chart_fr.pack(side="top", padx=20, pady=(20, 20), ipadx=20, ipady=30)


                        def open_linegraph(line_graph_chart_fr, user_id):
                            expense_budget_linegraph(line_graph_chart_fr, user_id)
                            

                        open_linegraph(line_graph_chart_fr, user_id=self.user_id)
                    
                        
                  except Exception as e:
                        print(f"Error @ dashboard_container | graph cards : {e}")
                        
                  
           
           except Exception as e:
                 print(f"Error @ dashboard_container: {e}")
            