import customtkinter as ctk
from utils.webhook_utils import set_webhook_url, send_webhook_message, delete_webhook, rename_webhook

def create_webhook_tab(tab):
    ctk.CTkLabel(tab, text="Discord Webhook Tools", font=("Arial", 16, "bold")).pack(pady=(20, 10))

    global webhook_url, webhook_message, webhook_rename

    webhook_frame = ctk.CTkFrame(tab, fg_color="transparent")
    webhook_frame.pack()
    webhook_url = ctk.CTkEntry(webhook_frame, width=400, height=40, placeholder_text="Webhook URL", font=("Arial", 14), justify="center")
    webhook_url.pack(side="left", padx=(0, 10))
    ctk.CTkButton(webhook_frame, text="Set", command=lambda: set_webhook_url(webhook_url)).pack(side="left")

    message_frame = ctk.CTkFrame(tab, fg_color="transparent")
    message_frame.pack()
    webhook_message = ctk.CTkEntry(message_frame, width=350, height=40, placeholder_text="Message to send", font=("Arial", 14))
    webhook_message.pack(side="left", padx=(0, 10))
    ctk.CTkButton(message_frame, text="Send", command=lambda: send_webhook_message(webhook_url, webhook_message)).pack(side="left")

    rename_frame = ctk.CTkFrame(tab)
    rename_frame.pack()
    webhook_rename = ctk.CTkEntry(rename_frame, width=350, height=40, placeholder_text="New webhook name", font=("Arial", 14))
    webhook_rename.pack(side="left", padx=(0, 10))
    ctk.CTkButton(rename_frame, text="Rename", command=lambda: rename_webhook(webhook_url, webhook_rename)).pack(side="left")

    ctk.CTkButton(tab, text="Delete Webhook", command=lambda: delete_webhook(webhook_url)).pack(pady=(10, 0))
