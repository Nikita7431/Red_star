from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf 
from tk_pdf_сollect_2 import create_pdf_with_numbering
import os 
import re
from PIL import Image, ImageTk


class NotebookPDF:
    
    def __init__(self, root):
        self.root = root 
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)
        
        tab1 = ttk.Frame(self.notebook)
        tab2 = ttk.Frame(self.notebook)
        self.notebook.add(tab1, text="Вкладка 1")
        self.notebook.add(tab2, text="Вкладка 2")
        
        tk.Label(tab1, text="Содержимое первой вкладки").pack(pady=20)
        tk.Label(tab2, text="Содержимое второй вкладки").pack(pady=20)
        
    def get_notebook(self):
        return self.notebook    
    