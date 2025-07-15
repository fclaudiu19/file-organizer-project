import tkinter as tk
from tkinter import filedialog, messagebox
from organizer import FileOrganizer

class OrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.folder = ""
        self.organizer = None

        self.label = tk.Label(root, text="Select a folder to organize:")
        self.label.pack(pady=5)

        self.select_button = tk.Button(root, text="Browse", command=self.select_folder)
        self.select_button.pack()

        self.organize_button = tk.Button(root, text="Organize", command=self.organize_files, state="disabled")
        self.organize_button.pack(pady=5)

        self.undo_button = tk.Button(root, text="Undo Last", command=self.undo_last, state="disabled")
        self.undo_button.pack()

    def select_folder(self):
        self.folder = filedialog.askdirectory()
        if self.folder:
            self.organizer = FileOrganizer(self.folder)
            self.organize_button.config(state="normal")
            self.undo_button.config(state="normal")

    def organize_files(self):
        try:
            self.organizer.organize()
            messagebox.showinfo("Success", "Files organized successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def undo_last(self):
        try:
            self.organizer.undo()
            messagebox.showinfo("Undo", "Last operation undone.")
        except Exception as e:
            messagebox.showerror("Error", str(e))