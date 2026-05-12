import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import sqlite3
import pandas as pd
from tkinter import filedialog
from tkinter.messagebox import OK, INFO, showinfo 
import discipline_window
import university_group_window
import kontrol_work_window
import student_group_window
import attendance_window
import git_update_window



def poisk_student(trv, pe):
        for item in trv.get_children():
            trv.delete(item)
            
        conn=sqlite3.connect("university.db", check_same_thread=False)
        cur=conn.cursor()
        cur.execute("SELECT * FROM student WHERE surname LIKE ?", (pe.get() + '%',))
        #cur.execute("DELETE FROM student WHERE id_student=?",(id_st,))
        rows = cur.fetchall()

        # 4. Вставляем данные в Treeview
        for row in rows:
            trv.insert("", tk.END, values=row)

def create_student_window(): 
    
    student_window = tk.Toplevel(root)  
    student_window.title("Работа со студентами")
    student_window.geometry("700x600")
    student_window.configure(bg="#FF8C00")  


    # Create Notebook
    notebook = ttk.Notebook(student_window)
    notebook.pack(expand=True, fill=tk.BOTH)

    style.configure(
        "Custom.TFrame",
        background="#7FFFD4"
        )

    # Create frames
    frame1 = ttk.Frame(notebook, style="Custom.TFrame")
    frame2 = ttk.Frame(notebook, style="Custom.TFrame")

    # Add frames as tabs
    notebook.add(frame1, text="Добавить нового студента")
    notebook.add(frame2, text="Работа со списком студентов")

    style.configure(
        "Custom.TLabel",
        background="#7FFFD4",
        foreground="black",
        font=("Arial", 16)
        )

    # Content inside frames (example)
    label1 = ttk.Label(frame1, text="Добавить нового студента", style='Custom.TLabel') 
    label1.pack(padx=5, pady=20, anchor="w")

    label2 = ttk.Label(frame1, text="Введите фамилию", style='Custom.TLabel') 
    label2.pack(padx=5, pady=20, anchor="w")

    style.configure(
        "Custom.TEntry",
        foreground = 'red'
        )

    surname_entry = ttk.Entry(frame1, width=30, font=("Arial", 16), style='Custom.TEntry')
    surname_entry.pack(padx=5, anchor="w")
    

    

    label3 = ttk.Label(frame1, text="Введите имя", style='Custom.TLabel') 
    label3.pack(padx=5, pady=20, anchor="w")


    name_entry = ttk.Entry(frame1, width=30, font=("Arial", 16), style='Custom.TEntry')
    name_entry.pack(padx=5, anchor="w")

    label4 = ttk.Label(frame1, text="Введите отчество", style='Custom.TLabel') 
    label4.pack(padx=5, pady=20, anchor="w")

    

    oldname_entry = ttk.Entry(frame1, width=30, font=("Arial", 16), style='Custom.TEntry')
    oldname_entry.pack(padx=5, anchor="w")
    
    style2 = ttk.Style()
    style2.configure(
    "CustomButton2.TButton",
    background="#FF8C00",
    foreground="white",
    relief="flat",
    borderwidth=0,
    
)
    
    style2.map(
    "CustomButton2.TButton",
    background=[("active", "#B22222")],  # Новый цвет при наведении
)
    

    
    def add_stud():
        conn=sqlite3.connect("university.db", check_same_thread=False)
        cur=conn.cursor()
        try:
            cur.execute("INSERT INTO student (surname, name, oldname) VALUES (?, ?, ?)",(surname_entry.get(), name_entry.get(), oldname_entry.get()))
        except Exception as e:
            print(e)
        conn.commit()
        
        showinfo(title="Уведомление АИС", message="Студент был успешно загружен в БД!")
        surname_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        oldname_entry.delete(0, tk.END)
        
    def add_stud_from_file():
        filepath = filedialog.askopenfilename()
        label_file.config(text=filepath)
        df = pd.read_csv(filepath , delimiter=',')
       #print(df["ФИО"])
        list_stud = list(df["ФИО"])
        print(list_stud)
        for i in list_stud:
            fio_stud = i.split()
            conn=sqlite3.connect("university.db", check_same_thread=False)
            cur=conn.cursor()
            try:
                cur.execute("INSERT INTO student (surname, name, oldname) VALUES (?, ?, ?)",(fio_stud[0] , fio_stud[1], fio_stud[2]))
            except Exception as e:
                 print(e)
            conn.commit()
        showinfo(title="Уведомление АИС", message="Список студентов был успешно загружен в БД!")
            #print(fio_stud)
            
    def get_list_stud():
        
        for item in tree.get_children():
            tree.delete(item)
        conn=sqlite3.connect("university.db", check_same_thread=False)
        cur=conn.cursor()
        cur.execute(f"SELECT * FROM student")
        rows = cur.fetchall()

        # 4. Вставляем данные в Treeview
        for row in rows:
            tree.insert("", tk.END, values=row)
            
    def update_stud():
        conn=sqlite3.connect("university.db", check_same_thread=False)
        cur=conn.cursor()
        try:
            cur.execute("UPDATE student SET surname=?, name=?, oldname=? WHERE id_student=?",(s_entry.get(), n_entry.get(), on_entry.get(), id_entry.get()))
        except Exception as e:
            print(e)
        conn.commit()
        
    def delete_stud(id_st):
        print(id_st)
        conn=sqlite3.connect("university.db", check_same_thread=False)
        cur=conn.cursor()
        try:
            cur.execute("DELETE FROM student WHERE id_student=?",(id_st,))
        except Exception as e:
            print(e)
        conn.commit()
            
    
        

    button_add = ttk.Button(frame1, text="Добавить студента в БД", width=59, style='CustomButton2.TButton', command=add_stud)
    button_add.pack(padx=5, pady=20, anchor="w")

    button_file = ttk.Button(frame1, text="Добавить список из файла", width=59, style='CustomButton2.TButton', command=add_stud_from_file)
    button_file.pack(padx=5, pady=20, anchor="w")
    
    label_file = ttk.Label(frame1)
    label_file.pack(padx=5, pady=20, anchor="w")
    
    
    #здесь пишем второй фрейм
    
    style3 = ttk.Style()
    style3.configure(
        "Custom3.TFrame",
        height=120,
        background="#FF8C00"
    )
    
    style4 = ttk.Style()
    style4.configure(
    "CustomButton4.TButton",
    background="#FF8C00",
    foreground="white",
    relief="raised",
    borderwidth=1,
    
)
    
    style4.map(
    "CustomButton4.TButton",
    background=[("active", "#B22222")],  # Новый цвет при наведении
)
    
    frame3 = ttk.Frame(frame2, style='Custom3.TFrame')
    frame3.pack(padx=5, pady=5, fill=tk.X)
    
    poisk_entry = ttk.Entry(frame3, width=30, font=("Arial", 16), style='Custom.TEntry')
    poisk_entry.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)
    
    button_poisk = ttk.Button(frame3 , style='CustomButton4.TButton', text='Поиск по фамилии', command=lambda: poisk_student(tree , poisk_entry))
    button_poisk.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)
    
    button_load_data = ttk.Button(frame3, style='CustomButton4.TButton', text='Загрузить список студентов', command = get_list_stud)
    button_load_data.grid(row=0, column=2, padx=10, pady=10, sticky=tk.EW)
    
    id_entry = ttk.Entry(frame3, width=10, font=("Arial", 16), style='Custom.TEntry')
    id_entry.grid(row=1, column=0, padx=10, pady=10, sticky=tk.EW)
    
    s_entry = ttk.Entry(frame3, width=15, font=("Arial", 16), style='Custom.TEntry')
    s_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)
    
    n_entry = ttk.Entry(frame3, width=15, font=("Arial", 16), style='Custom.TEntry')
    n_entry.grid(row=1, column=2, padx=10, pady=10, sticky=tk.EW)
    
    on_entry = ttk.Entry(frame3, width=15, font=("Arial", 16), style='Custom.TEntry')
    on_entry.grid(row=1, column=3, padx=10, pady=10, sticky=tk.EW)
    
    button_update_data = ttk.Button(frame3, style='CustomButton4.TButton', text='Изменить данные', command = update_stud)
    button_update_data.grid(row=1, column=4, padx=10, pady=10, sticky=tk.EW)
    
    
    frame4 = ttk.Frame(frame2 , style='Custom3.TFrame')
    frame4.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)
    
    columns = ("ID", "Фамилия", "Имя", "Отчество")
    tree = ttk.Treeview(frame4, columns=columns, show="headings")  # Создаем Treeview
    tree.heading("ID", text="ID", anchor='w')
    tree.heading("Фамилия", text="Фамилия", anchor='w')
    tree.heading("Имя", text="Имя", anchor='w')
    tree.heading("Отчество", text="Отчество", anchor='w')
    tree.pack(expand=True, fill=tk.BOTH)
    
    
    
    def create_context_menu(tree):
    
        context_menu = tk.Menu(tree, tearoff=0)

        def redact_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] # Если выделено несколько, берем первый. Если только один - все равно работает
            values = tree.item(selected_item, 'values')  # Получаем значения из столбцов
            print(values[0])
            id_entry.delete(0, tk.END)
            id_entry.insert(0, values[0])
            
            s_entry.delete(0, tk.END)
            s_entry.insert(0, values[1])
            
            n_entry.delete(0, tk.END)
            n_entry.insert(0, values[2])
            
            on_entry.delete(0, tk.END)
            on_entry.insert(0, values[3])
            
            

        def delete_item():
            selected_item = tree.selection()
            selected_item = selected_item[0] # Если выделено несколько, берем первый. Если только один - все равно работает
            values = tree.item(selected_item, 'values')  # Получаем значения из столбцов
            id_stud = values[0]
            #print(values[0])
            delete_stud(int(id_stud))
        context_menu.add_command(label="Редактировать запись", command=redact_item)
        context_menu.add_command(label="Удалить запись", command=delete_item)

        return context_menu

    def show_context_menu(event):
       
        selected_item = tree.identify_row(event.y)  # Определяем, над какой строкой кликнули
        if selected_item: # проверяем что кликнули над елементом
            tree.selection_set(selected_item) # выделяем строку
            context_menu.post(event.x_root, event.y_root)

        else:
            # Если щелкнуто вне элементов Treeview, снимаем выделение
            tree.selection_remove(tree.selection())
            
    context_menu = create_context_menu(tree)
    tree.bind("<Button-3>", show_context_menu)
    
    

