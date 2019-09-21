import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import re
from controller import *


PROGRAM_NAME = "Footprint Editor"
file_name = None

root = Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)

code_controller = None
selected_class = None
selected_class_index = None


new_file_icon = PhotoImage(file='icons/new_file.gif')
open_file_icon = PhotoImage(file='icons/open_file.gif')
save_file_icon = PhotoImage(file='icons/save.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')

# functions here

def display_about_messagebox(event=None):
    tkinter.messagebox.showinfo(
        "About", "{}{}".format(PROGRAM_NAME, "\nTkinter GUI Application\n Development Blueprints"))


def display_help_messagebox(event=None):
    tkinter.messagebox.showinfo(
        "Help", "Help Book: \nTkinter GUI Application\n Development Blueprints",
        icon='question')


def exit_editor(event=None):
    if tkinter.messagebox.askokcancel("Quit?", "Really quit?"):
        root.destroy()


def new_file(event=None):
    root.title("Untitled")
    # global file_name
    # file_name = None
    # content_text.delete(1.0, END)
    # on_content_changed()

def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt",
                                                         filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
        with open(file_name) as _file:
            global code_controller
            code_controller = ComplexityController(_file.read(), 'java')
            print(code_controller.getClassList())
            for i, _class in enumerate(code_controller.getClassList()):
                class_list_bar.insert(i, _class.className)
            # content_text.insert(1.0, _file.read())
        # on_content_changed()

def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                           filetypes=[("All Files", "*.*"),
                                                                      ("Text Documents", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        # write_to_file(file_name)
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
    return "break"


def save(event=None):
    global file_name
    if not file_name:
        save_as()
    # else:
    #     write_to_file(file_name)
    return "break"


def select_all(event=None):
    # content_text.tag_add('sel', '1.0', 'end')
    return "break"


def find_text(event=None):
    pass

def cut():
    # content_text.event_generate("<<Cut>>")
    # on_content_changed()
    return "break"


def copy():
    # content_text.event_generate("<<Copy>>")
    return "break"


def paste():
    # content_text.event_generate("<<Paste>>")
    # on_content_changed()
    return "break"


def undo():
    # content_text.event_generate("<<Undo>>")
    # on_content_changed()
    return "break"


def redo(event=None):
    # content_text.event_generate("<<Redo>>")
    # on_content_changed()
    return 'break'

def toggle_highlight(event=None):
    pass

def update_line_numbers():
    pass

def show_cursor_info_bar():
    pass

def change_theme():
    pass

def class_list_select(event):
    class_index = class_list_bar.curselection()[0]
    # load_class(class_index)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left',
                      image=open_file_icon, underline=0, command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt+F4', command=exit_editor)
menu_bar.add_cascade(label='File', menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_separator()
edit_menu.add_command(label='Copy', accelerator='Ctrl+C',
                      compound='left', image=copy_icon, command=copy)
edit_menu.add_separator()
edit_menu.add_command(label='Find', underline=0,
                      accelerator='Ctrl+F', command=find_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', underline=7,
                      accelerator='Ctrl+A', command=select_all)
menu_bar.add_cascade(label='Edit', menu=edit_menu)

view_menu = Menu(menu_bar, tearoff=0)
show_cursor_info = IntVar()
show_cursor_info.set(1)
themes_menu = Menu(menu_bar, tearoff=0)
view_menu.add_cascade(label='Themes', menu=themes_menu)

color_schemes = {
    'Default': '#000000.#FFFFFF',
    'Greygarious': '#83406A.#D1D4D1',
    'Aquamarine': '#5B8340.#D1E7E0',
    'Bold Beige': '#4B4620.#FFF0E1',
    'Cobalt Blue': '#ffffBB.#3333aa',
    'Olive Green': '#D1E7E0.#5B8340',
    'Night Mode': '#FFFFFF.#000000',
}

theme_choice = StringVar()
theme_choice.set('Default')
for k in sorted(color_schemes):
    themes_menu.add_radiobutton(
        label=k, variable=theme_choice, command=change_theme)
menu_bar.add_cascade(label='View', menu=view_menu)

about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About', command=display_about_messagebox)
about_menu.add_command(label='Help', command=display_help_messagebox)
menu_bar.add_cascade(label='About', menu=about_menu)
root.config(menu=menu_bar)

shortcut_bar = Frame(root, height=25)
shortcut_bar.pack(expand='no', fill='x')

icons = ('open_file', 'save', 'cut', 'copy', 'paste',
         'undo', 'redo', 'find_text')
for i, icon in enumerate(icons):
    tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon))
    cmd = eval(icon)
    tool_bar = Button(shortcut_bar, image=tool_bar_icon, command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side='left')

title_bar = Label(root,height=1)
title_bar.pack(side='top',fill='x')

main_window_frame = Frame(root,bg='lightyellow2')
main_window_frame.pack(expand='yes', fill='both')

class_window_frame = Frame(main_window_frame, width=30)
class_window_frame.pack(expand='yes', fill='both',side='left')
complex_window_frame = Frame(main_window_frame,bg='blue',width=1500)
complex_window_frame.pack(expand='yes', fill='both',side='left', anchor='w')

class_list_bar_title = Label(class_window_frame,text='Class List')
class_list_bar_title.pack(anchor='nw')


test_line_bar = Text(complex_window_frame,width=116, padx=3, takefocus=0, border=0,
                       background='yellow', state='disabled', wrap='word')
test_line_bar.pack(expand='yes', fill='both',anchor='w')


class_list_bar = Listbox(class_window_frame,selectmode=SINGLE)
class_list_bar.bind('<<ListboxSelect>>',class_list_select)
class_list_bar.pack(side='left',fill='y')

root.protocol('WM_DELETE_WINDOW', exit_editor)
root.mainloop()