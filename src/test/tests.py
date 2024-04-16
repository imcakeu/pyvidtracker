import sys
sys.path.append("../")
import unittest
from controllers.fileRepo import FileRepo
from models.point import Point
import os
import random



class MyTestClass(unittest.TestCase):
    def setup(self):
        pass


    def test_csv_file(self):
        point = Point(2, 3)
        point2 = Point(4, 7)
        point3 = Point(9, 1)
        myPoints = [point, point2, point3]
        path = FileRepo.CSVExport(FileRepo, myPoints, './test')

        self.assertTrue(FileRepo.is_csv_file(path), f"{path} n'est pas un fichier CSV.")
        

    def tearDown(self):
        pass


    def test_txt(self):
        point = Point(random.randint(0,100), random.randint(0,100))
        point2 = Point(random.randint(0,100), random.randint(0,100))
        point3 = Point(random.randint(0,100), random.randint(0,100))
        myPoints = [point, point2, point3]
        path = FileRepo.CSVExport(FileRepo, myPoints, './test.txt')
        self.assertTrue(FileRepo.is_csv_file(path), f"{path} n'est pas un fichier CSV.")


    def test_saved_values(self):
        pass




if __name__ == '__main__':
    unittest.main()