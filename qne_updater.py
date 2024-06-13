import os
import shutil
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def backup_bin_folder(source_folder, backup_base_folder):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_folder = os.path.join(backup_base_folder, f'Bin_Backup_{timestamp}')
    
    try:
        shutil.copytree(source_folder, backup_folder)
        print(f"Backup of '{source_folder}' created at '{backup_folder}'")
        return backup_folder
    except Exception as e:
        messagebox.showerror("Error", f"Failed to backup Bin folder: {e}")
        return None

def update_dll(source_dll, target_folder):
    dll_name = os.path.basename(source_dll)
    target_dll = os.path.join(target_folder, dll_name)
    
    try:
        shutil.copy2(source_dll, target_dll)
        print(f"Updated DLL '{dll_name}' copied to '{target_folder}'")
        messagebox.showinfo("Success", f"Updated DLL '{dll_name}' successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update DLL: {e}")

def select_dll():
    dll_path = filedialog.askopenfilename(
        title="Select DLL file",
        filetypes=[("DLL files", "*.dll"), ("All files", "*.*")]
    )
    if dll_path:
        dll_entry.delete(0, tk.END)
        dll_entry.insert(0, dll_path)

def select_backup_folder():
    backup_path = filedialog.askdirectory(title="Select Backup Folder")
    if backup_path:
        backup_entry.delete(0, tk.END)
        backup_entry.insert(0, backup_path)

def select_bin_folder():
    bin_path = filedialog.askdirectory(title="Select Bin Folder")
    if bin_path:
        bin_entry.delete(0, tk.END)
        bin_entry.insert(0, bin_path)

def execute_update():
    source_dll = dll_entry.get()
    backup_folder = backup_entry.get()
    bin_folder = bin_entry.get()

    if not os.path.exists(source_dll):
        messagebox.showerror("Error", "Selected DLL file does not exist.")
        return

    if not os.path.exists(bin_folder):
        messagebox.showerror("Error", "Selected Bin folder does not exist.")
        return

    if not os.path.exists(backup_folder):
        try:
            os.makedirs(backup_folder)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create backup folder: {e}")
            return

    backup_path = backup_bin_folder(bin_folder, backup_folder)
    if backup_path:
        update_dll(source_dll, bin_folder)

# Create the main window
root = tk.Tk()
root.title("QNE DLL Updater")

root.resizable(False, False)

# Create and place widgets
# Create and place widgets
tk.Label(root, text="QNE Bin Folder:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
bin_entry = tk.Entry(root, width=50)
bin_entry.insert(0, "C:/ASD Solutions/Bin")  # Default Bin folder location
bin_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse...", command=select_bin_folder).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="DLL File Location:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
dll_entry = tk.Entry(root, width=50)
dll_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse...", command=select_dll).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Backup Location:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
backup_entry = tk.Entry(root, width=50)
backup_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Browse...", command=select_backup_folder).grid(row=2, column=2, padx=5, pady=5)

tk.Button(root, text="Update", command=execute_update).grid(row=3, column=1, pady=10)


# Run the main event loop
root.mainloop()
