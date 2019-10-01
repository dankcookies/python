from unittest import TestCase
import math


class TestGeometry(TestCase):
    def test_rect_area(self):
        from geometry import rect_area
        self.assertEqual(rect_area(4, 5), 20)
        self.assertEqual(rect_area(1.2, 4), 4.8)

    def test_rect_perimeter(self):
        from geometry import rect_perimeter
        self.assertEqual(rect_perimeter(4, 5), 18)
        self.assertEqual(rect_perimeter(1.2, 4), 10.4)

    def test_triangle_area(self):
        from geometry import triangle_area
        self.assertEqual(triangle_area(10, 5), 25)

    def test_circle_area(self):
        from geometry import circle_area
        self.assertEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(3), 28.27431, 3)

    def test_circle_circumference(self):
        from geometry import circle_circumference
        self.assertEqual(circle_circumference(1), math.tau)
        self.assertAlmostEqual(circle_circumference(3), 18.8495, 3)

    def test_calculate_slope(self):
        from geometry import calculate_slope
        self.assertAlmostEqual(calculate_slope(0, 4, 3, 0), -1.33333, 3)
        self.assertEqual(calculate_slope(0, 0, 4, 4), 1)
