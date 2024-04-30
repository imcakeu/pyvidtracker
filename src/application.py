import tkinter as tk

from controllers.controller import Controller
from models.pointMode import PointMode
from views.view import View

# VideoTracker est un logiciel qui permet à l'utilisateur de lire des vidéos et
# utiliser le système de "pointage" pour placer des points et d'enregistrer des données.
# Lancez ce script pour commencer.
class Application(tk.Tk):
    def __init__(self, file_name="default", point_mode=PointMode.Disabled):
        super().__init__()
        # Paramétrage fênetre
        self.title('VideoTracker Media Player')
        self.geometry("640x400+300+300")
        self.resizable(True, True)

        # Variables
        self.file_name = file_name
        self.point_mode = point_mode

        # Création du view (fênetre) et controller (pointage et lecteur vidéo)
        self.view = View(self)
        self.controller = Controller(self, self.view, file_name, point_mode)

        print("Current mode: ", point_mode)

    # Détruit le lécteur précedent et redémarre Application avec de nouveaux paramètres.
    # Appelé dans View quand l'utilisateur ouvre une vidéo.
    def new_player(self, file_name):
        self.controller.videoPlayer.canvas.delete('all')
        self.destroy()
        self.__init__(file_name, PointMode.Disabled)

    # Idem, mais cette fois ci redémarre la *même vidéo* en basculant le mode pointage.
    # Appelé dans View quand l'utilisateur active/desactive ce mode.
    def new_player_toggle_point_mode(self):
        self.controller.videoPlayer.canvas.delete('all')
        self.destroy()

        new_point_mode = PointMode.Disabled
        if(self.point_mode == PointMode.Disabled):
            new_point_mode = PointMode.Enabled
        self.__init__(self.file_name, new_point_mode)

    # Affiche une boîte de dialogue d'erreur et affiche l'erreur dans le terminal.
    def error_handler(self, error):
        print("ERROR:", error)
        tk.messagebox.showerror(self.title, error)

if __name__ == '__main__':
    app = Application()
    app.mainloop()