import math

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        
        def new_polar_point(self, rho, theta):
            return Point(rho * math.cos(theta), rho * math.sin(theta))

    factory = PointFactory()

if __name__ == "__main__":
    p = Point(2, 3)
    p2 = Point.factory.new_cartesian_point(2, 3)
    p3 = Point.factory.new_polar_point(2, 3)

    print(p)
    print(p2)
    print(p3)