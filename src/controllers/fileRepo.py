import csv
from models.point import Point
from tkinter import filedialog

class FileRepo:
    def __init__(self):
        pass

    def CSVExport(self, points, path):
        with open(path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["X", "Y"])
            for point in points:
                writer.writerow([point.get_x(), point.get_y()])


    def open_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            return( file_path)


    def exporter(self, points):
        self.CSVExport(points, self.open_file(self))