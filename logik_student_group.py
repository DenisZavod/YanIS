import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import sqlite3
import pandas as pd
from tkinter import filedialog
from tkinter.messagebox import OK, INFO, showinfo 



def get_list_stud(tree):
        
        for item in tree.get_children():
            tree.delete(item)
        conn=sqlite3.connect("university.db", check_same_thread=False)
        cur=conn.cursor()
        cur.execute("SELECT student.id_student, surname, name, oldname from student left JOIN student_group on student_group.id_student = student.id_student where student_group.id_student is NULL")
        rows = cur.fetchall()

        for row in rows:
            tree.insert("", tk.END, values=row)
            
def load_univ_gr(trv):
    for item in trv.get_children():
        trv.delete(item)
            
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    cur.execute("SELECT * FROM university_group")
    rows = cur.fetchall()
        
    for row in rows:
        trv.insert("", tk.END, values=row)
        
        
def insert_stud_group(id_stud, id_group):
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("INSERT INTO student_group (id_student, id_univ_group) VALUES (?,?)",(id_stud.get(), id_group.get()))
    except Exception as e:
         print(e)
    conn.commit()
    
    showinfo(title="Уведомление АИС", message="Студент успешно добавлен в учебную группу!")
    #id_stud.delete(0, tk.END)
    

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
        
def delete_str(id_str):
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("DELETE FROM student_group WHERE id_str=?",(id_str,))
    except Exception as e:
        print(e)
    conn.commit()

    