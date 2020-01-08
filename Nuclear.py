import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

nuclear=tk.Tk()
nuclear.geometry("500x400")
nuclear.title("Nuclear")  

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

def change_font(nuclear):
    global font_now
    font_now = font_family.get()
    text_editor.configure(font = (font_now,font_size_now))

def change_size(nuclear):
    global font_size_now
    font_size_now = size_variable.get()
    text_editor.configure(font = (font_now,font_size_now))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)


def bold_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"] == 'normal':
        text_editor.configure(font =(font_now,font_size_now,"bold"))
    if text_get.actual()["weight"] == 'bold':
        text_editor.configure(font =(font_now,font_size_now,"normal"))

bold_btn.configure(command = bold_fun)

def Italic_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"] == 'roman':
        text_editor.configure(font =(font_now,font_size_now,"italic"))
    if text_get.actual()["slant"] == 'italic':
        text_editor.configure(font =(font_now,font_size_now,"roman"))

italic_btn.configure(command = Italic_fun)

def under_line_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"] == 0:
        text_editor.configure(font =(font_now,font_size_now,"underline"))
    if text_get.actual()["underline"] == 1:
        text_editor.configure(font =(font_now,font_size_now,"normal"))

underline_btn.configure(command = under_line_fun)

def Color_choose():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command = Color_choose)

def align_left():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("left",justify = tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"left")

align_left_btn.configure(command = align_left)

def align_center():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("center",justify = tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"center")

align_center_btn.configure(command = align_center)

def align_right():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify = tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"right")

align_right_btn.configure(command = align_right)



# status bar  word and character count 

status_bars = ttk.Label(nuclear,text = "Status bar")
status_bars.pack(side = tk.BOTTOM)

text_change = False

def change_word(event = None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        word = len(text_editor.get(1.0,"end-1c").split())
        chararcter = len(text_editor.get(1.0,"end-1c").replace(" ",""))
        status_bars.config(text = f"character :{chararcter} word :{word}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",change_word)


def change_theme():
    get_theme = theme_select.get()
    colour_tuple = color_dict.get(get_theme)
    fg_color,bg_color = colour_tuple[0],colour_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)

count = 0
for i in color_dict:
    theme.add_radiobutton(label = i,image = color_icons[count],variable = theme_select,compound = tk.LEFT,command = change_theme)
    count += 1

