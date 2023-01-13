import tkinter as tk
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('todolist.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS todo_list (task text, due_date text, status text)")
    conn.commit()

create_table()

def add_item():
    task = task_entry.get()
    due_date = date_entry.get()
    status = status_entry.get()
    c.execute("INSERT INTO todo_list (task, due_date, status) VALUES (?, ?, ?)",(task, due_date, status))
    conn.commit()
    task_entry.delete(0,tk.END)
    date_entry.delete(0,tk.END)
    status_entry.delete(0,tk.END)
    view_list()

def view_list():
    c.execute("SELECT * FROM todo_list WHERE status='incomplete'")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.execute("SELECT * FROM todo_list WHERE status='complete'")
    rows = c.fetchall()
    for row in rows:
        print(row)

def update_status():
    task = task_entry.get()
    status = status_entry.get()
    c.execute("UPDATE todo_list SET status = ? WHERE task = ?", (status, task))
    conn.commit()
    task_entry.delete(0,tk.END)
    date_entry.delete(0,tk.END)
    status_entry.delete(0,tk.END)
    view_list()

def delete_item():
    task = task_entry.get()
    c.execute("DELETE from todo_list WHERE task = ?", (task,))
    conn.commit()
    task_entry.delete(0,tk.END)
    date_entry.delete(0,tk.END)
    status_entry.delete(0,tk.END)
    view_list()

def search_list():
    query = search_entry.get()
    c.execute("SELECT * FROM todo_list WHERE task like ? OR due_date like ? OR status like ?", ('%'+query+'%', '%'+query+'%','%'+query+'%'))
    rows = c.fetchall()
    for row in rows:
        print(row)
    search_entry.delete(0,tk.END)

root = tk.Tk()
root.title("To-Do List")

task_label = ttk.Label(root, text="Task:")
task_label.grid(row=0, column=0)

task_entry = ttk.Entry(root)
task_entry.grid(row=0, column=1)

date_label = ttk.Label(root, text="Date:")
date_label.grid(row=1, column=0)

date_entry = ttk.Entry(root)
date_entry.grid(row=1, column=1)

status_label = ttk.Label(root, text="Status:")
status_label.grid(row=2, column=0)

status_entry = ttk.Entry(root)
status_entry.grid(row=2, column=1)

add_button = ttk.Button(root, text="Add", command=add_item)
add_button.grid(row=3, column=0, pady=10)

update_button = ttk.Button(root, text="Update", command=update_status)
update_button.grid(row=3, column=1)

delete_button = ttk.Button(root, text="Delete", command=delete_item)
delete_button.grid(row=3, column=2)

search_label = ttk.Label(root, text="Search:")
search_label.grid(row=4, column=0)

search_entry = ttk.Entry(root)
search_entry.grid(row=4, column=1)

search_button = ttk.Button(root, text="Search", command=search_list)
search_button.grid(row=4, column=2)

root.mainloop()

