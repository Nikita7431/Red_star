from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf 
from tk_pdf_сollect_2 import create_pdf_with_numbering
import os 
import re
from PIL import Image, ImageTk

from .tb_filebox import *


SIZE_TEXT = 10  
SIZE_TEXT_UI = 12

class Toolbar:
    
    
    
    def __init__(self,root,parent):
        self.root = root
        self.parent = parent
        self.toolbar = ttk.Frame(self.root, style="Toolbar.TFrame", height=50)
        self.toolbar.pack(side="top", fill="x")   
        self.toolbar.bind("<ButtonPress-1>", self.start_move)
        self.toolbar.bind("<ButtonRelease-1>", self.stop_move)
        self.toolbar.bind("<B1-Motion>", self.do_move)

        
        self.btn_close = tk.Button(self.toolbar, text="X", bg="#181818", fg="#cccccc", bd=0, font=("Segoe UI", SIZE_TEXT_UI),width =6, command=self.close_window)
        self.btn_close.pack(side="right", padx=0)

        self.btn_maximize = tk.Button(self.toolbar, text="□", bg="#181818", fg="#cccccc", bd=0, font=("Segoe UI", SIZE_TEXT_UI), width =6, command=self.toggle_maximize)
        self.btn_maximize.pack(side="right", padx=0)

        self.btn_minimize = tk.Button(self.toolbar, text="_", bg="#181818", fg="#cccccc", bd=0, font=("Segoe UI", SIZE_TEXT_UI), width =6, command=self.minimize_window)
        self.btn_minimize.pack(side="right", padx=0)
        
        
        self.btn_minimize.bind("<Enter>", self.on_enter_btn_minimize)  
        self.btn_minimize.bind("<Leave>", self.on_leave_btn_minimize)

        self.btn_maximize.bind("<Enter>", self.on_enter_btn_maximize)  
        self.btn_maximize.bind("<Leave>", self.on_leave_btn_maximize)

        self.btn_close.bind("<Enter>", self.on_enter_btn_close)  
        self.btn_close.bind("<Leave>", self.on_leave_btn_close)
        
        
        # menu_button = tk.Button(self.toolbar, text="Файл", width=10, bg="#181818", fg="#cccccc", bd=0, font=("Segoe UI", SIZE_TEXT))
        # menu_button.pack(side="left", padx=2)
         
        # ob_custom_menu = Custom_menu(self.root)
        # menu_button = ob_custom_menu.get_custom_menu()
        # menu_button.pack(side="left", padx=2)
        
        
        # self.toolbar.pack(side="top", fill="x")
   
    #  self.btn_close.pack(side="right", padx=0)
    #     self.btn_maximize.pack(side="right", padx=0)
    #     self.btn_minimize.pack(side="right", padx=0)
    #     self.menu_button.pack(side="left", padx=2)
    
    def get_toolbar(self):
        return self.toolbar
        
    def on_enter_btn_minimize(self,event):
        self.btn_minimize.config(bg="#333333", fg="white")
    def on_enter_btn_maximize(self,event):    
        self.btn_maximize.config(bg="#333333", fg="white")
    def on_enter_btn_close(self,event): 
        self.btn_close.config(bg="#e81123", fg="white")

    def on_leave_btn_minimize(self,event):
        self.btn_minimize.config(bg="#181818", fg="#cccccc")
    def on_leave_btn_maximize(self,event):
        self.btn_maximize.config(bg="#181818", fg="#cccccc")
    def on_leave_btn_close(self,event):
        self.btn_close.config(bg="#181818", fg="#cccccc")

                
    def minimize_window(self):
        self.parent.iconify() 
        
        
    def close_window(self):
        self.root.destroy()
        self.parent.destroy()
        print("Close")
    
    def save_file(self):

        print("Save_file")


    def toggle_maximize(self):
        if self.root.state() == 'zoomed':
            self.parent.state('normal')
            self.root.state('normal') 
        else:
            self.root.state('zoomed')  
            self.parent.state('zoomed')
        


        
    def start_move(self, event):
        global x_offset, y_offset
        x_offset = event.x_root
        y_offset = event.y_root

    def stop_move(self,event):
        global x_offset, y_offset
        x_offset = None
        y_offset = None
        
   
    def do_move(self,event):
        if x_offset is not None and y_offset is not None:
        
            x = event.x_root - x_offset
            y = event.y_root - y_offset

            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            window_width = self.root.winfo_width()
            window_height = self.root.winfo_height()

            x = max(0, min(x, screen_width - window_width))
            y = max(0, min(y, screen_height - window_height))

            self.parent.geometry(f"+{x}+{y}")
            self.root.geometry(f'+{x+8}+{y}')
