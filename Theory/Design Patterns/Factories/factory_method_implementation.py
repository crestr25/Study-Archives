import math

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * math.cos(theta), rho * math.sin(theta))


if __name__ == "__main__":
    p = Point(2, 3)
    p2 = Point.new_cartesian_point(2, 3)
    p3 = Point.new_polar_point(2, 3)

    print(p)
    print(p2)
    print(p3)