import tkinter as tk
from tkinter import *
import sys

class View(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.userinterfacte_menus()
        self.controller = None

    def setController(self, controller):
        print("Controller:", controller)
        self.controller = controller

    def userinterfacte_menus(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Ouvrir une vidéo...", command = self.onLoadVideo)
        fileMenu.add_command(label="Quitter", command = self.onExit)
        menubar.add_cascade(label="Fichier", menu=fileMenu)

        pointageMenu = Menu(menubar)
        pointageMenu.add_command(label="Activer/Désactiver Pointage", command = self.togglePointage)
        pointageMenu.add_command(label="Sauvegarder les données en CSV...", command = self.onSaveCSV)
        menubar.add_cascade(label="Pointage", menu=pointageMenu)

    def userinterface_videocontrol(self):
        # Create buttons
        self.start_button = Button(self.window, text="<<", command=self.onStartVideo)
        self.start_button.pack(side='left')
        self.move_back_button = Button(self.window, text="<", command=self.onMoveBackFrame)
        self.move_back_button.pack(side='left')

        self.play_pause_button = Button(self.window, text="II", command=self.onTogglePlayPause)
        self.play_pause_button.pack(side='left')

        self.move_fwd_button = Button(self.window, text=">", command=self.onMoveFwdFrame)
        self.move_fwd_button.pack(side='left')
        self.end_button = Button(self.window, text=">>", command=self.onEndVideo)
        self.end_button.pack(side='left')

    def onStartVideo(self):
        self.controller.videoPlayer.start_video()

    def onEndVideo(self):
        self.controller.videoPlayer.end_video()

    def onTogglePlayPause(self):
        self.controller.videoPlayer.toggle_play_pause()

    def onMoveBackFrame(self):
        self.controller.videoPlayer.move_back_frame()

    def onMoveFwdFrame(self):
        self.controller.videoPlayer.move_fwd_frame()

    def onLoadVideo(self):
        print("Bouton pressé: Ouvrir une video")
        self.controller.open_video()

    def togglePointage(self):
        print("Bouton pressé: Activer/Désactiver Pointage")
        self.controller.parent.new_player_pointage()

    def onSaveCSV(self):
        print("Bouton pressé: Sauvegarder en CSV")
        self.controller.exporter()

    def onExit(self):
        sys.exit("User has quit successfully")