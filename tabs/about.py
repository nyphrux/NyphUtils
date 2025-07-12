import customtkinter as ctk
from app_config import NAME

def create_about_tab(tab):
    ctk.CTkLabel(tab, text=NAME, font=("Arial", 24, "bold")).pack(pady=20)

    ctk.CTkLabel(tab, text=(
        "NyphUtils, developed by @nyphrux.\n"
        "Free, open-source utility toolkit for Discord and system tasks.\n"
        "Enhance your Discord experience and streamline system operations.\n"
        "Feel free to contribute or suggest features on GitHub."
    ), font=("Arial", 13)).pack(pady=(0, 10))
