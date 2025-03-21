import numpy

class Solution():

    def __init__(self,times,points):

        self.times  = times
        self.points = points

    @property
    def times(self):
        return self._times/(24*60*60)

    @times.setter
    def times(self,values:numpy.ndarray):
        self._times = numpy.ravel(values).reshape((1,-1))*(24*60*60)

    @property
    def points(self):
        return self._points/0.3048

    @points.setter
    def points(self,values:numpy.ndarray):
        self._points = numpy.ravel(values).reshape((-1,1))*0.3048

    @property
    def press(self):
        return self._press/6894.76

    @press.setter
    def press(self,values):
        self._press = values*6894.76