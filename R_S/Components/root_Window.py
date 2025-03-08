from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf 
from tk_pdf_сollect_2 import create_pdf_with_numbering
import os 
import re
from PIL import Image, ImageTk
from .parser_format import parse_format
from tkinter.messagebox import showerror, showwarning, showinfo

from .two_window import *
from .toolbar import *
from .tb_filebox import *
from .pdf_viewer import PDFViewer



class Root_Window:
    
    def __init__(self, parent):
        
        self.parent = parent
        self.root = tk.Toplevel(parent)
    
        parent_hight = self.parent.winfo_height()
        self.root.geometry(f"{self.parent.winfo_width()}x{parent_hight}+{self.parent.winfo_x()+8}+{self.parent.winfo_y()}")
        self.root.minsize(600, 100)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)

        # icon = PhotoImage(file="rs_icon.png")
        # self.root.iconphoto(True, icon)

       
        
        obj_toolbar = Toolbar(self.root, self.parent)
        toolbar = obj_toolbar.get_toolbar()
        
        self.menu_button = tk.Button(toolbar, text="Файл", width=10, bg="#181818", fg="#cccccc", bd=0, font=("Segoe UI", SIZE_TEXT))
        self.menu_button.pack(side="left", padx=2)

        # menu_button.bind("<Button-1>", show_menu)  
        self.menu_button.bind("<Enter>", self.on_enter_menu_button)  

        self.obj_custom_menu = Custom_menu(self.root,self.parent)
        
        self.custom_menu = self.obj_custom_menu.get_custom_menu()
        


        self.frame = ttk.Frame(self.root, style="Main.TFrame")
        self.frame.pack(fill=X, padx=0, pady=0)
        
        image_path = os.path.join(f"{os.getcwd()}\\R_S", "PLAY.PNG") 
        image = Image.open(image_path)
        image = image.resize((30, 30))  
        self.photo = ImageTk.PhotoImage(image)

        image_path_2 = os.path.join(f"{os.getcwd()}\\R_S", "PLAY_e.PNG") 
        image_2 = Image.open(image_path_2)
        image_2 = image_2.resize((30, 30))  
        self.photo_2 = ImageTk.PhotoImage(image_2)

        self.collect_button = tk.Button(self.frame,  font=("Segoe UI", SIZE_TEXT), height=20, width=20, bg="#181818", fg="#cccccc", relief='flat', bd= 0, command=self.collect_data, image=self.photo)
        self.collect_button.pack(side="right", padx=(0, 10), pady=5)

        self.collect_button.bind("<Enter>", self.on_enter_on_sobrat)  
        self.collect_button.bind("<Leave>", self.on_leave_on_sobrat)
        
        self.obj_two_window = Two_Windows(self.root , self.parent)
        self.paned_window = self.obj_two_window.get_two_window()
        
        self.pdf_viewer = PDFViewer(self.obj_two_window.pdf_frame)
        
        self.root.bind("<Button-1>", lambda event: self.hide_custom_menu(event) if event.widget != self.custom_menu else None)
        
       
    
    def get_root_window(self):
        return self.root    
    
    def collect_data(self):
        
        forma = self.obj_two_window.format_entry.get()
        forma = parse_format(forma)
        try:   
            format_value = forma
            share_value = self.obj_two_window.share_entry.get().strip()
            pages_value1 = self.obj_two_window.pages_entry.get().strip()
            
            final_share_value = 0
            match int(share_value):
                case 2:
                    final_share_value = 1
                case 4: 
                    final_share_value = 2
                case 8:
                    final_share_value = 3
                case 16:
                    final_share_value = 4            
            try:
                first_entry_value = int(self.obj_two_window.first_entry.get())
            except ValueError:
            
                self.root.attributes("-topmost", False)

                result = showwarning(title="Предупреждение", message="Введите первую страницу")
                if result: self.root.attributes("-topmost", True)
                
            try:
                pages_value = int(pages_value1)
            except:
                self.root.attributes("-topmost", False)

                result = showwarning(title="Предупреждение", message="Введите количество страниц")
                if result: self.root.attributes("-topmost", True)
            
            
            Format.read_format(format_value)
            
            print(f"Формат листа: {format_value}, Доля: {final_share_value}, Количество страниц: {pages_value}")
            
            file_name = f"{os.getcwd()}\\Test_Spoosks.pdf"

            if int(final_share_value) > 4:
                raise Exception("Доля должна быть меньше 5")
            
            number_public= self.obj_two_window.number_public_cont.get()
            create_pdf_with_numbering(file_name, int(pages_value), int(final_share_value), first_entry_value,number_public)

            
            self.pdf_viewer.open_pdf(file_name)
            """# if pdf_viewer.current_view == None:
                
            #     pdf_viewer.open_pdf(file_name)
            # else:
            #     pdf_viewer.current_view.destroy()
            #     pdf_viewer.open_pdf(file_name)

            
            # v1 = pdf.ShowPdf()
            # v2=v1.pdf_view(self.obj_two_window.pdf_frame,pdf_location=open(file_name, "r"), width=77, height=100)
            # v2.pack(pady=(0,0))"""
        except Exception as e :
            print(f"{e}")
            # self.open_warning(e)
 
    
    
    def open_warning(self,e): 
        top = tk.Toplevel(self.root)
        top.title("Предупреждение")
        top.geometry("300x100")
        top.attributes("-topmost", True)  
        tk.Label(top, text=f"Ошибка: {e}", fg="red").pack(pady=10)
        tk.Button(top, text="Закрыть", command=top.destroy).pack(pady=5)
    
    
    def hide_custom_menu(self,event):
        
        self.menu_widgets = [self.menu_button, self.obj_custom_menu.exit_button , self.obj_custom_menu.save_button] 
        if event.widget not in self.menu_widgets:
            self.menu_button.config(bg="#181818", fg="#cccccc")
            self.custom_menu.place_forget()

    
    
    """    
    # def close_window(self):
    #     self.root.destroy()
    #     self.parent.destroy()
    # print("Close")
    """
    def save_file(self):

        print("Save_file")

    
    
    def on_enter_on_sobrat(self,event): 
        self.collect_button.config(bg="#333333" ,image=self.photo_2)
    def on_leave_on_sobrat(self,event):
        self.collect_button.config(bg = "#181818",image=self.photo)
    
    
    
    def show_menu(self,event):
        x, y = self.menu_button.winfo_x(), self.menu_button.winfo_y()
        width =    self.menu_button.winfo_width()
        height = self.menu_button.winfo_height()
        self.custom_menu.place(x = x , y = y+height+1)
        self.custom_menu.lift()
        #file_menu.post(event.x_root, event.y_root)    
    
    def on_enter_menu_button(self,event):
        self.menu_button.config(bg="#333333", fg="white") 
        self.show_menu(event) 
    
    

        

        