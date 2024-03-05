import csv
from src.models.Point import *

def CSVExport(points, path):
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["X", "Y"])
        for point in points:
            writer.writerow([point.get_x(), point.get_y()])


point = Point(12, 34)
point2 = Point(56, 78)
point3 = Point(90, 0)

myPoints = [point, point2, point3]
CSVExport(myPoints, "./fichier.csv")