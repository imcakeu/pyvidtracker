from tkinter import *
from tkinter import messagebox
import PIL.Image, PIL.ImageTk
import cv2
import os

class VideoPlayer:
    def __init__(self, controller, window, video_file):
        self.controller = controller
        self.window = window
        self.canvas = Canvas(window)
        self.canvas.pack()
        self.delay = 15   # ms
        if video_file == "default":
            self.open_file(self.get_video_file("compteur.mp4"))
        else:
            self.open_file(video_file)
        self.play_video()
        # self.toggle_play_pause()
        # self.window.mainloop()

    def play_pause(self, value):
        self.pause = value
        self.play_video()
        self.controller.view.play_pause_button.config(text=">" if self.pause else "II")

    def toggle_play_pause(self):
        self.play_pause(not self.pause)

    def move_back_frame(self):
        self.move_frame(-1)

    def move_fwd_frame(self):
        self.move_frame(1)

    def move_frame(self, count):
        if self.cap.isOpened():
            current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            new_frame = max(0, current_frame + count)
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, new_frame)
            self.play_pause(True)

    def start_video(self):
        if self.cap.isOpened():
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.toggle_play_pause()

    def end_video(self):
        if self.cap.isOpened():
            # Seek to the last frame of the video
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.cap.get(cv2.CAP_PROP_FRAME_COUNT) - 10)
            # Pause the video
            self.play_pause(False)

    def get_video_file(self, video_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        video_path = os.path.abspath(os.path.join(script_dir, '..', '..', 'resources', 'videos', video_name))
        return video_path

    def open_file(self, filename):
        self.pause = False
        self.filename = filename
        print("Reading video:", self.filename)
        self.cap = cv2.VideoCapture(self.filename)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = self.width, height = self.height)

    def get_frame(self):
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                if ret:
                    return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                else:
                    # Notify play_video method that video has ended
                    self.pause = True
                    return (False, None)
        except Exception as e:
            print("Error:", e)
            return (False, None)

    def play_video(self):
        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        if not self.pause:
            self.window.after(self.delay, self.play_video)

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()