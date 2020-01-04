import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

nuclear=tk.Tk()
nuclear.geometry("500x400")
nuclear.title("nuclear")  

main_menu = tk.Menu()

#new_icon = tk.PhotoImage(file = "new.png")
#openn = tk.PhotoImage(load = "")
#save = tk.PhotoImage(load = "save.png")
#save_as = tk.PhotoImage(load = "")
#exit = tk.PhotoImage(load = "exit.png")

file = tk.Menu(main_menu,tearoff =False)
main_menu.add_cascade(label = "File", menu = file)

file.add_command(label = "New",compound = tk.LEFT,accelerator = "ctrl+N")
file.add_command(label = "Open",compound = tk.LEFT,accelerator = "ctrl+O")
file.add_command(label = "Save",compound = tk.LEFT,accelerator = "ctrl+S")
file.add_command(label = "Save As",compound = tk.LEFT,accelerator = "ctrl+shift+s")
file.add_command(label = "Exit",compound = tk.LEFT,accelerator = "ctrl+Q")



nuclear.config(menu = main_menu)
 
nuclear.mainloop()