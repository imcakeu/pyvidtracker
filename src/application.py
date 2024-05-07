import math
import os
import tkinter as tk
from tkinter import simpledialog

from controllers.controller import Controller
from models.pointMode import PointMode
from models.videoPlayer import VideoPlayer
from views.view import View

# VideoTracker est un logiciel qui permet à l'utilisateur de lire des vidéos et
# utiliser le système de "pointage" pour placer des points et d'enregistrer des données.
# Lancez ce script pour commencer.
class Application(tk.Tk):
    def __init__(self, file_name="default", point_mode=PointMode.Disabled, point_scale=1, point_origin = [0, 0]):
        super().__init__()
        # Paramétrage fênetre
        self.file_path = VideoPlayer.get_video_file(self, "compteur.mp4")
        self.title('VideoTracker Media Player')
        self.dimensions = VideoPlayer.get_video_dimensions(self,self.file_path)
        self.width, self.height = self.dimensions
        self.geometry(f"{self.width}x{self.height+50}")
        self.resizable(False, False)
        
        #ERREUR --> Chemin d'accès invalide
        #self.iconbitmap(self.get_image_file("icon.ico"))

        # Variables
        self.file_name = file_name
        self.point_mode = point_mode
        self.point_scale = point_scale
        # Valeur par défaut (milieu de l'écran)
        if point_origin == [0, 0]:
            self.point_origin = [self.width / 2, self.height / 2]
        else:
            self.point_origin = point_origin

        # Création du view (fênetre) et controller (pointage et lecteur vidéo)
        self.view = View(self)
        self.controller = Controller(self, self.view, file_name, point_mode, point_scale)

        if(point_mode == PointMode.SetScale):
            tk.messagebox.showinfo("Définir échelle", "Vous allez à présent définir l'échelle réelle sur cette vidéo. Faites un premier clic, puis un deuxième. Définissez ensuite la distance réelle entre ces deux points (dans l'unité de votre choix).")

        print("Current mode:", point_mode, "| Point scale:", point_scale)

    # Détruit le lécteur précedent et redémarre Application avec de nouveaux paramètres.
    # Appelé dans View quand l'utilisateur ouvre une vidéo.
    def new_player(self, file_name):
        self.controller.videoPlayer.canvas.delete('all')
        self.destroy()
        self.__init__(file_name, PointMode.Disabled, 1, [0, 0])

    # Idem, mais cette fois ci redémarre la *même vidéo* en basculant le mode pointage.
    # Appelé dans View quand l'utilisateur active/desactive ce mode.
    def new_player_toggle_point_mode(self):
        self.controller.videoPlayer.canvas.delete('all')
        self.destroy()

        new_point_mode = PointMode.Disabled
        if(self.point_mode == PointMode.Disabled):
            new_point_mode = PointMode.Enabled
        self.__init__(self.file_name, new_point_mode, self.point_scale, self.point_origin)

    # Idem, mais cette fois ci redémarre la *même vidéo* en basculant le mode échelle.
    # Appelé dans View quand l'utilisateur active/desactive ce mode.
    def new_player_toggle_scale_mode(self):
        self.controller.videoPlayer.canvas.delete('all')
        self.destroy()
        new_point_mode = PointMode.Disabled
        if(self.point_mode != PointMode.SetScaleStep):
            new_point_mode = PointMode.SetScale
        self.__init__(self.file_name, new_point_mode)

    # Définit l'échelle pixels / mètres sur la vidéo
    # Appelé dans controller après que les deux points sont définis
    def set_scale(self, scale_data):
        value = simpledialog.askfloat("Définir échelle", "Définissez la distance réelle entre ces deux points.")
        point_distance = math.sqrt( (scale_data[1].get_x() - scale_data[0].get_x())**2 + (scale_data[1].get_y()- scale_data[0].get_y())**2 )
        self.point_scale = point_distance / value
        self.point_origin = [scale_data[0].get_x(), scale_data[0].get_y()]
        self.new_player_toggle_point_mode()

    def get_image_file(self, image_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        video_path = os.path.abspath(os.path.join(script_dir,'..', 'resources', 'images', image_name))
        return video_path

    # Affiche une boîte de dialogue d'erreur et affiche l'erreur dans le terminal.
    def error_handler(self, error):
        print("ERROR:", error)
        tk.messagebox.showerror("Erreur", error)

if __name__ == '__main__':
    app = Application()
    app.mainloop()