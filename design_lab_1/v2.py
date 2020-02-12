class V2:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def add(self, other):
        return self.__add__(other)

    def mul(self, other):
        return self.__mul__(other)

    def __str__(self):
        return 'V2[{0}, {1}]'.format(self._x, self._y)

    def __add__(self, other):
        add_x = self.x + other.x
        add_y = self.y + other.y
        return V2(add_x, add_y)

    def __mul__(self, other):
        mul_x = self.x * other
        mul_y = self.y * other
        return V2(mul_x, mul_y)
