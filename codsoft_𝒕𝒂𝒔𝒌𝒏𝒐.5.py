import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()

# Add Contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        save_contacts(contacts)
        messagebox.showinfo("Success", "Contact Added Successfully!")
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Error", "Name and Phone are required!")

# View Contacts
def view_contacts():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Search Contact
def search_contact():
    query = search_entry.get().lower()
    listbox.delete(0, tk.END)
    for contact in contacts:
        if query in contact["name"].lower() or query in contact["phone"]:
            listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Delete Contact
def delete_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del contacts[index]
        save_contacts(contacts)
        view_contacts()
        messagebox.showinfo("Deleted", "Contact Deleted Successfully!")

# Update Contact
def update_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contacts[index] = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }
        save_contacts(contacts)
        view_contacts()
        messagebox.showinfo("Updated", "Contact Updated Successfully!")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Advanced Contact Book")
root.geometry("600x600")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

tk.Label(root, text="Search").pack()
search_entry = tk.Entry(root, width=40)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)

listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

view_contacts()

root.mainloop()