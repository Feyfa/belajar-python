import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("500x300")
window.resizable(False, False)
window.title('Jidan App')

# Variable
EMAIL = tk.StringVar()
PASSWORD = tk.StringVar()

# Function
def onClick(): 
    # variable
    email_val = EMAIL.get()
    password_val = PASSWORD.get()
    email_correct = "muhammadjidan@gmail.com"
    password_correct = "123456"
    # variable

    # validation
    if (email_val == '') :
        return showerror(title="Error", message="Nama Depan Is Required")
    if (password_val == '') :
        return showerror(title="Error", message="Nama Belakang Is Required")
    if (email_val != email_correct or password_val != password_correct) :
        return showerror(title="Error", message="Email Atau Password Anda Salah")

    showinfo(title="Success", message="Selamat Anda Berhasil Login")
    # validation

# iframe input
input_iframe = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_iframe.pack(
    padx=10,
    pady=10,
    fill="x",
)

# component
# 1. Label email
email_label = ttk.Label(input_iframe, text="Email")
email_label.pack(
    padx=5,
    fill="x",
    expand=True
)
# 2. entry email
email_entry = ttk.Entry(input_iframe, textvariable=EMAIL)
email_entry.pack(
    padx=5,
    pady=5,
    fill="x",
    expand=True,
    ipady=2
)
# 3. Label password
password_label = ttk.Label(input_iframe, text="Password")
password_label.pack(
    padx=5,
    fill="x",
    expand=True
)
# 4. entry password
password_entry = ttk.Entry(input_iframe, textvariable=PASSWORD)
password_entry.pack(
    padx=5,
    pady=5,
    fill="x",
    expand=True,
    ipady=2
)
# 5 Button
button_sapa = ttk.Button(input_iframe, text="Sapa!", command=onClick)
button_sapa.bind("<Return>", lambda e: onClick()) # untuk event ketika button di enter
button_sapa.pack(
    padx=5,
    pady=10,
    fill="x",
    expand=True
)

window.mainloop()