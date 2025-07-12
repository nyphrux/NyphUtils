import base64
import pyperclip
from tkinter import messagebox
from app_config import NAME

def set_result(widget, text):
    widget.configure(state="normal")
    widget.delete("1.0", "end")
    widget.insert("1.0", text)
    widget.configure(state="disabled")

def do_encode(entry, combo, result_widget):
    text = entry.get()
    codec = combo.get()
    try:
        if codec == "base64":
            encoded = base64.b64encode(text.encode()).decode()
        elif codec == "base32":
            encoded = base64.b32encode(text.encode()).decode()
        elif codec == "base16":
            encoded = base64.b16encode(text.encode()).decode()
        elif codec == "base85":
            encoded = base64.b85encode(text.encode()).decode()
        elif codec == "ascii85":
            encoded = base64.a85encode(text.encode()).decode()
        elif codec == "hex":
            encoded = text.encode().hex()
        else:
            encoded = "Unknown codec"
        set_result(result_widget, encoded)
    except Exception as e:
        set_result(result_widget, f"Error: {e}")

def do_decode(entry, combo, result_widget):
    text = entry.get()
    codec = combo.get()
    try:
        if codec == "base64":
            decoded = base64.b64decode(text.encode()).decode()
        elif codec == "base32":
            decoded = base64.b32decode(text.encode()).decode()
        elif codec == "base16":
            decoded = base64.b16decode(text.encode()).decode()
        elif codec == "base85":
            decoded = base64.b85decode(text.encode()).decode()
        elif codec == "ascii85":
            decoded = base64.a85decode(text.encode()).decode()
        elif codec == "hex":
            decoded = bytes.fromhex(text).decode()
        else:
            decoded = "Unknown codec"
        set_result(result_widget, decoded)
    except Exception as e:
        set_result(result_widget, f"Error: {e}")

def clear_codec_fields(entry, result_widget):
    entry.delete(0, "end")
    set_result(result_widget, "")

def copy_codec_result(result_widget):
    text = result_widget.get("1.0", "end-1c")
    if text:
        pyperclip.copy(text)
        messagebox.showinfo(NAME, "Result copied to clipboard.")
