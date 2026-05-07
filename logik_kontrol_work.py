import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import sqlite3
import pandas as pd
from tkinter import filedialog
from tkinter.messagebox import OK, INFO, showinfo 



id_disc = 0

id_kr = 0

id_disc_2 = 0

id_kr_sel = 0


def get_list_discipline(cmb):
    conn = sqlite3.connect('university.db')  # укажите путь к своей базе данных
    cursor = conn.cursor()
    cursor.execute("SELECT id_discipline, name_discipline FROM discipline")  # предположим, что у вас есть таблица subjects с полями id и name
    rows = cursor.fetchall()
    conn.close()
    
    disciplines_dict = {row[0]: row[1] for row in rows}
    names_list = list(disciplines_dict.values())
    #print(names_list)
    cmb.config(values=names_list)
    
    
    def show_selected(event):
        global id_disc
        discipline_name = cmb.get()
        discipline_id = next((key for key, value in disciplines_dict.items() if value == discipline_name), None)
        #print(f"Ваша дисциплина: {discipline_name}. Её ID: {discipline_id}")
        id_disc = discipline_id
       #print(id_disc)
    cmb.bind("<<ComboboxSelected>>", show_selected)
    

# def get_list_discipline_for_poisk(cmb, cmb2):
#     conn = sqlite3.connect('university.db')  # укажите путь к своей базе данных
#     cursor = conn.cursor()
#     cursor.execute("SELECT id_discipline, name_discipline FROM discipline")  # предположим, что у вас есть таблица subjects с полями id и name
#     rows = cursor.fetchall()
#     conn.close()
    
#     disciplines_dict = {row[0]: row[1] for row in rows}
#     names_list = list(disciplines_dict.values())
#     #print(names_list)
#     cmb.config(values=names_list)
    
    
#     # def show_selected(event):
#     #     global id_disc
#     #     discipline_name = cmb.get()
#     #     discipline_id = next((key for key, value in disciplines_dict.items() if value == discipline_name), None)
#     #     #print(f"Ваша дисциплина: {discipline_name}. Её ID: {discipline_id}")
#     #     id_disc = discipline_id
#     #     print(id_disc)
        
#     cmb.bind("<<ComboboxSelected>>", selector_kr(cmb , cmb2))
    
    
# def selector_kr(cmb_disc, cmb_kr):
#     conn = sqlite3.connect('university.db')  # укажите путь к своей базе данных
#     cursor = conn.cursor()
#     cursor.execute("SELECT id_control_work, name_control_work FROM control_work LEFT JOIN  discipline on discipline.id_discipline = control_work.id_discipline WHERE name_discipline=?", (cmb_disc.get(),))  # предположим, что у вас есть таблица subjects с полями id и name
#     rows = cursor.fetchall()
#     conn.close()
    
#     print("qwertty" + cmb_disc.get() + "334444444444444")
    
#     kr_dict = {row[0]: row[1] for row in rows}
#     names_list = list(kr_dict.values())
#     cmb_kr.config(values=names_list)
    
    
#     def show_selected(event):
#         global id_kr_sel
#         kr_name = cmb_kr.get()
#         kr_id = next((key for key, value in kr_dict.items() if value == kr_name), None)
#         #print(f"Ваша дисциплина: {discipline_name}. Её ID: {discipline_id}")
#         id_kr_sel = kr_id
#     cmb_kr.bind("<<ComboboxSelected>>", show_selected)
         
def get_list_discipline_for_poisk(cmb, cmb2):
    conn = sqlite3.connect('university.db')  # Подключение к вашей БД
    cursor = conn.cursor()
    cursor.execute("SELECT id_discipline, name_discipline FROM discipline")
    rows = cursor.fetchall()
    conn.close()
    
    disciplines_dict = {row[0]: row[1] for row in rows}
    names_list = list(disciplines_dict.values())
    cmb.config(values=names_list)
    
    # Связываем событие выбора дисциплины с обновлением второго выпадающего списка
    cmb.bind("<<ComboboxSelected>>", lambda event, cmb1=cmb, cmb2=cmb2: selector_kr(cmb1, cmb2))

def selector_kr(cmb_disc, cmb_kr):
    conn = sqlite3.connect('university.db')  # Подключение к вашей БД
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id_control_work, name_control_work "
        "FROM control_work "
        "LEFT JOIN discipline ON discipline.id_discipline = control_work.id_discipline "
        "WHERE name_discipline=?",
        (cmb_disc.get(),)
    )
    rows = cursor.fetchall()
    conn.close()
    
    kr_dict = {row[0]: row[1] for row in rows}
    names_list = list(kr_dict.values())
    cmb_kr.config(values=names_list)
    
    # Присваиваем выбранному элементу id контроля работ
    def show_selected(event):
        global id_kr_sel
        kr_name = cmb_kr.get()
        kr_id = next((key for key, value in kr_dict.items() if value == kr_name), None)
        id_kr_sel = kr_id
    cmb_kr.bind("<<ComboboxSelected>>", show_selected)   
    
