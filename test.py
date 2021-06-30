import unittest
from decimal import Decimal
from vector import Vector
from line import Line
from plane import Plane
from linsys import LinearSystem

# Vector
v1 = Vector([1,2,3])
v2 = Vector([5,-6,7])
v3 = Vector([6,8,10])
k0 = 0
k = -2

class TestVector(unittest.TestCase):

    def test_001_add(self):
        self.assertEqual(v1+v2, Vector([6,-4,10]))

    def test_002_subtract(self):
        self.assertEqual(v1-v3, Vector([-5,-6,-7]))

    def test_003_mult_by_scalar(self):
        self.assertEqual(v1*k0, Vector([0,0,0]))

    def test_004_mult_by_scalar(self):
        self.assertEqual(v2*k, Vector([-10,12,-14]))

    def test_005_dot_product(self):
        self.assertEqual(v1*v2, 14)

    def test_006_len(self):
        self.assertEqual(v1.len(), Decimal(14).sqrt())

    def test_007_cross_product(self):
        self.assertEqual(v1.cross_product(v2), Vector([32,8,-16]))


# Line
l1 = Line(Vector([2,4]),8)
l2 = Line(Vector([-4,-8]),-16)
l3 = Line(Vector([5,6]),7)
l4 = Line(Vector([2,4]),5)

class TestLine(unittest.TestCase):

    def test_008_is_parallel(self):
        self.assertTrue(l1.is_parallel(l2))

    def test_009_is_parallel(self):
        self.assertFalse(l1.is_parallel(l3))

    def test_010_is_same_line(self):
        self.assertEqual(l1,l2)

    def test_011_is_parallel_not_same_line(self):
        self.assertTrue(l1.is_parallel(l4) and l2 != l4)

    def test_012_intersection(self):
        self.assertEqual(l1.intersection(l3),(-2.5,3.25))



# Plane
p_1 = Plane(Vector([1,2,3]),4)
p_2 = Plane(Vector([2,4,6]),0)
p_3 = Plane(Vector([4,5,6]),7)
p_4 = Plane(Vector([-1,-2,-3]),-4)

class TestPlane(unittest.TestCase):

    def test_013_is_parallel(self):
        self.assertTrue(p_1.is_parallel(p_2))

    def test_014_is_parallel(self):
        self.assertFalse(p_1.is_parallel(p_3))

    def test_015_is_same_plane(self):
        self.assertEqual(p_1,p_4)

    def test_016_is_parallel_not_same_plane(self):
        self.assertTrue(p_1.is_parallel(p_2) and p_1 != p_2)



# Linear System
p0 = Plane(Vector([1,1,1]), 1)
p1 = Plane(Vector([0,1,0]), 2)
p2 = Plane(Vector([1,1,-1]), 3)
p3 = Plane(Vector([1,0,-2]), 2)

s = LinearSystem([p0,p1,p2,p3])


