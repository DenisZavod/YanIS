import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pandas as pd
from tkinter import filedialog
from tkinter.messagebox import OK, INFO, showinfo 
import logik_university_group as lgr


def create_university_group(root):

    univers_gr_window = tk.Toplevel(root)  
    univers_gr_window.title("Группы университета")
    univers_gr_window.geometry("700x600")
    univers_gr_window.configure(bg="#FF8C00") 
    
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
        width = 70
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

    
    notebook = ttk.Notebook(univers_gr_window)
    notebook.pack(expand=True, fill=tk.BOTH)
    
    frame1 = ttk.Frame(notebook, style="Custom.TFrame")
    frame2 = ttk.Frame(notebook, style="Custom.TFrame")

    # Add frames as tabs
    notebook.add(frame1, text="Добавить учебную группу")
    notebook.add(frame2, text="Работа со списком учебных групп")
    
    label1 = ttk.Label(frame1, text='Добавление новой учебной группы', style ="Custom1.TLabel", font='Arial, 16')
    label1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)
    
    label2 = ttk.Label(frame1, text='Введите курс учебной группы', style ="Custom1.TLabel", font='Arial, 16')
    label2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.EW)
    
    entry_kurs = ttk.Entry(frame1, style="Custom.TEntry", font=("Arial", 16))
    entry_kurs.grid(row=2, column=0, padx=10, pady=10, sticky=tk.EW)
    
    label3 = ttk.Label(frame1, text='Введите факультет учебной группы', style ="Custom1.TLabel", font='Arial, 16')
    label3.grid(row=3, column=0, padx=10, pady=10, sticky=tk.EW)
    
    entry_fac = ttk.Entry(frame1, style="Custom.TEntry", font=("Arial", 16))
    entry_fac.grid(row=4, column=0, padx=10, pady=10, sticky=tk.EW)
    
    label4 = ttk.Label(frame1, text='Введите номер учебной группы', style ="Custom1.TLabel", font='Arial, 16')
    label4.grid(row=5, column=0, padx=10, pady=10, sticky=tk.EW)
    
    entry_num = ttk.Entry(frame1, style="Custom.TEntry", font=("Arial", 16))
    entry_num.grid(row=6, column=0, padx=10, pady=10, sticky=tk.EW)
    
    button_create_disc = ttk.Button(frame1, text='Добавить новую учебную группу', style="Custom1.TButton", command=lambda:lgr.create_univ_group(entry_kurs, entry_fac, entry_num))
    button_create_disc.grid(row=7, column=0, padx=10, pady=10, sticky=tk.EW)
    
    
    
    
    frame_redact = ttk.Frame(frame2, style="Custom4.TFrame")
    frame_redact.pack(padx=10, pady=10, fill=tk.X)
    
    id_g_entry = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 16))
    id_g_entry.grid(row=0, column=0, padx=5, pady=20)
    
    kurs_g_entry = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 16))
    kurs_g_entry.grid(row=0, column=1, padx=5, pady=20)
    
    fac_g_entry = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 16))
    fac_g_entry.grid(row=0, column=2, padx=5, pady=20)
    
    num_g_entry = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 16))
    num_g_entry.grid(row=0, column=3, padx=5, pady=20)
    
    button_redact_gr = ttk.Button(frame_redact , text="Изменить название", style="CustomButton5.TButton", command=lambda:lgr.update_univ_gr(kurs_g_entry, fac_g_entry, num_g_entry, id_g_entry, table_d))
    button_redact_gr.grid(row=0, column=4, padx=5, pady=20)
    
    button_load_gr = ttk.Button(frame_redact , text="Загрузить данные", style="CustomButton5.TButton", command=lambda:lgr.load_univ_gr(table_d))
    button_load_gr.grid(row=0, column=5, padx=5, pady=20)
    
    frame_data = ttk.Frame(frame2)
    frame_data.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    columns = ("ID", "Курс", "Факультет", "Номер")
    table_d = ttk.Treeview(frame_data, columns=columns, show="headings")
    
    
    table_d.heading("ID", text="ID", anchor='w')
    table_d.heading("Курс", text="Курс", anchor='w')
    table_d.heading("Факультет", text="Факультет", anchor='w')
    table_d.heading("Номер", text="Номер", anchor='w')
    table_d.pack(expand=True, fill=tk.BOTH)
    
    
    def create_context_menu(tree):
    
        context_menu = tk.Menu(tree, tearoff=0)

        def redact_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] # Если выделено несколько, берем первый. Если только один - все равно работает
            values = tree.item(selected_item, 'values')  # Получаем значения из столбцов
            
            id_g_entry.delete(0, tk.END)
            id_g_entry.insert(0, values[0])
            
            kurs_g_entry.delete(0, tk.END)
            kurs_g_entry.insert(0, values[1])
    
            fac_g_entry.delete(0, tk.END)
            fac_g_entry.insert(0, values[2])
            
            num_g_entry.delete(0, tk.END)
            num_g_entry.insert(0, values[3])
            
            
            

        def delete_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] # Если выделено несколько, берем первый. Если только один - все равно работает
            values = tree.item(selected_item, 'values')  # Получаем значения из столбцов
            id_d = values[0]
            lgr.delete_univ_gr(id_d, table_d)
           
        context_menu.add_command(label="Редактировать запись", command=redact_item)
        context_menu.add_command(label="Удалить запись", command=delete_item)

        return context_menu

    def show_context_menu(event):
       
        selected_item = table_d.identify_row(event.y)  # Определяем, над какой строкой кликнули
        if selected_item: # проверяем что кликнули над елементом
            table_d.selection_set(selected_item) # выделяем строку
            context_menu.post(event.x_root, event.y_root)

        else:
            # Если щелкнуто вне элементов Treeview, снимаем выделение
            table_d.selection_remove(table_d.selection())
            
    context_menu = create_context_menu(table_d)
    table_d.bind("<Button-3>", show_context_menu)    