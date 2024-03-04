from dataclasses import dataclass
from decimal import Decimal
from sympy import Segment2D, Point as Point1

w = 800
h = 700


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
        return Point(nx, ny, self.vx, self.vy, self.cnt)


import unittest


class Test(unittest.TestCase):
    def test_f5(self):
        p1 = Point(767, 27, Decimal("-0.2"), Decimal("-0.7"))
        p2 = Point(267, 173, Decimal("0.3"), Decimal("0.5"))
        cnt = 0
        for i in range(20000):
            if (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 <= 1:
                cnt +=1
            p1 = p1.get_next_sec()
            p2 = p2.get_next_sec()
        self.assertEqual(cnt, 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
