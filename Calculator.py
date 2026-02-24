import tkinter as tk
from tkinter import messagebox
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Tkinter Calculator")
        self.root.geometry("420x550")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        self.entry = tk.Entry(self.root, font=("Arial", 22),
                              bd=10, relief=tk.RIDGE, justify="right")
        self.entry.grid(row=0, column=0, columnspan=5, pady=20, padx=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('√', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('x²', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('%', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('(', 4, 2), (')', 4, 3), ('+', 4, 4),
            ('C', 5, 0), ('⌫', 5, 1), ('^', 5, 2)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, font=("Arial", 14),
                            width=5, height=2,
                            command=lambda t=text: self.on_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

        equal_btn = tk.Button(self.root, text="=", font=("Arial", 16),
                              width=25, height=2,
                              bg="#4CAF50", fg="white",
                              command=self.calculate)
        equal_btn.grid(row=6, column=0, columnspan=5, pady=15)

    def on_click(self, value):
        if value == "C":
            self.entry.delete(0, tk.END)

        elif value == "⌫":
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current[:-1])

        elif value == "√":
            try:
                number = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.sqrt(number))
            except:
                messagebox.showerror("Error", "Invalid Input")

        elif value == "x²":
            try:
                number = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, number ** 2)
            except:
                messagebox.showerror("Error", "Invalid Input")

        elif value == "^":
            self.entry.insert(tk.END, "**")

        else:
            self.entry.insert(tk.END, value)

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)

        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero not allowed!")
        except:
            messagebox.showerror("Error", "Invalid Expression")


if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()