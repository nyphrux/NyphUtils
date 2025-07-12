import customtkinter as ctk

NAME = "NyphUtils V1"

def setup_app(app):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("assets/theme.json")
    app.title(NAME)
    app.geometry("720x520")
    app.resizable(False, False)
