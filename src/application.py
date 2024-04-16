import tkinter as tk
from controllers.controller import Controller
from views.view import View
class Application(tk.Tk):
    def __init__(self, file_name="default", is_pointage=False):
        super().__init__()
        self.title('VideoTracker Media Player')
        self.geometry("640x400+300+300")
        self.resizable(False, False)

        self.view = View(self)
        self.controller = Controller(self, self.view, file_name, is_pointage)
        self.file_name = file_name
        self.is_pointage = is_pointage

    # On crée un nouveau lecteur si on ouvre une nouvelle vidéo
    def new_player(self, file_name):
        self.controller.videoPlayer.canvas.delete('all')
        self.destroy()
        self.__init__(file_name, False)

    # On crée un nouveau lecteur mais avec le même fichier si on active le pointage
    # car VideoPlayer a un setup différent pour le pointage.
    def new_player_pointage(self):
        self.controller.videoPlayer.canvas.delete('all')
        self.destroy()
        self.__init__(self.file_name, not self.is_pointage)


if __name__ == '__main__':
    app = Application()
    app.mainloop()