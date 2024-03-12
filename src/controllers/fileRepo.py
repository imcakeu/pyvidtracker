import csv
from models.point import Point
from tkinter import filedialog

def CSVExport(points, path):
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["X", "Y"])
        for point in points:
            writer.writerow([point.get_x(), point.get_y()])
            
            
def open_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        return( file_path)
        
            
def exporter():
    point = Point(12, 34)
    point2 = Point(56, 78)
    point3 = Point(90, 0)

    myPoints = [point, point2, point3]
    CSVExport(myPoints, open_file())