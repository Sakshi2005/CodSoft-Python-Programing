import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors - Web Style")
root.geometry("600x500")
root.config(bg="#1e1e2f")

# Global Scores
user_score = 0
computer_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

# ---------------- Game Logic ---------------- #
def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    
    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer Choice: {computer_choice}")
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "You Lose! 😢"
        computer_score += 1
        
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score}  |  Computer: {computer_score}")

# ---------------- Reset Game ---------------- #
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    
    user_label.config(text="Your Choice: ")
    computer_label.config(text="Computer Choice: ")
    result_label.config(text="")
    score_label.config(text="Score - You: 0  |  Computer: 0")

# ---------------- UI Design ---------------- #

title = tk.Label(root, text="Rock Paper Scissors Game",
                 font=("Arial", 22, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=20)

instruction = tk.Label(root, text="Choose Rock, Paper, or Scissors",
                       font=("Arial", 14),
                       bg="#1e1e2f", fg="#cfcfcf")
instruction.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="🪨 Rock",
                     font=("Arial", 14),
                     width=12, bg="#4CAF50", fg="white",
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📄 Paper",
                      font=("Arial", 14),
                      width=12, bg="#2196F3", fg="white",
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors",
                         font=("Arial", 14),
                         width=12, bg="#f44336", fg="white",
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Result Display
user_label = tk.Label(root, text="Your Choice: ",
                      font=("Arial", 13),
                      bg="#1e1e2f", fg="white")
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer Choice: ",
                          font=("Arial", 13),
                          bg="#1e1e2f", fg="white")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="",
                        font=("Arial", 16, "bold"),
                        bg="#1e1e2f", fg="#FFD700")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0  |  Computer: 0",
                       font=("Arial", 14),
                       bg="#1e1e2f", fg="#00ffcc")
score_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(root, text="Reset Game",
                      font=("Arial", 12),
                      bg="#555555", fg="white",
                      command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()