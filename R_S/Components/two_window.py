from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf 
from PIL import Image, ImageTk

from models.read_format import *
from .read_json import *
from .tb_filebox import *
# from notebook_pdf import *

class Two_Windows:
    
    def __init__(self,root, parent):
        self.root = root 
        self.parent = parent
        self.paned_window = PanedWindow(self.root, relief="sunken",borderwidth=0, orient=HORIZONTAL)
        self.paned_window.pack( fill='both',side="top" , anchor = "s",expand=True )
        self.paned_window.configure(sashwidth = 2, background="#333333")


        # obj_pdf_notebook = NotebookPDF(self.root)

        # notebook = ttk.Notebook(self.root)
        # notebook.pack(fill="both", expand=True)
        self.pdf_frame = ttk.Frame(self.paned_window, style="Pdf.TFrame", width=self.parent.winfo_width())
        self.pdf_frame.pack(side="right", fill="both", expand=True)
        
        
                
        self.left_bar = ttk.Frame(self.paned_window, style="Left_bar.TFrame")
        self.left_bar.pack(side="left", fill="both", expand=True)
    

        # self.gradient_frame = GradientFrame(left_bar, color1="#450f65", color2="#070209", borderwidth=1, relief="sunken")
        # self.gradient_frame.pack(side="bottom", fill="both", expand=True)



        # format_container = ttk.Frame(self.left_bar,style="Left_bar.TFrame")
        # format_container.pack(fill="x", padx=5, pady=(40, 0))
        # ttk.Label(format_container, text="Формат листа:", style="Main.TLabel").pack(side="left", padx=2)
        # self.format_entry = ttk.Entry(format_container, width=13, style="Main.TEntry")
        # self.format_entry.pack(side="left", padx=10)    
        
        
        
        # self.menu_button = tk.Button(self.left_bar, text=, width=10, bg="#181818", fg="#cccccc", bd=0, font=("Segoe UI", SIZE_TEXT))
        # self.menu_button.pack(side="left", padx=2)
        
        
        formats = open_r_json("E:\\Никита Политех(Учеба\\Работы\\R_S_A\\R_S\\formatA.json")
        falcs = ["2                                 ","4                                 ","8                                 ","16                                 "]
               
        format_container = ttk.Frame(self.left_bar,style="Left_bar.TFrame")
        format_container.pack(fill="x", padx=5, pady=(40, 0))
        ttk.Label(format_container, text="Формат листа:", style="Main.TLabel").pack(side="left", padx=2)
        self.format_entry = ttk.Combobox(format_container,values=formats ,width=13,style="Main.TCombobox",state="readonly" )
        self.format_entry.pack(side="left", padx=10)
        

        share_container = ttk.Frame(self.left_bar,style="Left_bar.TFrame")
        share_container.pack(fill="x", padx=5, pady=(20, 0))
        ttk.Label(share_container, text="Доля:", style="Main.TLabel").pack(side="left", padx=2)
        # self.share_entry = ttk.Entry(share_container, width=10, style="Main.TEntry")
        # self.share_entry.pack(side="left", padx=10)
        self.share_entry = ttk.Combobox(share_container,values=falcs ,width=13,style="Main.TCombobox",state="readonly" )
        self.share_entry.pack(side="left", padx=10)

        pages_container = ttk.Frame(self.left_bar,style="Left_bar.TFrame")
        pages_container.pack(fill="x", padx=5, pady=(20, 0))
        ttk.Label(pages_container, text="Количество страниц:", style="Main.TLabel").pack(side="left", padx=2)
        self.pages_entry = ttk.Entry(pages_container, width=10, style="Main.TEntry")
        self.pages_entry.pack(side="left", padx=10)


        first_container = ttk.Frame(self.left_bar, style="Left_bar.TFrame")
        first_container.pack(fill="x", padx=5, pady=(20, 0))
        ttk.Label(first_container, text="Первая страница:", style="Main.TLabel").pack(side="left", padx=2)
        self.first_entry = ttk.Entry(first_container, width=10, style="Main.TEntry")
        self.first_entry.pack(side="left", padx=10)
             
        number_public_container = ttk.Frame(self.left_bar, style="Left_bar.TFrame")
        number_public_container.pack(fill = "x", padx=5, pady=(20, 0))
        ttk.Label(number_public_container, text="Реклама: ", style="Main.TLabel").pack(side="left", padx=2)
        self.number_public_cont = ttk.Entry(number_public_container, width=10, style="Main.TEntry")
        self.number_public_cont.pack(side="left", padx=10)
        
        self.paned_window.add(self.left_bar)
        self.paned_window.add(self.pdf_frame)
        
    
        
    def get_two_window(self):
        return self.paned_window
