import customtkinter as ctk
from utils.file_utils import do_file_search

def create_file_tools_tab(tab):
    ctk.CTkLabel(tab, text="File Search", font=("Arial", 14, "bold")).pack(pady=(10, 2))
    entry = ctk.CTkEntry(tab, width=300, placeholder_text="Filename or part")
    entry.pack()
    result_label = ctk.CTkLabel(tab, text="", font=("Arial", 12), justify="left")
    result_label.pack(pady=(0, 10))

    ctk.CTkButton(tab, text="Search", command=lambda: do_file_search(entry, result_label)).pack(pady=2)
