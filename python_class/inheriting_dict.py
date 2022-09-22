import math


class Vector:
    def __setitem__(self, key, value):
        # if key == int:
        if not isinstance(key, str):
            raise TypeError("Can only take a string key")
        super().__setitem__(key, value)

    def __getitem__(self, key, value):
        # if type == int:
        if not isinstance(key, str):
            raise TypeError("Can only take a string")
        return super(Vector, self).__getitem__(self, key, value)

    def __init__(self, x: float, y: float)-> None:
        self.x = x
        self.y = y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector{self.x}i + {self.y}j"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        return 1


v1 = Vector(2, 4)
print(bool(v1))