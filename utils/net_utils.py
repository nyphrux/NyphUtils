import os
import subprocess
import threading
import time

def do_ping(target_entry, size_entry, count_entry, mode_combo, thread_entry, output_label, total_label):
    target = target_entry.get()
    size = size_entry.get() or "32"
    count = count_entry.get() or "4"
    mode = mode_combo.get()
    thread_count = thread_entry.get() or "1"

    if not target:
        output_label.configure(text="Enter a target IP or host.")
        return

    param = "-n" if os.name == "nt" else "-c"
    size_param = "-l" if os.name == "nt" else "-s"

    try:
        count = int(count)
        size = int(size)
        thread_count = int(thread_count)
        if thread_count < 1:
            thread_count = 1
    except Exception:
        output_label.configure(text="Invalid count, size, or thread count.")
        return

    total_sent = [0]

    def ping_once():
        try:
            cmd = ["ping", param, "1", size_param, str(size), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                return result.stdout.splitlines()[-1]
            else:
                return "Timeout/Fail"
        except Exception as e:
            return f"Error: {e}"

    def update_total():
        total_label.configure(text=f"Total pings made: {total_sent[0]}")

    def run_pings():
        results = []

        if mode == "Normal":
            for _ in range(count):
                results.append(ping_once())
                total_sent[0] += 1
                update_total()
                output_label.configure(text="\n".join(results[-5:]))
                time.sleep(0.5)

        elif mode == "Flood":
            def flood_worker():
                for _ in range(count // thread_count):
                    results.append(ping_once())
                    total_sent[0] += 1
                    update_total()

            threads = []
            for _ in range(thread_count):
                t = threading.Thread(target=flood_worker)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
            output_label.configure(text="\n".join(results[-5:]))

        elif mode in ("DoS", "DDoS"):
            multiplier = 10 if mode == "DDoS" else 3
            total = count * multiplier

            def dos_worker():
                for _ in range(total // thread_count):
                    results.append(ping_once())
                    total_sent[0] += 1
                    update_total()

            threads = []
            for _ in range(thread_count):
                t = threading.Thread(target=dos_worker)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
            output_label.configure(text=f"{mode} complete. {len(results)} pings sent.")

        else:
            output_label.configure(text="Unknown mode.")

    threading.Thread(target=run_pings, daemon=True).start()
