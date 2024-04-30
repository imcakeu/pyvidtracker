import sys
sys.path.append("./src")

import os
import unittest
import random

from controllers.fileRepo import FileRepo
from models.point import Point

class MyTestClass(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_csv_file(self):
        point = Point(2, 3, 0.15)
        point2 = Point(4, 7, 0.34)
        point3 = Point(9, 1, 0.72)
        myPoints = [point, point2, point3]
        path = FileRepo.CSVExport(FileRepo, myPoints, 'test')

        self.assertTrue(FileRepo.is_csv_file(path), f"{path} n'est pas un fichier CSV.")

    def test_txt(self):
        point = Point(random.randint(0,100), random.randint(0,100), 0.12)
        point2 = Point(random.randint(0,100), random.randint(0,100), 0.36)
        point3 = Point(random.randint(0,100), random.randint(0,100), 0.48)
        myPoints = [point, point2, point3]
        path = FileRepo.CSVExport(FileRepo, myPoints, './test.txt')
        self.assertTrue(FileRepo.is_csv_file(path), f"{path} n'est pas un fichier CSV.")
    
    def is_mp4_file(self, file_path):
        _, file_extension = os.path.splitext(file_path)
        return file_extension.lower() == '.mp4'
    
    def test_get_x(self):
        point = Point(2, 3, 4)
        self.assertEqual(point.get_x(), 2)

    def test_get_y(self):
        point = Point(2, 3, 4)
        self.assertEqual(point.get_y(), 3)

    def test_get_t(self):
        point = Point(2, 3, 4)
        self.assertEqual(point.get_t(), 4)


if __name__ == '__main__':
    # Run unit test
    unittest.main()