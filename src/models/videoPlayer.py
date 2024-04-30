import os
import cv2
import PIL.Image, PIL.ImageTk

from tkinter import *

from models.pointMode import PointMode


# Crée un canvas et y affiche une vidéo.
class VideoPlayer:
    def __init__(self, controller, window, video_file, point_mode):
        # Variables
        self.controller = controller
        self.window = window
        self.delay = 15
        self.point_mode = point_mode

        # On crée le canvas qui affiche le lecteur vidéo.
        # Si on n'est pas en mode pointage on crée simplement le canvas.
        # Si on est en mode pointage, on paramètre le curseur de l'utilisateur de sorte à
        # ce qu'il soit en croix (+) pour indiquer le mode pointage.
        if(self.point_mode == PointMode.Disabled):
            self.canvas = Canvas(window)
        else:
            self.canvas = Canvas(window, cursor="cross")    
        self.canvas.grid(column=0,row=0, columnspan=15)

        # L'ouverture initiale du lecteur ouvre une vidéo par défaut.
        # Si un fichier à été precisé (ouverture vidéo de l'utilisateur) il sera ouvert.
        if video_file == "default":
            self.open_file(self.get_video_file("compteur.mp4"))
        else:
            self.open_file(video_file)

        # Quand tout est parametré, la vidéo commence à jouer.
        # Elle est mise en pause automatiquement si l'utilisateur est en mode pointage.
        self.play_video()
        self.pause = (self.point_mode == PointMode.Enabled)

    #### Contrôles
    ###

    # Bascule entre pause et lire (II / >)
    def toggle_play_pause(self):
        self.play_pause(not self.pause)

    # Recule d'une frame (<)
    def move_back_frame(self):
        if self.cap.isOpened():
            self.play_pause(True)
            current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame - 2)

    # Avance d'une frame (>)
    def move_fwd_frame(self):
        if self.cap.isOpened():
            self.play_pause(True)
            current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame + 1)

    # Reprend la vidéo au tout début (<<)
    def start_video(self):
        if self.cap.isOpened():
            self.play_pause(True)
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ## Passe la vidéo à la toute fin (>>)
    def end_video(self):
        if self.cap.isOpened():
            self.play_pause(True)
            last_frame = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, last_frame - 5)
            self.play_pause(False)

    ####
    #### Fin

    # Prend en compte la valeur donnée pour mettre en pause ou reprendre la lecture de la vidéo
    # Met à jour l'affichage du bouton lire/pause
    def play_pause(self, value):
        self.pause = value
        self.play_video()
        self.controller.view.play_pause_button.config(text=">" if self.pause else "II")

    # Retourne le path d'un fichier vidéo dans le dossier local resources/videos à partir de son nom.
    def get_video_file(self, video_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        video_path = os.path.abspath(os.path.join(script_dir, '..', '..', 'resources', 'videos', video_name))
        return video_path

    # Ouvre un fichier vidéo à partir d'un path
    def open_file(self, file_path):
        self.file_path = file_path
        self.pause = False

        self.cap = cv2.VideoCapture(self.file_path)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = 640, height = 360)

        print("Reading video:", self.file_path)

    # Extrait l'image à afficher du fichier vidéo
    def get_frame(self):
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                if ret:
                    return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                else:
                    # Notify play_video method that video has ended
                    self.pause = True
                    return (False, None)
        except Exception as e:
            print("Error:", e)
            return (False, None)

    # Joue la vidéo
    def play_video(self):
        ret, frame = self.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        if not self.pause:
            self.window.after(self.delay, self.play_video)

    # Get the playback time in seconds
    def get_playback_time(self):
        if self.cap.isOpened():
            playback_msec = self.cap.get(cv2.CAP_PROP_POS_MSEC)
            playback_sec = playback_msec / 1000
            return playback_sec
        else:
            return None

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()