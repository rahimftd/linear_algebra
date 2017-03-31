import math

class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
            self.CANNOT_ANGLE_ZERO_VECTOR_MSG = 'Cannot compute angle with zero vector'

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        new_coords = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coords)

    def __sub__(self, v):
        new_coords = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coords)

    def times_scalar(self, s):
        new_coords = [s * x for x in self.coordinates]
        return Vector(new_coords)

    def magnitude(self):
        sum_of_squares = sum(x**2 for x in self.coordinates)
        return math.sqrt(sum_of_squares)

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1 / magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            self_normalized = self.normalized()
            v_normalized = v.normalized()

            angle_radians = math.acos(self_normalized.dot(v_normalized))
            if in_degrees:
                return angle_radians * 180 / math.pi
            return angle_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_ANGLE_ZERO_VECTOR_MSG)
            else:
                raise e
