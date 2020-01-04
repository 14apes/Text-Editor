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
edit = tk.Menu(main_menu,tearoff = False)
view = tk.Menu(main_menu,tearoff =False)
theme= tk.Menu(main_menu,tearoff = False)

main_menu.add_cascade(label = "File", menu = file)
main_menu.add_cascade(label = "Edit", menu = edit)
main_menu.add_cascade(label = "View", menu = view)
main_menu.add_cascade(label = "Theme", menu = theme)

view.add_command(label = "Copy",compound = tk.LEFT,accelerator = "ctrl+C")
view.add_command(label = "Cut",compound = tk.LEFT,accelerator = "ctrl+X")
view.add_command(label = "Paste",compound = tk.LEFT,accelerator = "ctrl+V")
view.add_command(label = "Replace",compound = tk.LEFT,accelerator = "ctrl+H")
view.add_command(label = "Find",compound = tk.LEFT,accelerator = "ctrl+F")


file.add_command(label = "New",compound = tk.LEFT,accelerator = "ctrl+N")
file.add_command(label = "Open",compound = tk.LEFT,accelerator = "ctrl+O")
file.add_command(label = "Save",compound = tk.LEFT,accelerator = "ctrl+S")
file.add_command(label = "Save As",compound = tk.LEFT,accelerator = "ctrl+shift+s")
file.add_command(label = "Exit",compound = tk.LEFT,accelerator = "ctrl+Q")

edit.add_command(label = "Copy",compound = tk.LEFT,accelerator = "ctrl+C")
edit.add_command(label = "Cut",compound = tk.LEFT,accelerator = "ctrl+X")
edit.add_command(label = "Paste",compound = tk.LEFT,accelerator = "ctrl+V")
edit.add_command(label = "Replace",compound = tk.LEFT,accelerator = "ctrl+H")
edit.add_command(label = "Find",compound = tk.LEFT,accelerator = "ctrl+F")


file.add_command(label = "New",compound = tk.LEFT,accelerator = "ctrl+N")
file.add_command(label = "Open",compound = tk.LEFT,accelerator = "ctrl+O")
file.add_command(label = "Save",compound = tk.LEFT,accelerator = "ctrl+S")
file.add_command(label = "Save As",compound = tk.LEFT,accelerator = "ctrl+shift+s")
file.add_command(label = "Exit",compound = tk.LEFT,accelerator = "ctrl+Q")



nuclear.config(menu = main_menu)
 
nuclear.mainloop()