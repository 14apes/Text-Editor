import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

nuclear=tk.Tk()
nuclear.geometry("500x400")
nuclear.title("nuclear")  

main_menu = tk.Menu()

new_icon = tk.PhotoImage(file = "new.png")
openn = tk.PhotoImage(file = "open.png")
save = tk.PhotoImage(file = "save.png")
save_as = tk.PhotoImage(file = "save as.png")
exit = tk.PhotoImage(file = "exit.png")

file = tk.Menu(main_menu,tearoff =False)

copy = tk.PhotoImage(file = "copy.png")
cut = tk.PhotoImage(file = "cut.png")
paste = tk.PhotoImage(file = "paste.png")
replace = tk.PhotoImage(file = "replace.png")
find = tk.PhotoImage(file = "find.png")


edit = tk.Menu(main_menu,tearoff = False)

tool = tk.PhotoImage(file = "tool.png")
status = tk.PhotoImage(file = "status.png")

view = tk.Menu(main_menu,tearoff =False)

light_theme = tk.PhotoImage(file = "light_default.png")
light_plus_icon= tk.PhotoImage(file = "light_plus.png")
dark_theme = tk.PhotoImage(file = "dark.png")
red_theme = tk.PhotoImage(file = "red.png")
monokia_theme = tk.PhotoImage(file = "monokai.png")
night_theme = tk.PhotoImage(file = "night_blue.png")


theme= tk.Menu(main_menu,tearoff = False)

theme_select = tk.StringVar()

color_icons=(light_plus_icon,light_theme,dark_theme,red_theme,monokia_theme,night_theme)

color_dict = {
    'Light Default ' : ('#000000',"#ffffff"),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' :  ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}


main_menu.add_cascade(label = "File", menu = file)
main_menu.add_cascade(label = "Edit", menu = edit)
main_menu.add_cascade(label = "View", menu = view)
main_menu.add_cascade(label = "Theme", menu = theme)
###understand prop from here
tool_bar_label = ttk.Label(nuclear)
tool_bar_label.pack(side = tk.TOP,fill = tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar_label,width = 30,textvariable = font_family,state = "readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Meera"))
font_box.grid(row = 0,column = 0,padx = 5,pady = 5)

size_variable  = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label,width = 20,textvariable = size_variable,state = "readonly")
font_size["values"] = tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row = 0,column = 1,padx = 5)


bold_icon = tk.PhotoImage(file = "bold.png")
bold_btn = ttk.Button(tool_bar_label,image = bold_icon)
bold_btn.grid(row = 0,column = 2 ,padx = 5)

italic_icon = tk.PhotoImage(file='italic.png')
italic_btn = ttk.Button(tool_bar_label, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

underline_icon = tk.PhotoImage(file='underline.png')
underline_btn = ttk.Button(tool_bar_label, image = underline_icon)
underline_btn.grid(row = 0, column=4, padx=5)

font_color_icon = tk.PhotoImage(file='font_color.png')
font_color_btn = ttk.Button(tool_bar_label, image=font_color_icon)
font_color_btn.grid(row=0, column=5,padx=5)

align_left_icon = tk.PhotoImage(file='align_left.png')
align_left_btn = ttk.Button(tool_bar_label, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

align_center_icon = tk.PhotoImage(file='align_center.png')
align_center_btn = ttk.Button(tool_bar_label, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

align_right_icon = tk.PhotoImage(file='align_right.png')
align_right_btn = ttk.Button(tool_bar_label, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

text_editor = tk.Text(nuclear)
text_editor.config(wrap = "word",relief = tk.FLAT)

scroll_bar = tk.Scrollbar(nuclear)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

font_now = "Meera"
font_size_now = 16

view.add_command(label = "Tool Bar",image = tool,compound = tk.LEFT,accelerator = "ctrl+C")
view.add_command(label = "Status Bar",image = status,compound = tk.LEFT,accelerator = "ctrl+X")


file.add_command(label = "New",image = new_icon,compound = tk.LEFT,accelerator = "ctrl+N")
file.add_command(label = "Open",image = openn,compound = tk.LEFT,accelerator = "ctrl+O")
file.add_command(label = "Save",image = save,compound = tk.LEFT,accelerator = "ctrl+S")
file.add_command(label = "Save As",image = save_as,compound = tk.LEFT,accelerator = "ctrl+shift+s")
file.add_command(label = "Exit",image = exit,compound = tk.LEFT,accelerator = "ctrl+Q")

edit.add_command(label = "Copy",image = copy,compound = tk.LEFT,accelerator = "ctrl+C")
edit.add_command(label = "Cut",image = cut,compound = tk.LEFT,accelerator = "ctrl+X")
edit.add_command(label = "Paste",image = paste,compound = tk.LEFT,accelerator = "ctrl+V")
edit.add_command(label = "Replace",image = replace,compound = tk.LEFT,accelerator = "ctrl+H")
edit.add_command(label = "Find",image = find,compound = tk.LEFT,accelerator = "ctrl+F")




nuclear.config(menu = main_menu)
 
nuclear.mainloop()