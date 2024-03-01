import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

button = tk.Button(text="This is a button.")
button.pack()

entry = tk.Entry(text="This is an entry.")
entry.pack()

window.mainloop()