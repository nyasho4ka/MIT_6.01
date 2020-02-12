class Polynomial:
    def __init__(self, coefficients):
        self.coeffs = coefficients

    def coeff(self, i):
        if i >= len(self.coeffs):
            return 0
        return self.coeffs[-1 - i]

    def val(self, v):
        result = 0

        for i, coeff in enumerate(reversed(self.coeffs), 0):
            result += coeff * v ** i

        return result

    def roots(self):
        roots = []
        if len(self.coeffs) == 2:
            roots.append(-self.coeff(1) / self.coeff(0))
        elif len(self.coeffs) == 3:
            discriminant = self.coeff(1) ** 2 - 4 * self.coeff(2) * self.coeff(0)
            first_root = - (self.coeff(1) + discriminant ** 0.5) / (2 * self.coeff(2))
            second_root = - (self.coeff(1) - discriminant ** 0.5) / (2 * self.coeff(2))
            roots.append(first_root)
            roots.append(second_root)
        else:
            raise ValueError('Too high polynomial order!')
        return roots

    def add(self, other):
        # create coefficients for result Polynomial
        result_coefficients = get_result_coefficients_for_add(self, other)
        # create result Polynomial with these coefficients
        result_polynomial = Polynomial(result_coefficients)
        # return result Polynomial
        return result_polynomial

    def mul(self, other):
        # create coefficients for result Polynomial
        result_coefficients = get_result_coefficients_for_mul(self, other)
        # create result Polynomial with these coefficients
        result_polynomial = Polynomial(result_coefficients)
        # return result Polynomial
        return result_polynomial

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

    def __call__(self, x):
        return self.val(x)

    def __str__(self):
        return str(self.coeffs)

    def __repr__(self):
        return str(self)


def get_result_coefficients_for_add(first_polynomial, second_polynomial):
    result_coefficients = []

    coefficient_number = max(len(first_polynomial.coeffs), len(second_polynomial.coeffs))

    for index in range(coefficient_number):
        result_coefficients.append(first_polynomial.coeff(index) + second_polynomial.coeff(index))

    result_coefficients.reverse()
    return result_coefficients


def get_result_coefficients_for_mul(first_polynomial, second_polynomial):
    # count coefficient number
    coefficient_number = len(first_polynomial.coeffs) + len(second_polynomial.coeffs) - 1
    # set result coefficients with zeros
    result_coefficients = [0 for _ in range(coefficient_number)]
    # calculate result coefficients
    for i in range(len(first_polynomial.coeffs)):
        for j in range(len(second_polynomial.coeffs)):
            result_coefficients[i+j] += first_polynomial.coeff(i) * second_polynomial.coeff(j)

    result_coefficients.reverse()
    return result_coefficients
