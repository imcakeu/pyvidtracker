import tkinter as tk
import PIL.Image, PIL.ImageTk
from tkinter import Tk, Frame, Menu
import controllers.fileRepo as classFileRepo

class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.initUI()

    def setController(self, controller):
        self.controller = controller

    def initUI(self):
        self.master.title("Simple menu")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Charger video")
        fileMenu.add_command(label="Lire video")
        fileMenu.add_command(label="Quitter", command=self.onExit)
        menubar.add_cascade(label="Fichier", menu=fileMenu)

        scaleMenu = Menu(menubar)
        scaleMenu.add_command(label="Creer une nouvelle Echelle")
        scaleMenu.add_command(label="Activer l'affichage de l'Echelle")
        menubar.add_cascade(label="Echelle", menu=scaleMenu)
        
        pointageMenu = Menu(menubar)
        pointageMenu.add_command(label="Sauvegarder en CSV", command = self.onSave)
        menubar.add_cascade(label="Pointage", menu=pointageMenu)
        
    def onSave(self):
        print("Sauvegarder")
        classFileRepo.exporter()


    def onExit(self):
        self.quit()

def main():
    root = tk()
    root.geometry("250x150+300+300")
    app = View()
    root.mainloop()