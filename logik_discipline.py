import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import sqlite3
import pandas as pd
from tkinter import filedialog
from tkinter.messagebox import OK, INFO, showinfo 

def create_disc(name_disc):
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("INSERT INTO discipline (name_discipline) VALUES (?)",(name_disc.get(),))
    except Exception as e:
         print(e)
    conn.commit()
    
    showinfo(title="Уведомление АИС", message="Дисциплина была успешно загружена в БД!")
    name_disc.delete(0, tk.END)
    
def load_disc(trv):
    for item in trv.get_children():
        trv.delete(item)
            
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    cur.execute("SELECT * FROM discipline")
    rows = cur.fetchall()
        
    for row in rows:
        trv.insert("", tk.END, values=row)
        
        
def update_disc(id_d, name_d, trv):
    print(name_d.get())
    
    conn=sqlite3.connect("university.db", check_same_thread=False)
    cur=conn.cursor()
    try:
        cur.execute("UPDATE discipline SET name_discipline=? WHERE id_discipline=?",(name_d.get(), id_d.get()))
    except Exception as e:
        print(e)
    conn.commit()
    
    load_disc(trv)
    
def delete_disc(id_d, trv):
       
        conn=sqlite3.connect("university.db", check_same_thread=False)
        cur=conn.cursor()
        try:
            cur.execute("DELETE FROM discipline WHERE id_discipline=?",(id_d,))
        except Exception as e:
            print(e)
        conn.commit()
        
        load_disc(trv)
            