show_status_bar = tk.BooleanVar()
show_status_bar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar_label.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bars.pack_forget()
        tool_bar_label.pack(side = tk.TOP,fill = tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bars.pack(side=tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False 
    else :
        status_bars.pack(side=tk.BOTTOM)
        show_status_bar = True 



view.add_checkbutton(label = "Tool Bar",onvalue = True,offvalue = 0,variable =show_toolbar ,image = tool,compound = tk.LEFT,command =hide_toolbar)
view.add_checkbutton(label = "Status Bar",onvalue = True,offvalue = 0,variable = show_status_bar,image = status,compound = tk.LEFT,command =hide_statusbar)
# edit menu



edit.add_command(label = "copy",image = copy,compound = tk.LEFT,accelerator = "Ctrl+C",command = lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste",image=paste,compound=tk.LEFT,accelerator = "Ctrl+v",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut",image=cut,compound=tk.LEFT,accelerator = "Ctrl+x", command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Find",image=find,compound=tk.LEFT,accelerator = "Ctrl+Alt+x",command= lambda:text_editor.delete(1.0, tk.END))

def find_fun(event = None):

    def find():
        word = find_input.get()
        text_editor.tag_remove("match","1.0",tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match",start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground = "red",background = "blue")
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_popup = tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("find word")
    find_popup.resizable(0,0)

    # fram for find
    find_fram = ttk.LabelFrame(find_popup,text = "Find and Replac word")
    find_fram.pack(pady = 20)

    # label 
    text_find = ttk.Label(find_fram,text = "Find")
    text_replace = ttk.Label(find_fram,text = "Replace")

    # entry box
    find_input = ttk.Entry(find_fram,width = 30 )
    replace_input = ttk.Entry(find_fram,width = 30 )

    # button 
    find_button = ttk.Button(find_fram,text = "find",command = find)
    replace_button = ttk.Button(find_fram,text = "Replace",command = replace)

    # text label grid
    text_find.grid(row = 0,column = 0,padx = 4,pady = 4)
    text_replace.grid(row = 1,column = 0,padx = 4,pady = 4)

    # entry grid
    find_input.grid(row = 0,column = 1,padx = 4,pady = 4)
    replace_input.grid(row = 1,column = 1,padx = 4,pady = 4)

    # button grid
    find_button.grid(row = 2,column = 0,padx = 8 ,pady = 4)
    replace_button.grid(row=2,column=1,padx = 8,pady = 4)

edit.add_command(label="Find",image=find,compound=tk.LEFT,accelerator = "Ctrl+f",command= find_fun)

# file menu

text_url = " "

def new_file(event = None):
    global text_url
    text_url = " "
    text_editor.delete(1.0,tk.END)

file.add_command(label="New",image = new_icon,compound = tk.LEFT,accelerator = "Ctrl+N",command = new_file)




def open_file(event = None):
    global text_url 
    text_url = filedialog.askopenfilename(initialdir = os.getcwd(),title= "select file",filetypes = (("Text file","*.txt"),("All files","*.*")))
    try:
        with open(text_url,"r") as for_read:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(text_url))

file.add_command(label="Open",image=openn,compound=tk.LEFT,accelerator = "Ctrl+o",command = open_file)

def save_file(event = None):
    global text_url
    try:
        if text_url:
            content = str(text_editor.get(1.0,tk.END))
            with open(text_url,"w",encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_url = filedialog.asksaveasfile(mode = "w",defaultextension = ".txt",filetypes = (("Text file","*.txt"),("All files","*.*")))
            content2 = text_editor.get(1.0,tk.END)
            text_url.write(content2)
            text_url.close()
    except:
        return


file.add_command(label="Save",image=save,compound=tk.LEFT,accelerator = "Ctrl+s",command = save_file)

def Save_as(event = None):
    global text_url
    try:
        content = text_editor.get(1.0,tk.END)
        text_url = filedialog.asksaveasfile(mode = "w",defaultextension = ".txt",filetypes = (("Text file","*.txt"),("All files","*.*")))
        text_url.write(content)
        text_url.close()
    except:
        return

file.add_command(label="Save as",compound=tk.LEFT,accelerator = "Ctrl+Alt+s",command = Save_as)

def Exit_fun(event = None):
    global text_url,text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel("warning","Do you want to save this file")
            if mbox is True:
                if text_url:
                    content = text_editor.get(1.0,tk.END)
                    with open(text_url,"w",encoding = "utf-8") as for_read:
                        for_read.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    text_url = filedialog.asksaveasfile(mode = "w",defaultextension = ".txt",filetypes = (("Text file","*.txt"),("All files","*.*")))
                    text_url.write(content2)
                    text_url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label="Exit",image=exit,compound=tk.LEFT,accelerator = "Ctrl+",command = Exit_fun)


nuclear.config(menu = main_menu)

nuclear.mainloop()
######
#view.add_command(label = "Tool Bar",image = tool,compound = tk.LEFT,accelerator = "ctrl+C")
#view.add_command(label = "Status Bar",image = status,compound = tk.LEFT,accelerator = "ctrl+X")

#file.add_command(label = "New",image = new_icon,compound = tk.LEFT,accelerator = "ctrl+N")
#file.add_command(label = "Open",image = openn,compound = tk.LEFT,accelerator = "ctrl+O")
#file.add_command(label = "Save",image = save,compound = tk.LEFT,accelerator = "ctrl+S")
#file.add_command(label = "Save As",image = save_as,compound = tk.LEFT,accelerator = "ctrl+shift+s")
#file.add_command(label = "Exit",image = exit,compound = tk.LEFT,accelerator = "ctrl+Q")

#edit.add_command(label = "Copy",image = copy,compound = tk.LEFT,accelerator = "ctrl+C")
#edit.add_command(label = "Cut",image = cut,compound = tk.LEFT,accelerator = "ctrl+X")
#edit.add_command(label = "Paste",image = paste,compound = tk.LEFT,accelerator = "ctrl+V")
#edit.add_command(label = "Replace",image = replace,compound = tk.LEFT,accelerator = "ctrl+H")
#edit.add_command(label = "Find",image = find,compound = tk.LEFT,accelerator = "ctrl+F")

