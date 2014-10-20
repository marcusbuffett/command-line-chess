class Coordinate(tuple) :

    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    def __reduce__(self) :
        return (self.__class__, tuple(self))

    def __add__(self, other):
        return (self[0] + other[0], self[1] + other[1])
        #return tuple(sum(x) for x in zip(self, other))

    def __sub__(self, other):
        return self.__add__(-i for i in other)

