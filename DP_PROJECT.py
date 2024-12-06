import tkinter as tk
from tkinter import messagebox
import csv
import os

# Get the current directory where the script is running
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, "students_visual_studio.csv")

# Load data from the CSV file
def load_data():
    data = []
    try:
        with open(csv_file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        messagebox.showerror("Error", f"Data file not found! Ensure '{csv_file_path}' is in the correct location.")
    return data

# Fetch student data by School ID
def get_student_data(school_id):
    data = load_data()
    for student in data:
        if student["SchoolID"] == school_id:
            return student
    return None

# Handle "Submit" button click
def submit_action():
    school_id = entry_id.get().strip()
    if not school_id:
        messagebox.showwarning("Input Error", "Please enter a School ID.")
        return

    student = get_student_data(school_id)
    if student:
        student_info = (
            f"Student: {student['Name']}\n"
            f"Grade: {student['Grade']}\n"
            f"Status: {student['Status']}\n"
            f"Disciplinary Points (DP): {student['DP']}\n"
            f"Reason: {student['Reason']}"
        )
        messagebox.showinfo("Discipline Record", student_info)
    else:
        messagebox.showerror("Error", "No data found for the entered School ID. Please try again.")

# Clear the input field for new input
def clear_input():
    entry_id.delete(0, tk.END)

# Exit the application
def exit_action():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Discipline Tracker Pro")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Welcome Screen UI
tk.Label(root, text="Discipline Tracker Pro", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)
tk.Label(root, text="Enter the School ID to view the student's discipline record.", bg="#f0f0f0").pack(pady=5)

entry_id = tk.Entry(root, width=30)
entry_id.pack(pady=10)

# Buttons for Submit, Clear, and Exit actions
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Submit", command=submit_action, width=10).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Clear", command=clear_input, width=10).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Exit", command=exit_action, width=10).grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()

