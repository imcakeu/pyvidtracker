import tkinter as tk
from controllers.controller import Controller
from controllers.videoPlayer import VideoPlayer
from views.view import View
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('VideoTracker Media Player')
        self.geometry("640x400+300+300")
        self.resizable(False, False)

        self.view = View(self)
        self.controller = Controller(self, self.view, "default")

    def new_player(self, file_name):
        self.destroy()  # Destroy the main application window
        self.pack_forget()
        self.grid_forget()
        self.__init__()  # Recreate the application with a new instance
        self.controller = Controller(self, self.view, file_name)


if __name__ == '__main__':
    app = Application()
    app.mainloop()