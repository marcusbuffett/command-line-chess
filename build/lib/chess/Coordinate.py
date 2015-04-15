class Coordinate(tuple):

    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    def __reduce__(self):
        return (self.__class__, tuple(self))

    def __add__(self, other):
        return Coordinate(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):
        return Coordinate(self[0] - other[0], self[1] - other[1])
