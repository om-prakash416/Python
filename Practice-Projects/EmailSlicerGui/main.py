import tkinter as tk
from tkinter import messagebox


def slice_email():

    email = email_entry.get().strip()

    try:

        username, domain = email.split('@')

        result_label.config(text=f"Username: {username}\nDomain: {domain}")
    except ValueError:

        messagebox.showerror("Invalid Email", "Please enter a valid email address containing '@'.")


# Create the main Tkinter window
root = tk.Tk()
root.title("Email Slicer")
root.geometry("400x400")
root.configure(bg='#f0f8ff')
root.resizable(False, False)


custom_font = ("Arial", 12, "bold")


title_label = tk.Label(root, text="Email Slicer", font=("Helvetica", 20, "bold"), bg='#4682b4', fg='white',
                       relief="ridge", padx=10, pady=5)
title_label.pack(pady=10)


email_label = tk.Label(root, text="Enter your email address:", font=custom_font, bg='#f0f8ff', fg='#2f4f4f')
email_label.pack(pady=5)

email_entry = tk.Entry(root, font=("Arial", 14), width=30, relief="sunken", bd=3)
email_entry.pack(pady=5)


slice_button = tk.Button(
    root, text="Slice Email", font=("Arial", 12, "bold"), bg='#4682b4' , fg='white', relief="raised", borderwidth=3,
    activebackground='#5f9ea0', activeforeground='white' ,command=slice_email
)
slice_button.pack(pady=15)


result_label = tk.Label(root, text="", font=("Arial", 14), fg="#4b0082", bg='#f0f8ff', relief="solid", padx=10, pady=5)
result_label.pack(pady=10)


footer_label = tk.Label(root, text="Designed by OP_YDV", font=("Arial", 10), bg='yellow', fg='#2f4f4f')
footer_label.pack(side="bottom", pady=10)


root.mainloop()
