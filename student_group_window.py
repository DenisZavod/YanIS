import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pandas as pd
from tkinter import filedialog
from tkinter.messagebox import OK, INFO, showinfo 
import logik_student_group as lsg

def create_student_group_window(root):
    student_gr_window = tk.Toplevel(root)  
    student_gr_window.title("Студенческие группы")
    student_gr_window.geometry("700x600")
    student_gr_window.configure(bg="#FF8C00")
    
    
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
    
    notebook = ttk.Notebook(student_gr_window)
    notebook.pack(expand=True, fill=tk.BOTH)
    
    frame1 = ttk.Frame(notebook, style="Custom.TFrame")
    frame2 = ttk.Frame(notebook, style="Custom.TFrame")
    #frame3 = ttk.Frame(notebook, style="Custom.TFrame")
    #frame4 = ttk.Frame(notebook, style="Custom.TFrame")

    # Add frames as tabs
    notebook.add(frame1, text="Добавить студентов в учебную группу")
    notebook.add(frame2, text="Списки студентов по группам")
    #notebook.add(frame3, text="Добавить задание для к/р")
    #notebook.add(frame4, text="Заданя для к/р")
    
    frame_redact = ttk.Frame(frame1, style="Custom4.TFrame")
    frame_redact.pack(padx=10, pady=10, fill=tk.X)
    
    button_load = ttk.Button(frame_redact, text="Загрузить данные", style="CustomButton5.TButton", command=lambda:lsg.get_list_stud(table_d))
    button_load.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    
    
    button_load_group = ttk.Button(frame_redact, text="Загрузить учебные группы", style="CustomButton5.TButton", command=lambda:lsg.load_univ_gr(table_d_2))
    button_load_group.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
    
    entry_id_st = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 14), width=8)
    entry_id_st.grid(row=0, column=2, padx=5, pady=5, sticky=tk.EW)
    
    entry_sname_st = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 14))
    entry_sname_st.grid(row=0, column=4, padx=5, pady=5, sticky=tk.EW)
    
    entry_name_st = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 14))
    entry_name_st.grid(row=0, column=5, padx=5, pady=5, sticky=tk.EW)
    
    entry_oname_st = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 14))
    entry_oname_st.grid(row=0, column=6, padx=5, pady=5, sticky=tk.EW)
    
    entry_id_gr = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 14), width=8)
    entry_id_gr.grid(row=0, column=7, padx=5, pady=5, sticky=tk.EW)
    
    button_insert_group = ttk.Button(frame_redact, text="Добавить студента в группу", style="CustomButton5.TButton", command=lambda:lsg.insert_stud_group(entry_id_st, entry_id_gr))
    button_insert_group.grid(row=0, column=8, padx=5, pady=5, sticky=tk.W)
    
    frame_data = ttk.Frame(frame1 , style="Custom.TFrame")
    frame_data.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    columns = ("ID", "Фамилия", "Имя", "Отчество")
    table_d = ttk.Treeview(frame_data, columns=columns, show="headings")
    
    
    table_d.heading("ID", text="ID", anchor='w')
    table_d.heading("Фамилия", text="Фамилия", anchor='w')
    table_d.heading("Имя", text="Имя", anchor='w')
    table_d.heading("Отчество", text="Отчество", anchor='w')
    table_d.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    
    
    columns_2 = ("ID", "Курс", "Факультет", "Группа")
    table_d_2 = ttk.Treeview(frame_data, columns=columns_2, show="headings")
    
    
    table_d_2.heading("ID", text="ID", anchor='w')
    table_d_2.heading("Курс", text="Курс", anchor='w')
    table_d_2.heading("Факультет", text="Факультет", anchor='w')
    table_d_2.heading("Группа", text="Группа", anchor='w')
    table_d_2.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
    
    
    def create_context_menu(tree):
    
        context_menu = tk.Menu(tree, tearoff=0)

        def redact_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] # Если выделено несколько, берем первый. Если только один - все равно работает
            values = tree.item(selected_item, 'values')  # Получаем значения из столбцов
            
            entry_id_st.delete(0, tk.END)
            entry_id_st.insert(0, values[0])
            
            entry_sname_st.delete(0, tk.END)
            entry_sname_st.insert(0, values[1])
    
            entry_name_st.delete(0, tk.END)
            entry_name_st.insert(0, values[2])
            
            entry_oname_st.delete(0, tk.END)
            entry_oname_st.insert(0, values[3])
            
                
           
        context_menu.add_command(label="Редактировать запись", command=redact_item)

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
    
    
    frame2_redact = ttk.Frame(frame2, style="Custom4.TFrame")
    frame2_redact.pack(padx=10, pady=10, fill=tk.X)
    
    frame_2_data = ttk.Frame(frame2, style="Custom.TFrame")
    frame_2_data.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    
    columns_3 = ("ID", "Фамилия", "Имя", "Отчество", "ID записи")
    table_d_3 = ttk.Treeview(frame_2_data, columns=columns_3, show="headings")
    
    
    table_d_3.heading("ID", text="ID", anchor='w')
    table_d_3.heading("Фамилия", text="Фамилия", anchor='w')
    table_d_3.heading("Имя", text="Имя", anchor='w')
    table_d_3.heading("Отчество", text="Отчество", anchor='w')
    table_d_3.heading("ID записи", text="ID записи", anchor='w')
    table_d_3.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
    
    combobox_course = ttk.Combobox(frame2_redact, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_course.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)
    
    combobox_fac = ttk.Combobox(frame2_redact, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_fac.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)
    
    combobox_num = ttk.Combobox(frame2_redact, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_num.grid(row=0, column=2, padx=10, pady=10, sticky=tk.EW)
    
    button_sort_group = ttk.Button(frame2_redact, text="Сортировка по группе", style="CustomButton5.TButton", command=lambda:lsg.load_select_stud(combobox_course, combobox_fac, combobox_num, table_d_3))
    button_sort_group.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
    
    
    def create_context_menu_2(tree):
    
        context_menu_2 = tk.Menu(tree, tearoff=0)

        def delete_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] # Если выделено несколько, берем первый. Если только один - все равно работает
            values = tree.item(selected_item, 'values')  # Получаем значения из столбцов
            id_str = values[0]
            lsg.delete_str(id_str)
           
        context_menu_2.add_command(label="Удалить запись", command=delete_item)

        return context_menu_2
    
    def show_context_menu_2(event):
       
        selected_item = table_d_3.identify_row(event.y)  # Определяем, над какой строкой кликнули
        if selected_item: # проверяем что кликнули над елементом
            table_d_3.selection_set(selected_item) # выделяем строку
            context_menu_2.post(event.x_root, event.y_root)

        else:
            # Если щелкнуто вне элементов Treeview, снимаем выделение
            table_d.selection_remove(table_d_3.selection())
            
    context_menu_2 = create_context_menu_2(table_d_3)
    table_d_3.bind("<Button-3>", show_context_menu_2) 

    
    lsg.get_list_kurs(combobox_course)
    lsg.get_list_fac(combobox_fac)
    lsg.get_list_num(combobox_num)