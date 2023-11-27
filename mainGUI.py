import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from main import download_data

def browse_button():
    filename = filedialog.askdirectory()
    target_account.set(filename)

def start_download(target_account_entry, status_label):
    top_liked_users, top_commenters = download_data(target_account_entry.get())
    
    # Display top 3 liked users and commenters in the GUI
    status_label.config(text=f"Top 3 liked users: {', '.join(user[0] for user in top_liked_users)}\n"
                             f"Top 3 commenters: {', '.join(commenter[0] for commenter in top_commenters)}")


# Create main window
root = tk.Tk()
root.title("Instagram Data Downloader")

root.geometry("400x250")

# Create and set up GUI elements
target_account_label = tk.Label(root, text="Target Account:")
target_account_label.pack()

target_account = tk.StringVar()
target_account_entry = tk.Entry(root, textvariable=target_account)
target_account_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_button)
browse_button.pack()

start_button = tk.Button(root, text="Start Download", command=lambda: start_download(target_account_entry, status_label))
start_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# Start the main loop
root.mainloop()
