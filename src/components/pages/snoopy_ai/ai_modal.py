import customtkinter as ctk
from src.components.layout.center_window_display import CenterWindowToDisplay
from src.components.pages.snoopy_ai.model.ask_snoopy_gemini import ask_snoopy_gemini

def snoopy_ai_modal(master, user_id):
    modal = ctk.CTkToplevel(master)
    modal.title("Snoopy AI Assistant")
    modal.geometry(CenterWindowToDisplay(modal, 750, 650, modal._get_window_scaling))
    modal.resizable(False, False)
    modal.configure(fg_color="#ffffff")

    
    title = ctk.CTkLabel(modal, text="💬 Ask Snoopy!", font=("Poppins", 21, "bold"), text_color="#03393F")
    title.pack(pady=(20, 10))

    subtitle = ctk.CTkLabel(modal, text="Type your question or choose a quick one", font=("Poppins", 12), text_color="#4F4F4F")
    subtitle.pack(pady=(0, 15))

    # Input label and entry
    input_label = ctk.CTkLabel(modal, text="Ask anything:", font=("Poppins", 14, "bold"), text_color="#4F4F4F")
    input_label.pack(pady=(0, 5))

    entry_frame = ctk.CTkFrame(modal, fg_color="transparent")
    entry_frame.pack(pady=5)

    user_query = ctk.CTkEntry(entry_frame, fg_color="#FAFAFA", text_color="#000000", font=("Poppins", 16),
                              placeholder_text="Ask Snoopy", width=270)
    user_query.pack(side="left", padx=(10, 5))

    answer_frame = ctk.CTkFrame(modal, width=500, height=200, corner_radius=10, fg_color="#D9D9D9")
    answer_frame.pack(pady=(20, 10), padx=(20, 20), fill="both", expand=True)
    
    scrollable_answer_frame = ctk.CTkScrollableFrame(answer_frame, width=480, height=180, fg_color="#D9D9D9")
    scrollable_answer_frame.pack(pady=(10, 10), padx=(10, 10), fill="both", expand=True)
    
    answer_label = ctk.CTkLabel(
    scrollable_answer_frame,
    text="",
    font=("Poppins", 15),
    text_color="#252525",
    wraplength=600,
    anchor="w",        
    justify="left"    
)
    answer_label.pack(pady=(10, 10), padx=(10, 10), fill="x")


    def on_ask_btn_click():
        user_input = user_query.get()
        if user_input:
           
            response = ask_snoopy_gemini(user_input, user_id)

           
            answer_label.configure(text=response)
        else:
            answer_label.configure(text="Please enter a question.")

    ask_btn = ctk.CTkButton(
        entry_frame,
        text="Submit",
        font=("Poppins", 14, "bold"),
        fg_color="#03393F",
        hover_color="#022c30",
        text_color="#ffffff",
        width=40,
        corner_radius=5,
        command=on_ask_btn_click  
    )
    ask_btn.pack(side="left", padx=(10, 5))

   
    preset_label = ctk.CTkLabel(modal, text="Or try a quick question:", font=("Poppins", 12, "bold"), text_color="#4F4F4F")
    preset_label.pack(pady=(5, 5))

    btn_frame = ctk.CTkFrame(modal, fg_color="transparent")
    btn_frame.pack(pady=5)

    preset_queries = [
        "What's my biggest expense?",
        "Any budgeting tips?",
        "Summarize my spending"
    ]

    def on_preset_btn_click(query):
        response = ask_snoopy_gemini(query, user_id)

        answer_label.configure(text=response)

    for i, query in enumerate(preset_queries):
        btn = ctk.CTkButton(
            btn_frame,
            text=query,
            font=("Poppins", 14),
            corner_radius=20,
            fg_color="#71BBB2",
            hover_color="#5aa49c",
            text_color="#ffffff",
            width=150,
            height=40,
            command=lambda q=query: on_preset_btn_click(q)
        )
        btn.grid(row=i // 2, column=i % 2, padx=10, pady=8)

    # Close button
    close_btn = ctk.CTkButton(
        modal,
        text="Close",
        fg_color="#cccccc",
        hover_color="#aaaaaa",
        text_color="#333333",
        corner_radius=15,
        command=modal.destroy
    )
    close_btn.pack(pady=10)

    modal.focus_set()
    modal.grab_set()
