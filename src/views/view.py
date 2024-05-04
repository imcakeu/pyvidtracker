import tkinter as tk
from tkinter import *
import sys

from models.pointMode import PointMode
import matplotlib.pyplot as plt
import numpy as np
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
        fileMenu.add_command(label="Sauvegarder les données de Pointage en CSV...", command = self.onSaveCSV, accelerator="CTRL+S")
        fileMenu.add_command(label="Quitter", command = self.onExit)
        menubar.add_cascade(label="Fichier", menu=fileMenu)

        # Crée un menu "Modifier"
        editMenu = Menu(menubar)
        editMenu.add_command(label="Activer/désactiver Mode Pointage", command = self.togglePointage, accelerator="CTRL+Q")
        editMenu.add_command(label="Définir l'échelle...", command = self.onSetScale, accelerator="CTRL+E")
        menubar.add_cascade(label="Modifier", menu=editMenu)

        # Crée un menu "Affichage"
        viewMenu = Menu(menubar)
        viewMenu.add_command(label="Graphe de y(x)", command = self.openGraph_yx)
        viewMenu.add_command(label="Graphe de x(t)", command = self.openGraph_xt)
        viewMenu.add_command(label="Graphe de y(t)", command = self.openGraph_yt)
        menubar.add_cascade(label="Affichage", menu=viewMenu)

        # Paramètre les raccourcis
        self.bind_all("<Control-o>", lambda x: self.onLoadVideo())
        self.bind_all("<Control-q>", lambda x: self.togglePointage())
        self.bind_all("<Control-s>", lambda x: self.onSaveCSV())
        self.bind_all("<Control-e>", lambda x: self.onSetScale())

    # Crée les boutons de contrôle de la vidéo
    # Appelé par Controller après la création de VideoPlayer
    def userinterface_videocontrol(self):
        #configuration des colonnes

        self.grid_columnconfigure(4,weight=1)
        # Boutons début (<<) et recul (<)
        self.start_button = Button(self.window, text="<<", command=self.onStartVideo)
        self.start_button.grid(column=5,row=1)
        self.move_back_button = Button(self.window, text="<", command=self.onMoveBackFrame)
        self.move_back_button.grid(column=6,row=1)

        # Bouton lire/pause (par défaut II, ou > quand en pause)
        self.play_pause_button = Button(self.window, text="II", command=self.onTogglePlayPause)
        self.play_pause_button.grid(column=7,row=1)
        #self.play_pause_button.pack(side='left')

        # Boutons avance (>) et fin (>>)
        self.move_fwd_button = Button(self.window, text=">", command=self.onMoveFwdFrame)
        self.move_fwd_button.grid(column=8,row=1)
        #self.move_fwd_button.pack(side='left')
        self.end_button = Button(self.window, text=">>", command=self.onEndVideo)
        self.end_button.grid(column=9,row=1)
        #self.end_button.pack(side='left')

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
        self.controller.parent.bind("<Escape>", self.onSaveCSV_shortcut)

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

    def onSetScale(self):
        self.controller.parent.new_player_toggle_scale_mode()

    def openGraph(self, type):
        table_points = self.controller.point_data
        table_valeurs_x = []
        table_valeurs_y = []
        table_valeurs_t = []
        for i in range(len(table_points)):
            table_valeurs_x.append(table_points[i].get_x())
            table_valeurs_y.append(table_points[i].get_y())
            table_valeurs_t.append(table_points[i].get_t())

        if(type == "yx"):
            xpoints = np.array(table_valeurs_x)
            ypoints = np.array(table_valeurs_y)
            plt.xlabel("Position X")
            plt.ylabel("Position Y")

        elif(type == "xt"):
            xpoints = np.array(table_valeurs_t)
            ypoints = np.array(table_valeurs_x)
            plt.xlabel("Temps (en s)")
            plt.ylabel("Position X")


        elif(type == "yt"):
            xpoints = np.array(table_valeurs_t)
            ypoints = np.array(table_valeurs_y)
            plt.xlabel("Temps (en s)")
            plt.ylabel("Position Y")


        plt.plot(xpoints, ypoints)
        plt.show()

    def openGraph_yx(self):
        if self.controller.point_data != []:
            self.openGraph("yx")
        else:
            self.window.error_handler("Aucune donnée à afficher")

    def openGraph_xt(self):
        if self.controller.point_data != []:
            self.openGraph("xt")
        else:
            self.window.error_handler("Aucune donnée à afficher")

    def openGraph_yt(self):
        if self.controller.point_data != []:
            self.openGraph("yt")
        else:
            self.window.error_handler("Aucune donnée à afficher")

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
    def onSaveCSV_shortcut(self, var):
        if self.controller.point_mode == PointMode.Enabled:
            self.onSaveCSV()