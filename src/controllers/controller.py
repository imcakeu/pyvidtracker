from tkinter import filedialog

from controllers.fileRepo import FileRepo
from models.point import Point
from models.pointMode import PointMode
from models.videoPlayer import VideoPlayer

# Crée le VideoPlayer tout en gérant le système de pointage
class Controller:
    def __init__(self, parent, view, file_name, point_mode, point_scale):
        # Variables
        self.parent = parent
        self.point_mode = point_mode
        self.point_scale = point_scale
        self.point_data = []
        self.scale_data = []

        # Création d'un lecteur vidéo
        self.videoPlayer = VideoPlayer(self, self.parent, file_name, point_mode)
        # L'évènement de clic ne doit être assigné que si on est en mode pointage
        if(point_mode != PointMode.Disabled):
            self.videoPlayer.canvas.bind("<Button-1>", self.event_click_canvas)

        # Paramètrage du View pour rattacher les contrôles vidéo
        self.view = view
        self.view.set_controller(self)
        self.view.userinterface_videocontrol()

    # Enregistre la position du clic sur le lecteur vidéo
    # Évènement appelé seulement en mode pointage
    def event_click_canvas(self, event):
        # Mode pointage (on rajoute autant de points qu'on veut)
        if(self.point_mode == PointMode.Enabled):
            # On crée un point qu'on rajoute à point_data
            pos_x, pos_y = event.x, event.y
            var_t = round(self.videoPlayer.get_playback_time(), 4)
            new_point = Point(round(pos_x  / self.point_scale, 4), round(pos_y / self.point_scale, 4), var_t)
            self.point_data.append(new_point)

            # On avance d'une frame
            self.videoPlayer.move_fwd_frame()

            print(f"Click on x={pos_x}; y={pos_y}. Point(x={new_point.get_x()}; y={new_point.get_y()}; {var_t}s)")

        # Mode échelle (on rajoute deux points pour calculer leur distance
        elif(self.point_mode == PointMode.SetScale):
            # On rajoute le point d'origine à scale_data
            pos_x, pos_y = event.x, event.y
            var_t = self.videoPlayer.get_playback_time()
            new_point = Point(pos_x, pos_y, var_t)
            self.scale_data.append(new_point)

            # On avance d'une frame
            self.videoPlayer.move_fwd_frame()

            # On passe à la 2ème étape (qui necéssite un second clic)
            self.point_mode = PointMode.SetScaleStep

        elif (self.point_mode == PointMode.SetScaleStep):
            # On rajoute le point d'origine à scale_data
            pos_x, pos_y = event.x, event.y
            var_t = self.videoPlayer.get_playback_time()
            new_point = Point(pos_x, pos_y, var_t)
            self.scale_data.append(new_point)

            # On sauvegarde les données du pointage d'échelle
            self.parent.set_scale(self.scale_data)

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

    # Appelé depuis View quand l'utilisateur veut ouvrir une vidéo
    def open_video(self):
        file_path = self.open_file()
        if file_path:
            self.parent.new_player(file_path)

    # Appelé depuis View quand l'utilisateur exporte ses données de pointage
    def exporter(self):
        # On affiche une erreur si l'utilisateur n'est pas en mode pointage ou n'a pas de données
        if(self.point_mode != PointMode.Enabled):
            self.parent.error_handler("Impossible d'exporter si le mode pointage est desactivé")
            return True
        if(len(self.point_data) == 0):
            self.parent.error_handler("Aucune donnée à sauvegarder")
            return True

        # On laisse l'utilisateur choisir où sauvegarder ses données
        file_path = self.save_file()
        if file_path:
            FileRepo.CSVExport(FileRepo, self.point_data, file_path)

        self.parent.new_player_toggle_point_mode()