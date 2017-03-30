class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        new_vector = []
        for i in range(len(self.coordinates)):
            new_coord = self.coordinates[i] + v.coordinates[i]
            new_vector.append(new_coord)
        return Vector(new_vector)

    def __sub__(self, v):
        new_vector = []
        for i in range(len(self.coordinates)):
            new_coord = self.coordinates[i] - v.coordinates[i]
            new_vector.append(new_coord)
        return Vector(new_vector)

    def scalar_multiply(self, s):
        new_vector = []
        for i in range(len(self.coordinates)):
            new_coord = self.coordinates[i] * s
            new_vector.append(new_coord)
        return Vector(new_vector)