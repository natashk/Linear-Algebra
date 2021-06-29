from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        """
        Swap rows with indices row1 and row2
        """
        self.planes[row1], self.planes[row2] = self.planes[row2], self.planes[row1]


    def multiply_coefficient_and_row(self, coefficient, row):
        coefficient = Decimal(coefficient)
        n = self.planes[row].normal_vector * coefficient
        k = self.planes[row].constant_term * coefficient
        self.planes[row] = Plane(n, k)
        


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        coefficient = Decimal(coefficient)
        n1 = self.planes[row_to_add].normal_vector
        n2 = self.planes[row_to_be_added_to].normal_vector
        k1 = self.planes[row_to_add].constant_term
        k2 = self.planes[row_to_be_added_to].constant_term
        n_new = n1 * coefficient + n2
        k_new = k1 * coefficient + k2
        self.planes[row_to_be_added_to] = Plane(n_new, k_new)


    def find_nonzero_below(self,icur):
        n = len(self) # number of equations
        for i in range(icur+1,n):
            if self.planes[i].normal_vector.coordinates[icur] != 0:
                return i
        return -1


    def clear_coef_below(self, i, j):
        n = len(self) # number of equations
        c_i = self.planes[i].normal_vector.coordinates[j]
        for k in range(i+1,n):
            c_k = MyDecimal(self.planes[k].normal_vector.coordinates[j])
            if not c_k .is_near_zero():
                self.add_multiple_times_row_to_row(-c_k/c_i, i, k)


    def compute_triangular_form(self):
        system = deepcopy(self)
        n = len(system) # number of equations
        m = system.dimension # number of veriables
        for i in range(n):
            for j in range(i,m):
                c_i = MyDecimal(system.planes[i].normal_vector.coordinates[j])
                if c_i.is_near_zero():
                    nonzero_i = system.find_nonzero_below(i)
                    if nonzero_i != -1:
                        system.swap_rows(i, nonzero_i)
                    else:
                        continue
                system.clear_coef_below(i,j)
                break
        return system.planes


    def clear_coef_above(self, i, j):
        n = len(self) # number of equations
        for k in range(i):
            c_k = MyDecimal(self.planes[k].normal_vector.coordinates[j])
            if not c_k .is_near_zero():
                self.add_multiple_times_row_to_row(-c_k, i, k)


    def compute_rref(self):
        tf = self.compute_triangular_form()
        system = LinearSystem(tf)
        n = len(system) # number of equations
        pivot_indices = system.indices_of_first_nonzero_terms_in_each_row()
        for i in range(n-1,0,-1):
            j = pivot_indices[i]
            if j == -1:
                continue
            system.multiply_coefficient_and_row(Decimal(1)/tf[i].normal_vector.coordinates[j], i)
            system.clear_coef_above(i, j)
        return tf


    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