def create_kr(name_kr):
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("INSERT INTO control_work (name_control_work, id_discipline) VALUES (?,?)",(name_kr.get(), id_disc))
    except Exception as e:
         print(e)
    conn.commit()
    
    showinfo(title="Уведомление АИС", message="Контрольная работа была успешно загружена в БД!")
    name_kr.delete(0, tk.END)
    
    
def load_kr(trv):
    for item in trv.get_children():
        trv.delete(item)
            
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    cur.execute("SELECT id_control_work, name_control_work, discipline.id_discipline, name_discipline FROM control_work LEFT JOIN discipline on discipline.id_discipline = control_work.id_discipline")
    rows = cur.fetchall()
        
    for row in rows:
        trv.insert("", tk.END, values=row)
        

def update_kr(id_kr, name_kr, id_d, trv):
    
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("UPDATE control_work SET name_control_work=?, id_discipline=? WHERE id_control_work=?",(name_kr.get() , id_d.get() , id_kr.get()))
    except Exception as e:
        print(e)
    conn.commit()
    
    load_kr(trv)
    
def delete_kr(id_kr, trv):
       
        conn=sqlite3.connect("university.db", check_same_thread=False)
        cur=conn.cursor()
        try:
            cur.execute("DELETE FROM control_work WHERE id_control_work=?",(id_kr,))
        except Exception as e:
            print(e)
        conn.commit()
        
        load_kr(trv)


# 3 вкладка

def get_list_kr(cmb):
    conn = sqlite3.connect('university.db')  
    cursor = conn.cursor()
    cursor.execute("SELECT id_control_work, name_control_work FROM control_work") 
    rows = cursor.fetchall()
    conn.close()
    
    kr_dict = {row[0]: row[1] for row in rows}
    names_list = list(kr_dict.values())
    cmb.config(values=names_list)
    
    
    def show_selected(event):
        global id_kr
        kr_name = cmb.get()
        kr_id = next((key for key, value in kr_dict.items() if value == kr_name), None)
        #print(f"Ваша дисциплина: {discipline_name}. Её ID: {discipline_id}")
        id_kr = kr_id
        
    cmb.bind("<<ComboboxSelected>>", show_selected)
    
    
def load_kr_2(kr_cmb, name_d):
    conn = sqlite3.connect('university.db')  
    cursor = conn.cursor()
    cursor.execute("SELECT id_control_work, name_control_work FROM control_work LEFT JOIN discipline on discipline.id_discipline = control_work.id_discipline WHERE discipline.name_discipline=?", (name_d.get(),)) 
    rows = cursor.fetchall()
    conn.close()
    
    disc_dict = {row[0]: row[1] for row in rows}
    names_list = list(disc_dict.values())
    print(names_list)
    kr_cmb.config(values=names_list)
    
    
    def show_selected(event):
        global id_disc_2
        kr_name = kr_cmb.get()
        disc_2_id = next((key for key, value in disc_dict.items() if value == kr_name), None)
        #print(f"Ваша дисциплина: {discipline_name}. Её ID: {discipline_id}")
        id_disc_2 = disc_2_id
        
    kr_cmb.bind("<<ComboboxSelected>>", show_selected)
    

def create_tkr(name_tkr , mark , id_kr):
    print(name_tkr.get())
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("INSERT INTO task (name_task, mark_task, id_control_work) VALUES (?,?,?)",(name_tkr.get() , mark.get() , id_disc_2))
    except Exception as e:
         print(e)
    conn.commit()
    
    showinfo(title="Уведомление АИС", message="Задание было успешно загружено в БД!")
    name_tkr.delete(0, tk.END)
    mark.delete(0, tk.END)
    
    
    # 4 ВКЛАДКА
    
def load_tkr(trv):
    for item in trv.get_children():
        trv.delete(item)
            
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    cur.execute("SELECT id_task, name_task, mark_task, task.id_control_work, name_control_work, name_discipline FROM task LEFT JOIN control_work ON control_work.id_control_work = task.id_control_work LEFT JOIN discipline ON discipline.id_discipline = control_work.id_discipline")
    rows = cur.fetchall()
        
    for row in rows:
        trv.insert("", tk.END, values=row)   


def update_tkr(id_tkr, name_tkr, mark_tkr, id_kr, trv):
    
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("UPDATE task SET name_task=?, mark_task=?, id_control_work=? WHERE id_task=?",(name_tkr.get() , mark_tkr.get() , id_kr.get() , id_tkr.get()))
    except Exception as e:
        print(e)
    conn.commit()
    
    load_tkr(trv)
    
    
def delete_tkr(id_tkr, trv):
       
        conn=sqlite3.connect("university.db", check_same_thread=False)
        cur=conn.cursor()
        try:
            cur.execute("DELETE FROM task WHERE id_task=?",(id_tkr,))
        except Exception as e:
            print(e)
        conn.commit()
        
        load_tkr(trv)
        
        
def load_poisk_tkr(trv, disc, kr):
    for item in trv.get_children():
        trv.delete(item)
            
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    cur.execute("SELECT id_task, name_task, mark_task, task.id_control_work, name_control_work, name_discipline FROM task LEFT JOIN control_work ON control_work.id_control_work = task.id_control_work LEFT JOIN discipline ON discipline.id_discipline = control_work.id_discipline where name_discipline=? AND name_control_work=?", (disc.get(), kr.get()))
    rows = cur.fetchall()
        
    for row in rows:
        trv.insert("", tk.END, values=row)  
        
        
