from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf 
from tk_pdf_сollect_2 import create_pdf_with_numbering
import os 
import re
from PIL import Image, ImageTk


SIZE_TEXT = 10  

class Custom_menu:
    
    def __init__(self,root, parent):
        
        self.root = root
        self.parent = parent
        
        self.custom_menu = tk.Frame(root, bg="#333333", highlightbackground="#cccccc",highlightthickness=1)
        self.custom_menu.place_forget()

        self.open_button = tk.Button(self.custom_menu, text="Открыть",width=9,font=("Segoe UI", SIZE_TEXT), bg="#333333", fg="#cccccc", relief="flat", command=self.open_file)
        self.open_button.pack(fill="x", padx=2, pady=2)

      
        self.save_button = tk.Button(self.custom_menu, text="Сохранить",width=9,font=("Segoe UI", SIZE_TEXT), bg="#333333", fg="#cccccc", relief="flat", command=self.save_file)
        self.save_button.pack(fill="x", padx=2, pady=2)
        
        
        separator = tk.Frame(self.custom_menu, height=1, bg="#cccccc")
        separator.pack(fill="x", padx=2)

        self.exit_button = tk.Button(self.custom_menu, text="Выход", font=("Segoe UI", SIZE_TEXT), width=9, bg="#333333", fg="#cccccc", relief="flat", command=self.close_window)
        self.exit_button.pack(fill="x", padx=2, pady=2)

        self.open_button.bind("<Enter>", self.on_enter_open_btn_save)  
        self.open_button.bind("<Leave>", self.on_leave_open_btn_save)


        self.exit_button.bind("<Enter>", self.on_enter_menu_btn_exit)  
        self.exit_button.bind("<Leave>", self.on_leave_menu_btn_exit)

        self.save_button.bind("<Enter>", self.on_enter_menu_btn_save)  
        self.save_button.bind("<Leave>", self.on_leave_menu_btn_save)
        # self.menu_button.bind("<Enter>", self.on_enter_menu_button)  
    
    def get_custom_menu(self):
        return self.custom_menu
            
    
    
    # def on_enter_menu_button(self,event):
    #     self.menu_button.config(bg="#333333", fg="white") 
    #     self.show_menu(event) 
  
    
    # def show_menu(self,event):
    #     x, y = self.menu_button.winfo_x(), self.menu_button.winfo_y()
    #     width =    self.menu_button.winfo_width()
    #     height = self.menu_button.winfo_height()
    #     self.custom_menu.place(x = x , y = y+height+1)
    #     self.custom_menu.lift()
    #     #file_menu.post(event.x_root, event.y_root)
    
    
    
    # def add_func(self,close_func,save_func):
    #     self.close_func = close_func
    #     self.save_func = save_func
    
    def open_file(self):
       
        print("File open")
        
    def close_window(self):
        self.root.destroy()
        self.parent.destroy()
        print("Close")
    
    def save_file(self):

        print("Save_file")
     
    def on_enter_open_btn_save(self,event):    
        self.open_button.config(bg="#0078d4", fg="white") 
       
    def on_enter_menu_btn_exit(self,event):    
        self.exit_button.config(bg="#0078d4", fg="white")
    def on_enter_menu_btn_save(self, event): 
        self.save_button.config(bg="#0078d4", fg="white")    
    
    
    def on_leave_open_btn_save(self,event): 
        self.open_button.config(bg="#333333", fg="white")
    
    def on_leave_menu_btn_exit(self,event):    
        self.exit_button.config(bg="#333333", fg="white")
        
    def on_leave_menu_btn_save(self,event): 
        self.save_button.config(bg="#333333", fg="white")