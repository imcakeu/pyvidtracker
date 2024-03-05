import csv
import models.Point as classPoints

def CSVExport(points, path):
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["X", "Y"])
        for point in points:
            writer.writerow([point.get_x(), point.get_y()])
            
def exporter():
    point = classPoints.Point(12, 34)
    point2 = classPoints.Point(56, 78)
    point3 = classPoints.Point(90, 0)

    myPoints = [point, point2, point3]
    CSVExport(myPoints, "./fichier.csv")