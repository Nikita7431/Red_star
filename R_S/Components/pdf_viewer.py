from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf 
from read_format import *

class PDFViewer:
   
    
    def __init__(self, pdf_frame):
        self.pdf_frame = pdf_frame
        self.current_view = None 
        self.v1 = None

    def open_pdf(self, file_name):
       
        if self.current_view is not None:
            self.current_view.destroy()
          
            self.pdf_frame.update_idletasks()
        
       
        self.v1 = pdf.ShowPdf()
        self.v1.img_object_li.clear()
        self.current_view = self.v1.pdf_view(
            self.pdf_frame, 
            pdf_location=open(file_name, "r"), 
            width = int(Format._width), 
            height=int(Format._height)
        )
        self.current_view.pack(pady=(0, 0))
        self.current_view.update_idletasks()



