from decimal import Decimal
from typing import final
import unittest

from dataclasses import dataclass


@dataclass
class Point:
    x: Decimal
    y: Decimal
    vx: Decimal
    vy: Decimal

    def get_last_pos(self, t: Decimal):
        # consider > 0 first
        _finalx = self.x + t * self.vx
        _finaly = self.y + t * self.vy
        modx = _finalx % 800
        mody = _finaly % 700
        new_vx = self.vx
        new_vy = self.vy
        collide = _finalx // 800 + _finaly // 700 - 0 # same point to be done.
        if modx % 2 == 0:  # same sig
            _finalx %= 800
        if modx % 2 == 1:
            _finalx = 800 - (_finalx % 800)
            new_vx = -new_vx
        if mody % 2 == 0:  # same sig
            _finaly %= 700
        if mody % 2 == 1:
            _finaly = 700 - (_finaly % 700)
            new_vy = -new_vy

        return (_finalx, _finaly, new_vx, new_vy, collide)


class Test(unittest.TestCase):
    def test_f1(self):
        p = Point(2, 1, -4, -5)
        (x, y, *_) = p.get_last_pos(1)
        self.assertTupleEqual((x, y), (2, 4))

    def test_f21(self):
        p = Point(20, 30, Decimal("0.3"), Decimal("0.5"))
        (x, y, vx, vy, c) = p.get_last_pos(20000)
        self.assertTupleEqual((x, y), (420, 230))
        self.assertTupleEqual((vx, vy), (Decimal('0.3'), Decimal('0.5')))
        self.assertEqual(c, 0)
    def test_f22(self):
        p = Point(798, 501, Decimal("0.8"), Decimal("-0.4"))
        (x, y, vx, vy, c) = p.get_last_pos(20000)
        self.assertTupleEqual((x, y), ())
        self.assertTupleEqual((vx, vy), (()))
        self.assertEqual(c,0)

    def test_f23(self):
        p = Point(515, 309, Decimal("-0.5"), Decimal("-0.3"))
        (x, y, vx, vy, c) = p.get_last_pos(20000)
        self.assertTupleEqual((x, y), ())
        self.assertTupleEqual((vx, vy), (()))
        self.assertEqual(c,0)



if __name__ == "__main__":
    unittest.main(verbosity=2)
