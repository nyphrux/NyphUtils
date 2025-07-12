import os
import customtkinter as ctk
from PIL import Image
from app_config import NAME

def open_github():
    import webbrowser
    webbrowser.open("https://github.com/nyphrux")

def open_discord():
    import webbrowser
    webbrowser.open("https://discord.gg/JMpJPmSC")

def create_home_tab(tab):
    logo_file = "assets/icon.png"
    if os.path.exists(logo_file):
        img = ctk.CTkImage(light_image=Image.open(logo_file), size=(200, 200))
        ctk.CTkLabel(tab, image=img, text="").pack(pady=(20, 5))
    else:
        ctk.CTkLabel(tab, text=NAME, font=("Arial", 24, "bold")).pack(pady=20)

    home_btn_cfg = {"width": 220, "height": 38, "corner_radius": 6, "font": ("Arial", 13)}
    ctk.CTkLabel(tab, text="A multi-tool for Discord and system utilities.", font=("Arial", 13)).pack(pady=(0, 10))
    ctk.CTkButton(tab, text="GitHub", command=open_github, **home_btn_cfg).pack(pady=5)
    ctk.CTkButton(tab, text="Discord", command=open_discord, **home_btn_cfg).pack(pady=5)
