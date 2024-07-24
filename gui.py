import tkinter as tk
from tkinter import scrolledtext
import subprocess

def run_command(command):
    # Enable the text widget to modify it
    output_box.config(state=tk.NORMAL)
    output_box.insert(tk.END, f"Running command: {command}\n")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output_box.insert(tk.END, result.stdout)
        output_box.insert(tk.END, result.stderr)
    except Exception as e:
        output_box.insert(tk.END, str(e))
    
    # Scroll to the end of the text widget
    output_box.see(tk.END)
    
    # Disable the text widget to make it non-editable again
    output_box.config(state=tk.DISABLED)

def download():
    run_command("py download.py")

def migrate():
    run_command("py manage.py migrate")

def run_server():
    run_command("py manage.py runserver")

# Create the main window
root = tk.Tk()
root.title("Command Prompt")

# Create the output box
output_box = scrolledtext.ScrolledText(root, width=100, height=20)
output_box.pack(pady=10)
output_box.config(state=tk.DISABLED)

# Create the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

download_button = tk.Button(button_frame, text="Download", command=download)
download_button.pack(side=tk.LEFT, padx=5)

migrate_button = tk.Button(button_frame, text="Migrate", command=migrate)
migrate_button.pack(side=tk.LEFT, padx=5)

run_button = tk.Button(button_frame, text="Run Server", command=run_server)
run_button.pack(side=tk.LEFT, padx=5)

# Start the Tkinter event loop
root.mainloop()