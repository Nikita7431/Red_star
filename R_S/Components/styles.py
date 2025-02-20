from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf 
from tk_pdf_сollect_2 import create_pdf_with_numbering
import os 
import re
from PIL import Image, ImageTk

style = ttk.Style()
style.theme_use("default")
style.configure("Parent.TFrame", background="#181818",relief="sunken",borderwidth=1,highlightbackground="#cccccc")
style.configure("Toolbar.TFrame", background="#181818" )
style.configure("Left_bar.TFrame", background="#181818" )
style.configure("Pdf.TFrame", background="#181818" )