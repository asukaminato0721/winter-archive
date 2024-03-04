from dataclasses import dataclass
from decimal import Decimal
from sympy import Segment2D, Point as Point1


def check(p):
    if 

w = 800
h = 700


def cross(s1: Segment2D, s2: Segment2D):
    p = s1.intersection(s2)
    if p == []:
        return False
    return True


@dataclass
class Point:
    x: Decimal
    y: Decimal
    vx: Decimal
    vy: Decimal
    cnt: int = 0

    def get_next_sec(self):
        nx = self.x + self.vx
        ny = self.y + self.vy
        # print(nx, ny)
        # 分类讨论，共 9 类
        if nx <= 0 and ny <= 0:  # 1
            return Point(-nx, -ny, -self.vx, -self.vy, self.cnt + 1)
        if nx <= 0 and 0 < ny < h:  # 2
            return Point(-nx, ny, -self.vx, self.vy, self.cnt + 1)
        if nx <= 0 and ny >= h:  # 3
            return Point(-nx, h - (ny - h), -self.vx, -self.vy, self.cnt + 1)
        if 0 < nx < w and ny >= h:  # 4
            return Point(nx, h - (ny - h), self.vx, -self.vy, self.cnt + 1)
        if nx >= w and ny >= h:  # 5
            return Point(w - (nx - w), h - (ny - h), -self.vx, -self.vy, self.cnt + 1)
        if nx >= w and 0 < ny < h:  # 6
            return Point(w - (nx - w), ny, -self.vx, self.vy, self.cnt + 1)
        if nx >= w and ny <= 0:  # 7
            return Point(w - (nx - w), -ny, -self.vx, -self.vy, self.cnt + 1)
        if 0 < nx < w and ny <= 0:  # 8
            return Point(nx, -ny, self.vx, -self.vy, self.cnt + 1)
        if cross(
            Segment2D((self.x, self.y), (nx, ny)),
            Segment2D((100, 300), (600, 300)),
        ):
            return Point(nx, 300 - (ny - 300), self.vx, -self.vy, self.cnt)
        return Point(nx, ny, self.vx, self.vy, self.cnt)


import unittest


class Test(unittest.TestCase):
    def test_cross(self):
        self.assertTrue(cross(Segment2D((0, 0), (1, 1)), Segment2D((0, 1), (1, 0))))
        self.assertTrue(not cross(Segment2D((0, 0), (1, 0)), Segment2D((1, 1), (0, 1))))

    def test_f31(self):
        p = Point(10, 10, Decimal("0.1"), Decimal("0.6"))
        for i in range(20000):
            p = p.get_next_sec()
        self.assertTupleEqual((p.x, p.y), (0, 0))
    def test_f32(self):
        p = Point(296, 316, Decimal("2.1"), Decimal("-0.9"))
        for i in range(20000):
            p = p.get_next_sec()
        self.assertTupleEqual((p.x, p.y), (0, 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
