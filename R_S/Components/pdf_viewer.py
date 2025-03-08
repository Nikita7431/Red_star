from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf 
from models.read_format import *
import fitz  

class PDFViewer:
   
    
    def __init__(self, pdf_frame):
        self.pdf_frame = pdf_frame
        self.current_view = None 
        self.v1 = None

    def rotate_pdf(self, file_name, output_file, rotation_angle=90):
        """
        Поворачивает страницы PDF на заданный угол и сохраняет в новый файл.
        :param file_name: Исходный файл PDF.
        :param output_file: Выходной файл PDF.
        :param rotation_angle: Угол поворота (90, 180, 270).
        """
        doc = fitz.open(file_name)  # Открываем PDF
        for page in doc:  # Проходим по всем страницам
            page.set_rotation(rotation_angle)  # Поворачиваем страницу
        doc.save(output_file)  # Сохраняем измененный PDF
        doc.close()

    def open_pdf(self, file_name):
        if self.current_view is not None:
            self.current_view.destroy()
            self.pdf_frame.update_idletasks()
        
        # Поворачиваем PDF и сохраняем во временный файл
        rotated_file = "rotated_temp.pdf"
        self.rotate_pdf(file_name, rotated_file, rotation_angle=90)  # Поворот на 90 градусов

        # Отображаем повернутый PDF
        self.v1 = pdf.ShowPdf()
        self.v1.img_object_li.clear()
        self.current_view = self.v1.pdf_view(
            self.pdf_frame, 
            pdf_location=open(rotated_file, "r"), 
            width=int(Format._width), 
            height=int(Format._height)
        )
        self.current_view.pack(pady=(0, 0))
        self.current_view.update_idletasks()
    
    
    # def open_pdf(self, file_name):
       
    #     if self.current_view is not None:
    #         self.current_view.destroy()
          
    #         self.pdf_frame.update_idletasks()
        
       
    #     self.v1 = pdf.ShowPdf()
    #     self.v1.img_object_li.clear()
    #     self.current_view = self.v1.pdf_view(
    #         self.pdf_frame, 
    #         pdf_location=open(file_name, "r"), 
    #         width = int(Format._width), 
    #         height=int(Format._height)
    #     )
    #     self.current_view.pack(pady=(0, 0))
    #     self.current_view.update_idletasks()



