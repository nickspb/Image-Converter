import tkinter as tk
from PIL import Image

from tkinter import filedialog, messagebox

file_path = ""

def select_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        file_path_label.config(text=file_path)

def convert():
    try:
        global file_path
        format = text_field.get("1.0", tk.END).strip()
        if format:
            im = Image.open(file_path)
            im.save(f'image.{format}')
        else:
            messagebox.showerror("Error", "No image was selected.")
    except Exception as err:
        messagebox.showerror("Error", "Invalid format or smth else.")

root = tk.Tk()
root.title("Image Converter")

open_file_button = tk.Button(root, text="Select File", command=select_file)
open_file_button.pack(pady=10)

file_path_label = tk.Label(root, text="No file selected", font=("Arial", 12))
file_path_label.pack(pady=10)

text_field = tk.Text(root, height=3, width=30)
text_field.pack(pady=10)

get_info_button = tk.Button(root, text="Convert!", command=convert)
get_info_button.pack(pady=10)

root.mainloop()