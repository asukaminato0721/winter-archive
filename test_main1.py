from dataclasses import dataclass
from decimal import Decimal


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
        if 0 < nx < w and ny <= 0: #8
            return Point(nx, -ny, self.vx, -self.vy, self.cnt + 1)
        return Point(nx, ny, self.vx, self.vy, self.cnt)


import unittest


class Test(unittest.TestCase):
    def test_f1(self):
        p = Point(2, 1, -4, -5)
        newp = p.get_next_sec()
        self.assertTupleEqual((newp.x, newp.y), (2, 4))

    def test_f21(self):
        p = Point(20, 30, Decimal("0.3"), Decimal("0.5"))
        for i in range(20000):
            p = p.get_next_sec()
        self.assertTupleEqual((p.x, p.y), (380, 230))
        self.assertTupleEqual((p.vx, p.vy), (Decimal("-0.3"), Decimal("0.5")))
        self.assertEqual(p.cnt, 21)

    def test_f22(self):
        p = Point(798, 501, Decimal("0.8"), Decimal("-0.4"))
        for i in range(20000):
            p = p.get_next_sec()
        self.assertTupleEqual((p.x, p.y), (798, 499))
        self.assertTupleEqual((p.vx, p.vy),  (Decimal('0.8'), Decimal('0.4')))
        self.assertEqual(p.cnt, 28)

    def test_f23(self):
        p = Point(515, 309, Decimal("-0.5"), Decimal("-0.3"))
        for i in range(20000):
            p = p.get_next_sec()
        self.assertTupleEqual((p.x, p.y), (115, 91))
        self.assertTupleEqual((p.vx, p.vy), (Decimal("-0.5"), Decimal("0.3")))
        self.assertEqual(p.cnt, 20)
    

if __name__ == "__main__":
    unittest.main(verbosity=2)
