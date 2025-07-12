import customtkinter as ctk
from utils.net_utils import do_ping

def create_pinger_tab(tab):
    ctk.CTkLabel(tab, text="Pinger Tool", font=("Arial", 16, "bold")).pack(pady=(20, 10))

    pinger_frame = ctk.CTkFrame(tab)
    pinger_frame.pack(pady=10)

    pinger_target = ctk.CTkEntry(pinger_frame, width=220, placeholder_text="IP or Host")
    pinger_target.pack(side="left", padx=(0, 10))

    pinger_size = ctk.CTkEntry(pinger_frame, width=80, placeholder_text="Size (bytes)")
    pinger_size.pack(side="left", padx=(0, 10))

    pinger_count = ctk.CTkEntry(pinger_frame, width=80, placeholder_text="Count")
    pinger_count.pack(side="left")

    pinger_threads = ctk.CTkEntry(pinger_frame, width=80, placeholder_text="Threads")
    pinger_threads.pack(side="left", padx=(10, 0))

    mode_frame = ctk.CTkFrame(tab)
    mode_frame.pack(pady=5)

    pinger_mode = ctk.CTkComboBox(mode_frame, values=["Normal", "Flood", "DoS", "DDoS"], width=120)
    pinger_mode.set("Normal")
    pinger_mode.pack(side="left", padx=(0, 10))

    pinger_result = ctk.CTkLabel(tab, text="", font=("Arial", 12), justify="left")
    pinger_result.pack(pady=5)

    total_pings_label = ctk.CTkLabel(tab, text="Total pings made: 0", font=("Arial", 12))
    total_pings_label.pack(pady=(0, 5))

    def start_pinger():
        target = pinger_target.get()
        size = pinger_size.get() or "32"
        count = pinger_count.get() or "4"
        mode = pinger_mode.get()
        threads = pinger_threads.get() or "1"
        if not target:
            pinger_result.configure(text="Enter a target IP or host.")
            return
        pinger_result.configure(text="Pinging...")
        total_pings_label.configure(text="Total pings made: 0")
        do_ping(pinger_target, pinger_size, pinger_count, pinger_mode, pinger_threads, pinger_result, total_pings_label)

    ctk.CTkButton(tab, text="Start Ping", command=start_pinger).pack(pady=5)
