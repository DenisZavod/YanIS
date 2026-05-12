import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pandas as pd
from tkinter import filedialog
from tkinter.messagebox import OK, INFO, showinfo 
import logik_update_git as lug

def create_git_update_window(root):
    git_update_window = tk.Toplevel(root)  
    git_update_window.title("Обновления из Git-репозитория")
    git_update_window.geometry("700x600")
    git_update_window.configure(bg="#FF8C00")
    
    
    style = ttk.Style()
    style.configure(
        "Custom.TFrame",
        background="#7FFFD4"
        )
    
    style1 = ttk.Style()
    style1.configure(
        "Custom1.TLabel",
        background = "#7FFFD4",
    )
    
    style2 = ttk.Style()
    style2.configure(
        "Custom1.TButton",
        background="#FF8C00",
        foreground="white",
        relief="raised",
        borderwidth=1
    )
    
    style2.map(
    "Custom1.TButton",
    background=[("active", "#B22222")],  # Новый цвет при наведении
    )
    
    style3 = ttk.Style()
    style3.configure(
        "Custom.TEntry",
        foreground = 'red',
        width = 50
    )
    
    style4 = ttk.Style()
    style4.configure(
        "Custom4.TFrame",
        height=120,
        background="#FF8C00"
    )
    
    style5 = ttk.Style()
    style5.configure(
    "CustomButton5.TButton",
    background="#FF8C00",
    foreground="white",
    relief="raised",
    borderwidth=1,
    
    )
    
    style5.map(
    "CustomButton5.TButton",
    background=[("active", "#B22222")],  # Новый цвет при наведении
    )
    
    style6 = ttk.Style()
    style6.configure(
        "CustomCombobox6.TCombobox",
        foreground = 'red'
    )
    
    
    nav_frame = ttk.Frame(git_update_window)
    nav_frame.pack(expand=True, fill="both", padx=5, pady=5)

    button_check_git = ttk.Button(nav_frame, text="Проверить обновления", style="CustomButton5.TButton", command=lambda:lug.check_git_repos())
    button_check_git.grid(row=0, column=0, padx=5, pady=5, sticky="we")
    
    button_update_git = ttk.Button(nav_frame, text="Обновить приложение", style="CustomButton5.TButton")
    button_update_git.grid(row=1, column=0, padx=5, pady=5, sticky="we")
    
    nav_frame.grid_columnconfigure(0, weight=1)
    
    