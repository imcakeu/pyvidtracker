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
        self.view = View(self)

        # Controllers
        self.controller = Controller(self, self.view)

        # set the controller to view
        self.view.setController(self.controller)
        

if __name__ == '__main__':
    app = Application()
    app.mainloop()