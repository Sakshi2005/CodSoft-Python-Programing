import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# ---------- DATABASE SETUP ----------
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    due_date TEXT,
    priority TEXT,
    category TEXT,
    status TEXT
)
""")
conn.commit()


# ---------- FUNCTIONS ----------

def add_task():
    title = title_entry.get()
    desc = desc_entry.get()
    due = due_entry.get()
    priority = priority_combo.get()
    category = category_entry.get()

    if title == "":
        messagebox.showwarning("Warning", "Title is required!")
        return

    cursor.execute("INSERT INTO tasks (title, description, due_date, priority, category, status) VALUES (?, ?, ?, ?, ?, ?)",
                   (title, desc, due, priority, category, "Pending"))
    conn.commit()
    clear_fields()
    load_tasks()


def load_tasks():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM tasks")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


def delete_task():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task")
        return

    task_id = tree.item(selected[0])["values"][0]
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    load_tasks()


def mark_complete():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task")
        return

    task_id = tree.item(selected[0])["values"][0]
    cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
    conn.commit()
    load_tasks()


def search_task():
    keyword = search_entry.get()
    cursor.execute("SELECT * FROM tasks WHERE title LIKE ?", ('%' + keyword + '%',))
    results = cursor.fetchall()

    for row in tree.get_children():
        tree.delete(row)

    for row in results:
        tree.insert("", tk.END, values=row)


def clear_fields():
    title_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    priority_combo.set("Medium")


# ---------- UI ----------
root = tk.Tk()
root.title("Advanced To-Do List App")
root.geometry("950x600")
root.configure(bg="#1e1e1e")

# Title
tk.Label(root, text="Smart Task Manager", font=("Arial", 20, "bold"), bg="#1e1e1e", fg="white").pack(pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

# Inputs
tk.Label(frame, text="Title", fg="white", bg="#1e1e1e").grid(row=0, column=0)
title_entry = tk.Entry(frame, width=25)
title_entry.grid(row=0, column=1)

tk.Label(frame, text="Description", fg="white", bg="#1e1e1e").grid(row=1, column=0)
desc_entry = tk.Entry(frame, width=25)
desc_entry.grid(row=1, column=1)

tk.Label(frame, text="Due Date (YYYY-MM-DD)", fg="white", bg="#1e1e1e").grid(row=2, column=0)
due_entry = tk.Entry(frame, width=25)
due_entry.grid(row=2, column=1)

tk.Label(frame, text="Priority", fg="white", bg="#1e1e1e").grid(row=3, column=0)
priority_combo = ttk.Combobox(frame, values=["High", "Medium", "Low"])
priority_combo.set("Medium")
priority_combo.grid(row=3, column=1)

tk.Label(frame, text="Category", fg="white", bg="#1e1e1e").grid(row=4, column=0)
category_entry = tk.Entry(frame, width=25)
category_entry.grid(row=4, column=1)

# Buttons
tk.Button(frame, text="Add Task", command=add_task, bg="#4CAF50", fg="white").grid(row=5, column=0, pady=10)
tk.Button(frame, text="Delete Task", command=delete_task, bg="#f44336", fg="white").grid(row=5, column=1)
tk.Button(frame, text="Mark Complete", command=mark_complete, bg="#2196F3", fg="white").grid(row=6, column=0)

# Search
search_entry = tk.Entry(frame, width=20)
search_entry.grid(row=6, column=1)
tk.Button(frame, text="Search", command=search_task).grid(row=6, column=2)

# Table
columns = ("ID", "Title", "Description", "Due Date", "Priority", "Category", "Status")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(pady=20)

load_tasks()
root.mainloop()