import customtkinter as ctk 
from datetime import datetime
from PIL import Image, ImageTk

from src.components.layout.header import Header_Frame
from src.components.layout.container import Main_Container
from src.components.layout.sidepanel import Side_Panel_Frame
from src.components.layout.center_window_display import CenterWindowToDisplay


from src.components.pages.actions.goal_actions import fetch_goals_list, get_goal_metrics
from src.components.layout.metric_cards.create_metric_cards import create_metric_cards_ver

from src.components.pages.modal.goals.add_goal import add_goal_modal
from src.components.pages.modal.goals.view_goal import view_goal_modal
from src.components.pages.modal.goals.edit_goal import edit_goal_modal

class GoalTracker_Frame(Main_Container):
      def __init__(self, master, user_id, *args, **kwargs):
            super().__init__(master, *args, **kwargs)
            
            
            self.master = master 
            self.user_id = user_id
            
            # self.master.geometry("950x650")
            self.master.geometry(CenterWindowToDisplay(self.master, 1680, 900, self.master._get_window_scaling))
            
            self.goal_tracker_con()
            
            
      def goal_tracker_con(self):
            try:
                  side_panel = Side_Panel_Frame(self, user_id=self.user_id)
                  side_panel = side_panel.side_panel_container()
                  
                  header = Header_Frame(self, self.master.winfo_width(), 40)
                  header.pack(side="top", fill="x")
                  
                  ctk.CTkLabel(header, text="Snoopy Goals ", font=("Poppins", 24, "bold"), text_color="#2F2F2F").pack(
                        side="left", padx=(20, 0), pady=(30, 10))

                  main_container = Main_Container(self)
                  main_container.pack(side="top", fill="both", expand=True)

                  container = ctk.CTkFrame(main_container, corner_radius=20, fg_color="#F2F2F2")
                  container.pack(side="left", fill="both", expand=True, padx=20, pady=20)

                  add_goal_btn = ctk.CTkButton(container, text="+ Add Goal", font=("Poppins", 16, "bold"),
                                                fg_color="#324360", hover_color="#5697A6", text_color="#FFFFFF",
                                                command=lambda: add_goal_modal(self.master))
                  add_goal_btn.pack(side="top", anchor="e", padx=(20, 50), pady=(20, 0))

                  card_metrics_frame = ctk.CTkFrame(container, width=350, corner_radius=5, fg_color="#F2F2F2")
                  card_metrics_frame.pack(side="left", fill="y", padx=(20, 10), pady=10)

                  right_content_frame = ctk.CTkScrollableFrame(container, corner_radius=10, fg_color="#FFFFFF")
                  right_content_frame.pack(side="left", fill="both", expand=True, padx=(10, 20), pady=20)

                  for widget in right_content_frame.winfo_children():
                        widget.destroy()

                  goals = fetch_goals_list(self.user_id)

                  for goal in goals:
                        goal_id, goal_title, goal_amount, amount_saved, start_date, target_date, status = goal

                        # ? progress %
                        try:
                              progress = min(100, (amount_saved / goal_amount) * 100) if goal_amount > 0 else 0
                        except Exception:
                              progress = 0

                        
                        goal_frame = ctk.CTkFrame(right_content_frame, corner_radius=10, fg_color="white", width=200)
                        goal_frame.pack(fill="x", pady=10, padx=10)

                        title_label = ctk.CTkLabel(goal_frame, text=goal_title, font=("Poppins", 16, "bold"), text_color="#000000")
                        title_label.pack(anchor="w", padx=10, pady=(10, 5))

                        progress_container = ctk.CTkFrame(goal_frame, fg_color="transparent")
                        progress_container.pack(fill="x", padx=10, pady=(0, 10))

                        progress_bar = ctk.CTkProgressBar(progress_container)
                        progress_bar.set(progress / 100)
                        progress_bar.pack(side="left", fill="x", expand=True, pady=5)

                        percent_label = ctk.CTkLabel(progress_container, font=("Poppins", 14), text=f"{progress:.1f} %", width=50, text_color="#000000")
                        percent_label.pack(side="left", padx=10)


                     
                        actions_frame = ctk.CTkFrame(progress_container, fg_color="transparent")
                        actions_frame.pack(side="right")
                        
                        edit_icon = ctk.CTkImage(light_image=Image.open("src/assets/icons/actions_icon/edit.png"), size=(20, 20))
                        view_icon = ctk.CTkImage(light_image=Image.open("src/assets/icons/actions_icon/view.png"), size=(20, 20))
                        delete_icon = ctk.CTkImage(light_image=Image.open("src/assets/icons/actions_icon/delete.png"), size=(20, 20))
                        
                        edit_btn = ctk.CTkButton(progress_container, text="", image= edit_icon, width=50, fg_color="#5697A6",
                         command=lambda gid=goal_id: edit_goal_modal(self.master, gid))
                        edit_btn.pack(side="left", padx=(0, 10))


                
                        view_btn = ctk.CTkButton(actions_frame, text="", image=view_icon, width=50, height=28, font=("Poppins", 12),
                                                fg_color="#5697A6", text_color="white", hover_color="#324360",
                                                command=lambda gid=goal_id: view_goal_modal(self.master, gid))
                        view_btn.pack(side="left", padx=(0, 5))

                      
                        delete_btn = ctk.CTkButton(actions_frame, text="", image = delete_icon, width=50, height=28,
                                                fg_color="#C0392B", text_color="white", hover_color="#A93226",
                                                command=lambda gid=goal_id: self.delete_goal(gid))
                        delete_btn.pack(side="left")


                  # ? metric cards
                  try:
                        metrics = get_goal_metrics(user_id=self.user_id)
                        total_saved, in_progress_count, achieved_count = metrics

                        for widget in card_metrics_frame.winfo_children():
                              widget.destroy()

                        create_metric_cards_ver(card_metrics_frame, "Total Saved", f"PHP {total_saved:,.2f}", "", 1)
                        create_metric_cards_ver(card_metrics_frame, "In Progress", str(in_progress_count), "", 2)
                        create_metric_cards_ver(card_metrics_frame, "Achieved", str(achieved_count), "", 3)

                  except Exception as e:
                        print(f"Error @ goal_tracker.py: {e}")


            except Exception as e:
                  print(f"Error @ transactions.py: {e}")


      def delete_goal(self, goal_id):
            import tkinter.messagebox as messagebox  

            confirm = messagebox.askyesno(
                  "Delete Goal",
                  "Are you sure you want to delete this goal? This action cannot be undone."
            )

            if confirm:
                  try:
                        from src.components.pages.actions.goal_actions import delete_goal_by_id  
                        delete_goal_by_id(goal_id)
                        self.goal_tracker_con
                  except Exception as e:
                        print(f"Error deleting goal: {e}")
            else:
                  print("Deletion cancelled.")


           