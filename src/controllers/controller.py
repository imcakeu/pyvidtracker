import tkinter as tk
from controllers.fileRepo import FileRepo
from models.point import Point
from controllers.videoPlayer import VideoPlayer
from tkinter import filedialog

class Controller:
    def __init__(self, parent, view):
        self.parent = parent
        self.view = view
        self.videoPlayer = VideoPlayer(self.parent, "default")

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            print("Saving on FilePath:: ", file_path)
            return(file_path)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print("Opening File: ", file_path)
            return file_path
        
    def exporter(self):
        point = Point(12, 34)
        point2 = Point(56, 78)
        point3 = Point(90, 0)

        myPoints = [point, point2, point3]
        FileRepo.CSVExport(FileRepo, myPoints, self.save_file(self))

    def open_video(self):
        file_path = self.open_file()
        if file_path:
            self.videoPlayer = VideoPlayer(self.parent, file_path)