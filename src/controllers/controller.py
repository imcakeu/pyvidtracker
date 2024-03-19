import tkinter as tk
from controllers.fileRepo import FileRepo
from models.point import Point
from controllers.videoPlayer import VideoPlayer
from tkinter import filedialog

class Controller:
    def __init__(self, view):
        self.view = view

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            print("Saving on FilePath:: ", file_path)
            return(file_path)

    def open_file(self):
        file_path = filedialog.askopenfile()
        if file_path:
            print("Opening File: ", file_path)
            return(file_path)
        
    def exporter(self):
        point = Point(12, 34)
        point2 = Point(56, 78)
        point3 = Point(90, 0)

        myPoints = [point, point2, point3]
        FileRepo.CSVExport(FileRepo, myPoints, self.save_file(self))

    def open_video(self):
        VideoPlayer.open_file(VideoPlayer, self.open_file(self))