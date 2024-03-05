import tkinter as tk
import PIL.Image, PIL.ImageTk
from tkinter import ttk

class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        
    
    def setController(self, controller):
        self.controller = controller

    