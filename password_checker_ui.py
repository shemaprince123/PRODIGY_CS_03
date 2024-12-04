import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def password_strength_checker(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Calculate strength score
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    # Determine strength level
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Collect feedback
    feedback = []
    if not length_criteria:
        feedback.append("At least 8 characters long")
    if not uppercase_criteria:
        feedback.append("Include at least one uppercase letter")
    if not lowercase_criteria:
        feedback.append("Include at least one lowercase letter")
    if not number_criteria:
        feedback.append("Include at least one number")
    if not special_char_criteria:
        feedback.append("Include at least one special character (!@#$%^&*)")
    
    return strength, feedback

# Function to display results
def check_password():
    password = entry_password.get()
    strength, feedback = password_strength_checker(password)
    
    # Display results in a message box
    result = f"Password Strength: {strength}\n"
    if feedback:
        result += "\nSuggestions:\n" + "\n".join([f"- {tip}" for tip in feedback])
    else:
        result += "\nGreat job! Your password is strong."
    
    messagebox.showinfo("Password Strength Result", result)

# UI Setup
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x200")

# Label
label_instruction = tk.Label(root, text="Enter your password:", font=("Arial", 14))
label_instruction.pack(pady=10)

# Entry widget for password input
entry_password = tk.Entry(root, show="*", font=("Arial", 14), width=25)
entry_password.pack(pady=5)

# Button to check password
button_check = tk.Button(root, text="Check Password", command=check_password, font=("Arial", 12), bg="#4CAF50", fg="white")
button_check.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()


#run python password_checker_ui.py
