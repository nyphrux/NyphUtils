import requests

def extract_id_token(url):
    try:
        parts = url.rstrip("/").split("/")
        return parts[-2], parts[-1]
    except Exception:
        return None, None

def set_webhook_url(entry):
    print(f"[Webhook] URL set to: {entry.get()}")

def send_webhook_message(url_entry, msg_entry):
    url = url_entry.get()
    msg = msg_entry.get()
    if not url or not msg:
        print("[Error] Please set webhook URL and enter a message.")
        return
    try:
        res = requests.post(url, json={"content": msg})
        print(f"[Send Message] Status: {res.status_code}")
    except Exception as e:
        print(f"[Send Message] Failed: {e}")

def delete_webhook(url_entry):
    url = url_entry.get()
    webhook_id, webhook_token = extract_id_token(url)
    if not webhook_id or not webhook_token:
        print("[Error] Invalid webhook URL")
        return
    api_url = f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"
    try:
        res = requests.delete(api_url)
        if res.status_code == 204:
            print("[Delete Webhook] Successfully deleted webhook.")
            url_entry.delete(0, "end")
        else:
            print(f"[Delete Webhook] Failed: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"[Delete Webhook] Exception: {e}")

def rename_webhook(url_entry, rename_entry):
    url = url_entry.get()
    new_name = rename_entry.get()
    if not url or not new_name:
        print("[Error] Set webhook URL and enter a new name.")
        return
    webhook_id, webhook_token = extract_id_token(url)
    api_url = f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"
    try:
        res = requests.patch(api_url, json={"name": new_name})
        print(f"[Rename Webhook] Status: {res.status_code}")
    except Exception as e:
        print(f"[Rename Webhook] Failed: {e}")
