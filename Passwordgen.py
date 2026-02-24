import tkinter as tk
from tkinter import messagebox
import string
import secrets

# -------------------- Password Generator Function -------------------- #
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4!")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")
        return

    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase
    if lower_var.get():
        characters += string.ascii_lowercase
    if digit_var.get():
        characters += string.digits
    if symbol_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(secrets.choice(characters) for _ in range(length))
    password_var.set(password)

    check_strength(password)

# -------------------- Strength Checker -------------------- #
def check_strength(password):
    strength = "Weak"
    if len(password) >= 8 and any(c.isupper() for c in password) \
       and any(c.islower() for c in password) \
       and any(c.isdigit() for c in password) \
       and any(c in string.punctuation for c in password):
        strength = "Strong"
    elif len(password) >= 6:
        strength = "Medium"

    strength_label.config(text=f"Strength: {strength}")

# -------------------- Copy to Clipboard -------------------- #
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# -------------------- GUI Setup -------------------- #
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("450x400")
root.config(bg="#2c2c54")

# Variables
password_var = tk.StringVar()
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

# Title
tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"),
         bg="#2c2c54", fg="white").pack(pady=10)

# Length
tk.Label(root, text="Password Length:", bg="#2c2c54",
         fg="white").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Options
tk.Checkbutton(root, text="Include Uppercase", variable=upper_var,
               bg="#2c2c54", fg="white", selectcolor="#3a3a5c").pack()

tk.Checkbutton(root, text="Include Lowercase", variable=lower_var,
               bg="#2c2c54", fg="white", selectcolor="#3a3a5c").pack()

tk.Checkbutton(root, text="Include Digits", variable=digit_var,
               bg="#2c2c54", fg="white", selectcolor="#3a3a5c").pack()

tk.Checkbutton(root, text="Include Symbols", variable=symbol_var,
               bg="#2c2c54", fg="white", selectcolor="#3a3a5c").pack()

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password,
          bg="#00c896", fg="white").pack(pady=10)

# Password Display
tk.Entry(root, textvariable=password_var, width=30,
         font=("Arial", 12)).pack(pady=5)

# Strength Label
strength_label = tk.Label(root, text="Strength: ",
                          bg="#2c2c54", fg="yellow")
strength_label.pack(pady=5)

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_password,
          bg="#706fd3", fg="white").pack(pady=10)

root.mainloop()