def get_list_kurs(cmb):
    conn = sqlite3.connect('university.db')  
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT course FROM university_group") 
    rows = cursor.fetchall()
    conn.close()
    
    #kurs_dict = {row[0]: row[1] for row in rows}
    names_list = list(rows)
    cmb.config(values=names_list)
    
    
def get_list_fac(cmb):
    conn = sqlite3.connect('university.db')  
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT faculty FROM university_group") 
    rows = cursor.fetchall()
    conn.close()
    
    #kurs_dict = {row[0]: row[1] for row in rows}
    names_list = list(rows)
    cmb.config(values=names_list)
    
    
def get_list_num(cmb):
    conn = sqlite3.connect('university.db')  
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT number FROM university_group") 
    rows = cursor.fetchall()
    conn.close()
    
    #kurs_dict = {row[0]: row[1] for row in rows}
    names_list = list(rows)
    cmb.config(values=names_list)
    
    
    
def load_select_stud(s, n, o, trv):
    
    for item in trv.get_children():
        trv.delete(item)
            
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    cur.execute("select student.id_student, student.surname, student.name, student.oldname, id_str from student_group left join student on student.id_student = student_group.id_student left join university_group on university_group.id_univ_group = student_group.id_univ_group WHERE university_group.course=? AND university_group.faculty=? AND university_group.number=?", (s.get(), n.get(), o.get()))
    rows = cur.fetchall()
        
    for row in rows:
        trv.insert("", tk.END, values=row)
        
def insert_stud_tkr(id_st, id_z):
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("INSERT INTO student_control_work (id_student, id_task) VALUES (?,?)",(id_st.get() , id_z.get()))
    except Exception as e:
         print(e)
    conn.commit()
    
    showinfo(title="Уведомление АИС", message="Задание было успешно отмечено студенту в БД!")
    
    id_z.delete(0, tk.END)
    
def upload_result(k, f, n, d):

    conn = sqlite3.connect('university.db') 
    sql_query =f"""
    SELECT
        surname || ' ' || name || ' ' || oldname AS ФИО_студента,
        cw.name_control_work,
        t.name_task,
        t.mark_task
    FROM
        student s
    JOIN
        student_group sg ON s.id_student = sg.id_student
    JOIN
        university_group ug ON sg.id_univ_group = ug.id_univ_group
    JOIN
        student_control_work scw ON s.id_student = scw.id_student
    JOIN
        task t ON scw.id_task = t.id_task
    JOIN
        control_work cw ON t.id_control_work = cw.id_control_work
    JOIN
        discipline d ON cw.id_discipline = d.id_discipline
    WHERE
        ug.course = '{k.get()}' AND ug.faculty = '{f.get()}' AND ug.number = '{n.get()}' AND d.name_discipline = '{d.get()}';
    """
    
    df = pd.read_sql_query(sql_query, conn)
    conn.close()
    
    df['mark_task'] = pd.to_numeric(df['mark_task'], errors='coerce') 

   
    pivot_table = df.pivot_table(
        index='ФИО_студента',
        columns='name_control_work',
        values='mark_task',
        aggfunc='sum', 
        margins=True,
        margins_name='Итого'
    )


    pivot_table.to_excel("Ведомость-" + k.get() + "-" + f.get() + "-" + n.get() + " " + d.get() +  ".xlsx") 
    
    
def create_treeview_table(root, k, f, n, d):
    
    sql_query =f"""
    SELECT
        surname || ' ' || name || ' ' || oldname AS ФИО_студента,
        cw.name_control_work,
        t.name_task,
        t.mark_task
    FROM
        student s
    JOIN
        student_group sg ON s.id_student = sg.id_student
    JOIN
        university_group ug ON sg.id_univ_group = ug.id_univ_group
    JOIN
        student_control_work scw ON s.id_student = scw.id_student
    JOIN
        task t ON scw.id_task = t.id_task
    JOIN
        control_work cw ON t.id_control_work = cw.id_control_work
    JOIN
        discipline d ON cw.id_discipline = d.id_discipline
    WHERE
        ug.course = '{k.get()}' AND ug.faculty = '{f.get()}' AND ug.number = '{n.get()}' AND d.name_discipline = '{d.get()}';
    """

    try:
        
        conn = sqlite3.connect('university.db')
        df = pd.read_sql_query(sql_query, conn)
        conn.close()

        columns = list(df.columns)

        tree = ttk.Treeview(root, columns=columns, show="headings")

    
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)  

       
        for index, row in df.iterrows():
            values = list(row)  
            tree.insert("", tk.END, values=values)

        
        tree.pack(fill=tk.BOTH, expand=True)

       
        vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side='right', fill='y')
        hsb.pack(side='bottom', fill='x')

    except Exception as e:
        error_label = tk.Label(root, text=f"Ошибка: {e}", fg="red")
        error_label.pack()