def button1_clicked():
    print("Кнопка 1 была нажата!")
    create_student_window()

def button2_clicked():
    #print("Кнопка 2 была нажата!")
    student_group_window.create_student_group_window(root)

def button3_clicked():
    print("Кнопка 3 была нажата!")
    university_group_window.create_university_group(root)

def button4_clicked():
    print("Кнопка 4 была нажата!")
    kontrol_work_window.create_kontrol_work(root)

def button5_clicked():
    print("Кнопка 5 была нажата!")
    attendance_window.create_attendance(root)

def button6_clicked():
    print("Кнопка 6 была нажата!")
    discipline_window.create_discipline_window(root)
    
def button7_clicked():
    print("Кнопка 7 была нажата!")
    git_update_window.create_git_update_window(root)
    
def add_stud():
    st_dt = create_student_window()
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("INSERT INTO student (surname, name, oldname) VALUES (?, ?, ?)",(st_dt[0], st_dt[1], st_dt[2]))
    except Exception as e:
        print(e)
    conn.commit()
    



root = ThemedTk(theme="clam") #  Root window must be a ThemedTk window to apply themes.
root.geometry("700x500")
root.title("Информационная система успеваемости и посещаемости студентов")
root.resizable(False, False)
root.configure(bg="#7FFFD4")

