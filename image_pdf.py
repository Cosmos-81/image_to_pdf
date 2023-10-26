import convert
import tkinter as tk
from tkinter import filedialog

def select_input_folder():
    input_folder_path = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, input_folder_path)

def select_output_folder():
    output_folder_path = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, output_folder_path)

def convert_images_to_pdf():
    input_folder_path = input_folder_entry.get()
    output_folder_path = output_folder_entry.get()
    
    # 変換処理を実行
    convert.image_to_pdf(input_folder_path, output_folder_path)

root = tk.Tk()
root.title("Image to PDF Converter")

input_folder_label = tk.Label(root, text="Input Folder:")
input_folder_label.grid(row=0, column=0, padx=5, pady=5)

input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=0, column=1, padx=5, pady=5)

input_folder_button = tk.Button(root, text="Select Folder", command=select_input_folder)
input_folder_button.grid(row=0, column=2, padx=5, pady=5)

output_folder_label = tk.Label(root, text="Output Folder:")
output_folder_label.grid(row=1, column=0, padx=5, pady=5)

output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=5, pady=5)

output_folder_button = tk.Button(root, text="Select Folder", command=select_output_folder)
output_folder_button.grid(row=1, column=2, padx=5, pady=5)

submit_button = tk.Button(root, text="Convert to PDF", command=convert_images_to_pdf)
submit_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
