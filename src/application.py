import tkinter as tk
from controllers.controller import Controller
from controllers.videoPlayer import VideoPlayer
from views.view import View
class Application(tk.Tk):
    def __init__(self, file_name="default"):
        super().__init__()
        self.title('VideoTracker Media Player')
        self.geometry("640x400+300+300")
        self.resizable(False, False)

        self.view = View(self)
        self.controller = Controller(self, self.view, file_name)

    def new_player(self, file_name):
        self.controller.videoPlayer.canvas.delete('all')
        self.destroy()  # Destroy the main application window
        self.__init__(file_name)  # Recreate the application with a new instance
        # self.controller = Controller(self, self.view, file_name)


if __name__ == '__main__':
    app = Application()
    app.mainloop()