style = ttk.Style()
style.theme_use("clam") #Important to initialize this after themedTk. Root must be ThemedTk

icon_image = tk.PhotoImage(file="stud_icon.png")  #tk.PhotoImage, not PhotoImage. Also, using relative paths for images won't work unless the program is packaged.
icon_image_2 = tk.PhotoImage(file="stud_group.png")
icon_image_3 = tk.PhotoImage(file="learning_group.png")
icon_image_4 = tk.PhotoImage(file="control_work.png")
icon_image_5 = tk.PhotoImage(file="attendance.png")
icon_image_6 = tk.PhotoImage(file="discipline.png")
icon_image_7 = tk.PhotoImage(file="git.png")


style.configure(
    "CustomButton.TButton",
    background="#FF8C00",
    foreground="white",
    relief="flat",
    borderwidth=0,
    padding=(20, 40),
    font=("Arial", 18, "bold")
)



style.map(
    "CustomButton.TButton",
    background=[("active", "#B22222")],  # Новый цвет при наведении
)

# Создаем кнопки (стиль ttk)
button1 = ttk.Button(root, text="Студенты", command=button1_clicked, style="CustomButton.TButton", image=icon_image, compound="left")
button2 = ttk.Button(root, text="Студенческие группы", command=button2_clicked, style="CustomButton.TButton", image=icon_image_2, compound="left")
button3 = ttk.Button(root, text="Учебные группы", command=button3_clicked, style="CustomButton.TButton", image=icon_image_3, compound="left")
button4 = ttk.Button(root, text="Контрольные работы", command=button4_clicked, style="CustomButton.TButton", image=icon_image_4, compound="left")
button5 = ttk.Button(root, text="Посещаемость", command=button5_clicked, style="CustomButton.TButton", image=icon_image_5, compound="left")
button6 = ttk.Button(root, text="Дисциплины", command=button6_clicked, style="CustomButton.TButton", image=icon_image_6, compound="left")
button7 = ttk.Button(root, text="Обновления", command=button7_clicked, style="CustomButton.TButton", image=icon_image_7, compound="left")

# Размещаем кнопки с помощью grid
button1.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
button2.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
button3.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
button4.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
button5.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
button6.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
button7.grid(row=3, column=0, padx=5, pady=5, sticky="ew")


# Конфигурация для масштабирования при изменении размера окна
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=0)



root.mainloop()
