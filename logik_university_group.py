import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import sqlite3
import pandas as pd
from tkinter import filedialog
from tkinter.messagebox import OK, INFO, showinfo 

def create_univ_group(kurs, fac, num):
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("INSERT INTO university_group (course, faculty, number) VALUES (?,?,?)",(kurs.get(), fac.get(), num.get()))
    except Exception as e:
         print(e)
    conn.commit()
    
    showinfo(title="Уведомление АИС", message="Группа была успешно загружена в БД!")
    kurs.delete(0, tk.END)
    fac.delete(0, tk.END)
    num.delete(0, tk.END)
    

def load_univ_gr(trv):
    for item in trv.get_children():
        trv.delete(item)
            
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    cur.execute("SELECT * FROM university_group")
    rows = cur.fetchall()
        
    for row in rows:
        trv.insert("", tk.END, values=row)


def update_univ_gr(kurs, fac, gr, id_un, trv):
    
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("UPDATE university_group SET course=?, faculty=?, number=? WHERE id_univ_group=?",(kurs.get(), fac.get(), gr.get(), id_un.get()))
    except Exception as e:
        print(e)
    conn.commit()
    
    load_univ_gr(trv)
    
def delete_univ_gr(id_un, trv):
       
        conn=sqlite3.connect("university.db", check_same_thread=False)
        cur=conn.cursor()
        try:
            cur.execute("DELETE FROM university_group WHERE id_univ_group=?",(id_un,))
        except Exception as e:
            print(e)
        conn.commit()
        
        load_univ_gr(trv)