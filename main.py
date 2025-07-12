from customtkinter import CTk
from app_config import setup_app
from ui_setup import setup_tabs

app = CTk()
setup_app(app)
setup_tabs(app)

app.mainloop()
