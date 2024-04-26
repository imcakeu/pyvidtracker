import sys
import tkinter as tk
import tkinter.messagebox
sys.path.append("./src")
import unittest
import coverage
from controllers.fileRepo import FileRepo
from models.point import Point
from application import Application
from controllers.controller import Controller
from tkinter import filedialog
import os
import random

'''
# Initialize coverage
cov = coverage.Coverage()
cov.start()
'''

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

    def test_saved_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path[:3] == 'C:/':
            self.assertTrue(Controller.save_file(self))

    
    def is_mp4_file(self,file_path):
        _, file_extension = os.path.splitext(file_path)
        return file_extension.lower() == '.mp4'


    def test_open_file_and_video(self):
        file_path = filedialog.askopenfilename()
        self.assertTrue(self.is_mp4_file(file_path), f"{file_path} n'est pas un fichier mp4.")


    def test_exporter1(self):
        self.parent = Application()
        self.is_point_mode = False
        if(not self.is_point_mode):
            self.assertTrue(Controller.exporter(self))
        else:
            self.assertTrue(False)
        
    
    def test_get_x(self):
        point = Point(2, 3, 4)
        self.assertEqual(point.get_x(), 2)

    def test_get_y(self):
        point = Point(2, 3, 4)
        self.assertEqual(point.get_y(), 3)

    def test_get_t(self):
        point = Point(2, 3, 4)
        self.assertEqual(point.get_t(), 4)

    '''
    lorsque les deux fonctions test de la fonction exporter sont lancer lors de la même exécution, 
    test_exporter2 affiche une  erreur qui n'existe pas quand on les exécutes séparément
    '''
    def test_exporter2(self):
        self.parent = Application()
        self.is_point_mode = True
        self.point_data = []
        if(len(self.point_data) == 0):
            self.assertTrue(Controller.exporter(self))
        else:
            self.assertTrue(False)



if __name__ == '__main__':
    '''# Stop coverage
    cov.stop()
    # Save coverage results
    cov.save()
    # Generate coverage report
    cov.report()'''
    # Run unit test
    unittest.main()