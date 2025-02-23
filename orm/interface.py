import tkinter as tk
import orm
from tkinter import messagebox

root = tk.Tk()
root.title("Movie Manager")

label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_name = tk.Label(root, text="Name:")
label_name.grid(row=1, column=0)
entry_name = tk.Entry(root, width=50)
entry_name.grid(row=1, column=1, padx=10, pady=5)

label_year = tk.Label(root, text="Year:")
label_year.grid(row=2, column=0)
entry_year = tk.Entry(root, width=50)
entry_year.grid(row=2, column=1, padx=10, pady=5)

label_score = tk.Label(root, text="Score:")
label_score.grid(row=3, column=0)
entry_score = tk.Entry(root, width=50)
entry_score.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()
