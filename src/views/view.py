import tkinter as tk
import PIL.Image, PIL.ImageTk
from tkinter import Tk, Frame, Menu
from controllers.controller import Controller
import sys

class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initialiseUserInterface()
        self.controller = None

    def setController(self, controller):
        print("Controller:", controller)
        self.controller = controller

    def initialiseUserInterface(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Ouvrir une vidéo...", command = self.onLoadVideo)
        fileMenu.add_command(label="Quitter", command = self.onExit)
        menubar.add_cascade(label="Fichier", menu=fileMenu)

        pointageMenu = Menu(menubar)
        pointageMenu.add_command(label="Créer une nouvelle échelle")
        pointageMenu.add_command(label="Activer l'affichage de l'échelle")
        pointageMenu.add_command(label="Sauvegarder les données en CSV...", command = self.onSaveCSV)
        menubar.add_cascade(label="Pointage", menu=pointageMenu)

    def onLoadVideo(self):
        print("Bouton pressé: Ouvrir une video")
        self.controller.open_video()

    def onSaveCSV(self):
        print("Bouton pressé: Sauvegarder en CSV")
        self.controller.exporter()

    def onExit(self):
        sys.exit("User has quit successfully")