import tkinter as tk
from tkinter import *
import sys

# Gère l'affichage de l'interface
class View(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.userinterface_menus()

    def set_controller(self, controller):
        self.controller = controller

    # Crée le "menubar" (boutons de la navbar)
    def userinterface_menus(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # Crée un menu "Fichier"
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Ouvrir une vidéo...", command = self.onLoadVideo, accelerator="CTRL+O")
        fileMenu.add_command(label="Quitter", command = self.onExit)
        menubar.add_cascade(label="Fichier", menu=fileMenu)

        # Crée un menu "Pointage"
        pointageMenu = Menu(menubar)
        pointageMenu.add_command(label="Activer/désactiver Mode Pointage", command = self.togglePointage, accelerator="CTRL+Q")
        pointageMenu.add_command(label="Sauvegarder les données de Pointage en CSV...", command = self.onSaveCSV, accelerator="CTRL+S")
        menubar.add_cascade(label="Pointage", menu=pointageMenu)

        # Paramètre les raccourcis
        self.bind_all("<Control-o>", lambda x: self.onLoadVideo())
        self.bind_all("<Control-q>", lambda x: self.togglePointage())
        self.bind_all("<Control-s>", lambda x: self.onSaveCSV())

    # Crée les boutons de contrôle de la vidéo
    # Appelé par Controller après la création de VideoPlayer
    def userinterface_videocontrol(self):
        # Boutons début (<<) et recul (<)
        self.start_button = Button(self.window, text="<<", command=self.onStartVideo)
        self.start_button.pack(side='left')
        self.move_back_button = Button(self.window, text="<", command=self.onMoveBackFrame)
        self.move_back_button.pack(side='left')

        # Bouton lire/pause (par défaut II, ou > quand en pause)
        self.play_pause_button = Button(self.window, text="II", command=self.onTogglePlayPause)
        self.play_pause_button.pack(side='left')

        # Boutons avance (>) et fin (>>)
        self.move_fwd_button = Button(self.window, text=">", command=self.onMoveFwdFrame)
        self.move_fwd_button.pack(side='left')
        self.end_button = Button(self.window, text=">>", command=self.onEndVideo)
        self.end_button.pack(side='left')

        # Affecte les mêmes fonctions sur les touches du claiver.
        # Flèches gauche/droite pour recul/avance
        # Espace ou K pour lire/pause
        # J et L pour début/fin
        self.controller.parent.bind("<Left>", self.onMoveBackFrame_shortcut)
        self.controller.parent.bind("<Right>", self.onMoveFwdFrame_shortcut)
        self.controller.parent.bind("<space>", self.onTogglePlayPause_shortcut)
        self.controller.parent.bind("<k>", self.onTogglePlayPause_shortcut)
        self.controller.parent.bind("<j>", self.onStartVideo_shortcut)
        self.controller.parent.bind("<l>", self.onEndVideo_shortcut)

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
        self.controller.open_video()

    def togglePointage(self):
        self.controller.parent.new_player_toggle_point_mode()

    def onSaveCSV(self):
        self.controller.exporter()

    def onExit(self):
        sys.exit("User has quit successfully")

    # Système d'affectation de touches de clavier retourne 2 arguments
    # Ces fonctions ne font qu'appeler la bonne fonction sans utiliser ce 2ème argument
    # Sans ca, l'application crash...
    def onMoveBackFrame_shortcut(self, var):
        self.onMoveBackFrame()
    def onMoveFwdFrame_shortcut(self, var):
        self.onMoveFwdFrame()
    def onTogglePlayPause_shortcut(self, var):
        self.onTogglePlayPause()
    def onStartVideo_shortcut(self, var):
        self.onStartVideo()
    def onEndVideo_shortcut(self, var):
        self.onEndVideo()