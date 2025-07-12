import customtkinter as ctk
from tkinter import messagebox
import requests

def create_ip_lookup_tab(tab):
    ctk.CTkLabel(tab, text="IP Lookup", font=("Arial", 16, "bold")).pack(pady=(20, 10))

    ip_frame = ctk.CTkFrame(tab)
    ip_frame.pack(pady=10)
    ip_entry = ctk.CTkEntry(ip_frame, width=200, placeholder_text="Enter IP")
    ip_entry.pack(side="left", padx=(0, 10))
    ip_result = ctk.CTkLabel(tab, text="", font=("Arial", 12))
    ip_result.pack(pady=5)

    def lookup():
        ip = ip_entry.get()
        if not ip:
            messagebox.showinfo("IP Lookup", "Enter an IP address.")
            return
        try:
            res = requests.get(f"https://ipinfo.io/{ip}/json")
            if res.status_code == 200:
                data = res.json()
                info = f"IP: {data.get('ip')}\nCity: {data.get('city')}\nRegion: {data.get('region')}\nCountry: {data.get('country')}\nOrg: {data.get('org')}"
                ip_result.configure(text=info)
            else:
                ip_result.configure(text="Lookup failed.")
        except Exception as e:
            ip_result.configure(text=f"Error: {e}")

    ctk.CTkButton(ip_frame, text="Lookup", command=lookup).pack(side="left")
