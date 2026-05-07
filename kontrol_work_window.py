import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pandas as pd
from tkinter import filedialog
from tkinter.messagebox import OK, INFO, showinfo 
import logik_kontrol_work as lkr

def create_kontrol_work(root):
    univers_gr_window = tk.Toplevel(root)  
    univers_gr_window.title("Контрольные работы")
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
    
    style6 = ttk.Style()
    style6.configure(
        "CustomCombobox6.TCombobox",
        foreground = 'red'
    )

    
    notebook = ttk.Notebook(univers_gr_window)
    notebook.pack(expand=True, fill=tk.BOTH)
    
    frame1 = ttk.Frame(notebook, style="Custom.TFrame")
    frame2 = ttk.Frame(notebook, style="Custom.TFrame")
    frame3 = ttk.Frame(notebook, style="Custom.TFrame")
    frame4 = ttk.Frame(notebook, style="Custom.TFrame")
    frame5 = ttk.Frame(notebook, style="Custom.TFrame")
    frame6 = ttk.Frame(notebook, style="Custom.TFrame")

    # Add frames as tabs
    notebook.add(frame1, text="Добавить контрольную работу")
    notebook.add(frame2, text="Работа со списком контрольных работ")
    notebook.add(frame3, text="Добавить задание для к/р")
    notebook.add(frame4, text="Задания для к/р")
    notebook.add(frame5, text="Отметить к/р")
    notebook.add(frame6, text="Выгрузка успеваемости")
    
    
    label1 = ttk.Label(frame1, text='Добавление новой контрольной работы', style ="Custom1.TLabel", font='Arial, 16')
    label1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)
    
    label2 = ttk.Label(frame1, text='Введите название контрольной работы', style ="Custom1.TLabel", font='Arial, 16')
    label2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.EW)
    
    entry_name_kr = ttk.Entry(frame1, style="Custom.TEntry", font=("Arial", 16))
    entry_name_kr.grid(row=2, column=0, padx=10, pady=10, sticky=tk.EW)
    
    label3 = ttk.Label(frame1, text='Выберите название учебной дисциплины', style ="Custom1.TLabel", font='Arial, 16')
    label3.grid(row=3, column=0, padx=10, pady=10, sticky=tk.EW)
    
    combobox_disc = ttk.Combobox(frame1, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_disc.grid(row=4, column=0, padx=10, pady=10, sticky=tk.EW)
    
    
    button_create_kr = ttk.Button(frame1, text='Добавить контрольную работу', style="Custom1.TButton", command=lambda:lkr.create_kr(entry_name_kr))
    button_create_kr.grid(row=5, column=0, padx=10, pady=10, sticky=tk.EW)
    
    
    
    
    frame_redact = ttk.Frame(frame2, style="Custom4.TFrame")
    frame_redact.pack(padx=10, pady=10, fill=tk.X)
    
    id_kr_entry = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 16))
    id_kr_entry.grid(row=0, column=0, padx=5, pady=20)
    
    name_kr_entry = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 16))
    name_kr_entry.grid(row=0, column=1, padx=5, pady=20)
    
    id_d = ttk.Entry(frame_redact, style="Custom.TEntry", font=("Arial", 16))
    id_d.grid(row=0, column=2, padx=5, pady=20)
    
    
    button_redact_kr = ttk.Button(frame_redact , text="Изменить данные", style="CustomButton5.TButton", command=lambda:lkr.update_kr(id_kr_entry, name_kr_entry, id_d, table_d))
    button_redact_kr.grid(row=0, column=4, padx=5, pady=20)
    
    button_load_kr = ttk.Button(frame_redact , text="Загрузить данные", style="CustomButton5.TButton", command=lambda:lkr.load_kr(table_d))
    button_load_kr.grid(row=0, column=5, padx=5, pady=20)
    
    frame_data = ttk.Frame(frame2)
    frame_data.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    columns = ("ID", "Название к/р", "ID дисциплины", "Название дисциплины")
    table_d = ttk.Treeview(frame_data, columns=columns, show="headings")
    
    
    table_d.heading("ID", text="ID", anchor='w')
    table_d.heading("Название к/р", text="Название к/р", anchor='w')
    table_d.heading("ID дисциплины", text="ID дисциплины", anchor='w')
    table_d.heading("Название дисциплины", text="Название дисциплины", anchor='w')
    table_d.pack(expand=True, fill=tk.BOTH)
    
    
    def create_context_menu(tree):
    
        context_menu = tk.Menu(tree, tearoff=0)

        def redact_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] # Если выделено несколько, берем первый. Если только один - все равно работает
            values = tree.item(selected_item, 'values')  # Получаем значения из столбцов
            
            id_kr_entry.delete(0, tk.END)
            id_kr_entry.insert(0, values[0])
            
            name_kr_entry.delete(0, tk.END)
            name_kr_entry.insert(0, values[1])
    
            id_d.delete(0, tk.END)
            id_d.insert(0, values[2])
                
            

        def delete_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] # Если выделено несколько, берем первый. Если только один - все равно работает
            values = tree.item(selected_item, 'values')  # Получаем значения из столбцов
            id_kr = values[0]
            lkr.delete_kr(id_kr, table_d)
           
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
    
    lkr.get_list_discipline(combobox_disc)
    
    
    # 3 вкладка
    
    label13 = ttk.Label(frame3, text='Добавление новой задачи для к/р', style ="Custom1.TLabel", font='Arial, 16')
    label13.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)
    
    label35 = ttk.Label(frame3, text='Сортировка к/р по дисциплине', style ="Custom1.TLabel", font='Arial, 16')
    label35.grid(row=0, column=1, padx=30, pady=10, sticky=tk.EW)
    
    label36 = ttk.Label(frame3, text='Выберите дисциплину', style ="Custom1.TLabel", font='Arial, 16')
    label36.grid(row=1, column=1, padx=30, pady=10, sticky=tk.EW)

    combobox_discipline = ttk.Combobox(frame3, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_discipline.grid(row=2, column=1, padx=10, pady=10, sticky=tk.EW)


    button_sort_kr = ttk.Button(frame3, text='Отсортировать к/р по дисциплине', style="Custom1.TButton", command=lambda:lkr.load_kr_2(combobox_kr, combobox_discipline))
    button_sort_kr.grid(row=3, column=1, padx=10, pady=10, sticky=tk.EW)

    label23 = ttk.Label(frame3, text='Введите название задачи для к/р', style ="Custom1.TLabel", font='Arial, 16')
    label23.grid(row=1, column=0, padx=10, pady=10, sticky=tk.EW)

    entry_name_tkr = ttk.Entry(frame3, style="Custom.TEntry", font=("Arial", 16))
    entry_name_tkr.grid(row=2, column=0, padx=10, pady=10, sticky=tk.EW)

    label33 = ttk.Label(frame3, text='Введите балл задачи для к/р', style ="Custom1.TLabel", font='Arial, 16')
    label33.grid(row=3, column=0, padx=10, pady=10, sticky=tk.EW)

    entry_mark_tkr = ttk.Entry(frame3, style="Custom.TEntry", font=("Arial", 16))
    entry_mark_tkr.grid(row=4, column=0, padx=10, pady=10, sticky=tk.EW)

    label34 = ttk.Label(frame3, text='Выберите контрольную работу', style ="Custom1.TLabel", font='Arial, 16')
    label34.grid(row=5, column=0, padx=10, pady=10, sticky=tk.EW)

    combobox_kr = ttk.Combobox(frame3, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_kr.grid(row=6, column=0, padx=10, pady=10, sticky=tk.EW)

    button_create_tkr = ttk.Button(frame3, text='Добавить задачу', style="Custom1.TButton", command=lambda:lkr.create_tkr(entry_name_tkr, entry_mark_tkr, combobox_kr))
    button_create_tkr.grid(row=7, column=0, padx=10, pady=10, sticky=tk.EW)

    lkr.get_list_discipline(combobox_discipline)

    
    
    frame_redact_2 = ttk.Frame(frame4, style="Custom4.TFrame")
    frame_redact_2.pack(padx=10, pady=10, fill=tk.X)
    
    id_task = ttk.Entry(frame_redact_2, style="Custom.TEntry", font=("Arial", 16))
    id_task.grid(row=0, column=0, padx=5, pady=20)
    
    name_task = ttk.Entry(frame_redact_2, style="Custom.TEntry", font=("Arial", 16))
    name_task.grid(row=0, column=1, padx=5, pady=20)
    
    mark = ttk.Entry(frame_redact_2, style="Custom.TEntry", font=("Arial", 16))
    mark.grid(row=0, column=2, padx=5, pady=20)
    
    id_kr = ttk.Entry(frame_redact_2, style="Custom.TEntry", font=("Arial", 16))
    id_kr.grid(row=0, column=3, padx=5, pady=20)
    
    
    button_redact_tkr = ttk.Button(frame_redact_2 , text="Изменить данные", style="CustomButton5.TButton", command=lambda:lkr.update_tkr(id_task, name_task, mark, id_kr , table_d_2))
    button_redact_tkr.grid(row=0, column=4, padx=5, pady=20)
    
    button_load_tkr = ttk.Button(frame_redact_2 , text="Загрузить данные", style="CustomButton5.TButton", command=lambda:lkr.load_tkr(table_d_2))
    button_load_tkr.grid(row=0, column=5, padx=5, pady=20)
    
    combobox_disc_poisk = ttk.Combobox(frame_redact_2, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_disc_poisk.grid(row=1, column=0, padx=10, pady=10, sticky=tk.EW)
    
    combobox_kr_poisk = ttk.Combobox(frame_redact_2, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_kr_poisk.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)
    
    button_sort_tkr = ttk.Button(frame_redact_2 , text="Сортировка задач", style="CustomButton5.TButton", command=lambda:lkr.load_poisk_tkr(table_d_2, combobox_disc_poisk, combobox_kr_poisk))
    button_sort_tkr.grid(row=1, column=2, padx=5, pady=20, sticky=tk.EW)
    
    frame_data_2 = ttk.Frame(frame4)
    frame_data_2.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    columns_2 = ("ID", "Название задачи", "Балл", "ID к/р", "Название к/р", "Дисциплина")
    table_d_2 = ttk.Treeview(frame_data_2, columns=columns_2, show="headings")
    
    
    table_d_2.heading("ID", text="ID", anchor='w')
    table_d_2.heading("Название задачи", text="Название задачи", anchor='w')
    table_d_2.heading("Балл", text="Балл", anchor='w')
    table_d_2.heading("ID к/р", text="ID к/р", anchor='w')
    table_d_2.heading("Название к/р", text="Название к/р", anchor='w')
    table_d_2.heading("Дисциплина", text="Дисциплина", anchor='w')
    table_d_2.pack(expand=True, fill=tk.BOTH)
    
    
    
    def create_context_menu_2(tree):
    
        context_menu_2 = tk.Menu(tree, tearoff=0)

        def redact_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] # Если выделено несколько, берем первый. Если только один - все равно работает
            values = tree.item(selected_item, 'values')  # Получаем значения из столбцов
            
            id_task.delete(0, tk.END)
            id_task.insert(0, values[0])
            
            name_task.delete(0, tk.END)
            name_task.insert(0, values[1])
    
            mark.delete(0, tk.END)
            mark.insert(0, values[2])
            
            id_kr.delete(0, tk.END)
            id_kr.insert(0, values[3])
                
            

        def delete_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] # Если выделено несколько, берем первый. Если только один - все равно работает
            values = tree.item(selected_item, 'values')  # Получаем значения из столбцов
            id_tkr = values[0]
            lkr.delete_tkr(id_tkr, table_d_2)
           
        context_menu_2.add_command(label="Редактировать запись", command=redact_item)
        context_menu_2.add_command(label="Удалить запись", command=delete_item)

        return context_menu_2

    def show_context_menu_2(event):
       
        selected_item = table_d_2.identify_row(event.y)  # Определяем, над какой строкой кликнули
        if selected_item: # проверяем что кликнули над елементом
            table_d_2.selection_set(selected_item) # выделяем строку
            context_menu_2.post(event.x_root, event.y_root)

        else:
            # Если щелкнуто вне элементов Treeview, снимаем выделение
            table_d_2.selection_remove(table_d_2.selection())
            
    context_menu_2 = create_context_menu_2(table_d_2)
    table_d_2.bind("<Button-3>", show_context_menu_2)
    
    lkr.get_list_discipline_for_poisk(combobox_disc_poisk, combobox_kr_poisk)
    
    
    frame_redact4 = ttk.Frame(frame5, style="Custom4.TFrame")
    frame_redact4.pack(padx=10, pady=10, fill=tk.X)
    
    combobox_course = ttk.Combobox(frame_redact4, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_course.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)
    
    combobox_fac = ttk.Combobox(frame_redact4, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_fac.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)
    
    combobox_num = ttk.Combobox(frame_redact4, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_num.grid(row=0, column=2, padx=10, pady=10, sticky=tk.EW)
    
    button_sort_group = ttk.Button(frame_redact4, text="Загрузить список группы", style="CustomButton5.TButton", command=lambda:lkr.load_select_stud(combobox_course, combobox_fac, combobox_num, table_d5))
    button_sort_group.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
    
    
    combobox_discipline_25 = ttk.Combobox(frame_redact4, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_discipline_25.grid(row=1, column=0, padx=10, pady=10, sticky=tk.EW)
    
    combobox_kr_25 = ttk.Combobox(frame_redact4, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_kr_25.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)
    
    button_sort_kr_25 = ttk.Button(frame_redact4, text="Загрузить список заданий", style="CustomButton5.TButton", command=lambda:lkr.load_poisk_tkr(table_d_25, combobox_discipline_25, combobox_kr_25))
    button_sort_kr_25.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
    
    id_st = ttk.Entry(frame_redact4, style="Custom.TEntry", font=("Arial", 16))
    id_st.grid(row=2, column=0, padx=5, pady=5)
    
    ss = ttk.Entry(frame_redact4, style="Custom.TEntry", font=("Arial", 16))
    ss.grid(row=2, column=1, padx=5, pady=5)
    
    sn = ttk.Entry(frame_redact4, style="Custom.TEntry", font=("Arial", 16))
    sn.grid(row=2, column=2, padx=5, pady=5)
    
    so = ttk.Entry(frame_redact4, style="Custom.TEntry", font=("Arial", 16))
    so.grid(row=2, column=3, padx=5, pady=5)
    
    id_z = ttk.Entry(frame_redact4, style="Custom.TEntry", font=("Arial", 16))
    id_z.grid(row=2, column=4, padx=5, pady=5)
    
    button_insert_tkr_25 = ttk.Button(frame_redact4, text="Отметить задание", style="CustomButton5.TButton", command=lambda:lkr.insert_stud_tkr(id_st, id_z))
    button_insert_tkr_25.grid(row=2, column=5, padx=5, pady=5, sticky=tk.W)
    
    
    frame_data_25 = ttk.Frame(frame5)
    frame_data_25.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    
    columns_5 = ("ID", "Фамилия", "Имя", "Отчество")
    table_d5 = ttk.Treeview(frame_data_25, columns=columns_5, show="headings")
    
    
    table_d5.heading("ID", text="ID", anchor='w')
    table_d5.heading("Фамилия", text="Фамилия", anchor='w')
    table_d5.heading("Имя", text="Имя", anchor='w')
    table_d5.heading("Отчество", text="Отчество", anchor='w')
    table_d5.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    
    
    columns_25 = ("ID", "Название задачи", "Балл")
    table_d_25 = ttk.Treeview(frame_data_25, columns=columns_25, show="headings")
    
    
    table_d_25.heading("ID", text="ID", anchor='w')
    table_d_25.heading("Название задачи", text="Название задачи", anchor='w')
    table_d_25.heading("Балл", text="Балл", anchor='w')
    table_d_25.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
    
    
    def create_context_menu_25(tree):
    
        context_menu_25 = tk.Menu(tree, tearoff=0)

        def redact_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] # Если выделено несколько, берем первый. Если только один - все равно работает
            values = tree.item(selected_item, 'values')  # Получаем значения из столбцов
            
            id_st.delete(0, tk.END)
            id_st.insert(0, values[0])
            
            ss.delete(0, tk.END)
            ss.insert(0, values[1])
    
            sn.delete(0, tk.END)
            sn.insert(0, values[2])
            
            so.delete(0, tk.END)
            so.insert(0, values[3])
                
           
        context_menu_25.add_command(label="Редактировать запись", command=redact_item)
    
        return context_menu_25

    def show_context_menu_25(event):
       
        selected_item = table_d5.identify_row(event.y)  # Определяем, над какой строкой кликнули
        if selected_item: # проверяем что кликнули над елементом
            table_d5.selection_set(selected_item) # выделяем строку
            context_menu_25.post(event.x_root, event.y_root)

        else:
            # Если щелкнуто вне элементов Treeview, снимаем выделение
            table_d5.selection_remove(table_d5.selection())
            
    context_menu_25 = create_context_menu_25(table_d5)
    table_d5.bind("<Button-3>", show_context_menu_25)
    
    frame_redact5 = ttk.Frame(frame6, style="Custom4.TFrame")
    frame_redact5.pack(padx=10, pady=10, fill=tk.X)
    
    combobox_course6 = ttk.Combobox(frame_redact5, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_course6.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)
    
    combobox_fac6 = ttk.Combobox(frame_redact5, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_fac6.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)
    
    combobox_num6 = ttk.Combobox(frame_redact5, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_num6.grid(row=0, column=2, padx=10, pady=10, sticky=tk.EW)
    
    combobox_discipline6 = ttk.Combobox(frame_redact5, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_discipline6.grid(row=0, column=3, padx=10, pady=10, sticky=tk.EW)
    
    upload = ttk.Button(frame_redact5, text="Выгрузить ведомость", style="CustomButton5.TButton", command=lambda:lkr.upload_result(combobox_course6, combobox_fac6, combobox_num6, combobox_discipline6))
    upload.grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)
    
    frame_data6 = ttk.Frame(frame6)
    frame_data6.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    upload_tab = ttk.Button(frame_redact5, text="Загрузить данные", style="CustomButton5.TButton", command=lambda:lkr.create_treeview_table(frame_data6, combobox_course6, combobox_fac6, combobox_num6, combobox_discipline6))
    upload_tab.grid(row=0, column=5, padx=5, pady=5, sticky=tk.W)
    
    
    
    
    lkr.get_list_kurs(combobox_course)
    lkr.get_list_fac(combobox_fac)
    lkr.get_list_num(combobox_num)
    
    lkr.get_list_discipline(combobox_discipline_25)
    lkr.get_list_discipline_for_poisk(combobox_discipline_25, combobox_kr_25)
    
    lkr.get_list_kurs(combobox_course6)
    lkr.get_list_fac(combobox_fac6)
    lkr.get_list_num(combobox_num6)
    
    lkr.get_list_discipline(combobox_discipline6)
    