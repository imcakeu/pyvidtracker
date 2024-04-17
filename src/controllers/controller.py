import tkinter as tk
import tkinter.messagebox

from controllers.fileRepo import FileRepo
from models.point import Point
from models.videoPlayer import VideoPlayer
from tkinter import filedialog

# Crée la View et le VideoPlayer tout en gérant le système de pointage
class Controller:
    def __init__(self, parent, view, file_name, is_point_mode):
        # Variables
        self.parent = parent
        self.is_point_mode = is_point_mode
        self.point_data = []

        # Création d'un lecteur vidéo
        self.videoPlayer = VideoPlayer(self, self.parent, file_name, is_point_mode)
        # L'évènement de clic ne doit être appelé que si on est en mode pointage
        if(is_point_mode):
            self.videoPlayer.canvas.bind("<Button-1>", self.event_click_canvas)

        # Paramètrage du View pour rattacher les contrôles vidéo
        self.view = view
        self.view.setController(self)
        self.view.userinterface_videocontrol()

    # Enregistre la position du clic sur le lecteur vidéo
    # Évènement appelé seulement en mode pointage
    def event_click_canvas(self, event):
        # On crée un point qu'on rajoute à point_data
        pos_x, pos_y = event.x, event.y
        var_t = self.videoPlayer.get_playback_time()
        new_point = Point(pos_x, pos_y, var_t)
        self.point_data.append(new_point)

        # On avance d'une frame
        self.videoPlayer.move_fwd_frame()

        print(f"Clic ({var_t}) : X = {pos_x} ; Y = {pos_y}")

    # Ouvre une fênetre dialogue pour sauvegarder un fichier
    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            print("Saving on FilePath:: ", file_path)
            return(file_path)

    # Ouvre une fênetre dialogue pour ouvrir un fichier
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print("Opening File: ", file_path)
            return file_path

    # Appelé dans View quand l'utilisateur ouvre une vidéo
    def open_video(self):
        file_path = self.open_file()
        if file_path:
            self.parent.new_player(file_path)

    # Appelé dans View quand l'utilisateur exporte ses données de pointage
    def exporter(self):
        # On affiche une erreur si l'utilisateur n'est pas en mode pointage ou n'a pas de données
        if(not self.is_point_mode):
            self.parent.error_handler("Impossible d'exporter si le mode pointage est desactivé")
            return
        if(len(self.point_data) == 0):
            self.parent.error_handler("Aucune donnée à sauvegarder")
            return

        # On laisse l'utilisateur choisir où sauvegarder ses données
        file_path = self.save_file()
        if file_path:
            FileRepo.CSVExport(FileRepo, self.point_data, file_path)