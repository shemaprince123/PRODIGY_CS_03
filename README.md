# PRODIGY_CS_03

---

# Password Complexity Checker

This project provides a graphical user interface (GUI) tool to check the strength of passwords. The tool evaluates passwords based on several criteria such as length, uppercase and lowercase letters, numbers, and special characters. It gives feedback on how strong or weak the password is and provides suggestions to improve the password strength.

---

## Features

- **Password Strength Evaluation**: Checks passwords for multiple criteria like length, uppercase and lowercase letters, numbers, and special characters.
- **Clear Feedback**: Displays password strength along with specific suggestions on how to improve the password if necessary.
- **Simple and User-Friendly**: Easy-to-use GUI that allows users to quickly evaluate their passwords.

---

## Requirements

- Python 3.x
- `tkinter` (for the GUI)
- `re` (for regular expressions)

Tkinter comes pre-installed with Python, so there are no extra dependencies to install. Just make sure Python is properly installed.

---

## How to Use

1. **Run the Program**:
   - Download or clone the project.
   - Open a terminal/command prompt and navigate to the project directory.
   - Run the script with the following command:
     ```bash
     python password_checker_ui.py
     ```

2. **Input Password**:
   - The application will launch a window asking you to enter your password.
   - Type your password into the input box and click "Check Password".

3. **View Results**:
   - A message box will appear showing the strength of your password and suggesting ways to improve it if necessary.

---

## Example Output

When you check a password, the app will display a message like this:

- **Password Strength**: Very Strong  
  *Great job! Your password is strong.*

- **Password Strength**: Weak  
  *Suggestions:*
  - At least 8 characters long
  - Include at least one uppercase letter
  - Include at least one number
  - Include at least one special character (!@#$%^&*)

---

## Screenshots
![image](https://github.com/user-attachments/assets/157a3efb-4a94-41ca-8048-a3e0c5060179)

*Very Weak password*

![image](https://github.com/user-attachments/assets/1084e6eb-891f-4713-9bfa-42b1a814e0a0)

*Very Strong password*

![image](https://github.com/user-attachments/assets/664969cc-59df-47cd-aa84-e7524e2941a7)

---

## Code Explanation

1. **Password Validation**: The code checks the entered password against five criteria using regular expressions (`re` module).
2. **Strength Calculation**: Based on the criteria met, the password is categorized as "Very Strong," "Strong," "Moderate," "Weak," or "Very Weak".
3. **User Interface**: `Tkinter` provides a window where users can input their password and see the results.

---

## License

This project is free to use and modify for educational purposes or personal projects.

---

Thank you for using the Password Complexity Checker!

---
