import tkinter as tk
import controllers.Controller as controllerClass
import models.Video as videoClass
import views.view as viewClass

class Application(tk.Tk):
    def __init__(self):

        super().__init__()
        self.title('Video Tracker')
        # create a video model
        video = videoClass.Video()
        # create a view and place it on the root window
        view = viewClass.View(self)

        # create a controller
        controller = controllerClass.Controller(video, view)

        # set the controller to view
        view.setController(controller)
        

if __name__ == '__main__':
    app = Application()
    app.mainloop()