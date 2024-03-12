import tkinter as tk
from src.controllers.fileRepo import FileRepo
from src.models.point import Point
from src.controllers.videoPlayer import VideoPlayer

class Controller:
    def __init__(self, view, videoPlayer):
        self.view = view
        self.videoPlayer = videoPlayer
        
    def exporter(self):
        point = Point(12, 34)
        point2 = Point(56, 78)
        point3 = Point(90, 0)

        myPoints = [point, point2, point3]
        FileRepo.exporter(FileRepo, myPoints)