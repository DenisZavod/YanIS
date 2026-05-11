import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pandas as pd
from tkinter import filedialog
from tkinter.messagebox import OK, INFO, showinfo
import logik_kontrol_work as lkr
from tkcalendar import Calendar
import logik_attendance as la

def create_attendance(root):
    attendance_window = tk.Toplevel(root)  
    attendance_window.title("Посещаемость")
    attendance_window.geometry("700x600")
    attendance_window.configure(bg="#FF8C00") 
    
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

    
    notebook = ttk.Notebook(attendance_window)
    notebook.pack(expand=True, fill=tk.BOTH)
    
    frame1 = ttk.Frame(notebook, style="Custom.TFrame")
    frame2 = ttk.Frame(notebook, style="Custom.TFrame")

    # Add frames as tabs
    notebook.add(frame1, text="Отметить посещаемость")
    notebook.add(frame2, text="Работа со списком посещаемости")

    frame_redact = ttk.Frame(frame1, style="Custom4.TFrame")
    frame_redact.pack(padx=10, pady=10, fill=tk.X)

    combobox_course = ttk.Combobox(frame_redact, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_course.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)
    
    combobox_fac = ttk.Combobox(frame_redact, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_fac.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)
    
    combobox_num = ttk.Combobox(frame_redact, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_num.grid(row=0, column=2, padx=10, pady=10, sticky=tk.EW)
    
    button_sort_group = ttk.Button(frame_redact, text="Загрузить список группы", style="CustomButton5.TButton", command=lambda:lkr.load_select_stud(combobox_course, combobox_fac, combobox_num, table_d))
    button_sort_group.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

    combobox_discipline = ttk.Combobox(frame_redact, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_discipline.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    cal = Calendar(frame_redact, selectmode="day", date_pattern="yyyy-mm-dd", locale="ru_RU")
    cal.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

    frame_data = ttk.Frame(frame1)
    frame_data.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    
    columns = ("ID", "Фамилия", "Имя", "Отчество")
    table_d = ttk.Treeview(frame_data, columns=columns, show="headings")
    
    
    table_d.heading("ID", text="ID", anchor='w')
    table_d.heading("Фамилия", text="Фамилия", anchor='w')
    table_d.heading("Имя", text="Имя", anchor='w')
    table_d.heading("Отчество", text="Отчество", anchor='w')
    table_d.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)



    lkr.get_list_kurs(combobox_course)
    lkr.get_list_fac(combobox_fac)
    lkr.get_list_num(combobox_num)
    lkr.get_list_discipline(combobox_discipline)

    def print_date(cal):
        selected_date = cal.selection_get()
        formatted_date = selected_date.strftime('%d-%m-%Y')  # Форматирование даты
        print(selected_date)
    

    def create_context_menu(tree):
    
        context_menu = tk.Menu(tree, tearoff=0)

        def redact_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] 
            values = tree.item(selected_item, 'values')  
           
            la.create_attendance_stud(cal, combobox_discipline, 'Присутствовал', values[0])

            tree.tag_configure('green', background='green')

            tree.item(selected_item, tags=('green'))

            
            all_items = tree.get_children()     
            current_index = tree.index(selected_item)
            next_index = current_index + 1

            if next_index < len(all_items):  
                next_item = all_items[next_index]  
                tree.focus(next_item)              
                tree.selection_set(next_item)      
            else:
                print("Дальше двигать нельзя.")
        

        def redact_item_2():
            selected_item = tree.selection()
            selected_item = selected_item[0] 
            values = tree.item(selected_item, 'values')  
           
            la.create_attendance_stud(cal, combobox_discipline, 'Отсутствовал', values[0])

            tree.tag_configure('red', background='red')

            tree.item(selected_item, tags=('red'))

            
            all_items = tree.get_children()     
            current_index = tree.index(selected_item)
            next_index = current_index + 1

            if next_index < len(all_items):  
                next_item = all_items[next_index]  
                tree.focus(next_item)              
                tree.selection_set(next_item)      
            else:
                print("Дальше двигать нельзя.")
            
                
           
        context_menu.add_command(label="Присутствовал", command=redact_item)
        context_menu.add_command(label="Отсутствовал", command=redact_item_2)
    
        return context_menu

    def show_context_menu(event):
       
        selected_item = table_d.identify_row(event.y)
        if selected_item: 
            table_d.selection_set(selected_item)
            context_menu.post(event.x_root, event.y_root)

        else:
            table_d.selection_remove(table_d.selection())
            
    context_menu = create_context_menu(table_d)
    table_d.bind("<Button-3>", show_context_menu)


    frame_redact_2 = ttk.Frame(frame2, style="Custom4.TFrame")
    frame_redact_2.pack(padx=10, pady=10, fill=tk.X)

    combobox_course_2 = ttk.Combobox(frame_redact_2, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_course_2.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)
    
    combobox_fac_2 = ttk.Combobox(frame_redact_2, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_fac_2.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)
    
    combobox_num_2 = ttk.Combobox(frame_redact_2, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_num_2.grid(row=0, column=2, padx=10, pady=10, sticky=tk.EW)
    
    button_sort_group_2 = ttk.Button(frame_redact_2, text="Загрузить список группы", style="CustomButton5.TButton", command=lambda:la.load_att_stud(combobox_course_2, combobox_fac_2, combobox_num_2, combobox_discipline_2, table_d22))
    button_sort_group_2.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

    combobox_discipline_2 = ttk.Combobox(frame_redact_2, style="CustomCombobox6.TCombobox", font=("Arial", 16))
    combobox_discipline_2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    button_save_to_excel = ttk.Button(frame_redact_2, text="Сохранить в файл", style="CustomButton5.TButton", command=lambda:la.upload_result(combobox_course_2, combobox_fac_2, combobox_num_2, combobox_discipline_2))
    button_save_to_excel.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

    frame_data_2 = ttk.Frame(frame2)
    frame_data_2.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    
    columns_22 = ("#", "ID студента", "Фамилия", "Имя", "Отчество", "Дата", "Метка")
    table_d22 = ttk.Treeview(frame_data_2, columns=columns_22, show="headings") #2-05-05 21 апреля в 14:00
    

    table_d22.heading("#", text="#", anchor='w')
    table_d22.heading("ID студента", text="ID студента", anchor='w')
    table_d22.heading("Фамилия", text="Фамилия", anchor='w')
    table_d22.heading("Имя", text="Имя", anchor='w')
    table_d22.heading("Отчество", text="Отчество", anchor='w')
    table_d22.heading("Дата", text="Дата", anchor='w')
    table_d22.heading("Метка", text="Метка", anchor='w')
    table_d22.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    lkr.get_list_kurs(combobox_course_2)
    lkr.get_list_fac(combobox_fac_2)
    lkr.get_list_num(combobox_num_2)
    lkr.get_list_discipline(combobox_discipline_2)
    