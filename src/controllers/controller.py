import tkinter as tk
import tkinter.messagebox

from controllers.fileRepo import FileRepo
from models.point import Point
from models.videoPlayer import VideoPlayer
from tkinter import filedialog

class Controller:
    def __init__(self, parent, view, file_name, is_pointage):
        self.parent = parent
        self.is_pointage = is_pointage
        self.videoPlayer = VideoPlayer(self, self.parent, file_name, is_pointage)

        self.view = view
        self.view.setController(self)
        self.view.userinterface_videocontrol()

        self.pointage_data = []
        if(is_pointage):
            self.videoPlayer.canvas.bind("<Button-1>", self.event_click_canvas)

    # Appelé quand l'utilisateur clique sur le lecteur vidéo.
    # Activé seulement si is_pointage est True car on ne veut enregistrer
    # les données seulement quand on est en mode pointage.
    def event_click_canvas(self, event):
        pos_x, pos_y = event.x, event.y
        new_point = Point(pos_x, pos_y)
        self.pointage_data.append(new_point)

        self.videoPlayer.move_fwd_frame()

        print(f"Position : abscisse = {pos_x} ; ordonnées = {pos_y}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            print("Saving on FilePath:: ", file_path)
            return(file_path)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print("Opening File: ", file_path)
            return file_path
        
    def exporter(self):
        if(not self.is_pointage):
            self.parent.error_handler("Impossible d'exporter si le mode pointage est desactivé")
            return

        if(len(self.pointage_data) == 0):
            self.parent.error_handler("Aucune donnée à sauvegarder")
            return

        path = self.save_file()
        FileRepo.CSVExport(FileRepo, self.pointage_data, path)

    def open_video(self):
        file_path = self.open_file()
        if file_path:
            self.parent.new_player(file_path)