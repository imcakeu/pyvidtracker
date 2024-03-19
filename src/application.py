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

        # Views
        view = View(self)

        # Controllers
        videoPlayer = VideoPlayer(self)
        controller = Controller(view)

        # set the controller to view
        view.setController(controller)
        

if __name__ == '__main__':
    app = Application()
    app.mainloop()