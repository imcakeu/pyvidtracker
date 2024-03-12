import tkinter as tk
from controllers.controller import Controller
# from controllers.videoPlayer import VideoPlayer
from models.video import Video
from views.view import View

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Video IHM')

        # Views
        view = View(self)

        # Models
        video = Video()

        # Controllers
        controller = Controller(video, view)

        # set the controller to view
        view.setController(controller)
        

if __name__ == '__main__':
    app = Application()
    app.mainloop()