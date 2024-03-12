class Point():
    def __init__(self, x, y):
        self.__x = x  # private variable for X
        self.__y = y  # private variable for Y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y