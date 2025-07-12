import os

def do_file_search(entry, result_label):
    name = entry.get()
    results = []
    for root, dirs, files in os.walk("."):
        for f in files:
            if name.lower() in f.lower():
                results.append(os.path.join(root, f))
    if results:
        result_label.configure(text="\n".join(results[:5]))
    else:
        result_label.configure(text="No files found.")
