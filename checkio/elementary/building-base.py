class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.north = self.south + width_NS

        self.west = west
        self.east = self.west + width_WE

        self.dwe = width_WE
        self.dns = width_NS
        self.h = height

        self._area = width_WE * width_NS

    def corners(self):
        return {
            'north-east': [self.north, self.east],
            'south-east': [self.south, self.east],
            'south-west': [self.south, self.west],
            'north-west': [self.north, self.west]
        }

    def area(self):
        return self._area

    def volume(self):
        return self._area * self.h

    def __repr__(self):
        return "%s(%s, %s, %s, %s, %s)" % (self.__class__.__name__, self.south, self.west, self.dwe, self.dns, self.h)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)

    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
