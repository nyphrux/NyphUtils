import customtkinter as ctk
from tabs.home import create_home_tab
from tabs.about import create_about_tab
from tabs.webhook import create_webhook_tab
from tabs.ip_lookup import create_ip_lookup_tab
from tabs.text_utils import create_text_utils_tab
from tabs.file_tools import create_file_tools_tab
from tabs.pinger import create_pinger_tab

def setup_tabs(app):
    tabs = ctk.CTkTabview(app, width=680, height=440, corner_radius=10)
    tabs.pack(pady=20)

    create_home_tab(tabs.add("Home"))
    create_about_tab(tabs.add("About"))
    create_webhook_tab(tabs.add("Webhook"))
    create_ip_lookup_tab(tabs.add("IP Lookup"))
    create_text_utils_tab(tabs.add("Text Utils"))
    create_file_tools_tab(tabs.add("File Tools"))
    create_pinger_tab(tabs.add("Pinger"))
