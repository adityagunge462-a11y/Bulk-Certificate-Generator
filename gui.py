
import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import sys

selected_csv = "students.csv"


def browse_csv():
    global selected_csv

    file_path = filedialog.askopenfilename(
        title="Select Student CSV File",
        filetypes=[
            ("CSV Files", "*.csv"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        selected_csv = file_path
        file_label.config(
            text="Selected: " + os.path.basename(file_path)
        )


def generate_certificates():
    try:
        subprocess.run(
            [sys.executable, "main.py", selected_csv],
            check=True
        )

        messagebox.showinfo(
            "Success",
            "All certificates generated successfully!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def create_zip():
    try:
        subprocess.run(
            [sys.executable, "zip_certificates.py"],
            check=True
        )

        messagebox.showinfo(
            "Success",
            "ZIP file created successfully!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def open_certificates():
    folder = os.path.abspath("certificates")
    os.startfile(folder)


# Main window
window = tk.Tk()
window.title("Bulk Certificate Generator")
window.geometry("500x420")
window.resizable(False, False)


# Heading
title = tk.Label(
    window,
    text="Bulk Certificate Generator",
    font=("Arial", 20, "bold")
)
title.pack(pady=25)


# Browse CSV button
browse_button = tk.Button(
    window,
    text="Browse CSV File",
    font=("Arial", 12),
    width=25,
    command=browse_csv
)
browse_button.pack(pady=10)


# Selected file label
file_label = tk.Label(
    window,
    text="Selected: students.csv",
    font=("Arial", 10)
)
file_label.pack(pady=5)


# Generate button
generate_button = tk.Button(
    window,
    text="Generate Certificates",
    font=("Arial", 12),
    width=25,
    command=generate_certificates
)
generate_button.pack(pady=10)


# ZIP button
zip_button = tk.Button(
    window,
    text="Create ZIP File",
    font=("Arial", 12),
    width=25,
    command=create_zip
)
zip_button.pack(pady=10)


# Open folder button
open_button = tk.Button(
    window,
    text="Open Certificates Folder",
    font=("Arial", 12),
    width=25,
    command=open_certificates
)
open_button.pack(pady=10)


# Run GUI
window.mainloop()
