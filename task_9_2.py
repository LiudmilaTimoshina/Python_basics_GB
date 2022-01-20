#2. Реализовать класс Road (дорога).

class Road:
    _length, _width = 0, 0

    def __init__(self, length, width, wigth_sq_mt, thickness):
        self._wigth_sq_mt, self._thickness, self._length, self._width = wigth_sq_mt / 1000, thickness, length, width

    def asphalt(self):
        return self._length * self._width * self._wigth_sq_mt * self._thickness


calc = Road(5000, 20, 25, 5)
print(calc.asphalt())