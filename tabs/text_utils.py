import customtkinter as ctk
from utils.codec_utils import do_encode, do_decode, clear_codec_fields, copy_codec_result

codec_result = None
codec_entry = None
codec_combo = None

def create_text_utils_tab(tab):
    global codec_result, codec_entry, codec_combo

    ctk.CTkLabel(tab, text="Encoder / Decoder", font=("Arial", 14, "bold")).pack(pady=(10, 2))
    encode_types = ["base64", "base32", "base16", "base85", "ascii85", "hex"]

    codec_row = ctk.CTkFrame(tab)
    codec_row.pack(pady=2)
    codec_entry = ctk.CTkEntry(codec_row, width=300, placeholder_text="Text to encode/decode")
    codec_entry.pack(side="left")
    codec_combo = ctk.CTkComboBox(codec_row, values=encode_types, width=100)
    codec_combo.set("base64")
    codec_combo.pack(side="left", padx=(0, 10))

    ctk.CTkButton(tab, text="Encode", command=lambda: do_encode(codec_entry, codec_combo, codec_result)).pack(pady=2)
    ctk.CTkButton(tab, text="Decode", command=lambda: do_decode(codec_entry, codec_combo, codec_result)).pack(pady=2)
    ctk.CTkButton(tab, text="Clear", command=lambda: clear_codec_fields(codec_entry, codec_result)).pack(pady=2)
    ctk.CTkButton(tab, text="Copy Result", command=lambda: copy_codec_result(codec_result)).pack(pady=2)

    codec_result = ctk.CTkTextbox(tab, width=300, height=20, font=("Arial", 12))
    codec_result.pack(pady=(0, 10))
    codec_result.configure(state="disabled")