class TestLinSys(unittest.TestCase):

    def test_017_swap_rows(self):
        s.swap_rows(0,1)
        self.assertTrue(s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3)

    def test_018_swap_rows(self):
        s.swap_rows(1,3)
        self.assertTrue(s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0)

    def test_019_swap_rows(self):
        s.swap_rows(3,1)
        self.assertTrue(s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3)


    def test_020_multiply_coefficient_and_row(self):
        s.multiply_coefficient_and_row(1,0)
        self.assertTrue(s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3)

    def test_021_multiply_coefficient_and_row(self):
        s.multiply_coefficient_and_row(-1,2)
        self.assertTrue(s[0] == p1 and
                        s[1] == p0 and
                        s[2] == Plane(Vector([-1,-1,1]), -3) and
                        s[3] == p3)

    def test_022_multiply_coefficient_and_row(self):
        s.multiply_coefficient_and_row(10,1)
        self.assertTrue(s[0] == p1 and
                        s[1] == Plane(Vector([10,10,10]), 10) and
                        s[2] == Plane(Vector([-1,-1,1]), -3) and
                        s[3] == p3)

    def test_023_add_multiple_times_row_to_row(self):
        s.add_multiple_times_row_to_row(0,0,1)
        self.assertTrue(s[0] == p1 and
                        s[1] == Plane(Vector([10,10,10]), 10) and
                        s[2] == Plane(Vector([-1,-1,1]), -3) and
                        s[3] == p3)

    def test_024_add_multiple_times_row_to_row(self):
        s.add_multiple_times_row_to_row(1,0,1)
        self.assertTrue(s[0] == p1 and
                        s[1] == Plane(Vector([10,11,10]), 12) and
                        s[2] == Plane(Vector([-1,-1,1]), -3) and
                        s[3] == p3)

    def test_025_add_multiple_times_row_to_row(self):
        s.add_multiple_times_row_to_row(-1,1,0)
        self.assertTrue(s[0] == Plane(Vector([-10,-10,-10]), -10) and
                        s[1] == Plane(Vector([10,11,10]), 12) and
                        s[2] == Plane(Vector([-1,-1,1]), -3) and
                        s[3] == p3)


    def test_026_compute_triangular_form(self):
        p1 = Plane(Vector([1,1,1]), 1)
        p2 = Plane(Vector([0,1,1]), 2)
        s = LinearSystem([p1,p2])
        t = s.compute_triangular_form()
        self.assertTrue(t[0] == p1 and
                        t[1] == p2)

    def test_027_compute_triangular_form(self):
        p1 = Plane(Vector([1,1,1]), 1)
        p2 = Plane(Vector([1,1,1]), 2)
        s = LinearSystem([p1,p2])
        t = s.compute_triangular_form()
        self.assertTrue(t[0] == p1 and
                        t[1] == Plane(constant_term=1))

    def test_028_compute_triangular_form(self):
        p1 = Plane(Vector([1,1,1]), 1)
        p2 = Plane(Vector([0,1,0]), 2)
        p3 = Plane(Vector([1,1,-1]), 3)
        p4 = Plane(Vector([1,0,-2]), 2)
        s = LinearSystem([p1,p2,p3,p4])
        t = s.compute_triangular_form()
        self.assertTrue(t[0] == p1 and
                        t[1] == p2 and
                        t[2] == Plane(Vector([0,0,-2]), 2) and
                        t[3] == Plane())

    def test_029_compute_triangular_form(self):
        p1 = Plane(Vector([0,1,1]), 1)
        p2 = Plane(Vector([1,-1,1]), 2)
        p3 = Plane(Vector([1,2,-5]), 3)
        s = LinearSystem([p1,p2,p3])
        t = s.compute_triangular_form()
        self.assertTrue(t[0] == Plane(Vector([1,-1,1]), 2) and
                        t[1] == Plane(Vector([0,1,1]), 1) and
                        t[2] == Plane(Vector([0,0,-9]), -2))


    def test_030_compute_rref(self):
        p1 = Plane(Vector([1,1,1]), 1)
        p2 = Plane(Vector([0,1,1]), 2)
        s = LinearSystem([p1,p2])
        r = s.compute_rref()
        self.assertTrue(r[0] == Plane(Vector([1,0,0]), -1) and
                        r[1] == p2)

    def test_031_compute_rref(self):
        p1 = Plane(Vector([1,1,1]), 1)
        p2 = Plane(Vector([1,1,1]), 2)
        s = LinearSystem([p1,p2])
        r = s.compute_rref()
        self.assertTrue(r[0] == p1 and
                        r[1] == Plane(constant_term=1))

    def test_032_compute_rref(self):
        p1 = Plane(Vector([1,1,1]), 1)
        p2 = Plane(Vector([0,1,0]), 2)
        p3 = Plane(Vector([1,1,-1]), 3)
        p4 = Plane(Vector([1,0,-2]), 2)
        s = LinearSystem([p1,p2,p3,p4])
        r = s.compute_rref()
        self.assertTrue(r[0] == Plane(Vector([1,0,0]), 0) and
                        r[1] == p2 and
                        r[2] == Plane(Vector([0,0,-2]), 2) and
                        r[3] == Plane())

    def test_033_compute_rref(self):
        p1 = Plane(Vector([0,1,1]), 1)
        p2 = Plane(Vector([1,-1,1]), 2)
        p3 = Plane(Vector([1,2,-5]), 3)
        s = LinearSystem([p1,p2,p3])
        r = s.compute_rref()
        self.assertTrue(r[0] == Plane(Vector([1,0,0]), Decimal(23)/Decimal(9)) and
                        r[1] == Plane(Vector([0,1,0]), Decimal(7)/Decimal(9)) and
                        r[2] == Plane(Vector([0,0,1]), Decimal(2)/Decimal(9)))


    def test_034_compute_ge_solution(self):
        p1 = Plane(Vector([5.862,1.178,-10.366]), -8.15)
        p2 = Plane(Vector([-2.931,-0.589,5.183]), -4.075)
        s = LinearSystem([p1,p2])
        self.assertTrue(s.solution() == "No solution")

    def test_035_compute_ge_solution(self):
        p1 = Plane(Vector([8.631,5.112,-1.816]), -5.113)
        p2 = Plane(Vector([4.315,11.132,-5.27]), -6.775)
        p3 = Plane(Vector([-2.158,3.01,-1.727]), -0.831)
        s = LinearSystem([p1,p2,p3])
        self.assertTrue(s.solution() == "Infinite solutions")

    def test_036_compute_ge_solution(self):
        p1 = Plane(Vector([5.262,2.739,-9.878]), -3.441)
        p2 = Plane(Vector([5.111,6.358,7.638]), -2.152)
        p3 = Plane(Vector([2.016,-9.924,-1.367]), -9.278)
        p4 = Plane(Vector([2.167,-13.543,-18.883]), -10.567)
        s = LinearSystem([p1,p2,p3,p4])
        self.assertTrue(s.solution() == [Decimal('-1.17720187578995858313947665147'), Decimal('0.707150558138740933006474968221'), Decimal('-0.0826635849022828890650647196946')])


if __name__ == '__main__':
    unittest.main() #failfast = True, verbosity=2, tb_locals=True
