import customtkinter as ctk
from datetime import datetime



from src.components.layout.header import Header_Frame
from src.components.layout.container import Main_Container
from src.components.layout.sidepanel import Side_Panel_Frame
from src.components.layout.center_window_display import CenterWindowToDisplay


from src.components.pages.actions.budget_actions import fetch_budget_data


class Budget_Frame(Main_Container):
      def __init__(self, master, user_id, *args, **kwargs):
            super().__init__(master, *args, **kwargs)
            
            
            self.master = master 
            self.user_id = user_id
            
            # self.master.geometry("950x650")
            self.master.geometry(CenterWindowToDisplay(self.master, 1680, 900, self.master._get_window_scaling))
            
            self.budget_container()
            
            
      def budget_container(self):
            
            
           try:
                 
                 
                  side_panel = Side_Panel_Frame(self, user_id=self.user_id)
                  side_panel = side_panel.side_panel_container()
                  
                  header = Header_Frame(self, self.master.winfo_width(), 40)
                  header.pack(side="top", fill="x")
                  
                  ctk.CTkLabel(header, text="View Budget", font=("Poppins", 24, "bold"), text_color="#2F2F2F").pack(side="left", padx=(20, 0), pady=(30, 10))
                  
                  main_container = Main_Container(self)
                  main_container.pack(side="top", fill="both", expand=True)
                  
                  try:
                        from src.components.pages.modal.set_budget import set_budget_modal
                        
                        set_budget_btn = ctk.CTkButton(main_container, text="Set Budget", font=("Poppins", 18, "bold"), text_color="#FFFFFF", fg_color="#324360", hover_color="#5697A6", width=200, height=40, cursor="hand2",
                                                       command= lambda: set_budget_modal(self)
                                                       
                                                       )
                        set_budget_btn.pack(side="top", padx=(20, 0), pady=40, anchor="w")
                        
                        
                  except Exception as e:
                        print(f"Error @ set_budget_btn: {e}")

                  tbl_header_fr = ctk.CTkFrame(self, width=200, height=600, fg_color="#324360")
                  tbl_header_fr.pack(fill="x", pady=(10, 0), padx=20)
                  
                  tbl_headers = ["Category", "Description", "Amount", "Amount Spent", "Date",  "Status"]

                  column_header_w = [150, 250, 200, 180, 160, 160]
            
                  for idx, header in enumerate(tbl_headers):
                        header_label = ctk.CTkLabel(tbl_header_fr, text=header, text_color="#FFFFFF", font=("Poppins", 20, "bold"))
                        header_label.grid(row=0, column=idx, padx=30, pady=(10, 5), sticky="w")
                        
                        header_label.configure(width=column_header_w[idx])
                        
                        
                        if idx < len(tbl_headers) - 1:
                              ctk.CTkFrame(tbl_header_fr, width=1, height=10, fg_color="#84B5BA").grid(row=1, column=idx, padx=10, pady=(5,0), sticky="w")
                              
                  
                  data_scrollable_fr = ctk.CTkScrollableFrame(self, width=200, height=600, fg_color="#FFFFFF")
                  data_scrollable_fr.pack(fill="x", pady=(0, 20), padx=20)
                  

                  budgets = fetch_budget_data(user_id=self.user_id)  
                  for i, budget in enumerate(budgets):
                        category, description, amount, amount_spent, end_date, status = budget

                        today = datetime.now().date()

                        if amount_spent > amount:
                            status = "Exceeded" # Pag sobra na sa budget
                        elif today > end_date:
                            if amount_spent == 0:
                                status = "Unused" # Pag nag end date na tas di ka gumastos
                            else:
                                status = "Completed"
                        else:
                            status = "Active"

                        row_data = [category, description, f"₱{amount:.2f}", f"₱{amount_spent:.2f}", end_date.strftime("%b %d, %Y"), status]

                        for j, item in enumerate(row_data):
                              data_lbl = ctk.CTkLabel(data_scrollable_fr, text=item, text_color="#2F2F2F", anchor="w", font=("Poppins", 21, "bold"), width=column_header_w[j])
                              data_lbl.grid(row=i, column=j, padx=(40, 25), pady=10, sticky="w")
                        
           
           
           except Exception as e:
                 print(f"Error @ budget.py: {e}")
            