import csv
from models.point import Point

class FileRepo:
    def __init__(self):
        pass

    def CSVExport(self, points, path):
        with open(path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["X", "Y"])
            for point in points:
                writer.writerow([point.get_x(), point.get_y()])