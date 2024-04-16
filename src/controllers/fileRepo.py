import sys
sys.path.append("../")
import csv
from models.point import Point
import os


class FileRepo:
    def __init__(self):
        pass
    
    def is_csv_file(file_path):
        _, file_extension = os.path.splitext(file_path)
        return file_extension.lower() == '.csv'
    
    def CSVExport(self, points, path):
        if not self.is_csv_file(path):
            path += '.csv'
        with open(path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["X", "Y"])
            for point in points:
                writer.writerow([point.get_x(), point.get_y()])
        return path
    
    
