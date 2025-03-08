from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf 
from tk_pdf_сollect_2 import create_pdf_with_numbering
import os 
import re
from PIL import Image, ImageTk

from Components.two_window import *
from Components.toolbar import *
from Components.tb_filebox import *
from Components.root_Window import *




def sync_child_size(event):
    global root
    parent_hight = parent.winfo_height()
    root.geometry(f"{parent.winfo_width()}x{parent_hight}+{parent.winfo_x()+8}+{parent.winfo_y()}")
    # left_window.geometry(f"{200}x{parent_hight}+{parent.winfo_x()+8}+{root.winfo_y()-10}")

def on_parent_iconify(event=None):

    if root.winfo_exists():  
        root.destroy()

def close_window(self):
    self.root.destroy()
    self.parent.destroy()
    print("Close")
    
def on_parent_deiconify(event=None):
    
    global root
    if not root or not root.winfo_exists():
            obj_root = Root_Window(parent)
            root = obj_root.get_root_window()

parent = tk.Tk()
parent.geometry("800x600")
parent.title("Parent Window")

style = ttk.Style()
style.theme_use("default")
style.configure("Parent.TFrame", background="#181818",relief="sunken",borderwidth=1,highlightbackground="#cccccc")
style.configure("Toolbar.TFrame", background="#181818" )
style.configure("Left_bar.TFrame", background="#181818" )
style.configure("Pdf.TFrame", background="#181818" )

style.configure("Notebook.TNotebook", background = "#181818")
# style.configure("TNotebook.Tab", background="#333333", foreground="#ffffff", padding=[10, 5])
# style.map("TNotebook.Tab", background=[("selec ted", "#444444")])

style.configure("Main.TFrame", background="#181818",relief="sunken",borderwidth=1,highlightbackground="#cccccc")
style.configure("Main.TLabel", background="#181818", font=("Segoe UI", SIZE_TEXT), foreground ="#cccccc" )
style.configure("Main.TEntry", font=("Segoe UI", SIZE_TEXT) ,foreground ="#181818", background="#d9d9d9" , fieldbackground="#d9d9d9" )
style.configure("Main.TButton", font=("Segoe UI", SIZE_TEXT),relief='flat',padding=-3)
# style.configure("Main.TCombobox", font=("Segoe UI", 12), foreground="#cccccc", background="transparent", fieldbackground="#333333")
style.configure("Main.TCombobox",
                fieldbackground="#d9d9d9",  # Цвет фона выпадающего списка
                background="#d9d9d9",  # Цвет фона поля
                foreground="#181818",  # Цвет шрифта
                selectbackground="#d9d9d9",  # Цвет фона при выборе
                selectforeground="#181818",  # Цвет шрифта при выборе
                font=("Segoe UI", 12)
                )

parent_frame = ttk.Frame(parent, style="Parent.TFrame")
parent_frame.pack(side="bottom", fill="both", expand=True)

# parent.bind("<Unmap>", on_parent_iconify)  
# parent.bind("<Map>", on_parent_deiconify)

obj_root = Root_Window(parent)
root = obj_root.get_root_window()

root.protocol("WM_DELETE_WINDOW", close_window)



parent.bind("<Configure>", sync_child_size)
parent.mainloop()

