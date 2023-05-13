import tkinter as tk

def button_clicked():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Simple GUI Application")
root.geometry("300x100")

label = tk.Label(root, text="Welcome to Tkinter!")
label.pack(pady=10)

button = tk.Button(root, text="Click Me!", command=button_clicked)
button.pack(pady=5)

root.mainloop()