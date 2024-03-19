import tkinter as tk
from controllers.controller import Controller
from controllers.videoPlayer import VideoPlayer
from views.view import View

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Video IHM')
        self.geometry("500x150+300+300")

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