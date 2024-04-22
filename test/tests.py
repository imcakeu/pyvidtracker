import sys
sys.path.append("./src")
import unittest
import coverage
from controllers.fileRepo import FileRepo
from models.point import Point
import os
import random

# Initialize coverage
cov = coverage.Coverage()
cov.start()

class MyTestClass(unittest.TestCase):
    def setup(self):
        pass

    def test_csv_file(self):
        point = Point(2, 3, 0.15)
        point2 = Point(4, 7, 0.34)
        point3 = Point(9, 1, 0.72)
        myPoints = [point, point2, point3]
        path = FileRepo.CSVExport(FileRepo, myPoints, 'test')

        self.assertTrue(FileRepo.is_csv_file(path), f"{path} n'est pas un fichier CSV.")

    def tearDown(self):
        pass

    def test_txt(self):
        point = Point(random.randint(0,100), random.randint(0,100), 0.12)
        point2 = Point(random.randint(0,100), random.randint(0,100), 0.36)
        point3 = Point(random.randint(0,100), random.randint(0,100), 0.48)
        myPoints = [point, point2, point3]
        path = FileRepo.CSVExport(FileRepo, myPoints, './test.txt')
        self.assertTrue(FileRepo.is_csv_file(path), f"{path} n'est pas un fichier CSV.")

    def test_saved_values(self):
        pass

if __name__ == '__main__':
    # Stop coverage
    cov.stop()
    # Save coverage results
    cov.save()
    # Generate coverage report
    cov.report()
    # Run unit test
    unittest.main()